import sys
import json

def hw(sent_file, tweet_file):
	wordSentiments = twoColumnFileToDictionary(sent_file, "\t")
	tweets = list()
	tweetSentiments = list()
	for line in tweet_file:
		tweets += [json.loads(line)]
	for aTweet in tweets:
		try:
			sentSum = 0
			for aWord in aTweet['text'].split():
				try:
					sentSum += int( wordSentiments[aWord.lower().encode('utf-8')] )
				except KeyError:
					sentSum += 0
			tweetSentiments += [sentSum]
		except KeyError:
			tweetSentiments += [0]
	for aSent in tweetSentiments:
		print aSent

def twoColumnFileToDictionary(aFile, deliminator):
	data = {} # initialize an empty dictionary
	for line in aFile:
		term1, term2  = line.split(deliminator)  # The file is tab-delimited. "\t" means "tab character"
		data[term1] = int(term2)  # Convert the score to an integer.
	return data

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw(sent_file, tweet_file)



if __name__ == '__main__':
    main()
