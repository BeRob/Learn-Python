# format strings
# alles was zwischen "..." steht ist ein strings
# in dieser Übung lernen wir strings die variablen enthalten

my_name = 'Robert Benner'
my_age = 25 # lie
my_height = 182 # cm
my_weight = 78 # kg
my_eyes = 'Blue-grey'
my_dick = 'very long'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height}cm tall.")
print(f"He's {my_weight}kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His dick is {my_dick} depending on the bitch.")

total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height} and {my_weight} I get {total}.")
