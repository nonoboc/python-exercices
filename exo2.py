"""Ecrire les chiffres de 1 a 100
Tous les mutliples de 3 - ecrire 'Fizz'  a la plce du chiffres
Tous les multiples de 5 ecrire 'Buzz' a la place du chiffre
Tous les multiples de 3 et 5 ecrire 'FizzBuzz' a la place du chiffre
(aller a la ligne entre chauwe chiffre)"""

  
  for k in range(1,101):
    if k%3==0 and k%5==0:
      print("FizzBuzz\n")
    elif k%3==0:
      print("Fizz\n")
    elif k%5==0:
      print("Buzz\n")
    else:
      print(k)
    return
