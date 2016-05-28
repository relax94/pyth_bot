import simplejson as json
import flashapi


def callback(replyid, data):
    print (data['text'])
    """TODO PUT PUBLISH WITH RESULT"""





flash = flashapi.FlashApi()
flash.setBotToken('572da4cb83e64b0c2fb98617')
flash.recieve_command(callback)


