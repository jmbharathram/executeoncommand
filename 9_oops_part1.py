class Avengers:

  __team = []
  _name = "Avengers"
  headquarters = "890 Fifth Avenue, Manhattan, New York City, NY" 

  def __init__(self, director):
    self._director = director

  def get_name(self):
    return Avengers._name

  def get_director(self):
    return self._director

  def add_hero(self, hero):
    Avengers.__team.append(hero)

  def show_team(self):
    print(Avengers.__team)

class NickFury(Avengers):

  def __init__(self):

    self.original_name = "Nicholas Joseph Fury"
    self.birth_place = "Alabama"
    self.health = 100

class Talos(Avengers):

  def __init__(self):

    self.original_name = "Talos the Skrull"
    self.birth_place = "Tarnax IV"
    self.health = 100

nf = NickFury()
av1 = Avengers(nf.original_name)
print(av1.headquarters)
print(av1._director)

ta = Talos()
av2 = Avengers(ta.original_name)
print(av2.headquarters)
print(av2._director)

#nf.add_hero("Captain America")
#nf.show_team()
