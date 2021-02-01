infile = "NS-test-text.txt"
outfile = "cleaned_file.txt"

# Clear words from stl text file
delete_list = ["solid AutoCAD", "facet normal", "outer loop", "vertex", "endloop", "endfacet", "end", '     ']
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)

f = open('cleaned_file.txt', 'r')
lines = f.readlines()

# Create (x,y,z) list format from values in the text file and save in dataset
dataset = []
for i in range(0, len(lines)):
    line = lines[i]
    values = line.split()
    if len(values) == 3:
        dataset.append((float(values[0]), float(values[1]), float(values[2])))

# Clean out all unnecessary out of plane laserdata points from dataset
sealnomdata = []
for i in range(0, len(dataset)):
    if dataset[i][2] > 0 and dataset[i][2] < 1:
        sealnomdata.append((dataset[i][0], dataset[i][1]))

# Delete repeating coordinates
sealnomdata = list(dict.fromkeys(sealnomdata))

# Delete all values with same x or y value
sealnomdata = [item for index, item in enumerate(sealnomdata) if item[0] not in [row[0] for row in (sealnomdata[:index] + sealnomdata[index + 1:])] and item[1] not in [row[1] for row in (sealnomdata[:index] + sealnomdata[index + 1:])]]

# Order laserdata in terms of increasing x term
sealnomdata.sort()

# Create final laserdata set in ( (x,y) , (x,y) ) line format
lines = []
for i in range(0, len(sealnomdata) - 1):
        lines.append((sealnomdata[i], sealnomdata[i + 1]))

# Creating separate list for dearpygui plotting
sealnomx = []
for i in range(0, len(sealnomdata)):
    sealnomx.append(sealnomdata[i][0])

sealnomy = []
for i in range(0, len(sealnomdata)):
    sealnomy.append(sealnomdata[i][1])
