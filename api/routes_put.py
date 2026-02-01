import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json

from routes_get import transactions_dict


# PUT /transactions/{id}
def update_transaction(tx_id, body):
    try:
        data = json.loads(body)
    except:
        return 400, json.dumps({"error": "Invalid JSON"})

    if tx_id not in transactions_dict:
        return 404, json.dumps({"error": "Transaction not found"})

    existing = transactions_dict[tx_id]

    for key in data:
        if key != "id":
            existing[key] = data[key]

    return 200, json.dumps(existing, indent=4)
