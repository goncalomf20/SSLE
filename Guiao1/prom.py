from prometheus_client import start_http_server, Gauge
import requests
import time

# Create a metric to track health status
health_metric = Gauge('service_health', 'Health status of the service', ['service', 'alive'])

# Create services array – these are examples
SERVICES = ['http://localhost:5000']

def check_service_health():
    for service in SERVICES:
        try:
            response = requests.get(service)
            health_status = 1 if response.status_code == 200 else 0
        except requests.exceptions.RequestException:
            health_status = 0
        health_metric.labels(service=service, alive=health_status).set(health_status)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Simulate health checks periodically
    while True:
        check_service_health()
        time.sleep(5)  # Check every 5 seconds