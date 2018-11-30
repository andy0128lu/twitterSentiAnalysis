import sys
import json

def state_transform():
    states = {
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
            'WY': 'Wyoming'
    }

    states_value = states
    states_short = states
    for key, value in states.items():
        states_value[value] = 0.0
        states_short[value] = key
    
    return states_value, states_short 


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
    states_value, states_short = state_transform()

    tweets = []
    for line in tweet_file:
    	tweets.append(json.loads(line))


    for t in tweets:
    	sum = 0  
        state = None
    	#if t.get('text', "") is not "":
        if 'text' in t:
            list_text = t.get('text').encode('utf-8').split(" ")
            for text in list_text:
                s = scores.get(text.lower(), 0)
                sum += s

        if 'name' in t:
            state = t.get('place', "").get('name', "").encode('utf-8')
            states_value[state] += sum
      
    for state, value in states_value.items():
        theState = ""
        maxValue = 0.0
        if value > maxValue:
            theState = states_short[state]
        #states[state] = value/len(tweets)

    print theState
    
        
      

if __name__ == '__main__':
    main()
