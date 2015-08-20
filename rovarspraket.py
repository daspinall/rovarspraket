#A function that creates Rovarspraket, or Robber's language
#Essentially takes every consonant, doubles it, and puts an "o" between them
#Leaves the vowels the same

def rovarspraket(phrase):

	#store the vowels and spaces so they won't be changed
	ignore_chars = {
		"a":None,
		"e":None,
		"i":None,
		"o":None,
		"u":None,
		" ":None,
		".":None,
		",":None,
		"?":None,
		"!":None,
		"(":None,
		")":None
	}

	#split the phrase into individual letters
	split_words = [c for c in phrase]
	new_phrase = ""

	#for each letter, add it doubled + o if it's a consonant
	for letter in split_words:

		if not ignore_chars.has_key(letter):
			new_phrase += letter + "o" + letter.lower()

		else:
			new_phrase += letter

	return new_phrase

#Test cases
phrase = "Hello David!"
print rovarspraket(phrase)