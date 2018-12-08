import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[0].encode('utf-8')
    dna = record[1][:-10].encode('utf-8')
    if dna not in mr.intermediate.values():
        mr.emit_intermediate(dna, 1)

def reducer(key, dna):
    #print len(mr.intermediate)
    """
    replicated_keys = [k for k, d in mr.intermediate.items() if d == dna]
    if len(replicated_keys) == 1:
    """
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
