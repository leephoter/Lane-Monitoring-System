fruit = ["apple", "grape"]

print("1", fruit)

fruit.clear()
print("2", fruit)

del fruit
try:
    print("3", fruit)
except:
    pass

print("5 bye")
