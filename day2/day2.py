with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

def checkRed(col):
    return int(col.strip().split(' ')[0]) <= 12

def checkBlue(col):
    return int(col.strip().split(' ')[0]) <= 14

def checkGreen(col):
    return int(col.strip().split(' ')[0]) <= 13

games = []

for l in lines:
    gid = int(l.split(':')[0].split(' ')[1])
    sets = l.split(':')[1].split(';')
    possible = True
    for s in sets:
        if not possible:
            break
        cols = s.split(',')

        for c in cols:
            if 'red' in c and not checkRed(c):
                possible = False
                break

            if 'blue' in c and not checkBlue(c):
                possible = False
                break

            if 'green' in c and not checkGreen(c):
                possible = False
                break

    if possible:
        games.append(gid)

print(sum(games))