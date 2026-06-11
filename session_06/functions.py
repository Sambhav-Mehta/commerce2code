# Commerce2Code | Session 06
# Functions — def, parameters, return
# Real examples: Aadhaar verification · loan approval · tip calculator

print("=" * 55)
print("PART 1: WHAT IS A FUNCTION")
print("=" * 55)

# A function is a named, reusable block of code
# Define once — call anywhere, any number of times

def verify_aadhaar(aadhaar_number):
    number = int(aadhaar_number)
    if len(str(number)) == 12:
        return "Valid"
    return "Invalid"

print(f"\n{verify_aadhaar('123456789012')}")  # Valid
print(f"{verify_aadhaar('1234')}")            # Invalid
print("\nSame function. Different inputs. Called twice.")

print("\n" + "=" * 55)
print("PART 2: FUNCTION ANATOMY")
print("=" * 55)

# def        = keyword that defines a function
# name       = what you call it
# parameter  = placeholder for input
# body       = what it does
# return     = what it gives back

def check_eligibility(score):           # def + name + parameter
    if score >= 700:                    # body
        return True                     # return
    return False                        # return

print(f"\nScore 742 eligible: {check_eligibility(742)}")
print(f"Score 600 eligible: {check_eligibility(600)}")

print("\n" + "=" * 55)
print("PART 3: CALLING VS DEFINING")
print("=" * 55)

# def writes the recipe once
def calculate_tip(bill):
    return bill * 0.10

# Calling executes it — as many times as needed
print(f"\nTip on ₹2400 : ₹{calculate_tip(2400)}")
print(f"Tip on ₹850  : ₹{calculate_tip(850)}")
print(f"Tip on ₹1200 : ₹{calculate_tip(1200)}")
print("\nOne definition. Three calls. Zero repetition.")

print("\n" + "=" * 55)
print("PART 4: PARAMETERS AND ARGUMENTS")
print("=" * 55)

# Parameters = placeholders in the definition
# Arguments  = actual values passed when calling

def greet_customer(name, score):            # parameters
    return f"Hi {name}, your score is {score}"

print(f"\n{greet_customer('Sambhav', 742)}")    # arguments
print(f"{greet_customer('Priya', 810)}")
print(f"{greet_customer('Rahul', 650)}")

print("\n" + "=" * 55)
print("PART 5: RETURN KEYWORD")
print("=" * 55)

def loan_decision(score, income):
    eligible = score >= 700 and income >= 500000
    return eligible                 # hands back True or False

result1 = loan_decision(742, 1200000)
result2 = loan_decision(650, 300000)

print(f"\nloan_decision(742, 1200000) → {result1}")
print(f"loan_decision(650, 300000) → {result2}")

print("\n" + "=" * 55)
print("PART 6: FULL EXAMPLE — Everything in one function")
print("=" * 55)

# Sessions 01-05 working together inside one function
def process_application(name, score_text, income_text):
    score  = int(score_text)            # type conversion (S05)
    income = int(income_text)           # type conversion (S05)

    if score >= 700 and income >= 500000:  # operators + control flow (S03+S04)
        decision = "Approved"
    else:
        decision = "Rejected"

    return f"{name}: {decision} (score={score}, income=₹{income:,})"

print(f"\n{process_application('Sambhav', '742', '1200000')}")
print(f"{process_application('Priya',   '810', '800000')}")
print(f"{process_application('Rahul',   '620', '300000')}")
