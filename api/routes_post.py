import sys
import os
import json
from datetime import datetime
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from routes_get import transactions, transactions_dict


# POST /transactions
def create_transaction(body):
    try:
        data = json.loads(body)
    except:
        return 400, json.dumps({"error": "Invalid JSON"})

    # Required fields (excluding id and timestamp, since we generate them)
    required = ["type", "amount", "sender", "receiver"]
    for field in required:
        if field not in data:
            return 400, json.dumps({"error": f"Missing field: {field}"})

    # Generate unique ID automatically
    tx_id = str(random.randint(10**10, 10**11 - 1))

    # Generate timestamp automatically
    timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S %p")

    # Build the transaction object
    transaction = {
        "id": tx_id,
        "type": data["type"],
        "amount": data["amount"],
        "sender": data["sender"],
        "receiver": data["receiver"],
        "timestamp": timestamp,
    }

    # Check if ID already exists (unlikely with uuid4, but safe)
    if tx_id in transactions_dict:
        return 400, json.dumps({"error": "Transaction ID already exists"})

    # Save transaction
    transactions.append(transaction)
    transactions_dict[tx_id] = transaction

    return 201, json.dumps(transaction, indent=4)

