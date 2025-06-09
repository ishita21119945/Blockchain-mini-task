import random

# PoW Simulation
miners = [{"name": "Miner1", "power": random.randint(10, 100)},
          {"name": "Miner2", "power": random.randint(10, 100)}]

pow_winner = max(miners, key=lambda x: x['power'])
print(f"⚡ PoW Winner: {pow_winner['name']} with power {pow_winner['power']}")
print("🔍 Logic: Validator with highest computational power is selected.\n")

# PoS Simulation
stakers = [{"name": "Staker1", "stake": random.randint(10, 100)},
           {"name": "Staker2", "stake": random.randint(10, 100)}]

pos_winner = max(stakers, key=lambda x: x['stake'])
print(f"💰 PoS Winner: {pos_winner['name']} with stake {pos_winner['stake']}")
print("🔍 Logic: Validator with highest coin stake is selected.\n")

# DPoS Simulation
delegates = ["Alice", "Bob", "Charlie"]
votes = {"Alice": 2, "Bob": 3, "Charlie": 1}
dpos_winner = max(votes, key=votes.get)

print(f"🗳️ DPoS Winner: {dpos_winner} with {votes[dpos_winner]} votes")
print("🔍 Logic: Delegate with most community votes is selected.\n")
