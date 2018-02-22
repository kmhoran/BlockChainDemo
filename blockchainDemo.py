# import genesis_block as start
# from block import Block
from chain import Chain

def run():
    chain1 = Chain()
    
    print(chain1)
    firstBlock = chain1.ledger[0]
    print("\n")
    print(firstBlock)

    # print(chain1.is_chain_valid(chain1.blocks))
    print("\n")
    chain1.add_block("this is a new block")

    latestBlock = chain1.ledger[-1]
    print("\n")
    
    print(latestBlock)
    print("\n")
    chain1.add_block({'name': 'new block', 'type':'test'})
    lastBlock = chain1.ledger[-1]
    print("\n")
    print(chain1)
    print("\n")
    print(lastBlock)


if __name__ == "__main__":
    run()
