collections = [1, 2, 3]
print(len(collections))
print(collections[0])
print(collections[-1])
print(collections[-2])
print(collections[0:2]) # position 0 and 1
print(collections[:2])
print(collections[:])
collections[2] = 4
print(collections)
collections.append(5)
print(collections)
collections.clear()
print(collections)

collections2 = [2, 4, 1]
collections2.sort()
collections2.reverse()
print(collections2)

collections3 = [1, 2, 3]
print(collections3.count(2))

collections4 = [4, 5, 6]
collections3.extend(collections4)
print(collections3)
print(collections3.index(4))
collections3.insert(0, 9)
print(collections3)

collections3.pop(0)
print(collections3)

collections3.remove(6)
print(collections3)
