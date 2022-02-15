#Assignment 1
# Q.3
'''
n=int(input('Enter a Number: '))
for i in range(1,n):
    for j in range(i):
        print("*",end='')
    print()    
    
for i in range(1,n):
    for j in range(i,n):
        print("*",end='')
    print()        
'''


#Q.2
'''
test = '12345'*5
print(test)

print(len(test)) 

output1 =slice(0,25,5)
print(test[output1])

output2 =slice(4,25,5)
print(test[output2])

print(test[::-1])
'''

#Q.1
'''
myDict = {'age': ['12'], 'address': ['34 Main Street, 212 First Avenue'],'firstName': ['Alan', 'Mary-Ann'], 'lastName': ['Stone', 'Lee']}

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

print search(myDict, 'Mary') 
'''

#Assignment 2
#Q.1
'''
Input = [('Tuple1', 121), ('Tuple2', 125), ('Tuple1', 135), ('Tuple4', 478)]
print(Input)
set1 = set()
output1 = []

for a,b in Input:
    if not a in set1:
      set1.add(a)
      output1.append((a, b))
print(output1)
'''

#Q.2
'''
import collections

class Solution:
    
    def winner(self,arr,n):
        
        votes = collections.defaultdict(int) 
        
        for name in arr:
            votes[name] += 1
        
        maxVotes = 0
        winner = []
        
        for name in votes.keys():
            if votes[name] > maxVotes:
                maxVotes = votes[name]
                winner.clear()
                winner.append(name)
            
            elif votes[name] == maxVotes:
                winner.append(name)
                
        winner.sort()
        finalwinner = winner[0]
        
        # for win in winner:
        #     if len(win) < len(finalwinner):
        #         finalwinner = win
        
        return finalwinner, votes[finalwinner]
        

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])

'''