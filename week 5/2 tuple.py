snack = ("candy", "jelly", "lollipop")
print("1", snack)
print("2", snack[0])
print("3", snack[-1])
print("4", snack[-3])
print("5", snack[1:2])
print("6", snack[:2])
print("7", snack[1:])
print("8", snack[::2])
print("9", all(snack))
print("10", any(snack))
snack[1] = "cookie"
print("11", snack)
print("12", len(snack))
drink = tuple(("juice", "cola"))
print("13", drink)
cup = drink.copy()
print("14", cup)
smile = drink
print("15", smile)
happy = drink + snack
print("16", happy)
# smile.extend(snack)
# print("17", smile)

# smile.remove("cola")
# print("18", smile)
# happy.pop(1)
# print("19", happy)
# del smile[2]
# print("20", smile)

# happy.clear()
# print("21", happy)
# del smile
# print("22", smile)

# snack.append("cracker")
# print("23", snack)
# snack.insert(2, "chocolate")
# print("24", snack)
# snack = snack + ["cookie"]
# print("25", snack)
print("26", snack.index("candy"))
print("27", snack.count("cookie"))
# snack.reverse()
# print("28", snack)
# snack.sort()
# print("29", snack)

if "cola" in snack:
    print("30 hahaha")
else:
    print("30 ung-ung")

for x in snack:
    print("31 I like \"%s\"." % (x))
