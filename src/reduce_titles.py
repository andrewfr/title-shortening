import spacy
from spacy.symbols import dobj
# from pprint import pprint

album_titles = (
	'...Baby One More Time',
	'Appetite for Destruction',
	'Back In Black',
	'Bat Out Of Hell',
	'Born In The U.S.A.',
	'Cracked Rear View',
	'Dark Side of the Moon',
	'Hotel California',
	'Hysteria',
	'It Takes a Nation of Millions to Hold Us Back',
	'Jagged Little Pill',
	'Led Zeppelin II',
	'No Jacket Required',
	'Physical Graffiti',
	'Purple Rain',
	'Sgt. Pepper’s Lonely Hearts Club Band',
	'Slippery When Wet',
	'Thriller',
	'Wide Open Spaces',
	'Yourself or Someone Like You',
)
movie_titles = (
	'2001: A Space Odyssey',
	'Blade Runner',
	'Blazing Saddles',
	'Brief Encounter',
	'Casablanca',
	'Die Hard',
	'Gone with the wind',
	'Mad Max 2',
	'Man with a Movie Camera',
	'Nausicaä of the Valley of the Wind',
	'Rocky',
	'Saving Private Ryan',
	'Some Like It Hot',
	'The Empire Strikes Back',
	'The Godfather',
	'The Shawshank Rendemption',
)
tv_titles = (
	'All In The Family',
	'Battlestar Galactica',
	'Breaking Bad',
	'Cheers',
	'Curb Your Enthusiasm',
	'Deadwood',
	'Doctor Who',
	'Friends',
	'Game of Thrones',
	'I Love Lucy',
	'Law & Order',
	'Lost',
	'M*A*S*H',
	'Mad Men',
	'Orange is the new Black',
	'Saturday Night Live',
	'Seinfeld',
	'Sex and the City'
	'Six Feet Under',
	'South Park',
	'Stranger Things',
	'The Big Bang Theory',
	'The Office',
	'The Simpsons',
	'The Sopranos',
	'The West Wing',
	'The Wire',
	'The X-Files',
	'Twin Peaks',
	'Walking Dead',
)
book_titles = (
	'Alice’s Adventures in Wonderland',
	'All Quiet on the Western Front',
	'And Then There Were None',
	'Angels & Demons',
	'Anne of Green Gables',
	'Ben-Hur: A Tale of the Christ',
	'Black Beauty',
	'Charlie and the Chocolate Factory',
	'Charlotte’s Web',
	'Harry Potter and the Philosopher’s Stone',
	'Jonathan Livingston Seagull',
	'Le Petit Prince',
	'Lolita',
	'Nineteen Eighty-Four',
	'Pride and Prejudice',
	'Shōgun',
	'The Adventures of Pinocchio',
	'The Adventures of Sherlock Holmes',
	'The Adventures of Tom Sawyer.',
	'The Bridges of Madison County',
	'The Cat in the Hat'
	'The Catcher in the Rye',
	'The Da Vinci Code',
	'The Girl with the Dragon Tattoo',
	'The Great Gatsby',
	'The Hitchhiker’s Guide to the Galaxy',
	'The Hobbit',
	'The Lion, The Witch and the Wardrobe',
	'The Lord of the Rings',
	'The Mark of Zorro',
	'The Naked Ape',
	'The Tale of Peter Rabbit',
	'The Very Hungry Caterpillar',
	'To Kill a Mockingbird',
	'Twenty Thousand Leagues Under the Sea',
	'Valley of the Dolls',
	'War and Peace',
	'Watership Down',
)
phrases = (
	'Apple is looking at buying U.K. startup for $1 billion',
)

model='en_core_web_sm'
nlp = spacy.load(model)


def subphrase(full_string):
	doc = nlp(full_string)
	results = []

	for token in doc:
		# print(
		#     token.text,
		#     # token.norm_,
		#     # token.lemma_, # the base form of the word
		#     # token.pos_, # the simple part-of-speech tag
		#     # token.tag_, # the detailed part-of-speech tag
		#     # token.dep_, # syntactic dependency, ie. the relation betwen tokens
		#     # token.shape_, # the word shape; caps/punc/digits
		#     # token.is_alpha, # is the token an alpha character
		#     # token.is_stop # is the token part of a stop list; ie. most common words
		# )

		if token.dep_ == 'ROOT':
			for l in token.lefts:
				results.append(l.text)

			# place the root token in between lefts and rights
			results.append(token.text )

			for right in token.rights:
				results.append(right.text)

			print('results:', ' '.join(results), '\n')

		# if token.dep_ == 'dobj':
		# 	print('direct obj:', token)
		# 	for t in token.children:
		# 		print('direct obj child:', t)
		# 		# if t.dep_ == 'dobj':
		# 			# ie. 'nation'

# for phrase in album_titles:
for phrase in movie_titles:
	print('subphrasing:', phrase)
	subphrase(phrase)
