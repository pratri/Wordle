import fileinput

def main():
	words = []
	adding_to_list(words)
	# testing_list(words)
	
	for i in range(5):
		word = input("Enter in the word ")
		if len(word) != 5:
			print("WRong length")
			quit()
		correctness = input("Enter in a string of 5 characters, 1 for letter not in word, 2 for letter in word, but wrong position, 3 for letter in right place ")
		if len(correctness) != 5:
			print("Wrong Lenght")
			quit()
		for j in range(5):
			if int(correctness[j]) == 1:
				removing_words_with_letter(words, word[j])
			elif int(correctness[j]) == 2:
				removing_words_with_letter_and_position(words, word[j], j)
				removing_words_without_letter(words, word[j])
			elif int(correctness[j]) == 3:
				removing_words_without_letter_and_position(words, word[j], j)
			else:
				quit()
		print(words)
	# print("FINAL", words)
	# testing_list(words)

def adding_to_list(words):
	for line in fileinput.input(files = "wordlewords.txt"):
		words.append(line.strip())
	# Creates a giant list of all possible wordle words

def removing_words_without_letter_and_position(words,letter,pos):
	trash = []
	for word in words:
		if letter.lower() != word[pos]:
			print(word)
			trash.append(word)
	for word in trash:
		words.remove(word)

def removing_words_with_letter_and_position(words, letter, pos):
	# Given a letter and position removes every word with that lettre
	trash = []
	for word in words:
		# print(word, letter, pos, word[pos])
		if letter.lower() == word[pos]:
			print(word)
			trash.append(word)
	for word in trash:
		words.remove(word)
	

def removing_words_with_letter(words, letter):
	trash = []
	print("LETTER: ", letter)
	for word in words:
		if letter.lower() in word:
			print(word)
			trash.append(word)
	for word in trash:
		words.remove(word)

def removing_words_without_letter(words, letter):
	trash = []
	for word in words:
		if letter.lower() not in word:
			# print("Removing", word, letter.lower())
			trash.append(word)
	for word in trash:
		words.remove(word)


def testing_list(words):
	for word in words:
		print(word)

main(); 