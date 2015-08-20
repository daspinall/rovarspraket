#A function that creates Rovarspraket, or Robber's language
#Essentially takes every consonant, doubles it, and puts an "o" between them
#Leaves the vowels the same

def rovarspraket(phrase):

	#store the consonants to change
	consonant_dict = {}
	consonants = [c for c in "bcdfghjklmnpqrstvwxyz"]

	for char in consonants:
		consonant_dict[char] = None

	#split the phrase into individual letters
	split_words = [c for c in phrase]
	new_phrase = ""

	#for each letter, add it doubled + o if it's a consonant
	for letter in split_words:

		if letter.lower() in consonant_dict:
			new_phrase += letter + "o" + letter.lower()

		else:
			new_phrase += letter

	return new_phrase

#Test cases
phrase = "Hello there, what do you think of this language??? Yay!"
print rovarspraket(phrase)
