import pika
import sys

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

channel.queue_declare(queue='task_queue')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))
print(" [x] Sent %r" % message)
