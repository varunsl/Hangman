import random

def choose_word():
#converts random word from list into blanks
  text_file = open("wordlist.txt", "r")
  word_list = text_file.read().split('\n')
  text_file.close()
  word = word_list[random.randint(0,len(word_list))]
  blanks = ["_"] * len(word)
  return word, blanks

def search_string(string, character):
#stores all occurrences of a character in a string to a list
  char_occurrences = []
  for index, item in enumerate(string):
    if item == character:
      char_occurrences.append(index)
  return char_occurrences

def check_guess(word, blanks, guess, wrong_guesses):
  if len(guess) == 1 and guess.isalpha():
  #checks for single letter input
    if guess in word:
    #if the guess is in the word, replace the corresponding blanks with the guess
      for x in search_string(word, guess):
        blanks[x] = guess
    else:
      wrong_guesses.append(guess)
  else:
    print "Invalid Input"

def draw_hangman(wrong_guesses):
  if len(wrong_guesses) == 0:
    print "  ____"
    print " |    |"
    print " |"
    print " |"
    print " |"
    print "[ ]"
  elif len(wrong_guesses) == 1:
    print "  ____"
    print " |    |"
    print " |    O"
    print " |"
    print " |"
    print "[ ]"
  elif len(wrong_guesses) == 2:
    print "  ____"
    print " |    |"
    print " |    O"
    print " |    |"
    print " |"
    print "[ ]"
  elif len(wrong_guesses) == 3:
    print "  ____"
    print " |    |"
    print " |    O"
    print " |    |"
    print " |   / "
    print "[ ]"
  elif len(wrong_guesses) == 4:
    print "  ____"
    print " |    |"
    print " |    O"
    print " |    |"
    print " |   / \\"
    print "[ ]"
  elif len(wrong_guesses) == 5:
    print "  ____"
    print " |    |"
    print " |    O"
    print " |   /|"
    print " |   / \\"
    print "[ ]"
  elif len(wrong_guesses) == 6:
    print "  ____"
    print " |    |"
    print " |    O"
    print " |   /|\\"
    print " |   / \\"
    print "[ ]"

def update_screen(blanks, wrong_guesses):
#updates blanks, hangman, guesses
  draw_hangman(wrong_guesses)
  print ' '.join(blanks)
  if wrong_guesses == []:
    print "Wrong guesses: none"
  else:
    print "Wrong guesses: " + ', '.join(wrong_guesses)

def main():
  playing = True
  while playing == True:
    word, blanks = choose_word()
    wrong_guesses = []
    draw_hangman(wrong_guesses)
    print ' '.join(blanks)
    while "_" in blanks != False:
      guess = raw_input("Guess a letter:")
      guess = guess.lower()
      check_guess(word, blanks, guess, wrong_guesses)
      update_screen(blanks, wrong_guesses)
      if len(wrong_guesses) == 6:
        break
    if len(wrong_guesses) <= 5:
      print "You win!"
    else:
      print "You lose! The word was " + word + "."
    again = raw_input("Play again? (y/n)")
    again = again.lower()
    if again == "y":
      playing = True
    else:
      playing = False

main()
