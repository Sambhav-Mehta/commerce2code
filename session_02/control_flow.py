# Commerce2Code | Session 02
# Control Flow — if, elif, else
# Real example: Swiggy Delivery Fee Calculator

# Customer order details
has_swiggy_one = False
order_value = 250
restaurant_distance_km = 4.5
is_raining = True

print("=" * 50)
print("SWIGGY DELIVERY FEE CALCULATOR")
print("=" * 50)
print(f"\nOrder Value     : ₹{order_value}")
print(f"Distance        : {restaurant_distance_km} km")
print(f"Swiggy One      : {has_swiggy_one}")
print(f"Raining         : {is_raining}")

print("\n" + "=" * 50)
print("DECISION ENGINE")
print("=" * 50)

# The decision tree — checked top to bottom
# First condition that is True wins. Rest are ignored.

if has_swiggy_one:
    delivery_fee = 0
    reason = "Swiggy One membership — always free"

elif order_value >= 299:
    delivery_fee = 0
    reason = "Order above ₹299 — free delivery unlocked"

elif restaurant_distance_km <= 2:
    delivery_fee = 15
    reason = "Restaurant nearby — reduced fee"

elif is_raining:
    delivery_fee = 60
    reason = "Raining outside — surge pricing applied"

else:
    delivery_fee = 30
    reason = "Standard delivery fee"

print(f"\nDelivery Fee : ₹{delivery_fee}")
print(f"Reason       : {reason}")
print(f"\nOrder Total  : ₹{order_value} + ₹{delivery_fee} = ₹{order_value + delivery_fee}")
