pack = {"snack":"candy", "drink":"cola", "fruit":"apple"}
# print("1", pack)
# a = pack["snack"]
# print("2", a)

# print("3", pack.get("drink", "snack"))
# pack["snack"] = "cracker"
# print("4", pack)

# print("5", all(pack))
# print("6", any(pack))
# pack["plate"] = "red-cup"
# print("7", pack)
# print("8", len(pack))
happy = dict(pack)
# happy2 = happy.copy()
# print("9", happy)
# print(happy2)
smile = pack.copy()
# print("10", smile)
print(smile)
x = smile.setdefault("fruit")
print("11", x)
print("12", smile)

# all = {"pack":pack, "happy":happy, "smile":smile}
# print("13", all)

# meeting = dict(year="2020", month="May", day="7", time="14")
# print("14", meeting)

# meeting.pop("year")
# print("15", meeting)
# meeting.popitem()
# print("16", meeting)

# del meeting["month"]
# print("17", meeting)
# meeting.update({"year": "2019"})
# print("18", meeting)
# meeting.update({"year": "2018"})
# print("19", meeting)
# happy.clear()
# print("20", happy)

# del meeting
# #print("21", meeting)


# x = ('key1', 'key2', 'key3')
# y = "hello"
# greeting = dict.fromkeys(x, y)
# print("22", greeting)

# print("22-2",pack)
# if "drink" in pack:
#     print("23 hahaha")
# else:
#     print("23 ung-ung")

# for x in pack:
#     print("24",x )

# for x in pack:
#     print("25", pack[x])

# for x in pack.values():
#     print("26", x)

# for x in pack.items():
#     print("27", x)

# for x in pack.keys():
#     print("28", x)
