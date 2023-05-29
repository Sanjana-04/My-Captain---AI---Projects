"""
Created on Mon May 29 17:05:53 2023

@author: SANJANA
"""
#Program to illustrate diferent set operations
#Let A represent the first set and B represent the second set
A={1,2,3,4,5,6,7,8}
B={1,3,9,7,0}
#Union of two sets
print("Union of sets A and B is :",A.union(B))
#Intersection of two sets
print("Intersection of sets A and B is :",A.intersection(B))
#Symmetric difference of two sets
print("Symmetric difference of sets A and B is :",A.symmetric_difference(B))
#Difference of two sets
print("Difference of sets A and B is :",A.difference(B))

            
