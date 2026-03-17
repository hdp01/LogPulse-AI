# 🚀 LogPulse-AI: Intelligent Log Anomaly Detection

**LogPulse-AI** is a modern observability pipeline that replaces traditional threshold-based alerting with **Unsupervised Machine Learning** and **Natural Language Processing (NLP)**. By analyzing the semantic meaning and latency patterns of system logs, it detects "Unknown-Unknowns" that standard monitoring tools often miss.

## 🧠 Why this project?
Traditional monitoring (like standard ELK) requires manual rules (e.g., "Alert if error > 5"). **LogPulse-AI** doesn't need rules. It learns what "Normal" looks like and flags anything statistically different.

* **Semantic Analysis:** Uses TF-IDF to understand if log messages (e.g., "Connection Timeout") are rare or common.
* **Latency Awareness:** Detects performance degradation before it becomes a total outage.
* **EK Stack Architecture:** A lightweight alternative to ELK that replaces the heavy Logstash layer with a high-performance Python Intelligence engine.

---

## 🛠️ Tech Stack
| Component | Technology | Role |
| :--- | :--- | :--- |
| **Source** | Flask (Python) | Generates real-time web traffic logs. |
| **Storage** | Elasticsearch 8.x | High-speed distributed search engine. |
| **Visualization** | Kibana 8.x | Dashboarding and data exploration. |
| **ML Model** | Scikit-learn | Isolation Forest (Unsupervised Outlier Detection). |
| **NLP Engine** | TF-IDF Vectorizer | Numerical conversion of log text. |
| **Infrastructure** | Docker Compose | Containerized service management. |

---

## 📂 Project Structure
```text
.
├── compose.yaml          # Docker configuration for ES & Kibana
├── app.py                # Flask application (Log Generator)
├── ai_detector.py        # ML/NLP Intelligence & ES Uploader
├── run_project.sh        # Master Automation Script (Linux)
├── requirements.txt      # Python dependencies
├── .gitignore            # Keeps repo clean (ignores venv & logs)
└── README.md             # Project documentation