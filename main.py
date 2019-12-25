import sys
import time


def rstart():

  def type(statement):
      for x in statement:
          sys.stdout.write(x)
          sys.stdout.flush()
          time.sleep(0.069)

  def n():
    print('\n')



  one="Panda"
  two="Beautiful"
  three="Umbrella"
  four="MilkTea"
  five="Aristocracy"

  print("Welcome to H # N G M A N")
  time.sleep(3)
  n()
  print("There are 5 words/phrases to choose to guess: 1 2 3 4 5")
  n()
  time.sleep(6)
  print("You have 12 tries for each word.")
  time.sleep(4)
  n()

  while True:
    player_pickle=input("Input a number to choose your word: ")
    if player_pickle not in ("1","2","3","4","5"):
      print("Give me a number from 1 to 5. Not your password.")
    else:
      break
  time.sleep(2)
  n()


  if int(player_pickle)==1:
    answer="Panda"
    number=5
    numberz=5
  elif int(player_pickle)==2:
    answer="Beautiful"
    number=9
    numberz=9
  elif int(player_pickle)==3:
    answer="Umbrella"
    number=8
    numberz=8
  elif int(player_pickle)==4:
    answer="MilkTea"
    number=7
    numberz=7
  elif int(player_pickle)==5:
    answer="HoQuanPhu"
    number=9
    numberz=9

  print("Here is your mystery word:")
  time.sleep(1)
  anzwer="_ "*int(number)
  n()
  print(anzwer)
  n()
  tries=12
  time.sleep(2)

  if int(player_pickle)==1:
    while tries!=0 and numberz!=0:

      guess=input("Guess?: ")

      if guess.lower()==answer[0] or guess.upper()==answer[0]:
        numberz-=1
        n
        tries-=1
        anzwer=answer[0]+anzwer[1:] 
        n()
        print(anzwer)
        n()
      

      elif guess.lower()==answer[1] or guess.upper()==answer[1]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:2]+answer[1]+anzwer[3:]
        if int(player_pickle)==1:
          numberz-=1
          n
          anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[2] or guess.upper()==answer[2]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:4]+answer[2]+anzwer[5:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[3] or guess.upper()==answer[3]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:6]+answer[3]+anzwer[7:]
        n()
        print(anzwer)
        n()   
      
      
      else:
        print("Wrong!")
        n()
        tries-=1

  if int(player_pickle)==2:
    while tries!=0 and numberz!=0:

      guess=input("Guess?: ")

      if guess.lower()==answer[0] or guess.upper()==answer[0]:
        numberz-=1
        n
        tries-=1
        anzwer=answer[0]+anzwer[1:] 
        n()
        print(anzwer)
        n()
      

      elif guess.lower()==answer[1] or guess.upper()==answer[1]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:2]+answer[1]+anzwer[3:]
        if int(player_pickle)==1:
          numberz-=1
          n
          anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[2] or guess.upper()==answer[2]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:4]+answer[2]+anzwer[5:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[3] or guess.upper()==answer[3]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:6]+answer[3]+anzwer[7:]
        if int(player_pickle)==2:
          anzwer=anzwer[0:14]+answer[7]+anzwer[15:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()   
      
      elif guess.lower()==answer[4] or guess.upper()==answer[4]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[5] or guess.upper()==answer[5]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:10]+answer[5]+anzwer[11:]
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[6] or guess.upper()==answer[6]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:12]+answer[6]+anzwer[13:]
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[8] or guess.upper()==answer[8]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:16]+answer[8]+anzwer[17:]
        n()
        print(anzwer)
        n()  
      
      else:
        print("Wrong!")
        n()
        tries-=1

  if int(player_pickle)==3:   
    while tries!=0 and numberz!=0:

      guess=input("Guess?: ")

      if guess.lower()==answer[0] or guess.upper()==answer[0]:
        numberz-=1
        n
        tries-=1
        anzwer=answer[0]+anzwer[1:] 
        n()
        print(anzwer)
        n()
      

      elif guess.lower()==answer[1] or guess.upper()==answer[1]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:2]+answer[1]+anzwer[3:]
        if int(player_pickle)==1:
          numberz-=1
          n
          anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[2] or guess.upper()==answer[2]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:4]+answer[2]+anzwer[5:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[3] or guess.upper()==answer[3]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:6]+answer[3]+anzwer[7:]
        if int(player_pickle)==2:
          anzwer=anzwer[0:14]+answer[7]+anzwer[15:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()   
      
      elif guess.lower()==answer[4] or guess.upper()==answer[4]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[5] or guess.upper()==answer[5]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:10]+answer[5]+anzwer[11:]
        if int(player_pickle)==3:
          anzwer=anzwer[0:12]+answer[6]+anzwer[13:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[7] or guess.upper()==answer[7]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:14]+answer[7]+anzwer[15:]
        n()
        print(anzwer)
        n()  
      
      else:
        print("Wrong!")
        n()
        tries-=1

  if int(player_pickle)==4:   
    while tries!=0 and numberz!=0:

      guess=input("Guess?: ")

      if guess.lower()==answer[0] or guess.upper()==answer[0]:
        numberz-=1
        n
        tries-=1
        anzwer=answer[0]+anzwer[1:] 
        n()
        print(anzwer)
        n()
      

      elif guess.lower()==answer[1] or guess.upper()==answer[1]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:2]+answer[1]+anzwer[3:]
        if int(player_pickle)==1:
          numberz-=1
          n
          anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[2] or guess.upper()==answer[2]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:4]+answer[2]+anzwer[5:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[3] or guess.upper()==answer[3]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:6]+answer[3]+anzwer[7:]
        if int(player_pickle)==2:
          anzwer=anzwer[0:14]+answer[7]+anzwer[15:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()   
      
      elif guess.lower()==answer[4] or guess.upper()==answer[4]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[5] or guess.upper()==answer[5]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:10]+answer[5]+anzwer[11:]
        if int(player_pickle)==3:
          anzwer=anzwer[0:12]+answer[6]+anzwer[13:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[6] or guess.upper()==answer[6]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:12]+answer[6]+anzwer[13:]
        n()
        print(anzwer)
        n()  
      
      else:
        print("Wrong!")
        n()
        tries-=1

  if int(player_pickle)==5:   
    while tries!=0 and numberz!=0:

      guess=input("Guess?: ")

      if guess.lower()==answer[0] or guess.upper()==answer[0]:
        numberz-=1
        n
        tries-=1
        anzwer=answer[0]+anzwer[1:] 
        if int(player_pickle)==5:
          anzwer=anzwer[0:14]+answer[7]+anzwer[15:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()
      

      elif guess.lower()==answer[1] or guess.upper()==answer[1]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:2]+answer[1]+anzwer[3:]
        if int(player_pickle)==1:
          numberz-=1
          n
          anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[2] or guess.upper()==answer[2]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:4]+answer[2]+anzwer[5:]
        n()
        print(anzwer)
        n()   
      

      elif guess.lower()==answer[3] or guess.upper()==answer[3]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:6]+answer[3]+anzwer[7:]
        if int(player_pickle)==2:
          anzwer=anzwer[0:14]+answer[7]+anzwer[15:]
          numberz-=1
          n
        if int(player_pickle)==5:
          anzwer=anzwer[0:16]+answer[8]+anzwer[17:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()   
      
      elif guess.lower()==answer[4] or guess.upper()==answer[4]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:8]+answer[4]+anzwer[9:]
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[5] or guess.upper()==answer[5]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:10]+answer[5]+anzwer[11:]
        if int(player_pickle)==3:
          anzwer=anzwer[0:12]+answer[6]+anzwer[13:]
          numberz-=1
          n
        n()
        print(anzwer)
        n()  

      elif guess.lower()==answer[6] or guess.upper()==answer[6]:
        numberz-=1
        n
        tries-=1
        anzwer=anzwer[0:12]+answer[6]+anzwer[13:]
        n()
        print(anzwer)
        n()  
      
      else:
        print("Wrong!")
        n()
        tries-=1

  if tries==0 and numberz!=0:
    print("You ran out of tries! ")
    time.sleep(1)
    n()
    print("Want to try a different word? Simply restart the game. If not, thanks for playing!")
    time.sleep(1)
    n()
    print("~ ")
   
        


  if numberz==0:
    print("SuCcEsS!")
    n()
    time.sleep(1)
    print("Want to try a different word? Simply restart the game. If not, thanks for playing!")
    time.sleep(1)
    n()
    print("~ ")


rstart();
