class hash_map:
    def __init__(self):
        self.size = 50  #to reduce collision
        self.list = [ None for i in range( self.size )]

    def hash_function(self,key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.size
    
    def add_item(self,key,value):
        ind = self.hash_function(key)
        self.list[ind] = [value]