import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json

from routes_get import transactions, transactions_dict


# POST /transactions
def create_transaction(body):
    try:
        data = json.loads(body)
    except:
        return 400, json.dumps({"error": "Invalid JSON"})

    required = ["id", "type", "amount", "sender", "receiver", "timestamp"]
    for field in required:
        if field not in data:
            return 400, json.dumps({"error": f"Missing field: {field}"})

    if data["id"] in transactions_dict:
        return 400, json.dumps({"error": "Transaction ID already exists"})

    transactions.append(data)
    transactions_dict[data["id"]] = data

    return 201, json.dumps(data, indent=4)
