import simplejson as json
import flashapi


def callback(replyid, data):
    command = data['body']
    print (command)
    if command == "%how":
       print ("recieve command %s" % replyid)
       flash.push_answer(data['queue'], "How to be ?")
    elif command == "%start":
        print ("recieve start command")






flash = flashapi.FlashApi()
flash.setBotToken('572da4cb83e64b0c2fb98617')
flash.recieve_command(callback)


