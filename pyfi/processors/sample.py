
def do_something(message, *args, plugs={}, output={}, **kwargs):
   print("PLUGS:",plugs)
   print("DO SOMETHING ELSE!")
   print("Message:",message)

   plugs['plug1'] = ["Message "+str(message)]

   output['result'] = "The result!"
   output['data'] = {'key':'result'}

   argstr = ' '.join(args)
   return "TEXT:"+str(message)+argstr

def do_this(message, *args, plugs={}, output={},**kwargs):
   print("Do this!", message)

   argstr = ' '.join(args)
   return "Do this String: "+str(message)+argstr

def do_that(message, *args, plugs={}, output={},**kwargs):
   print("Do THAT!", message)

   argstr = ' '.join(args)
   return "Do THAT: "+str(message)+argstr
