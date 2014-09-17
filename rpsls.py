#!/usr/bin/python

import random
import os
import sys

os.system('clear')

# choices for rpsls
choices = ["rock", "paper", "scissors", "lizard", "spock"]
comp_score = 0;
user_score = 0;

# Win actions
actions = {
  "rock": {
    "scissors": "crushes",
    "lizard": "crushes"
  },
  "paper": {
    "rock": "covers",
    "spock": "disproves"
  },
  "scissors": {
    "paper": "cuts",
    "lizard": "decapitates"
  },
  "lizard": {
    "spock": "poisons",
    "paper": "eats"
  },
  "spock": {
    "rock": "vaporizes",
    "scissors": "smashes"
  }
};

# Function to display the game scores
def display_score(comp_score, user_score):
  print("\nComp: {}".format(comp_score))
  print("User: {}\n".format(user_score))
  
def display_choices(comp_choice, user_choice):
  print("\nComp chooses: {}".format(comp_choice))
  print("User chooses: {}\n".format(user_choice))  

# Function to get the choice from the user
def user_choice_input():
  print('Type "exit" to end the game');
  user_choice = input("Choose by number: 1)rock, 2)paper, 3)scissors, 4)lizard, 5)spock \n?> ")

  if user_choice == "exit":
    os.system('clear')
    print("The final score is...")
    display_score(comp_score, user_score)
    print("Thanks for playing!")
    exit();

  user_choice_int = int(user_choice) - 1;  
  return user_choice_int

def validate_choices(comp_choice, user_choice):
  
  # Run through the logic to see who wins or loses.
  if comp_choice == "rock":
    if user_choice == "lizard" or user_choice == "scissors":
      winner = -1
    elif user_choice == "spock" or user_choice == "paper":
      winner = 1
    else:
      winner = 0    

  elif comp_choice == "paper":
    if user_choice == "rock" or user_choice == "spock":
      winner = -1
    elif user_choice == "scissors" or user_choice == "lizard":
      winner = 1
    else:
      winner = 0    

  elif comp_choice == "scissors":
    if user_choice == "paper" or user_choice == "lizard":
      winner = -1
    elif user_choice == "rock" or user_choice == "spock":
      winner = 1
    else:
      winner = 0    

  elif comp_choice == "lizard":
    if user_choice == "paper" or user_choice == "spock":
      winner = -1
    elif user_choice == "rock" or user_choice == "scissors":
      winner = 1
    else:
      winner = 0    

  elif comp_choice == "spock":
    if user_choice == "scissors" or user_choice == "rock":
      winner = -1
    elif user_choice == "paper" or user_choice == "lizard":
      winner = 1
    else:
      winner = 0
      
  # Returns the winner      
  return winner
  
def display_output_message(winner_choice, loser_choice, actions):
    print("{} {} {}".format(winner_choice, actions[winner_choice][loser_choice], loser_choice))
  
while True:
  # Computer chooses.
  comp_choice = random.choice(choices)
  
  user_choice = -1;
  
  while(user_choice == -1 or user_choice < 0 or user_choice > 5):
  
    # User Chooses
    user_choice = user_choice_input();
    os.system('clear')
  
  winner = validate_choices(comp_choice, choices[user_choice])
  
  display_choices(comp_choice, choices[user_choice])
  
  if winner == -1:
    comp_score = comp_score + 1;
    display_output_message(comp_choice, choices[user_choice], actions)
    
  elif winner == 1:
    user_score = user_score + 1;
    display_output_message(choices[user_choice], comp_choice, actions)
  else:
    print("You both chose the same, and therefore is a tie!")
    
  display_score(comp_score, user_score)  