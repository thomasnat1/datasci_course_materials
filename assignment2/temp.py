import myToolbox

aFile = open('query.txt')

docs = {}
for line in aFile:
	try:
		docs[line.split('\t')[0]] += int(line.split('\t')[2].strip())
	except:
		docs[line.split('\t')[0]] = int(line.split('\t')[2].strip()[1:-1])
docs = myToolbox.sortedDictBySelector(docs, "value")
for doc, val in docs:
	print doc, val