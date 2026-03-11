# List of inputs that user and computer will select from 
choices = {"1":"Rock", "2": "Paper", "3": "Scissors"}


print("Welcome to rock paper scissors game!\n")

game_active = True 
scores = {"Player": 0, "Computer": 0} 


# Outcomes of the Round, Adds 1 point to winner of the round, no points for draw or losers
def outcomes(player_weapon,computer_weapon):
    if player_weapon == "Rock" and computer_weapon == "Scissors":

        print(f"Player's {player_weapon} wins the round!\n")
        scores["Player"] +=1

    elif player_weapon == "Paper" and computer_weapon == "Rock":

        print(f"Player's {player_weapon} wins the round!\n")
        scores["Player"] +=1

    elif player_weapon == "Scissors" and computer_weapon == "Paper":

        print(f"Player's {player_weapon} wins the round!\n")
        scores["Player"] +=1

    elif player_weapon == computer_weapon:
        print(f"Draw!: Both players chose {player_weapon}\n")

    else:
        print(f"Computer's {computer_weapon} wins the round!\n")
        scores["Computer"] +=1


# Functioin Built to Check the Winner of the Game! 
# Requests user if they want to play again
def determine_game_winner(scores):
    
    if scores["Player"] == 3 or scores["Computer"] == 3:
        
        print("------------------------") 
        print ("Game Over! Final Scores:")
        print("------------------------")
        print(f"Player : {scores["Player"]}")
        print(f"Computer : {scores['Computer']}\n")
        print("------------------------")

        play_again = input("Do you want to play again? ")
        

        # Asks user if they want to play again
        if play_again.upper() == 'Y':
            scores["Player"] = 0
            scores["Computer"] = 0
            print("New Game!\n")
        else:
            print("/n Game Over!")
            exit()



while game_active: 
   
    print(f"Player Score: {scores["Player"]}\t Computer Score: {scores["Computer"]}")
    
    player_choice = input ("Select 1 = Rock, 2 = Paper, or 3 = Scissors: ")
    print("\n")
    # We convert choices.keys() into list to allow the computer to choose randomly.
    computer_choice = rand.choice(list(choices.keys()))
    
    # Prints out the value of choices dictoianry for each player.
    if player_choice in choices.keys():
        
        print(f"Player chose: {choices[player_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")
  
        player_weapon = choices[player_choice] 
        computer_weapon = choices[computer_choice]
        
        # Calls on outcomes function to determine choice outcome
        outcomes(player_weapon,computer_weapon)

        # Calls check_winner to check if we have winner
        determine_game_winner(scores)
    else:
        # Invalid input 
        print("Invalid Input! Try Again!\n")
   
  
    
        
        

 




