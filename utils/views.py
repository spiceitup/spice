from rest_framework.response import Response

class RestAPI:
    """RestAPI decorator is wrapper for forming reponse data
    """    
    def __init__(self, function): 
        self.function = function 

        self.data_field_name = 'data'
      
    def __call__(self, *args, **kwargs): 
        # Call function
        response = self.function(*args, **kwargs) 

        # TODO Forming response

        
        return response