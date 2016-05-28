import pika
import simplejson as json

class FlashApi:

    def startConnection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def setBotToken(self, token):
        self.startConnection()
        self.token = token
        self.q = self.channel.queue_declare(queue=self.token, durable=True)

    def nativecallback(self, ch, method, properties, body):
      data = json.loads(str(body))
      self.remote_callback(properties.reply_to, data)
      """TODO PUT PUBLISH WITH RESULT"""


    def recieve_command(self, callback):
        self.remote_callback = callback
        self.channel.basic_consume(self.nativecallback, self.token, no_ack=True)
        self.channel.start_consuming()

    def push_answer(self, reciever_id, message):
        data = dict()
        data["reply_to"] = reciever_id
        data["text"] = message
        self.channel.publish('','server',json.dumps(data))

    def close_connection(self):
        self.channel.close()