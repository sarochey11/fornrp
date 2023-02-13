beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

for i in range(1):
    beatles.append(input())

print(beatles)

del beatles[3]
del beatles[3]

print(beatles)

beatles.insert(0, "Ringo Starr")

print(beatles)