# ─────────────────────────────────────────────────────
# Commerce2Code · Series 02 · Post 03
# Topic: Tuples & Sets in Python
# Author: Sambhav Mehta
# GitHub: github.com/Sambhav-Mehta/commerce2code
# ─────────────────────────────────────────────────────
# Real-world hook:
# You just paid ₹500 on GPay. The receipt appears —
# TXN ID, amount, merchant, date. Nobody changes that
# receipt after the fact. Not you. Not the bank.
# Not even the code. That's a tuple.
#
# Open GPay's monthly summary. You've ordered Swiggy
# 14 times. But "Swiggy" appears once in the list.
# That's a set.
# ─────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════
# PART 1 — TUPLES
# Ordered. Fixed. Cannot be changed after creation.
# ══════════════════════════════════════════════════════

# ── 1a. Creating a Tuple ─────────────────────────────
# A payment receipt has fixed facts.
# Once the transaction is complete — nothing changes.

payment = ("TXN4821093", "15-Jan-2025", 500.00, "Swiggy")
#           txn_id        date            amount   merchant

print("Payment receipt:", payment)
print()


# ── 1b. Accessing Elements by Index ──────────────────
# Same as a list — index starts at 0.

txn_id   = payment[0]    # "TXN4821093"
date     = payment[1]    # "15-Jan-2025"
amount   = payment[2]    # 500.00
merchant = payment[3]    # "Swiggy"

print(f"TXN ID   : {txn_id}")
print(f"Date     : {date}")
print(f"Amount   : ₹{amount}")
print(f"Merchant : {merchant}")
print()


# ── 1c. Tuple Unpacking ──────────────────────────────
# A cleaner way to grab all values at once.

txn_id, date, amount, merchant = payment
print(f"Unpacked → {txn_id} | ₹{amount} → {merchant}")
print()


# ── 1d. Immutability — The Core Feature ──────────────
# Try to change the amount and Python throws an error.
# This is intentional — a receipt must be tamper-proof.

try:
    payment[2] = 0.00              # Attempt to change amount
except TypeError as e:
    print(f"Cannot modify tuple: {e}")
    print("This is by design — payment records must never change.")
print()


# ── 1e. When to Use Tuples ───────────────────────────
# Use a tuple when the data must stay fixed after creation.

transaction_log = ("TXN4821093", "15-Jan-2025", 500.00, "Swiggy")  # receipt
coordinates     = (19.0760, 72.8777)    # lat/lng — fixed location
account_details = ("HDFC0001234", "98765XXXXX")  # IFSC + account, never changes

# Contrast: use a list when data should be able to change
recent_transactions = [500.00, 1200.00, 89.00]   # can add/remove entries
recent_transactions.append(349.00)                # works fine


# ══════════════════════════════════════════════════════
# PART 2 — SETS
# Unique values only. Unordered. No duplicates.
# ══════════════════════════════════════════════════════

# ── 2a. Creating a Set ───────────────────────────────
# GPay's "Paid to this month" view.
# You've ordered Swiggy 14 times — it appears once.

merchants_this_month = {"Swiggy", "Zomato", "Netflix", "Zepto", "IRCTC"}

print("Merchants this month:", merchants_this_month)
print("Note: order may vary — sets are unordered.")
print()


# ── 2b. Adding to a Set ──────────────────────────────
merchants_this_month.add("BookMyShow")
print("After adding BookMyShow:", "BookMyShow" in merchants_this_month)


# ── 2c. No Duplicates — Ever ─────────────────────────
# Pay Swiggy 5 more times — it still appears once.

merchants_this_month.add("Swiggy")
merchants_this_month.add("Swiggy")
merchants_this_month.add("Swiggy")

print("Size stays same:", len(merchants_this_month))
print("Swiggy still appears once — sets reject duplicates silently.")
print()


# ── 2d. Removing from a Set ─────────────────────────
merchants_this_month.discard("Netflix")   # safe — no error if not found
print("After removing Netflix:", "Netflix" in merchants_this_month)
print()


# ── 2e. Membership Check ────────────────────────────
# Sets are extremely fast at checking if something exists.

if "Zepto" in merchants_this_month:
    print("Zepto: paid this month ✓")
else:
    print("Zepto: not paid this month")
print()


# ── 2f. Set Operations ───────────────────────────────
# Compare what you paid on two different payment apps.

gpay_merchants   = {"Swiggy", "Zomato", "Netflix", "Zepto", "BookMyShow"}
phonepay_merchants = {"Swiggy", "Zomato", "IRCTC", "Meesho", "BookMyShow"}

# Merchants paid on BOTH apps
both = gpay_merchants & phonepay_merchants
print("Paid on both:", both)

# Merchants paid only on GPay
only_gpay = gpay_merchants - phonepay_merchants
print("Only on GPay:", only_gpay)

# All unique merchants across both apps
all_merchants = gpay_merchants | phonepay_merchants
print("All unique merchants:", all_merchants)
print()


# ══════════════════════════════════════════════════════
# PART 3 — QUICK REFERENCE
# List vs Tuple vs Set
# ══════════════════════════════════════════════════════

print("── When to use what ──")
print()
print("LIST  → ordered, changeable, duplicates OK")
print("        recent_transactions = [500, 1200, 89, 500]")
print()
print("TUPLE → ordered, fixed/immutable, duplicates OK")
print("        payment = ('TXN001', '15-Jan', 500.00, 'Swiggy')")
print()
print("SET   → unordered, changeable, NO duplicates")
print("        merchants = {'Swiggy', 'Zomato', 'Netflix'}")
