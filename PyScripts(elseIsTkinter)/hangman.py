from random import randint 
from time import sleep


def turn(player_lives: int, player_name: str, sentence: str, sentence_out: str) -> list: # [state_of_choice, reformed_sentence, lives_to_remove]
	found = False
	letters = "qwertzuiopasdfghjklyxcvbnm"
	counter = 0
	if player_lives > 0:
		letter = input(f"{player_name}, please enter a letter: ")
		if len(letter) == 1 and letter in letters:
			for i in range(len(sentence)):
				if sentence.lower()[i] == letter:
					found = True
					sentence_out = sentence_out[:i] + letter + sentence_out[i+1:]
					counter += 1
		elif len(letter) > 1:
			if letter.lower() == sentence.lower():
				return ["correct_sentence", sentence_out, 0]
			else:
				return ["incorrect", sentence_out, 1]
		else:
			return ["incorrect", sentence_out, 1]
	if found:
		return ["correct", sentence_out, counter] # return[2] -> Num of letter appearences
	else:
		return ["incorrect", sentence_out, 1]


def count(sentence: str) -> int:
	counter = 0
	for i in sentence: 
		if i == '*':
			counter += 1
	return counter



def game(player_1: str, player_2: str) -> None:

	pl_1_lives = 3
	pl_2_lives = 3

	sentences = [
		"Politicians in croatia are dumb", 
		"I can not believe you are acctually playing this",
		"Bruh just do something useful",
		"Assume penguin is a cylindrical object",
		"Chess is a great game that improves your brain functions",
		"People are living in a simulation",
		"People are acctually very similar to artificial intelligence",
		"Writing this without API makes me wanna die",
		"Can not wait to find help with creating sentences"
	] #TODO -> Try taking data from some API instead making your own sentences

	print (f"Hello, today {player_1} will be playing hangman against {player_2}.\n")
	sleep(5)
	print(f"1. Every single one of you will have a choice to pick a letter until you find the sentence .\n")
	sleep(5)
	print(f"2. Every correct letter gives you letter appearence points and every correct sentence gives you\n that points that are left in a sentence(exact number of letters left)\n")
	sleep(7)
	print("If you enter more than one letter it is considered as an sentence input (until I upgrade code)")
	print("\nSTARTING NOW, GLHF!\n")
	sleep(5)

	letters = "qwertzuiopasdfghjklyxcvbnm"



	player_1_points = 0
	player_2_points = 0



	while len(sentences) > 0:
		sentence = sentences[randint(0, len(sentences) - 1)]
		sentence_out = ""
		for i in sentence.lower():
			if i in letters:
				sentence_out += "*"
			else:
				sentence_out += " "
		
		while "*" in sentence_out:
			pl_1_lives_curr = 1
			pl_2_lives_curr = 1
			print("\nSentence: " + sentence_out)
			results1 = turn(pl_1_lives_curr, player_1, sentence, sentence_out)
			if results1[0] == "correct_sentence":
				print(f"\nGreat job! That is correct sentence!\n {str(count(results1[1]))} points for {player_1}!")
				player_1_points += count(results1[1])
				sentences.remove(sentence)
				break

			elif results1[0] == "correct":
				print(f"\nGreat job! That is correct letter!\nOne point for {player_1}!")
				player_1_points += results1[2]
				sentence_out = results1[1]
			else:
				print(f"\nINCORRECT!\nOne point taken from {player_1}!")
				player_1_points -= 1 

			print("\nSentence: " + sentence_out)
			results2 = turn(pl_2_lives_curr, player_2, sentence, sentence_out)
			if results2[0] == "correct_sentence":
				print(f"\nGreat job! That is correct sentence!\n {str(count(results2[1]))} points for {player_2}!")
				player_2_points += count(results2[1])
				sentences.remove(sentence)
				break 
			elif results2[0] == "correct":
				print(f"\nGreat job! That is correct letter!\nOne point for {player_2}!")
				player_2_points += results2[2]
				sentence_out = results2[1]
			else:
				print(f"\nINCORRECT!\nOne point taken from {player_2}!")
				player_2_points -= 1 


	print(f"\nAND FOR FINAL CHECKING OF POINTS WINNER IS ...\n")
	sleep(9)
	if player_1_points == player_2_points:
		print(f"NOBODY, WOW, THAT IS SO RARE!!!\nBOTH OF YOU HAD WON {player_1_points}.\n")
		sleep(2)

	elif player_1_points > player_2_points:
		print(f"{player_1} with {player_1_points}!!!\n {player_2} had {player_2_points}.\n")
		sleep(2)

	else :
		print(f"{player_2} with {player_2_points}!!!\n {player_1} had {player_1_points}.\n")
		sleep(2)
		


def main():
	player_1 = input("Enter name of player 1: ")
	print()
	if len(player_1) == 0:
		print("I'll call you than Mr_X")
		player_1 = "Mr_X"
	player_2 = input("Enter name of player 2: ")
	print()
	if len(player_2) == 0:
		print("I'll call you than Mr_Y")
		player_2 = "Mr_Y"

	game(player_1, player_2)



if __name__ == '__main__':
	main()

