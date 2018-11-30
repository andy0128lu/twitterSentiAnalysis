import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def transform(sent_file):
    	afinnfile = open(sent_file)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

	return scores # Print every (term, score) pair in the dictionary    

def main():
    scores = transform(sys.argv[1])
    tweet_file = open(sys.argv[2])

    tweets = []
    for line in tweet_file:
    	tweets.append(json.loads(line))

    for t in tweets:
        ratio = 0.0
        positive = 0.0
        negative = 1.0
    	if t.get('text', "") is not "":
    		list_text = t.get('text').encode('utf-8').split(" ")

        unknown_term = []
        for text in list_text:
            s = scores.get(text.lower(), 0)
            if s == 0:
                unknown_term.append(text)
            elif s > 0:    
                positive += 1
            else:
                negative += 1  
            ratio = positive/negative
        for term in unknown_term:
            print term, ratio    

if __name__ == '__main__':
    main()
