def emit_one(one, *args, plugs={}, output={}, **kwargs):
    """ emit one """
    if one: return one
    return 1


def emit_two(two, *args, plugs={}, output={}, **kwargs):
    if two: return two
    return 5


def add_two(one, two, *args, plugs={}, output={}, **kwargs):
    return int(one) + int(two)


def emit_add(one, five, *args, plugs={}, output={}, **kwargs):
    print("EMIT_ADD: ", int(one) + int(five))
    return int(one) + int(five)


def do_something(message, *args, plugs={}, output={}, **kwargs):
    """ do_something """
    from random import randrange

    print("PLUGS:", plugs)
    print("DO SOMETHING ELSE!")
    print("Message:", message)

    plugs['plug1'] = ["Message " + str(message)]

    output['result'] = "The result!"
    output['data'] = {'key': 'result'}

    argstr = ' '.join(args)
    message = "TEXT:" + str(message) + argstr
    value = randrange(10)
    graph = {'tag': {'name': 'tagname', 'value': 'tagvalue'}, 'name': 'temperature', 'value': value}
    print("doSomething: GRAPH COMPLETE!")
    print("doSomething: VALUE", value)
    # raise Exception()
    return {'message': message, 'graph': graph}


def do_this(message, *args, plugs={}, output={}, **kwargs):
    from random import randrange

    print("Do this!", message)

    argstr = ' '.join(args)
    message = "Do this String: " + str(message) + argstr
    graph = {'tag': {'name': 'tagname', 'value': 'tagvalue'}, 'name': 'distance', 'value': randrange(50)}
    print("doThis: GRAPH CREATED!")
    return {'message': message, 'graph': graph}


def do_that(message, *args, plugs={}, output={}, **kwargs):
    print("Do THAT!", message)

    argstr = ' '.join(args)
    return "Do THAT: " + str(message) + argstr
