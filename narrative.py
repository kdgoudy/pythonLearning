import random


def character_name():
  name = input('What do you want to name your character? ')
  return name


def race():
  race_options = ['elf', 'human', 'halfling']
  return random.choice(race_options)

def hair():
  hair_options = ['bald', 'short', 'medium', 'long']
  return random.choice(hair_options)

def ears():
  ear_options = ['pointy', 'rounded', 'small']
  return random.choice(ear_options)

def feet():
  feet_options = ['talons', 'human feet', 'hobbit feet']
  return random.choice(feet_options)





def create_character():
  name = character_name()
  return f"{name} is a {race()} with {hair()} hair, {ears()} ears, and {feet()}."

print(create_character())
