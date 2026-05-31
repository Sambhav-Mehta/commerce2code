# Commerce2Code | Session 01
# Variables, Data Types & f-strings

# #1. Storing data in memory as variables
customer_name = "Sambhav"
credit_score = 742
annual_income = 1200000.00
is_eligible = True

print("=" * 50)
print("LOAN APPLICATION VARIABLES")
print("=" * 50)

# #2. Displaying variables using f-strings
print(f"\nCustomer Name: {customer_name}")
print(f"Credit Score: {credit_score}")
print(f"Annual Income: ₹{annual_income:,.2f}")
print(f"Pre-approved: {is_eligible}")

# #3. Understanding data types
print("\n" + "=" * 50)
print("DATA TYPES EXPLAINED")
print("=" * 50)

print(f"\nString (text): {type(customer_name)} → '{customer_name}'")
print(f"Integer (whole number): {type(credit_score)} → {credit_score}")
print(f"Float (decimal): {type(annual_income)} → {annual_income}")
print(f"Boolean (yes/no): {type(is_eligible)} → {is_eligible}")

# #4. Real-world scenario — generating SMS
print("\n" + "=" * 50)
print("SMS NOTIFICATION")
print("=" * 50)

if is_eligible:
    sms_message = f"Congrats {customer_name}! Your score of {credit_score} qualifies you."
    print(f"\n📱 {sms_message}")
else:
    sms_message = f"Sorry {customer_name}, your score is too low."
    print(f"\n📱 {sms_message}")
