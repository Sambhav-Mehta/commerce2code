# Commerce2Code | Session 04
# Operators — Arithmetic, Comparison, Logical
# Real examples: Splitwise · CRED · Loan Approval

print("=" * 55)
print("PART 1: ARITHMETIC OPERATORS — Splitwise Bill Split")
print("=" * 55)

# You learned these in school. Apps use them the same way.
bill = 2400
friends = 4

per_person = bill / friends    # divide equally
tip = bill * 0.10              # 10% tip
remainder = bill % friends     # anything left over?
total_with_tip = bill + tip    # final amount

print(f"\nBill          : ₹{bill}")
print(f"Friends       : {friends}")
print(f"Per person    : ₹{per_person}")
print(f"Tip (10%)     : ₹{tip}")
print(f"Remainder     : ₹{remainder}")
print(f"Total with tip: ₹{total_with_tip}")

print("\n" + "=" * 55)
print("PART 2: COMPARISON OPERATORS — CRED Cashback Check")
print("=" * 55)

# Comparison operators always return True or False
# The app asks a yes/no question about your data
credit_score = 742

print(f"\nCredit Score: {credit_score}")
print(f"\ncredit_score >= 700  →  {credit_score >= 700}")
print(f"credit_score == 800  →  {credit_score == 800}")
print(f"credit_score != 600  →  {credit_score != 600}")
print(f"credit_score < 500   →  {credit_score < 500}")

if credit_score >= 700:
    print(f"\n✅ Eligible for cashback — score qualifies")
else:
    print(f"\n❌ Not eligible — score too low")

print("\n" + "=" * 55)
print("PART 3: LOGICAL OPERATORS — Loan Approval")
print("=" * 55)

# Logical operators combine multiple comparisons
# The bank doesn't just check one thing — it checks everything
score = 742
income = 1200000
has_existing_loan = False

print(f"\nCredit Score    : {score}")
print(f"Annual Income   : ₹{income:,.0f}")
print(f"Existing Loan   : {has_existing_loan}")

# and — ALL conditions must be True
score_ok = score >= 700
income_ok = income >= 500000
no_existing_loan = not has_existing_loan

approved = score_ok and income_ok and no_existing_loan

print(f"\nScore OK        : {score_ok}")
print(f"Income OK       : {income_ok}")
print(f"No Existing Loan: {no_existing_loan}")
print(f"\nLoan Approved   : {approved}")

if approved:
    print("✅ Congratulations! Your loan is approved.")
else:
    print("❌ Sorry, your application was rejected.")

print("\n" + "=" * 55)
print("PART 4: ALL THREE TOGETHER — The Full Picture")
print("=" * 55)

# This is what real app logic looks like
bill = 2400
friends = 4
has_promo = True
min_order_for_promo = 500

per_person = bill / friends                          # arithmetic
promo_applies = per_person > min_order_for_promo and has_promo  # comparison + logical

if promo_applies:
    discount = per_person * 0.10                     # arithmetic
    final = per_person - discount                    # arithmetic
    print(f"\nPromo applied! Pay ₹{final:.1f} instead of ₹{per_person:.1f}")
else:
    print(f"\nNo promo. Pay full: ₹{per_person:.1f}")
