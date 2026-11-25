def drink_me(param):
    msg = 'Drinking ' + param + ' glass'
    print(msg)
    return 'empty'

glass = 'full'
glass = drink_me(glass)
print('The glass is', glass)
