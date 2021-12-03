snack = {"candy", "jelly", "lollipop"}
print("1", snack)
print("2", all(snack))
print("3", any(snack))
print("4", len(snack))

drink = set(("juice", "cola"))
print("5", drink)

drink.add("milk")
print("6", drink)
drink.add("milk")
print("7", drink)

cup = drink.copy()
print("8", cup)

glass = drink
print("9", glass)

happy = cup.union(snack)
print("10", happy)

b = snack > happy
print("11", b )

happy.update(["ice-cream", "apple"])
print("12", happy)

happy.remove("jelly")
print("13", happy)

happy.remove("lollipop")
print("14", happy)

happy.pop()
print("15", happy)

glass.clear()
print("16", glass)

del cup
# print("17", cup)

if "cola" in happy:
    print("18 hahaha")
else:
    print("18 ung-ung")

for x in snack:
    print("19 I like \"%s\"." % (x))
