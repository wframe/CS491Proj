import nltk, string

NOUNS = ['NN', 'NNS', 'NNP', 'NNPS']

def tag_sentence(sentence): 
	return nltk.pos_tag(sentence)

def get_sentences(text):
	# lazy load sentence detector
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	return sent_detector.tokenize(text)

def get_nouns(sentence): 
	tagged_sentence = tag_sentence(sentence)
	return [word if pos in NOUNS else '' for word,pos in tagged_sentence]