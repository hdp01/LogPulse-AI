import logging
from flask import Flask, request
import random
import time

app = Flask(__name__)

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(path)s | %(message)s | %(resp_time)s'
)

@app.route('/home')
def home():
    rt = random.randint(10, 80)
    time.sleep(rt / 1000)
    app.logger.info(f"INFO | /home | User dashboard load | {rt}")
    return "Home"

@app.route('/login')
def login():
    rt = random.randint(2000, 4000)
    time.sleep(rt / 1000)
    app.logger.warning(f"WARN | /login | Slow database response | {rt}")
    return "Login"

if __name__ == '__main__':
    app.run(port=5000)