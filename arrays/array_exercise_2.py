heroes=['spider man','thor','hulk','iron man','captain america']

print(len(heroes))
heroes.append("black panther")
print(heroes)
heroes.pop()
heroes.insert(3,"black panther")
print(heroes)
heroes[1:3] = ["doctor strange"]
print(heroes)
print(sorted(heroes))

