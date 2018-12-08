import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    friend = record[1]
    mr.emit_intermediate(key.encode('utf-8'), friend.encode('utf-8'))

def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    for friend in list_of_values:
        if friend in mr.intermediate:
            if key not in mr.intermediate[friend]:
                mr.emit((friend, key))
                mr.emit((key, friend))

        else:
            mr.emit((key, friend))
            mr.emit((friend, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
