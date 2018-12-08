import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    tweets = []
    hashtags = dict()

    for line in tweet_file:
    	tweets.append(json.loads(line))

    for t in tweets:
    	if 'entities' in t:
            list_hashtag = t.get('entities').get('hashtags')

            #print type(list_hashtag)
            for hashtag in list_hashtag:
                h = hashtag['text'].encode('utf-8') 
                #print h
                if h in hashtags:
                    hashtags[h] += 1.0
                else:
                    hashtags[h] = 1.0

    #print hashtags
    for key in sorted(hashtags, key=hashtags.__getitem__)[-10:]:
        print key, hashtags[key]

if __name__ == '__main__':
    main()
