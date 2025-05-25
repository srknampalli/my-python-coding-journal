import json

# Your JSON array
data = [
    { "name": "Alice", "age": 30 },
    { "name": "Bob", "age": 25 }
]

# Convert to JSONL format and save to file
with open("output.jsonl", "w") as f:
    for record in data:
        f.write(json.dumps(record) + "\n")
