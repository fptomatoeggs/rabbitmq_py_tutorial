import sys

import pika

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

serverity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = ' '.join(sys.argv[2:]) or 'info: Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=serverity,
                      body=message)

print(' [x] Sent %r:%r' % (serverity, message))
connection.close()
