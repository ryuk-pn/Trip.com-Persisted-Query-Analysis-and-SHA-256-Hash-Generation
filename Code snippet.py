import hashlib
import json

def generate_sha256_hash(data):
    # Convert dic into json
    json_data = json.dumps(data, separators=(',', ':'), sort_keys=True)
    # SHA-256 hash
    sha256_hash = hashlib.sha256(json_data.encode()).hexdigest()
    return sha256_hash

#data payload
data_payload = {
    "operationName": "routeInfo",
    "variables": {
        "request": {
            "departure": "BLR",
            "arrival": "BKK",
            "searchCriteria": {
                "searchSegmentList": [
                    {"departCity": "BLR", "arriveCity": "BKK"},
                    {"departCity": "BKK", "arriveCity": "BLR"}
                ]
            },
            "tripType": "RT"
        }
    }
}

# Generaten Hash
generated_hash = generate_sha256_hash(data_payload)
print(f"Generated SHA-256 Hash: {generated_hash}")

#compare 
provided_hash = "26c6f9703c762620476c83cea0122d31c7ab15b9a949aaae1cb933dcfc832ed0"
is_valid = generated_hash == provided_hash
print(f"Is the generated hash valid? {'Yes' if is_valid else 'No'}")

 
