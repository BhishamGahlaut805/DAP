l1 = ["A", "B", "C", "D", "E"]
l2 = ["C", "B", "E"]
s1 = set(l1)
s2 = set(l2)
print("UNION:", s1.union(s2))
print("INTERSECTION:", s1.intersection(s2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

sym_diff = list(set(list1) ^ set(list2))
print("Symmetric Difference:", sym_diff)

odd={x for x in range(1,21) if x%2!=0}
primes={x for x in range(2,21)
        if all(x%i!=0 for i in range(2,int(x**0.5)+1))}
print("All odds : ",odd)
print("All Primes : ",primes)

print("All odd Intersection Primes : ",odd^primes)
print("All odd union Primes  : ",odd|primes)
print("All Symmetic difference of odd and Primes  : ",(odd|primes)-(odd^primes))

#Output:
'''
PS C:\Users\bhish\OneDrive\Desktop\DAP> python -u "c:\Users\bhish\OneDrive\Desktop\DAP\2__Set_Operations_basics.py"
UNION: {'D', 'C', 'B', 'E', 'A'}
INTERSECTION: {'C', 'B', 'E'}
Symmetric Difference: [1, 2, 3, 6, 7, 8]
All odds :  {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
All Primes :  {2, 3, 5, 7, 11, 13, 17, 19}
All odd Intersection Primes :  {1, 2, 9, 15}
All odd union Primes  :  {1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19}
All Symmetic difference of odd and Primes  :  {3, 5, 7, 11, 13, 17, 19}
PS C:\Users\bhish\OneDrive\Desktop\DAP> 
'''