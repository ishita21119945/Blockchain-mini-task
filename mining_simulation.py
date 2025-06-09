import hashlib
import time

class Block:
    def __init__(self, data):
        self.timestamp = time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = "0" * difficulty
        start_time = time.time()

        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()

        end_time = time.time()
        print(f"✅ Block mined: {self.hash}")
        print(f"⛏️ Nonce attempts: {self.nonce}")
        print(f"⏱️ Time taken: {round(end_time - start_time, 2)} seconds")

# Example usage
difficulty = 4
block = Block("Mining simulation block")
block.mine_block(difficulty)
