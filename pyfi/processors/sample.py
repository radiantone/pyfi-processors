
def do_something(message, plugs={}, output={}):
   print("PLUGS:",plugs)
   print("DO SOMETHING ELSE!")
   print("Message:",message)
   if 'pyfi.queue2' in plugs: 
      plugs['pyfi.queue2'] = ["Message "+message]
   output['result'] = "The result!"
   output['data'] = {'key':'result'}
   return "Message:",message

def do_this(message,plugs={}, output={}):
   print("Do this!",message)
   return "Do this: "+str(message)
