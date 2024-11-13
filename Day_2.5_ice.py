ice = input("what do you want ice?🍧🍦🍨").lower().strip()

# Shop
stock1 = "vanilla"
stock2 = "green tea"
stock3 = "lemon"
stock4 = "chocolate"

# Case 1
# Yes, we have vanilla in stock

# if ice == stock1 :
#     print(f'Yes,we have {ice} in stock')
# elif ice== stock2:
#     print(f'Yes, we have {ice} in stock')
# elif ice== stock3:
#     print(f'Yes, we have {ice} in stock')
# elif ice== stock4:
#     print(f'Yes, we have {ice} in stock')
# else :
#     print(f'sorry.we ran out of {ice}')


# Case 2:
# "orange"
# Sorry, we ran out of orange

# Task 1.2
# Clue: Logical Operators (or)


# # or operator
# print(5 > 3 or 5 < 4) # True or False -> True


# if (ice==stock1) or (ice==stock2) or (ice==stock3) or (ice==stock4)  :
#     print(f'Yes,we have {ice} in stock')
# else :
#     print(f'sorry.we ran out of {ice}')

if ice in [stock1, stock2, stock3, stock4]:
    print(f"Yes,we have {ice} in stock❤️‍🔥")
else:
    print(f"sorry.we ran out of {ice}😭😭")
