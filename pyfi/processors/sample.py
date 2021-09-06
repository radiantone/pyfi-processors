
def do_something(message, *args, plugs={}, output={}, **kwargs):
   print("PLUGS:",plugs)
   print("DO SOMETHING ELSE!")
   print("Message:",message)

   plugs['pyfi.queue3'] = []
   plugs['pyfi.queue2'] = []
   if 'pyfi.queue2' in plugs and 'pyfi.queue3' in plugs: 
       plugs['pyfi.queue2'] = ["Message "+str(message)]

   output['result'] = "The result!"
   output['data'] = {'key':'result'}

   argstr = ' '.join(args)
   return "Message:"+str(message)+argstr

def do_this(message, *args, plugs={}, output={},**kwargs):
   print("Do this!", message)

   argstr = ' '.join(args)
   return "Do this: "+str(message)+argstr
