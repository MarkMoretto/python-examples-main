
#Question: https://stackoverflow.com/questions/56723790/how-to-print-lists-within-a-list-in-separate-columns-using-for-loops

# table[y][x]
table = [['Tom','Dick','Harry','John'],
         ['Apples','Oranges','Strawberries','Grapes'],
         ['Brocolli', 'Asparagus', 'Carrots', 'Potatoes']]


# table = [['Tom','Dick','Harry','John'], ['Apples','Oranges','Strawberries','Grapes'],['Brocolli', 'Asparagus', 'Carrots', 'Potatoes']]


fin = list()
tmp = list()
abc = iter(table)



for i in range(1, len(table)+1):
    for j in range(1, len(table[i-1]) + 1):
        if j % i == 0:
            print(table[i-1][j-1], end='\n')
        else:
            print(table[i-1][j-1], end=' ')




i = len(table)
while i > 0:
    lst = table[i]
    for j in range(len(table[i])):
        print(table[j][i])
    i+= 1





tmp = list()
fin = list()
for i in range(len(table)):
    for j in range(len(table[i])):
        print(j, ', ', i)



for i, j in enumerate(table, 1):
    for k, l in enumerate(table[i], 1):
        print(i, ' - ', j,  ',', k, ' - ', l)



def enum(sequence, start=0):
    """Reconstrucuring of enumerate() function using iter()."""
    for v in iter(sequence):
        yield start, v
        start += 1
        


for x, y in enumerate(table):
    for a, b in enumerate(table[x]):  
        if a in x:
            print(y, ',', b)



def reshape_table(seq):
    for itm in seq:
        if isinstance(itm, list):