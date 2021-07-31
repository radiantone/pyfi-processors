from celery import Celery


def do_something(message, plugs=[]):
   print("DO SOMETHING ELSE!")
   print("Message:",message)
   plugs['pyfi.queue2'] += ["Message "+message]
   return "Message:",message

def do_this(message,outlets=[]):
   print("Do this!",message)
   return "Do this: "+message
