
"""
Topic: Evaluate degree distributions for a given social media network

Author: Mark Moretto
Date Created: Nov 18, 2017

"""

### Link to Facebook data set (csv file)
# https://app.box.com/s/tykt68vic7wr8dtk05dopw7vrqzmrwv7


file_path = r'C:\\\\\fb_User_User_Network_data.csv'

def degreeDist(x):
     import csv

     with open(x, newline='', encoding='utf-8)') as file:
         reader = csv.reader(file)
         data = [row for row in reader]

     ### Remove header values
     data.pop(0)

     dataDict = {}
     for k, v in data:
          dataDict.setdefault(k, []).append(v)

     countDict = {}
     for k, v in dataDict.items():
          countDict.setdefault(k, []).append(sum(1 for i in v if i))

     ### Reverse key-value pairs
     data2 = [(v, k) for k, v in countDict.items()]

     ### Unpack tuples from list
     list1, list2 = zip(*data2)
     list3 = ",".join([str(i[0]) for i in list1])
     list1 = list3.split(sep=',')

     ### Zipping formatted lists back together
     newList = [[x, y] for x, y in zip(list1, list2)]

     newDict = {}
     for k, v in newList:
          newDict.setdefault(k, []).append(v)
     ddict = {int(k):v for k, v in newDict.items()}

     print('{0:>8s}{1:^5s}{2:<6s}'.format('Degree', '-', 'Count'))
     print('   ----------------    ')
     for k, v in sorted(ddict.items(), reverse=False):
          print('{0:8d}{1:^5s}{2:<6}'.format(k, '-', len([i for i in v if i])))



def main():
    degreeDist(file_path)

if __name__ == '__main__':
    main()