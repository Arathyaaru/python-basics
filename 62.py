#add any iterable

#the extand() method does not have a appendlists,
 # you can add any iterable object(tuples, sets, dictionaries etc.)

 #add elements of a tuple to alist?

thislist = ["apple", "banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)