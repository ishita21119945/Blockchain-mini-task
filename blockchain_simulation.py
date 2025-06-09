import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Creating 3 linked blocks
blockchain = []

# Genesis block
blockchain.append(Block(0, time.time(), "Genesis Block", "0"))

# Block 1
blockchain.append(Block(1, time.time(), "Block 1 Data", blockchain[0].hash))

# Block 2
blockchain.append(Block(2, time.time(), "Block 2 Data", blockchain[1].hash))

# Display all blocks
print("🔗 Blockchain Before Tampering:\n")
for block in blockchain:
    print(f"Index: {block.index}, Hash: {block.hash}, PrevHash: {block.previous_hash}")

# Tampering Block 1
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].compute_hash()
blockchain[2].previous_hash = blockchain[1].hash  # Updating block 2’s previous hash without recalculating its hash

print("\n⚠️ Blockchain After Tampering Block 1 (Without Fixing Block 2 Hash):\n")
for block in blockchain:
    print(f"Index: {block.index}, Hash: {block.hash}, PrevHash: {block.previous_hash}")
