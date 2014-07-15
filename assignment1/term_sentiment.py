import sys
import operator

def lines(fp):
    print str(len(fp.readlines()))

def twoColumnFileToDictionary(aFile, deliminator):
	data = {} # initialize an empty dictionary
	for line in aFile:
		term1, term2  = line.split(deliminator)  # The file is tab-delimited. "\t" means "tab character"
		data[term1] = int(term2)  # Convert the score to an integer.
	return data

def hasKey(aDict, key):
	try:
		return aDict[key] != None
	except KeyError:
		return False

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	wordSentiments = twoColumnFileToDictionary(sent_file, "\t")

	nonSentimentWords = {}

	tweets = list(dict())
	for tweet in tweet_file:
		# rate the line and then assign all unknown words in that line that rating
		unknowns = []
		tweetRating = 0
		words = tweet.split()
		for word in words:
			if hasKey(wordSentiments, word.lower()):
				tweetRating += wordSentiments[word.lower()]
			else:
				unknowns += [word]
		for newWord in unknowns:
			if(hasKey(nonSentimentWords, newWord)):
				nonSentimentWords[newWord] += tweetRating
			else:
				nonSentimentWords[newWord] = tweetRating
	nonSentimentWords = sorted(nonSentimentWords.iteritems(), key=operator.itemgetter(1))
	print(nonSentimentWords)
	for aWord, score in nonSentimentWords:
		print aWord, score

if __name__ == '__main__':
    main()
