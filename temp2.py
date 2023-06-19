import hashlib

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class Blockchain:
    def __init__(self):
        hashLast = hashGenerator('gen_last')
        hashStart = hashGenerator('gen_hash')

        genesis = Block('gen-data', hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)

# Create an instance of the Blockchain
bc = Blockchain()

# User interface for entering multiple temperature values
print("Enter temperature values (type 'done' to finish):")
while True:
    temperature = input("Temperature: ")
    if temperature == 'done':
        break
    bc.add_block(temperature)

    # Print the details of the newly added block
    print("Block added:")
    block = bc.chain[-1]
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.prev_hash)
    print()

# Print the details of each block in the chain
print("\nBlockchain:")
for block in bc.chain:
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.prev_hash)
    print()
