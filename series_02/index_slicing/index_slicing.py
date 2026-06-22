# ─────────────────────────────────────────────────────
# Commerce2Code · Series 02 · Post 04
# Topic: Index & Slicing in Python
# Author: Sambhav Mehta
# GitHub: github.com/Sambhav-Mehta/commerce2code
# ─────────────────────────────────────────────────────
# Real-world hook:
# Open BookMyShow. Tap a movie. The seat map loads —
# and four seats in the middle are already glowing,
# recommended for your group booking.
# That's not magic. That's slicing.
# ─────────────────────────────────────────────────────


# ── 1. The Seat Row as a List ────────────────────────
# Row F has 16 seats. Order in the list = physical order in the row.

seat_row = ["F1","F2","F3","F4",
            "F5","F6","F7","F8",
            "F9","F10","F11","F12",
            "F13","F14","F15","F16"]

print("Row F:", seat_row)
print()


# ── 2. INDEXING — One Seat at a Time ─────────────────
# Index starts at 0. Use it to grab a single seat.

first_seat = seat_row[0]     # "F1"  — first seat in the row
fifth_seat = seat_row[4]     # "F5"  — index 4 = 5th seat
last_seat  = seat_row[-1]    # "F16" — negative index counts from the end

print(f"First seat : {first_seat}")
print(f"5th seat   : {fifth_seat}")
print(f"Last seat  : {last_seat}")
print()

# Negative indexing is the real unlock —
# you never need to know the row's exact length to grab the last seat.
second_last = seat_row[-2]   # "F15"
print(f"2nd-to-last seat: {second_last}")
print()


# ── 3. SLICING — A Range of Seats ────────────────────
# list[start:stop] grabs items from start up to (NOT including) stop.

# BookMyShow's "recommended for your group" middle block
group_pick = seat_row[8:12]       # → ["F9","F10","F11","F12"]
print("Recommended group seats:", group_pick)

# Premium zone — first 4 seats of the row
premium_zone = seat_row[:4]       # → F1 to F4
print("Premium zone:", premium_zone)

# Recliner zone — last 4 seats of the row
recliner_zone = seat_row[-4:]     # → F13 to F16
print("Recliner zone:", recliner_zone)
print()


# ── 4. STEP — Skipping Through a Slice ───────────────
# list[start:stop:step] adds a 3rd value to skip seats.

aisle_seats = seat_row[::4]       # → F1, F5, F9, F13 (every 4th = aisle-adjacent)
print("Aisle-adjacent seats:", aisle_seats)


# ── 5. REVERSING — The Step Trick ────────────────────
reversed_row = seat_row[::-1]
print("Row reversed:", reversed_row)
print()


# ── 6. WHY THIS MATTERS — Quick Reference ────────────
print("── Index vs Slice ──")
print()
print("INDEX    → seat_row[4]     returns ONE item    → 'F5'")
print("SLICE    → seat_row[8:12]  returns A LIST       → ['F9'...'F12']")
print("NEGATIVE → seat_row[-1]    counts from the end  → 'F16'")
print("STEP     → seat_row[::4]   skips through items  → every 4th seat")
print("REVERSE  → seat_row[::-1]  flips the whole list")
print()
print("The pattern behind every app that shows you a 'recommended' selection,")
print("a top-5 list, or a last-3-orders view — it's almost always a slice.")
