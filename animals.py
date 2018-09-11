class Tetrapoda:
  spine = true
  leg = 4
class Birds(Tetrapoda):
  plumage = true
  child = egg
class Theria(Tetrapoda):
  child = viviparous
  children_food = milk
class Home_Animals:
  locality = farme
  feed = true
class Cow(Theria, Home_Animals):
  weight > 350 #кг
  voice = 'му му'
  use =cow_milk
  feed = hay
class Goat(Theria, Home_Animals):
 35 < weight < 50 #кг
 voice = 'ме ме'
 use = goat_milk
 feed = hay
class  Sheep (Theria, Home_Animals):
  45 < weight < 100 #кг
  voice = 'бе бе'
  use = wool
  feed = hay
class  Pig (Theria, Home_Animals):
  150 < weight < 300 #кг
  voice = 'бе бе'
  use = meat
  feed = forage
class  Duck (Birds, Home_Animals):
  1,5 < weight < 3 #кг
  voice = 'кря кря'
  use = meat
  feed = mixed_fodder
class  Goose (Birds, Home_Animals):
  5 < weight < 10 #кг
  voice = 'га га'
  use = meat
  feed = mixed_fodder
class  Goose (Birds, Home_Animals):
  2 < weight < 5 #кг
  voice = 'ко ко'
  use = egg
  feed = mixed_fodder