import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block(index={self.index}, previous_hash='{self.previous_hash}', timestamp={self.timestamp}, data='{self.data}', hash='{self.hash}')"

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + previous_hash + str(timestamp) + data
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Inicializando a blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Adicionando novos blocos
num_of_blocks_to_add = 5

for i in range(num_of_blocks_to_add):
    data = f"Block {i + 1} Data"
    new_block = create_new_block(previous_block, data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Bloco {new_block.index} adicionado à blockchain!")
    print(f"Hash: {new_block.hash}\n")

# Exibindo a blockchain
print("Blockchain:")
for block in blockchain:
    print(block)
