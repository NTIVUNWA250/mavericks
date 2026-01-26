import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import os

from dsa.xml_parser import xmlParsing
from dsa.search_linear import linear_search
from dsa.search_dict import transactionDict, dictLookup


# Load and parse XML once when the server starts
XML_FILE = os.path.join(os.path.dirname(__file__), "../dsa/modified_sms_v2.xml")
transactions = xmlParsing(XML_FILE)

# Prepare dictionary version for fast search
transactions_dict = transactionDict(transactions)


# ------------------------------
# GET /transactions
# ------------------------------
def get_all_transactions():
    return 200, json.dumps(transactions, indent=4)


# ------------------------------
# GET /transactions/{id}
# ------------------------------
def get_transaction_by_id(tx_id):
    # First: try fast lookup
    result = dictLookup(transactions_dict, tx_id)

    # If not found, fall back to linear search
    if not result:
        result = linear_search(transactions, tx_id)

    if result:
        return 200, json.dumps(result, indent=4)
    else:
        return 404, json.dumps({"error": "Transaction not found"})

