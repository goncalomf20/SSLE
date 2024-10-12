import requests

def consume_api():
    url = 'http://127.0.0.1:5002/services'  # Replace with your API endpoint
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Available services:")
        for service in data:
            print(f"Service ID: {service['id']}, Name: {service['name']}, URL: {service['url']}")
        
        service_id = input("Enter the service ID to get more details: ")
        
        response = requests.get(f"{url}/{service_id}")
        if response.status_code == 200:
            data = response.json()
            response = requests.get(data['url'])
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print(f"Failed to retrieve data: {response.status_code}")
        else:
            print(f"No service found with ID {service_id}")
        
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    

if __name__ == "__main__":
    consume_api()