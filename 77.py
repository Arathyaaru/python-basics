#return "arathy" instead of "chandhu" ?

names = ["aadhi","arathy","maalu","anju"]

newlist = [x if x != "chandu" else" arathy" for x in names]
print(newlist)

