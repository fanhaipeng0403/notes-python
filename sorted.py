def log(func):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

   

    
 