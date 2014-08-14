import MapReduce
import sys
import json

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# def mapper(record):
#     # key: document identifier
#     # value: document contents
#     key = record[0]
#     value = record[1]
#     words = value.split()
#     for w in words:
#       mr.emit_intermediate(w, 1)

# def reducer(key, list_of_values):
#     # key: word
#     # value: list of occurrence counts
#     # print list_of_values
#     total = 0
#     for v in list_of_values:
#       total += v
#     mr.emit((key, total))

# def mapper(record):
#     # key: document identifier
#     # value: document contents
#     # output: word : text document in which it appears
#     key = record[0]
#     value = record[1]
#     words = value.split()
#     for w in words:
#         mr.emit_intermediate(w, key)


# def reducer(key, list_of_values):  
#   # key: word
#   # value: list of occurrence counts
#   # output: word : [list of documents]
#   mr.emit((key, list(set((list_of_values)))))

# def mapper(record):
#   # input: a record
#   # output: order_id : rest of dat shit
#   mr.emit_intermediate(record[1], record)

# def reducer(key, list_of_values):
#   # key: word
#   # value: list of occurrence counts
#   # output: word : [list of documents]
#   for record in list_of_values[1:]:
#     join = list_of_values[0] + record
#     mr.emit(join)
def mapper(record):
  if(record[0] == "a"):
    for k in range(0, 5):
      mr.emit_intermediate((record[1], k), ("a", record[2], record[3]))
  else:
    for i in range(0, 5):
      mr.emit_intermediate((i, record[2]), ("b", record[1], record[3]))

def reducer(key, list_of_values):
  # print key, list_of_values
  sumsA = list(0 for i in range(0, 5))
  sumsB = list(0 for i in range(0, 5))
  for line in list_of_values:
    if line[0] == "a":
      sumsA[line[1]] = line[2]
    else:
      sumsB[line[1]] = line[2]
  totSum = 0
  for i in range(0,5):
    totSum += sumsA[i] * sumsB[i]
  mr.emit((key[0], key[1], totSum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
