
def do_something(message, plugs={}, output={}):
   print("PLUGS:",plugs)
   print("DO SOMETHING ELSE!")
   print("Message:",message)

   if 'pyfi.queue2' in plugs and 'pyfi.queue3' in plugs: 
      if message.find('queue3') > -1:
         plugs['pyfi.queue3'] = ["Message "+message]
      else:
         plugs['pyfi.queue2'] = ["Message "+message]

   output['result'] = "The result!"
   output['data'] = {'key':'result'}

   return "Message:",message

def do_this(message,plugs={}, output={}):
   print("Do this!",message)

   return "Do this: "+str(message)
