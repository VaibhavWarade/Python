

import random
import words
import stages

end_of_game = False
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

print(stages.logo)

display = []
for _ in range(word_length):
    display += "_"
lives=6
while not end_of_game:
    print('\n********************************\n')
    guess = input("Guess a letter: ").lower()
    found=0
  
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            found+=1
   
    
    if found==0 and lives>0:
        lives-=1
    else:
        print("You Lose")   
        print(stages.death_bringer)
        print("\n Correct Word was "+chosen_word)
        end_of_game = True
    
    print(f"{' '.join(display)}")
    win=0
    
    if "_" not in display:
        end_of_game = True
        print("You win. ヽ(´▽`)/ ")
        win=1
        print(stages.win_cup)
        exit()
    if win!=1:
        print('\n-------------------------------------\n')
        print(stages.stages[lives])
        
