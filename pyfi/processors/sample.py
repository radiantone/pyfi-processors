from celery import Celery


def do_something(message):
   print("DO SOMETHING ELSE!")
   print("Message:",message)
   return "Message:",message
