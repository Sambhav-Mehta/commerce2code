# Commerce2Code | Series 01 — Wrap Up
# All 6 sessions working together in one script
# Sessions: Variables · Control Flow · Loops · Operators · Type Conversion · Functions

print("=" * 60)
print("SERIES 01 — ALL SESSIONS TOGETHER")
print("=" * 60)
print("Loan Application Processor — built with Python fundamentals\n")

# ============================================================
# SESSION 01 — Variables & Data Types
# Storing information in named boxes
# ============================================================

applicants = [
    ("Sambhav", "742", "1200000"),
    ("Priya",   "810", "800000"),
    ("Rahul",   "620", "300000"),
    ("Ananya",  "700", "500000"),
]

min_score  = 700          # int — whole number
min_income = 500000       # int — whole number
bank_name  = "BFHL Bank"  # str — text
is_open    = True         # bool — yes or no

# ============================================================
# SESSION 06 — Functions
# Write once. Call everywhere.
# ============================================================

def process_loan(name, score_text, income_text):

    # SESSION 05 — Type Conversion
    # Data from forms always arrives as text — convert before using
    score  = int(score_text)
    income = int(income_text)

    # SESSION 04 — Operators
    # Arithmetic, comparison, logical — school maths at scale
    premium  = score >= 750 and income >= 800000
    standard = score >= min_score and income >= min_income

    # SESSION 02 — Control Flow
    # How the app makes the decision
    if premium:
        status     = "Approved — Premium"
        loan_limit = income * 5
    elif standard:
        status     = "Approved — Standard"
        loan_limit = income * 3
    else:
        status     = "Rejected"
        loan_limit = 0

    return {
        "name":       name,
        "score":      score,
        "income":     income,
        "status":     status,
        "loan_limit": loan_limit,
    }

def display_result(result):
    print(f"  Applicant : {result['name']}")
    print(f"  Score     : {result['score']}")
    print(f"  Income    : ₹{result['income']:,}")
    print(f"  Status    : {result['status']}")
    if result['loan_limit'] > 0:
        print(f"  Max Loan  : ₹{result['loan_limit']:,}")
    print("  " + "-" * 38)

# ============================================================
# SESSION 03 — Loops
# Process ALL applicants automatically — no copy-pasting
# ============================================================

print(f"Processing applications for {bank_name}\n")
print("-" * 60)

approved = 0
rejected = 0

for name, score, income in applicants:
    result = process_loan(name, score, income)
    display_result(result)

    if result['status'] != "Rejected":
        approved += 1
    else:
        rejected += 1

# ============================================================
# SUMMARY — All sessions visible in the final output
# ============================================================

total         = len(applicants)
approval_rate = (approved / total) * 100

print(f"\nSUMMARY — {bank_name}")
print("=" * 60)
print(f"  Total applications : {total}")
print(f"  Approved           : {approved}")
print(f"  Rejected           : {rejected}")
print(f"  Approval rate      : {approval_rate:.1f}%")
