import pika
import sys

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

exchange_name = 'direct_logs'

channel.exchange_declare(exchange=exchange_name,
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

serverities = sys.argv[1:]
if not serverities:
    sys.stderr.write('Usage: %s [info] [warning] [error]\n' % sys.argv[0])
    sys.exit()

for serverity in serverities:
    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name,
                       routing_key=serverity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(' [x] %r:%r' % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
