class eventHandler(object):
    """ 
    Event Handler
    """
    def __init__(self):
        """
        Intialize a dictionary of events
            {'event':[list of fucntions]}
        """
        self._events={}
        return
    
    def emit(self,sender,event,obj):
        """
        self.emit - Event Emitter
        input : 
            sender (obj) - function or class reponsible for event 
            event (str) - registered name of event 
            obj (any type) - any varible or object you want to pass to the on function
        if event doesn't exist it will register it 
        """
        try:
            for func in self._eventlist[event]:
                func(sender,obj)
        except KeyError:
            self.register(event)


    def on(self,event,func):
        """
        self.on - Event Catch
        Input:
            event (str) - registered name of event 
            func(func) - function that is called when the event is emitted
        Returns: self
        """
        #add try statement to catch keyerror
        self._events[event].append(func)
        return self
        
    
    def register(self,eventlist):
        """ 
        add new events in list form []
        """
        for event in eventlist:
            if event not in self._events.keys:
                self._events[event]=[]
        return self 
                

        
    
    def remove(self,event,func):
        self._events[event].remove(func)
        return self

    __call__ = emit 
