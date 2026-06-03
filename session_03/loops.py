# Commerce2Code | Session 03
# Loops — for, while, break, continue
# Real examples: Zomato Delivery Partner Assignment + OTP Verification

print("=" * 55)
print("PART 1: FOR LOOP — Ping all nearby delivery partners")
print("=" * 55)

delivery_partners = ["Ravi", "Suresh", "Amit", "Priya", "Kiran"]

print("\nPinging all nearby delivery partners...")
for partner in delivery_partners:
    print(f"📍 Pinging {partner}...")

print("\nAll partners notified!")

print("\n" + "=" * 55)
print("PART 2: CONTINUE + BREAK — Find first available partner")
print("=" * 55)

partners = [
    {"name": "Ravi",   "available": False},
    {"name": "Suresh", "available": False},
    {"name": "Amit",   "available": True},
    {"name": "Priya",  "available": True},
    {"name": "Kiran",  "available": True},
]

print("\nFinding first available partner...")
order_assigned = False

for partner in partners:
    if not partner["available"]:
        print(f"⏭️  {partner['name']} is busy — skipping")
        continue        # skip this one, move to next
    print(f"✅ {partner['name']} accepted the order!")
    order_assigned = True
    break               # stop looking, order is assigned

if not order_assigned:
    print("❌ No partners available. Please try again.")

print("\n" + "=" * 55)
print("PART 3: WHILE LOOP — OTP Verification (3 attempts max)")
print("=" * 55)

correct_otp = "4829"
max_attempts = 3
attempts = 0
logged_in = False

# Simulated user inputs — edit to try different scenarios
simulated_inputs = ["1234", "5678", "4829"]

print(f"\nOTP sent to your registered mobile number.")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    entered_otp = simulated_inputs[attempts]
    attempts += 1

    print(f"Attempt {attempts}: User entered — {entered_otp}")

    if entered_otp == correct_otp:
        print("✅ OTP verified! Login successful.")
        logged_in = True
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Wrong OTP. {remaining} attempt(s) remaining.\n")

if not logged_in:
    print("\n🔒 Account locked. Too many failed attempts.")
    print("Please try again after 30 minutes.")
