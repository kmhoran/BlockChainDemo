import hashlib

class Block:
    def __init__(self, id, timestamp, data, previous_hash):
        self.id = id
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash


    @property
    def hash(self):
        sha = hashlib.sha256()

        sha.update(str(self.id).encode('utf-8') +
                   str(self.timestamp).encode('utf-8')+ 
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()

    def __repr__(self):
        return "BLOCK {0}\n    data: {1}\n    hash: {2}".format(self.id, self.data, self.hash)