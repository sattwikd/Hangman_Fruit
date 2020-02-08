from random import choice


def game_start():

	word_list=[]
	with open('fruit_list.txt') as file:
		word_list = file.read().splitlines()
    
	print('\n')
	print('************************************************')
	print('** Welcome to the Hangman Fruit Game          **')
	print('************************************************')

	answer = str(choice(word_list))
	make_guess(answer)

def display_word(answer,r_word,letter_pos):
	if letter_pos == 0 and r_word == '':
		display_ans = '*'*len(answer)
	else:
		i=0
		r_word2=''
		for alphabet in r_word:
			if i==letter_pos-1:
				r_word2 = r_word2 + answer[i]
			else:
				r_word2 = r_word2 + alphabet
			i+=1
		display_ans = r_word2
	return display_ans

def make_guess(answer):
	attempt_cnt = 1
	guess_list = []
	r_word = display_word(answer,'',0)
	print('\nFruit: '+r_word)

	while  attempt_cnt < 11:
		guess_letter = (input('Enter a letter between a-z that can be part of this fruit: ')).lower()
		
		guess_list.append(guess_letter)
		l_pos = answer.find(guess_letter)+1

		if l_pos > 0:
			r_word = display_word(answer,r_word,l_pos)
			l_pos2 = answer[l_pos:].find(guess_letter)
			while l_pos2 != -1:
				l_pos = l_pos + answer[l_pos:].index(guess_letter)+1
				r_word = display_word(answer,r_word,l_pos)
				l_pos2 = answer[l_pos:].find(guess_letter)
			print('\nFruit: '+r_word)
			print(f'Guessed letters list: {guess_list} ')
		else:
			print('\nFruit: '+r_word)
			print(f'Guessed letters list: {guess_list} ')
			print(f"Oops it was wrong!!. Only {10-attempt_cnt} chances left." )
			attempt_cnt+=1

		if r_word == answer:
			print('\n Congrats you won!!!!!')
			break

	else:
		print('\n Sorry, you exhausted all your chances!!')


	

def check_for_replay():
	print('\n')
	return input('Would you like to play again(Y/N)?: ')

play_on = True
while  play_on:
	game_start()
	replay_choice = check_for_replay()

	if replay_choice.upper() == 'N':
		play_on = False
	else:
		print('\n'*100)
		
