import random
import time
from prometheus_client import start_http_server, Gauge
start_http_server(8000)
random_number_gauge = Gauge('random_number', 'A random number between 100 and 1000')
while True:
    number=random.randint(100,1000)
    random_number_gauge.set(number)
    print(number)
    time.sleep(10)