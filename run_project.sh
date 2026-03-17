#!/bin/bash

rm -f app.log
echo "🧹 Old logs cleared."

docker compose up -d
echo "🐳 Docker containers starting..."

source venv/bin/activate

python3 app.py & 
FLASK_PID=$!
echo "🌐 Flask running in background (PID: $FLASK_PID)..."

sleep 3

echo "🚗 Generating traffic..."
for i in {1..25}; do 
    curl -s http://localhost:5000/home > /dev/null
done

for i in {1..5}; do 
    curl -s http://localhost:5000/login > /dev/null
done
echo "✅ 30 logs generated in app.log."

echo "🧠 Running AI Anomaly Detection..."
python3 ai_detector.py

kill $FLASK_PID
echo "🛑 Flask app stopped. You can now check Kibana at http://localhost:5601"