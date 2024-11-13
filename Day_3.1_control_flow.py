# Task - 1
# Expected output
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥
# fire_rows = int(input("How many rows?"))
# a = 1
# while a <= fire_rows:
#     print("🔥" * a)
#     a = a + 1

# Task - 1.2
# # Get number of rows from user

# fire_rows = int(input("How many rows?"))
# pattern = input("How many rows?")
# a = 1
# while a <= fire_rows:
#     odd_num = 2 * a - 1
#     spaces = fire_rows - a
#     print(" " * (spaces) + pattern * (odd_num))
#     a = a + 1


fire_rows = int(input("How many rows?"))
for fire_roes in range(1, 4):
    print(fire_rows)

rows = int(input("How many rows?"))
emoji = input("select emoji?")

for i in range(1, rows + 1):
    print(emoji * i)
