class record():
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return f"{self.name}, {self.cost}"

allrecord = [record('john', 100), record('lina', 110), record('joe', 120)]

def pigeonhole_sort(records):
    recMin = 100
    recMax = 120
    recRange = recMax - recMin + 1

    holes = [[] for i in range(recRange)]

    for i in range(len(records)):
        print(i)
        holes[records[i].cost - recMin].append(records[i])

    i = 0
    for hole in holes:
        for item in hole:
            records[i] = item
            i += 1
    return records

allrecord = pigeonhole_sort(allrecord) 
print(allrecord)