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

	allTags = {}

	for tweet in tweet_file:
		try:
			for tag in json.loads(tweet)['entities']['hashtags']:
				if(hasKey(allTags, tag['text'])):
					allTags[tag['text']] += 1
				else:
					allTags[tag['text']] = 1
		except KeyError:
			pass

	for aTag, score in sorted(allTags.iteritems(), key=operator.itemgetter(1), reverse=True)[0:10]:
		print aTag, score

if __name__ == '__main__':
    main()
