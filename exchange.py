import pika

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) 
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

message = 'Hello from Brian'

channel.basic_publish(exchange='logs',
        routing_key='',
        body=message)
# channel.queue_declare(queue='hello')
# def callback(ch, method, properties, body):
#     print (' [x] Received %r' % body)
# channel.basic_consume(callback, queue='hello', no_ack=True)
# 
# print (' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()
