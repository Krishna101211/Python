"""
#wap to generate a list if it is individual data type
#reverse it else keep it as it is
a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]

"""

#wap to return an iterator having the words and its length pair as a dictionary inside the tuple.
l=["charlie","golden retriever","scooby","sandy","german shepherd"]


# wap to generate a+b,a-b,a*b,a/b by taking a and b from user




# wap to return a iterator which is having square
# root of values present in the list

l=[25,36,49,81,9,16]


# wap to return a iterator having tuples of
# word and its len pair and typecast into dictionary

# z=["instagram","facebook","whatsapp","meta","oracle"]
# d={}
# def dictionary(z):
#     for i in z:
#         d[i]:len(i)
#     yield d
# o=dictionary(["instagram","facebook","whatsapp","meta","oracle"])
# print(next(o))

# wap to generate only numeric values in given list

# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# def numeric(l):
#     for i in l:
#         if isinstance(i,int):
#             yield i
#
# o=numeric(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])
# print(list(o))


# wap to generate a list if it is individual data type
# reverse it else return its type of the data
l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
k=[]
def reverse(l):
    for i in l:
        if isinstance(i,int):
            p=str(i)

            k.append(p[::-1])
            yield k

z=reverse(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])
print(next(z))





# wap to create a list of numbers if number are even square it else cube it
l=[2,3,4,5,6,7]



# wap to generate the first letter
# of the word as key and words starting with letter as value
s="python is a programming language and programming is part of life"
j={}
for i in s.split():
    if i[0] not in j:
        j[i[0]]=i
    else:
        j[i[0]]=i

print(j)



# output:-->[{'p': ['python', 'programming', 'programming', 'part'],'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]"""
