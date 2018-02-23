import hashlib
import time

class Block:
    def __init__(self, id, timestamp, data, previous_hash, workDifficulty):
        self.id = id
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.workDifficulty = workDifficulty
        self.nonce = 0
        self.workTime = 0


    @property
    def hash(self):
        sha = hashlib.sha256()

        sha.update(str(self.id).encode('utf-8') +
                   str(self.timestamp).encode('utf-8')+ 
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))

        return sha.hexdigest()



    def __repr__(self):
        return "BLOCK {0}\n    data: {1}\n    nonce: {2}\n    difficulty: {3}\n    work time: {4}ms\n    hash: {5}".format(self.id, self.data,self.nonce, self.workDifficulty, self.workTime, self.hash)


    def calculate_nonce(self):
        start_time = int(round(time.time() * 1000))
        while(str(self.hash)[0:self.workDifficulty] != '0' * self.workDifficulty):
            self.nonce += 1
        
        self.workTime = int(round(time.time() * 1000)) - start_time

