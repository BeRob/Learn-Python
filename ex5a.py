# format strings
# alles was zwischen "..." steht ist ein strings
# in dieser Übung lernen wir strings die variablen enthalten

name = 'Robert Benner'
age = 25 # lie
height = 182 # cm
weight = 78 # kg
eyes = 'Blue-grey'
dick = 'very long'
hair = 'brown'

weight_pounds = weight * 2.2
height_inch = height * 0.39
print(f"Let's talk about {name}.")
print(f"He's {height_inch} inches tall.")
print(f"He's {weight_pounds} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His dick is {dick} depending on the bitch.")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")
