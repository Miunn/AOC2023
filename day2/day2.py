with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

def checkRed(col):
    return int(col.strip().split(' ')[0]) <= 12

def checkBlue(col):
    return int(col.strip().split(' ')[0]) <= 14

def checkGreen(col):
    return int(col.strip().split(' ')[0]) <= 13

def amountRed(col):
    return int(col.strip().split(' ')[0])

def amountBlue(col):
    return int(col.strip().split(' ')[0])

def amountGreen(col):
    return int(col.strip().split(' ')[0])

games = []

for l in lines:
    gid = int(l.split(':')[0].split(' ')[1])
    sets = l.split(':')[1].split(';')
    possible = True
    minRed = 0
    minBlue = 0
    minGreen = 0
    for s in sets:
        if not possible:
            break
        cols = s.split(',')


        for c in cols:
            if 'red' in c and amountRed(c) > minRed:
                minRed = amountRed(c)

            if 'blue' in c and amountBlue(c) > minBlue:
                minBlue = amountBlue(c)

            if 'green' in c and amountGreen(c) > minGreen:
                minGreen = amountGreen(c)

    games.append(minRed * minBlue * minGreen)

print(sum(games))