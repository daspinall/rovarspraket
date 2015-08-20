#A function that creates Rovarspraket, or Robber's language
#Essentially takes every consonant, doubles it, and puts an "o" between them
#Leaves the vowels the same

def rovarspraket(phrase):

	#split the phrase into individual letters
	split_words = [c for c in phrase]
	new_phrase = ""

	#for each letter, add it doubled + o if it's a consonant
	for letter in split_words:

		#checks ASCII values to see if there's a consonant
		if (ord('a') < ord(letter.lower()) < ord('e')
			or ord('e') < ord(letter.lower()) < ord('i')
			or ord('i') < ord(letter.lower()) < ord('o')
			or ord('o') < ord(letter.lower()) < ord('u')
			or ord('u') < ord(letter.lower())):

			new_phrase += letter + "o" + letter.lower()

		else:
			new_phrase += letter

	return new_phrase

#Test cases
phrase = "Hello there, what do you think of this language??? Yay!"
print rovarspraket(phrase)
