from flask import Flask, request, render_template
import custom_tokenize
import logodds
import extract_phrases
import twitter_scrapper
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	results = None
	if request.method == 'POST':
		text1 = None
		text2 = None
		if request.form['submit'] == 'plaintext':
			text1 = request.form['text1']
			text2 = request.form['text2']
		else:
			text1 = twitter_scrapper.get_tweets(request.form['handle1'], 100)
			text2 = twitter_scrapper.get_tweets(request.form['handle2'], 100)

		tokenized = custom_tokenize.generate_tokens(text1, text2)
		# print "tokenized"
		# print tokenized
		# list1 = ['a', 'a', 'b', 'c', 'c', 'c', 'c', 'a', 'c', 'a', 'e', 'gas', 'gas']
		# list2 = ['a', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'dededededed', 'd', 'h', 'i', 'j']
		phrases1 = list(phrasifier.phrases_of_sents(tokenized[0]))
		phrases2 = list(phrasifier.phrases_of_sents(tokenized[1]))
		# print "phrases"
		# print phrases1
		# print phrases2
		results = logodds.get_analysis(phrases1, phrases2, large_prior)
		sortedResults = sorted(results.items(), key=lambda x:x[1][0])
		lowestLogScores = sortedResults[:10]
		highestLogScores = sortedResults[-10:]
		fullSortedResults = sortedResults
		sortedResults = {'scores':(lowestLogScores, highestLogScores)}
		# print "results"
		# print results
		# print sortedResults
		return render_template("index.html", results=results, sortedResults=sortedResults, fullSortedResults=fullSortedResults)
	else:
		return render_template("index.html", results=None, sortedResults=None)

def loganalysis(text1, text2):
	return text1 + ' ' + text2

if __name__ == "__main__":
        print >> sys.stderr, "loading phrasifier..."
        phrasifier = extract_phrases.get_default_phrasifier()
        print >> sys.stderr, "loading large prior..."
        large_prior = logodds.get_large_prior()
	app.run()
