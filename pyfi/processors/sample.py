print("worker:",worker)

@worker.app.task(name='pyfi.processors.sample.do_something')
def do_something(message, plugs=[]):
   print("DO SOMETHING ELSE!")
   print("Message:",message)
   plugs['pyfi.queue2'] = ["Message "+message]
   return "Message:",message

def do_this(message,plugs=[]):
   print("Do this!",message)
   return "Do this: "+str(message)
