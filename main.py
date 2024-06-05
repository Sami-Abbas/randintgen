from flask import Flask
from prometheus_client import start_http_server, Counter
import random
import time

app = Flask(__name__)

# Define a Prometheus counter metric
random_number_counter = Counter('random_number', 'Random number generated')

@app.route('/generate')
def generate_random_number():
    random_number = random.randint(100, 1000)
    random_number_counter.inc()  # Increment the counter
    return f"Random number generated: {random_number}"

if __name__ == '__main__':
    # Start the Prometheus HTTP server
    start_http_server(9090)
    # Start the Flask app
    app.run(host='0.0.0.9090', port=9090)
