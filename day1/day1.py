with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]

output = 0
for l in lines:
    value = ''
    for c in l:
        try:
            value = str(int(c))
            break;
        except:
            continue
    
    for c in l[::-1]:
        try:
            value += str(int(c))
            break;
        except:
            continue
    
    output += int(value)

print(output)