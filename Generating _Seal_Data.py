infile = "NS-test-text.txt"
outfile = "cleaned_file.txt"

delete_list = ["solid AutoCAD", "facet normal", "outer loop", "vertex", "endloop", "endfacet", "end", '     ']
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)

f = open('cleaned_file.txt', 'r')
lines = f.readlines()

dataset = []
for i in range(0, len(lines)):
    line = lines[i]
    values = line.split()
    if len(values) == 3:
        dataset.append((float(values[0]), float(values[1]), float(values[2])))

cleandata = []

for i in range(0, len(dataset)):
    if dataset[i][2] > 0 and dataset[i][2] < 1:
        cleandata.append((dataset[i][0], dataset[i][1]))

cleandata = list(dict.fromkeys(cleandata))

cleandata = [item for index, item in enumerate(cleandata) if item[0] not in [row[0] for row in (cleandata[:index] + cleandata[index+1 :])] and item[1] not in [row[1] for row in (cleandata[:index] + cleandata[index+1 :])]]

print(cleandata)
