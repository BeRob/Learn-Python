types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# in der nächsten Zeile wird ein string in einem string genutzt
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}.")
print(f"I also said: '{y}'")

hilarious = False
acceptable = True
joke_evaluation = "isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))
print(joke_evaluation.format(acceptable))   # diese zeile habe ich zur
                                            # verständnis erstellt

w = "This is the left side of..."
e = "a string with right side."

print(w + e)
