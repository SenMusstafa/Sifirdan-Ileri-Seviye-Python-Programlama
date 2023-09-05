import random

def random_module_example():
    result = dir(random)

    # result = random.random()  # Generates a number between 0.0 and 1.0
    result = random.random() * 100  # Generates a number between 0.0 and 100.0
    result = random.uniform(1, 10)  # Generates a decimal number between 1 and 10
    result = int(random.uniform(1, 10))  # Generates a whole number between 1 and 10
    result = random.randint(1, 100)  # Generates a whole number between 1 and 100
    greeting = 'Hello There'
    names = ['Victor', 'Sérgio', 'Abdülkerim', 'Sacha', 'Kaan', 'Léo']
    # result = names[random.randint(0, len(names) - 1)]
    result = random.choice(names)  # Picks a random element from the list
    result = random.choice(greeting)  # Picks a random character from 'Hello There'

    liste = list(range(10))
    random.shuffle(liste)  # Shuffles the elements in the list randomly
    result = liste

    liste = range(100)
    result = random.sample(liste, 3)  # Selects 3 random numbers from the list
    result = random.sample(names, 2)  # Selects 2 random names from the list

    print(result)

if __name__ == "__main__":
    random_module_example()
