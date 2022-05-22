print("starting betaFormater.py")

compiledDataset = ""

file =  open("Scraper\dataset.txt", "r", encoding="utf-8")

songs = file.read().split("\n\n")

file.close()

for song in songs:
    lines = song.split('\n')
    linesToDel = []
    for j in range(len(lines)):
        if len(lines[j]) > 0:
            if (lines[j][0] == 'A') or (lines[j][0] == 'B') or (lines[j][0] == 'C') or (lines[j][0] == 'D'):
                linesToDel.append(j)
            elif (lines[j][0] == 'F') or (lines[j][0] == 'H') or (lines[j][0] == 'I') or (lines[j][0] == 'N'):
                linesToDel.append(j)
            elif (lines[j][0] == 'O') or (lines[j][0] == 'r') or (lines[j][0] == 's') or (lines[j][0] == 'T'):
                linesToDel.append(j)
            elif (lines[j][0] == 'W' or lines[j][0] == 'w') or (lines[j][0] == 'X') or (lines[j][0] == 'Z'):
                linesToDel.append(j)
            lines[j] = lines[j] + '\n'
        else:
            linesToDel.append(j)
    
    linesToDel.sort(reverse=True)
    for line in linesToDel:
        lines.pop(line)
    compiledDataset += ''.join(lines) + '\n\n'

print("all songs foramted, saving in to dataset")

open("datasets/b/dataset.txt", "w", encoding="utf-8").write(compiledDataset)