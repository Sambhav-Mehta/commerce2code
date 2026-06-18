# ─────────────────────────────────────────────────────
# Commerce2Code · Series 02 · Post 02
# Topic: Dictionaries in Python
# Author: Sambhav Mehta
# GitHub: github.com/Sambhav-Mehta/commerce2code
# ─────────────────────────────────────────────────────
# Real-world hook:
# When you check in on IndiGo, the app knows your seat,
# meal, class, and boarding status — all at once.
# That's not a list. That's a dictionary.
# ─────────────────────────────────────────────────────


# ── 1. CREATING A DICTIONARY ─────────────────────────
# A dictionary stores data as key: value pairs.
# Each key is a label. Each value is the actual data.

my_booking = {
    "passenger": "Sambhav Mehta",
    "flight":    "6E-345",
    "from":      "Mumbai",
    "to":        "Delhi",
    "seat":      "12A",
    "class":     "Economy",
    "meal":      "Veg",
    "status":    "Checked In"
}

print("── Booking created ──")
print(my_booking)
print()


# ── 2. ACCESS ────────────────────────────────────────
# Use the key (label) to get the value.
# No guessing positions like a list — just use the name.

seat = my_booking["seat"]
print(f"Seat: {seat}")           # → 12A

meal = my_booking["meal"]
print(f"Meal preference: {meal}")  # → Veg
print()


# ── 3. UPDATE ────────────────────────────────────────
# Change the value of an existing key.

my_booking["status"] = "Boarding"
print(f"Updated status: {my_booking['status']}")  # → Boarding
print()


# ── 4. ADD ───────────────────────────────────────────
# Add a brand new key-value pair — key didn't exist before.

my_booking["gate"] = "B4"
print(f"Gate added: {my_booking['gate']}")  # → B4
print()


# ── 5. DELETE ────────────────────────────────────────
# Remove a key and its value permanently.

del my_booking["meal"]
print("After deleting meal preference:")
print(my_booking)
print()


# ── 6. CHECK IF KEY EXISTS ───────────────────────────
# Useful before accessing, to avoid KeyError.

if "meal" in my_booking:
    print(f"Meal: {my_booking['meal']}")
else:
    print("No meal preference on file.")   # → prints this
print()


# ── 7. LOOP THROUGH A DICTIONARY ─────────────────────
# .items() gives you both key and value together.

print("── Full booking summary ──")
for key, value in my_booking.items():
    print(f"  {key}: {value}")
print()


# ── 8. LIST vs DICTIONARY — SIDE BY SIDE ─────────────

# List: order-based, no labels
booking_as_list = ["12A", "Economy", "Checked In"]
print(f"List[0] = {booking_as_list[0]}")   # You have to remember index 0 = seat

# Dictionary: label-based, self-describing
booking_as_dict = {"seat": "12A", "class": "Economy", "status": "Checked In"}
print(f"Dict['seat'] = {booking_as_dict['seat']}")  # Clear. No guessing.
print()

print("Use a list when:  items are all the same kind, order matters.")
print("Use a dict when:  each item means something different, you look up by name.")
