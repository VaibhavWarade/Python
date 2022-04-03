import random
rint=input("Choose H or T \n")
if random.choice('H''T')=='H':
      print("Heads")
      if(rint=='H'):
            print("You Win!! ʘ‿ʘ")
      else:
            print("You Loose ಥ_ಥ")
else :
      print("Tails")  
      if(rint=='T') :
            print("You Win!! ʘ‿ʘ")
      else:
        print("You Loose ಥ_ಥ")
