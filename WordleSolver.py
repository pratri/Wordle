
def main():
	words = []
	adding_to_list(words)
	testing_list(words)
	removing_words_with_letter_and_position(words, 'h', 0)
	testing_list(words)


def adding_to_list(words):
	# Creates a giant list of all possible wordle words
	words.append("Hello")
	words.append("Working")
	pass


def removing_words_with_letter_and_position(words, letter, pos):
	# Given a letter and position removes every word with that letter
	for word in words:
		print(word, letter, pos, word[pos])
		if letter.lower() == word[pos]:
			words.remove(word)
	pass

def removing_words_with_letter(words, letter):
	for word in words:
		if letter.lower() in word:
			words.remove(word)

def testing_list(words):
	print(words)
	print("working")

main();  