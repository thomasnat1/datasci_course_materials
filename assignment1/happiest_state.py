import sys
import json
import operator
# from pygeocoder import Geocoder

states = states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}

def hasKey(aDict, key):
	try:
		return aDict[key] != None
	except KeyError:
		return False

def hw(sent_file, tweet_file):
	wordSentiments = twoColumnFileToDictionary(sent_file, "\t")
	tweets = list()
	tweetSentiments = list()

	stateHappiness = {}

	for line in tweet_file:
		tweets += [json.loads(line)]

	for aTweet in tweets:
		# try to locate tweet:
		state = None
		if hasKey(aTweet, 'place'):
			if aTweet['place']['country'] == "United States":
				state = aTweet['place']['full_name'].split(', ')[1]
				if state not in states:
					continue
			else: continue
		else: continue

		try:
			sentSum = 0
			for aWord in aTweet['text'].split():
				try:
					sentSum += int( wordSentiments[aWord.lower().encode('utf-8')] )
				except KeyError:
					# no sentiment found
					pass
			if(hasKey(stateHappiness, state)):
				stateHappiness[state] += sentSum
			else: 
				stateHappiness[state] = sentSum
		except KeyError:
			# no text field for tweet
			pass
	# print stateHappiness
	print sorted(stateHappiness.iteritems(), key=operator.itemgetter(1)).pop()[0]

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
