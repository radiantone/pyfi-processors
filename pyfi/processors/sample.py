
def do_something(message, *args, plugs={}, output={}, **kwargs):
   from random import randrange

   print("PLUGS:",plugs)
   print("DO SOMETHING ELSE!")
   print("Message:",message)

   plugs['plug1'] = ["Message "+str(message)]

   output['result'] = "The result!"
   output['data'] = {'key':'result'}

   argstr = ' '.join(args)
   message = "TEXT:"+str(message)+argstr
   graph = { 'tag': {'name':'tagname','value':'tagvalue'}, 'name':'temperature', 'value':randrange(10) }
   return { 'message': message, 'graph': graph}


def do_this(message, *args, plugs={}, output={},**kwargs):
   from random import randrange

   print("Do this!", message)

   argstr = ' '.join(args)
   message = "Do this String: "+str(message)+argstr
   graph = { 'tag': {'name':'tagname','value':'tagvalue'}, 'name':'distance', 'value':randrange(50) }
   return { 'message': message, 'graph': graph}


def do_that(message, *args, plugs={}, output={},**kwargs):
   print("Do THAT!", message)

   argstr = ' '.join(args)
   return "Do THAT: "+str(message)+argstr
