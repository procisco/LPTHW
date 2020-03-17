name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# convert the height from inches to centemeters
height_in_cm = height / 0.39370
weight_in_kilos = weight / 2.2046
print(f"His height in inches is {height}, and in centemeters is {height_in_cm}. Let's round that off to {round(height_in_cm)} centemeters.")
print(f"His weight in pounds is {weight}, and in kilograms is {weight_in_kilos}. Let's round that off to {round(weight_in_kilos)} kilograms.")
