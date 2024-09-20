# PROBLEM

class OldSystem:
    def specific_request(self):
        return "Old System: Specific Request"
    
class NewSystem:
    def request(self):
        pass
    
class Adapter(NewSystem):
    '''Adapter is the key to this pattern it will translate calls b/w the two incompatible
       interfaces. '''
    def __init__(self, old_system: OldSystem):
        '''(__init__) initializes the **Adapter** object by taking an instance of 
           **old system** as a parameter. 
           
           The **Adapter** will hold a reference to the old system object and use it 
           to call its methods. '''
        self.old_system = old_system
        
    def request(self):
        return self.old_system.specific_request()
    
def client_code(new_system: NewSystem):
    print(new_system.request())
    
old_system = OldSystem()

adapter = Adapter(old_system)

client_code(adapter)