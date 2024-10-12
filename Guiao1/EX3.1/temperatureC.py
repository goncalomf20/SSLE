import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def consume_messages():
    # Establish a connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='temperature')

    # Set up subscription on the queue
    channel.basic_consume(queue='temperature',
                          on_message_callback=callback,
                          auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()