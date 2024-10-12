import pika
import random
import time

def publish_message(message):
    # Establish a connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='temperature')

    # Publish a message to the queue
    channel.basic_publish(exchange='',
                          routing_key='temperature',
                          body=message)
    print(f" [x] Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    while True:
        temperature = random.uniform(20.0, 30.0)  # Simulate a temperature reading between 20.0 and 30.0 degrees Celsius
        message = f"Temperature (C): {temperature:.2f} C"
        publish_message(message)
        time.sleep(30)  # Wait for 30 seconds before sending the next temperature