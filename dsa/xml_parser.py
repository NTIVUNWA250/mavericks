import xml.etree.ElementTree as ET
import re

def xmlParsing(xml_file):

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        print(root[0].tag)
        print(len(root[0]))

        record = []

        for sms in root.iter('sms'):
            body = sms.get("body", "")
            timestamp = sms.get("readable_date", "")
            idFind = re.search(r'(?:TxId:|Financial Transaction Id:)\s*(\d+)', body)
            tx_id = idFind.group(1) if idFind else "N/A"
            amountFind = re.search(r'([\d,]+)\s*RWF', body)
            amount = amountFind.group(1).replace(',', '') if amountFind else 0.0

            if "received" in body:
                transactionType = "Transfer"
                senderFind = re.search(r'from\s+(.*?)\s+\(', body)
                sender = senderFind.group(1) if senderFind else "Unknown Person"
                receiver = "Me"
            elif "payment" in body:
                transactionType = "Payment"
                sender = "Me"
                receiverFind = re.search(r'to\s+(.*?)\s+(?:\d|has)', body)
                receiver = receiverFind.group(1).strip() if receiverFind else "MTN"
            elif "deposit" in body:
                transactionType = "Bank Deposit"
                sender = "Bank System"
                receiver = "Me"
            else:
                transactionType = "Other"
                sender = "Unidentified or System"
                receiver = "Unidentified or System"

            record.append({
                "id": tx_id,
                "type": transactionType,
                "amount": amount,
                "sender": sender,
                "receiver": receiver,
                "timestamp": timestamp
            })

        return [r for r in record if r['id'] != "N/A"]

    except Exception as e:
        print(f"Error parsing XML: {e}")
        return []
