import requests

def consume_api():
    url = 'http://127.0.0.1:5002/services/1'  # Replace with your API endpoint
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    
    url = 'http://127.0.0.1:5002/services/2'  # Replace with your API endpoint
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    

if __name__ == "__main__":
    consume_api()