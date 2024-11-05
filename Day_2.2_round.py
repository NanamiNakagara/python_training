# # Task 2.2: With f-string | Clue: round()
# # Fahrenheit to celsius
# # Please provide your Fahrenheit: 100
# # The 100°F is 37.78°C

a=input('Please provide your Fahrenheit:')
b= (float(a) - 32) * (5/9)
print(f'the {a}°F is {round(b, 3)}°C')