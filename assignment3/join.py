import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    elements = record[1:]
    mr.emit_intermediate(key.encode('utf-8'), elements)

def reducer(key, elements):
    # key: word
    # value: list of documents
    """
    output = []
    output.append(key)
    output.append(list(set(list_of_values)))
    """
    #print key, elements
    id = elements[0]
    if key == 'order':
        for r_order in elements:
            o_id = r_order[0]
            for r_line in mr.intermediate['line_item']:
                l_id = r_line[0]
                if o_id.encode('utf-8') == l_id.encode('utf-8'):
                    remains = [ x.encode('utf-8') for x in (r_order + ['line_item']+ 'r_line)]
                    mr.emit([key] + ['line_item'] + remains)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
