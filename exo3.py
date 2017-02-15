# exercice en python 2 (pas 3)
#faire une fonction "invert_string" qui prend une chaine de caracteres et revoie cette chaine a l'envers

def invert_string(name):
  return name #fixme

assert invert_string('nadir') == 'ridan', "should return ridan for nadir"


#faire une autre fonction qui utilise invert_string sur les elements d'un tableau et renvoie un tableau de noms a l'envers

def invert_array(arr):
  return arr #fixme

users = ['toto', 'titi', 'tata']
res = invert_array(users)
print res
assert res[0] == 'otot', "first element should be otot"
assert res[1] == 'itit', "second element should be itit"
assert res[2] == 'atat', "third element should be atat"
