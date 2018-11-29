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
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #score_output = open("score_output.txt", "a")

    scores = transform(sys.argv[1])
    #print scores

    tweets = []
    for line in tweet_file:
    	tweets.append(json.loads(line))
    """
    hw()
    lines(sent_file)
    lines(tweet_file)
    """

    for t in tweets:
    	sum = 0  
    	if t.get('text', "") is not "":
    		list_text = t.get('text').encode('utf-8').split(" ")
        #print type(list_text), list_text

        #list_text = list_text.split()

        #print type(list_text), list_text.split(" ")
        for text in list_text:
              s = scores.get(text.lower(), 0)
              #print s
              sum += s
      
    	print sum
      
    	#score_output.write(str(sum) + '\n')




if __name__ == '__main__':
    main()
