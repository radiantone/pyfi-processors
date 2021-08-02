
def do_something(message, plugs={}):
   print("PLUGS:",plugs)
   print("DO SOMETHING ELSE!")
   print("Message:",message)
   if 'pyfi.queue2' in plugs: 
      plugs['pyfi.queue2'] = ["Message "+message]
   return "Message:",message

def do_this(message,plugs=[]):
   print("Do this!",message)
   return "Do this: "+str(message)
