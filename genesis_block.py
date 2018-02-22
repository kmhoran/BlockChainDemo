from datetime import datetime
from block import Block

def spawn_origin_block():
    return Block(id=0, 
                 timestamp= datetime.now,
                 data="Origin Block",
                 previous_hash="")
