import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json

from routes_get import transactions, transactions_dict


# DELETE /transactions/{id}
def delete_transaction(tx_id):
    if tx_id not in transactions_dict:
        return 404, json.dumps({"error": "Transaction not found"})

    item = transactions_dict.pop(tx_id)
    transactions.remove(item)

    return 200, json.dumps({"message": "Transaction deleted"})
