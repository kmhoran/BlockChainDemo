import uuid
from block import Block
from datetime import datetime 
import time

class Chain:

    @staticmethod
    def origin_data():
        return "Origin Block" 

    @property
    def difficulty(self):
        return 3

    def __init__(self):
        self.ledger = []
        self.id = str(uuid.uuid4())
        self.last_updated = datetime.now()
        self.spawn_origin_block()
        

    def __repr__(self): 
        return "CHAIN {0}\n    length: {1}\n    difficulty: {2}\n    last updated: {t.year}-{t.month}-{t.day}_{t.hour}:{t.minute}:{t.second}".format(self.id, len(self.ledger),self.difficulty, t=self.last_updated)



    def spawn_origin_block(self):

        if(len(self.ledger) == 0):
            origin = Block(id=0, 
                           timestamp= datetime.now,
                           data= Chain.origin_data(),
                           previous_hash="",
                           workDifficulty= 0)
        
            self.ledger.append(origin)



    def add_block(self, data):
        temp_ledger = list(self.ledger)

        last_block = temp_ledger[-1]
        new_block = Block(id= last_block.id + 1,
                          timestamp= datetime.now(),
                          data=data,
                          previous_hash = last_block.hash,
                          workDifficulty = self.difficulty)
        
        # Do work!
        new_block.calculate_nonce()

        temp_ledger.append(new_block)

        self.try_replace_ledger(temp_ledger)            
    


    def try_replace_ledger(self, new_ledger):
        
        if len(new_ledger) <= len(self.ledger):
            return False

        if not self.is_ledger_valid(new_ledger):
            return False
        
        self.ledger = new_ledger
        self.last_updated = datetime.now()
        return True




    def is_ledger_valid(self, ledger):
        if(ledger is None or len(ledger) == 0):
            return false

        for i in range(len(ledger)-1, -1,-1):
            if i == 0:
                if ledger[i].data != Chain.origin_data():
                    return False
                continue

            if ledger[i].previous_hash != ledger[i-1].hash:
                return False
            
            # This ine is not stricktly necessary, but 
            # I like to keep a good sequence.
            if ledger[i].id - ledger[i-1].id != 1:
                return False
            
            if not self.block_has_valid_proof_of_work(ledger[i]):
                return False
        
        return True
    

    
    def block_has_valid_proof_of_work(self, block):

        # Proof of work must be up to this chain's standard
        if self.difficulty > block.workDifficulty:
            return False
        
        # Block must meet its own proof of work standard
        if str(block.hash)[0:block.workDifficulty] != '0' * block.workDifficulty:
            return False

        return True
        


