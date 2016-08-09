import sys

import pika

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

exchange_name = 'topic_logs'

channel.exchange_declare(exchange=exchange_name,
                         type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange=exchange_name,
                      routing_key=routing_key,
                      body=message)

print(' [x] Sent %r:%r' % (routing_key, message))
connection.close()
