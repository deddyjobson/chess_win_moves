import csv
from numpy import array, savetxt

with open('dataset.csv','r') as f:
    data = list(csv.reader(f))#full file into a list. Ok for small files.

# print(*data,sep='\n')

# first convert data to numeric form
data = list(zip(*data)) #transpose
for i in range(3):
    data[2*i] = list(map(lambda ch:int(ord(ch)-ord('a')+1),data[2*i]))
    data[2*i+1] = list(map(int,data[2*i+1]))

numbers = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12,
  'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'draw':17}

data[-1]  = list(map(lambda n:numbers[n],data[-1]))

data = array(list(zip(*data)),dtype='int')

savetxt(open('quantified_array.txt','w+'),data,fmt='%d')
