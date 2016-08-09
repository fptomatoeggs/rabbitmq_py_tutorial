import sys

import pika

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: Hello World!'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(' [x] Sent %r' % message)
