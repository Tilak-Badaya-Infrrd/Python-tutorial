import random

value = random.random()
print(value)

value = random.uniform(1,10)
print(value)

value = random.randint(1,6)
print(value)

value = random.randint(0,1)
print(value)

greetings = ['Hello' , 'hi' , 'Hey' , 'Howdy' , 'Hola']

value = random.choice(greetings)
print(value)

results = random.choices(greetings, weights = [1,2,3,4,5],k=10)
print(results)


deck = list(range(1,53))
random.shuffle(deck)
print(deck)

hand = random.sample(deck,k=5)
print(hand)


