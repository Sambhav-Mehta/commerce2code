# ─────────────────────────────────────────────────────
# Commerce2Code · Series 02 · Post 05
# Topic: JSON in Python
# Author: Sambhav Mehta
# GitHub: github.com/Sambhav-Mehta/commerce2code
# ─────────────────────────────────────────────────────
# Real-world hook:
# When PhonePe talks to your bank, they exchange
# a tiny text packet. That packet is JSON.
# ─────────────────────────────────────────────────────

import json

# ── 1. JSON Looks Like a Dict — But It's Plain Text ──
# A Python dict only exists inside Python.
# JSON is text — any app, server, or language can read it.

payment_request = {
    "txn_id": "TXN4821093",
    "amount": 500.00,
    "vpa": "sambhav@upi",
    "is_verified": True,
    "remarks": None
}

print("Python dict:")
print(payment_request)
print(type(payment_request))   # <class 'dict'>
print()


# ── 2. dict → JSON: json.dumps() ─────────────────────
# "dumps" = dump string. Converts a Python dict into JSON text.
# This is what PhonePe sends OUT to the bank's server.

request_json = json.dumps(payment_request)

print("JSON text (what actually gets sent over the network):")
print(request_json)
print(type(request_json))      # <class 'str'> — it's just text now
print()

# Notice what changed:
#   True   → true     (lowercase, no quotes)
#   None   → null      (JSON's version of "nothing")
#   keys   → always double-quoted, never single-quoted


# ── 3. JSON → dict: json.loads() ─────────────────────
# "loads" = load string. Converts JSON text back into a Python dict.
# This is what your app does when the bank's response arrives.

bank_response_json = '''
{
  "status": "SUCCESS",
  "approved": true,
  "bank_ref": "HDFC92837",
  "error": null
}
'''

bank_response = json.loads(bank_response_json)

print("Bank's response, converted back into a Python dict:")
print(bank_response)
print(type(bank_response))     # <class 'dict'> — usable in Python again
print()

print(f"Payment status : {bank_response['status']}")
print(f"Bank reference : {bank_response['bank_ref']}")
print()


# ── 4. Pretty-Printing JSON ───────────────────────────
# indent= makes JSON human-readable — useful for debugging.

pretty = json.dumps(payment_request, indent=2)
print("Pretty-printed JSON:")
print(pretty)
print()


# ── 5. Key Differences — Python dict vs JSON ──────────
print("── Python dict vs JSON — what changes ──")
print()
print("True / False   →   true / false   (lowercase, unquoted)")
print("None           →   null")
print("Single quotes  →   double quotes ONLY")
print("Tuples & Sets  →   don't exist in JSON — only objects {} and arrays []")
print("Trailing comma →   not allowed in JSON")
print()
print("json.dumps()  →  Python object  →  JSON text   (sending data out)")
print("json.loads()  →  JSON text      →  Python object (reading data in)")
