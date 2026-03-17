#!/bin/bash

if [ ! -d "venv" ]; then
    echo "⚙️ Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "📦 Installing requirements..."
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

if [ -f app.log ]; then
    rm app.log
    echo "🧹 Old logs cleared."
fi

docker compose up -d
echo "🐳 Docker containers starting..."

python3 app.py & 
FLASK_PID=$!
echo "🌐 Flask running in background (PID: $FLASK_PID)..."

echo "⏳ Waiting for services to stabilize..."
sleep 10

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
echo "🛑 Flask app stopped. Check Kibana at http://localhost:5601"