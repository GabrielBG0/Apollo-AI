import os

for i in range(321400):
    file = open('Scraper/dataset/' + str(i) + '.txt', 'r+')

    lines = file.readlines()
    hasValue = False
    linesToDel = []
    for j in range(len(lines)):
        if 'W:' in lines[j] or 'w:' in lines[j]:
            linesToDel.append(j)
        elif lines[j][0] == 'V':
            hasValue = True
    
    if hasValue:
        print("updating id: " + str(i))
        linesToDel.sort(reverse=True)
        for line in linesToDel:
            lines.pop(line)
        file.close()
        os.remove('./Scraper/dataset/' + str(i) + '.txt')
        open('./Scraper/dataset/'  + str(i) + '.txt', 'w+').write(''.join(lines))
    else:
        print("deleting id: " + str(i))
        file.close()
        os.remove('./Scraper/dataset/' + str(i) + '.txt')

