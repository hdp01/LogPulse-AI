import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def run_ai():
    rows = []
    try:
        with open('app.log', 'r') as f:
            for line in f:
                p = line.strip().split(' | ')
                if len(p) == 5:
                    rows.append({'msg': p[3], 'time': int(p[4])})
    except FileNotFoundError:
        print("Log file not found! Visit http://localhost:5000 first.")
        return

    if not rows:
        print("Log file is empty. Generate some traffic!")
        return

    df = pd.DataFrame(rows)
    
    tfidf = TfidfVectorizer()
    sparse_matrix = tfidf.fit_transform(df['msg'])
    text_df = pd.DataFrame.sparse.from_spmatrix(sparse_matrix)
    
    combined = pd.concat([df[['time']], text_df], axis=1)
    combined.columns = combined.columns.astype(str)

    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(combined.values)

    for i, row in df.iterrows():
        doc = {
            "message": row['msg'], 
            "latency": int(row['time']), 
            "is_anomaly": int(row['anomaly'] == -1)
        }
        es.index(index="web-logs", document=doc)
    
    print("SUCCESS: AI Analysis Complete. Data indexed in Elasticsearch.")

if __name__ == "__main__":
    run_ai()