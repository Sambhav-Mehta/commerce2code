# ─────────────────────────────────────────────────────
# Commerce2Code · Series 02 · Post 06 — THE PAYOFF
# Topic: Every data structure from Series 02, working together
# Author: Sambhav Mehta
# GitHub: github.com/Sambhav-Mehta/commerce2code
# ─────────────────────────────────────────────────────
# Real-world hook:
# I built a working cart system.
# Here's every data structure doing its job together.
# ─────────────────────────────────────────────────────

import json
import random


# ── THE MENU — a DICT ────────────────────────────────
# Post 02: key:value pairs. Look up a price by name, instantly.

menu = {
    "Biryani":      249,
    "Lassi":        79,
    "Gulab Jamun":  99,
    "Butter Naan":  49,
    "Paneer Tikka": 219
}

# A second dict — every item also belongs to a category
item_category = {
    "Biryani":      "Food",
    "Lassi":        "Beverages",
    "Gulab Jamun":  "Dessert",
    "Butter Naan":  "Food",
    "Paneer Tikka": "Food"
}


# ── THE CART — a LIST ────────────────────────────────
# Post 01: order matters. Same item can be added twice.

cart_items = []

def add_to_cart(item_name):
    cart_items.append(item_name)
    print(f"Added: {item_name}  (₹{menu[item_name]})")

add_to_cart("Biryani")
add_to_cart("Lassi")
add_to_cart("Gulab Jamun")
add_to_cart("Biryani")     # ordering the biryani twice — lists allow this

print(f"\nCart: {cart_items}")


# ── THE TOTAL — DICT lookup inside a LIST ────────────
total = sum(menu[item] for item in cart_items)
print(f"Total: ₹{total}\n")


# ── FIRST / LAST / RECENT — INDEX & SLICING ──────────
# Post 04: grabbing items by position, not by searching.

first_item     = cart_items[0]      # → "Biryani"
last_item      = cart_items[-1]     # → "Biryani" (the 2nd one added)
last_two_added = cart_items[-2:]    # → preview the 2 most recent adds

print(f"First item added : {first_item}")
print(f"Last item added  : {last_item}")
print(f"Last 2 added     : {last_two_added}\n")


# ── UNIQUE CATEGORIES — a SET ────────────────────────
# Post 03: even with 2 "Food" items in the cart, the category
# appears once. Sets don't care how many times something repeats.

categories_in_cart = {item_category[item] for item in cart_items}
print(f"Categories in this cart: {categories_in_cart}\n")


# ── THE ORDER ID — a TUPLE ───────────────────────────
# Post 03: fixed the moment checkout starts. Never changes after.

order_id = (f"TXN{random.randint(10000,99999)}", "Sambhav's Kitchen")
print(f"Order locked: {order_id}")

try:
    order_id[0] = "HACKED"          # try to tamper with it
except TypeError as e:
    print(f"Cannot modify order_id: {e}\n")


# ── CHECKOUT — Converting everything to JSON ─────────
# Post 05: before this order leaves your app and reaches the
# restaurant's server, it has to become plain text. Every
# structure above collapses into one JSON packet.

order = {
    "order_id":   order_id[0],
    "restaurant": order_id[1],
    "items":      cart_items,                 # the list
    "total":      total,
    "categories": list(categories_in_cart)    # sets aren't valid JSON — convert to list
}

order_json = json.dumps(order, indent=2)

print("── Final checkout payload (sent to the kitchen) ──")
print(order_json)


# ══════════════════════════════════════════════════════
# THE PAYOFF — every Series 02 concept, one program:
# ══════════════════════════════════════════════════════
print("\n── Series 02, end to end ──")
print("LIST    → cart_items, the order itself")
print("DICT    → menu, instant price & category lookup")
print("TUPLE   → order_id, locked the moment checkout starts")
print("SET     → categories_in_cart, no duplicates no matter what")
print("INDEX/SLICE → first/last/recent items, by position")
print("JSON    → the final packet, leaving your app for good")
