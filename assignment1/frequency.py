import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    tweets = []
    list_term = dict()
    sum_allTerm = 0.0

    for line in tweet_file:
    	tweets.append(json.loads(line))

    for t in tweets:

    	if t.get('text', "") is not "":
    		list_text = t.get('text').encode('utf-8').split(" ")

        for word in list_text:
            word = word.strip()
            if word in list_term:
                list_term[word] += 1.0
            else:
                list_term[word] = 1.0
        sum_allTerm = sum(list_term.values())

        for key, value in list_term.items():
            print key, value/sum_allTerm   

if __name__ == '__main__':
    main()
