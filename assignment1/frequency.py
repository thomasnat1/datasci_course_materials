import sys
import operator
import json

def hasKey(aDict, key):
	try:
		return aDict[key] != None
	except KeyError:
		return False

def main():
	tweet_file = open(sys.argv[1])

	allWords = {}
	totalWords = 0

	for tweet in tweet_file:
		try:
			words = json.loads(tweet)['text'].split()
		except KeyError:
			continue
		for word in words:
			if hasKey(allWords, word):
				allWords[word] += 1.0
			else:
				allWords[word] = 1.0
			totalWords += 1

	for aWord, score in sorted(allWords.iteritems(), key=operator.itemgetter(1), reverse=True):
		print aWord, score / totalWords


if __name__ == '__main__':
    main()
