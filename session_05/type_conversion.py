# Commerce2Code | Session 05
# Type Conversion — int(), float(), str()
# Real examples: PhonePe · Zomato · Swiggy

print("=" * 55)
print("PART 1: THE PROBLEM — Why Types Matter")
print("=" * 55)

# Data from any form always arrives as text
user_input = "500"
print(f"\nUser typed  : {user_input}")
print(f"Python sees : {type(user_input)}")

# You cannot do maths on text
try:
    result = user_input + 100
except TypeError as e:
    print(f"\nERROR: {e}")
    print("Fix: convert text to number first")

print("\n" + "=" * 55)
print("PART 2: str → int — Text to Whole Number")
print("=" * 55)

credit_score = int("742")
otp          = int("4829")

print(f"\nint('742')  = {credit_score}  {type(credit_score)}")
print(f"int('4829') = {otp}  {type(otp)}")
print(f"\nScore + 50 bonus : {credit_score + 50}")
print(f"OTP match        : {otp == 4829}")

print("\n" + "=" * 55)
print("PART 3: int → float — Whole Number to Decimal")
print("=" * 55)

per_person = float(600)
tip        = per_person * 0.10
total      = per_person + tip

print(f"\nfloat(600)   = {per_person}  {type(per_person)}")
print(f"Tip (10%)    : ₹{tip}")
print(f"Total        : ₹{total}")

print("\n" + "=" * 55)
print("PART 4: int/float → str — Number to Text")
print("=" * 55)

amount       = 240
delivery_min = 32
restaurant   = "Biryani Blues"

sms = f"Your order from {restaurant} of ₹{amount} arrives in {delivery_min} mins."
print(f"\n📱 SMS: {sms}")

print(f"\nstr(240) = '{str(amount)}'  {type(str(amount))}")

print("\n" + "=" * 55)
print("PART 5: = vs == — The Most Confusing Difference")
print("=" * 55)

score = 742             # = STORES the value

print(f"\nscore = 742     → stored in memory")
print(f"score == 742    → {score == 742}   is score equal to 742?")
print(f"score == 800    → {score == 800}  is score equal to 800?")

print("\n" + "=" * 55)
print("PART 6: BONUS — ** and // Operators")
print("=" * 55)

print(f"\n2 ** 3  = {2**3}   (2 to the power of 3)")
print(f"10 ** 2 = {10**2}  (10 squared)")

items  = 7
people = 2
print(f"\n{items} items between {people} people:")
print(f"Each gets  : {items // people}  ({items} // {people})")
print(f"Left over  : {items % people}   ({items} %  {people})")
