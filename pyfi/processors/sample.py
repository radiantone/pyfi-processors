from celery import Celery


def do_something(message,outlets=[]):
   print("DO SOMETHING ELSE!")
   print("Message:",message)
   outlets['pyfi.queue3'] += ["Message "+message]
   return "Message:",message

def do_this(message,outlets=[]):
   print("Do this!",message)
   return "Do this: "+message
