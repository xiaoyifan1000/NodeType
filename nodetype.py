import time

class nodetype(dict):
    def __init__(self, count, parent_node):
        super(nodetype, self).__init__()
        self.update(dict.fromkeys([f"{parent_node}{_a}" for _a in range(1, count+1)]))
        self.timestamp = time.time()
        
    def set_timestamp(self):
        self.timestamp = time.time()
    
    def get_timestamp(self):
        return self.timestamp
        