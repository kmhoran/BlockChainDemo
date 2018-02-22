import uuid
from block import Block
from datetime import datetime 

class Chain:

    def __init__(self):
        self.ledger = []
        self.id = str(uuid.uuid4())
        self.last_updated = datetime.now()
        self.spawn_origin_block()


    def __repr__(self): 
        return "CHAIN {0}\n    length: {1}\n    last updated: {t.year}-{t.month}-{t.day}_{t.hour}:{t.minute}:{t.second}".format(self.id, len(self.ledger), t=self.last_updated)



    def spawn_origin_block(self):

        if(len(self.ledger) == 0):
            origin = Block(id=0, 
                           timestamp= datetime.now,
                           data="Origin Block",
                           previous_hash="")
            self.ledger.append(origin)



    def add_block(self, data):
        temp_ledger = list(self.ledger)

        last_block = temp_ledger[-1]
        new_block = Block(id= last_block.id + 1,
                          timestamp= datetime.now(),
                          data=data,
                          previous_hash = last_block.hash)
        temp_ledger.append(new_block)

        self.try_replace_ledger(temp_ledger)
            
    


    def try_replace_ledger(self, new_ledger):
        
        if len(new_ledger) > len(self.ledger):
            if self.is_ledger_valid(new_ledger):
                self.ledger = new_ledger
                self.last_updated = datetime.now()




    def is_ledger_valid(self, ledger):
        if(ledger is None or len(ledger) == 0):
            return false
        
        isledgerValid = True

        for i in range(len(ledger)-1, -1,-1):
            if i == 0:
                continue
            if ledger[i].previous_hash != ledger[i-1].hash:
                isledgerValid  = False
            if ledger[i].id - ledger[i-1].id != 1:
                isledgerValid  = False
        
        return isledgerValid 

