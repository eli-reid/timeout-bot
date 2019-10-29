class Event(object):
    """simple event emitter"""

    def __init__(self, doc=None):
        self.__doc__= doc

    def __get__(self,obj,objtype=None):
        if obj is None:
            return self 
        return EventHandler(self,obj)

    def __set__(self,obj,value):
        pass

class EventHandler(object):

    def __init__(self,event,obj):
        self.event=event 
        self.obj=obj

    def _getfunctionlist(self):
        try:
            eventhandler = self.obj.__eventhandler__ 
        except AttributeError:  
            eventhandler = self.obj.__eventhandler__ = {}
        return eventhandler.setdefault(self.event, [])

    def add(self,funcs):
        for func  in funcs:   
            self._getfunctionlist().append(func)
        return self
    
    def remove(self,func):
        self._getfunctionlist().remove(func)
        return self
    
    def fire(self,earg=None):
        for func in self._getfunctionlist():
            func(self.obj,earg)

    __iadd__ = add
    __isub__ = remove
    __call__ = fire

    


    
