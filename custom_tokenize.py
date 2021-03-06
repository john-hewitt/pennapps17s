from nltk.tokenize import sent_tokenize, regexp_tokenize
from nltk.tokenize import casual

# sent_tokenize is an nltk function that splits the input string into a list of sentences based
# on an some machine learning that smart people did
#
# regexp_tokenize tokenizes based on what the user defines as a token. it is currently defined
# \w+\'*\w*
#
# yes: normal words, contracted words
# no:  extraneous punctuation
def generate_tokens(text1, text2):
	tokens1 = [regexp_tokenize(t, '\w+\'*\w*') for t in sent_tokenize(text1)]
	tokens2 = [regexp_tokenize(t, '\w+\'*\w*') for t in sent_tokenize(text2)]
	return (tokens1, tokens2)

def generate_tokens_twitter(text1, text2):
	text1 = casual.remove_handles(text1)
	text2 = casual.remove_handles(text2)
	return generate_tokens(text1, text2)