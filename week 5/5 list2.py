for x in range(4):
    print("1 ",x)

color = ["red", "blue", "white"]
for x in color:
    print("2 ", x)

color = [1, 2, 3]
y = [x*x for x in color]
print("3 ", y)

z = []
for x in color:
    z.append(x*x)
print("3 ", z)
