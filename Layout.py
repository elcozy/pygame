
layoutArray = []
layoutFile = open('layout_structure.txt', 'r')
layoutLine = layoutFile.readlines()
currentLine = 0

for line in layoutLine:
    layoutArray.append(line)
