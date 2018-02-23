# import genesis_block as start
# from block import Block
from chain import Chain

def run():
    chain = Chain()
    print("\n## Created chain with origin block. ##\n")
    print(chain)
    print("\n")
    chain.add_block("This is the first real block!")
    print("    >> Added block 1. <<\n")
    chain.add_block({'name': 'new block', 'type':'test'})
    print("    >> Added block 2. <<\n")
    chain.add_block({'name': 'some other type of data', 'series':['a', 'b', 'c']})
    print("    >> Added block 3. <<\n")
    for i in range(len(chain.ledger)):
        print(chain.ledger[i])
        print("\n")



if __name__ == "__main__":
    run()
