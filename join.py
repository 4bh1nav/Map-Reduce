import MapReduce
import sys

 

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
     
    
    order_id = record[1]
    iteam = record[0]
    mr.emit_intermediate(order_id,record)
     
     

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order = []
    iteam_list = [] 
    for x in list_of_values:
        if x[0] == 'order':
            order.append(x)
        else:
            iteam_list.append(x)    
    for y in iteam_list:
        for x in order:
            mr.emit(x+y)        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open('data/records.json')
  mr.execute(inputdata, mapper, reducer)
