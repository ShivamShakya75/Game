import random

def gamewin(you,me):
    if you == me:
        return none
    elif you == 's':
        if me == 'c':
       return false
   elif me == 'p':
            return true

    elif you == 'p':
        if me == 's':
            return false
        elif me == 'c':
            return true

        elif you == 'c':
        if me == 'p':
        return false
         elif me =='s':
             return true

print("you: stone(s) paper(p) or scissor(c) ?" )
randno = random.randint(1,3)
      if randno == 1:
          you = s
      elif randno == 2:
          you = p
       elif randno == 3:
           you = c

me = input("me: stone(s) paper(p) or scissor(c) ?")


a = gamewin(you,me)

print(f"you choose {you} ")
print(f"me choose {me} ")

if you == me:
     print("this game is tie")
elif a:
    print("you win")
else:
    print("you loose")





