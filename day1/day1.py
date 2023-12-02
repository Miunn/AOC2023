with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]


def literalToNumber(literal):
    if literal == 'one':
        return '1'
    if literal == 'two':
        return '2'
    if literal == 'three':
        return '3'
    if literal == 'four':
        return '4'
    if literal == 'five':
        return '5'
    if literal == 'six':
        return '6'
    if literal == 'seven':
        return '7'
    if literal == 'eight':
        return '8'
    if literal == 'nine':
        return '9'

    return ''

def searchLiteral(literals, c, reverse=False):
    for i in range(len(literals)):
        literals[i] += c
        conv = literalToNumber(literals[i] if not reverse else literals[i][::-1])
        if conv != '':
            return (literals, conv)
    
    literals.append(c)
    
    return (literals, '')

output = 0
for l in lines:
    value = ''
    literals = []
    for c in l:
        literals, converted = searchLiteral(literals, c)
        if converted != '':
            value += converted
            break

        try:
            value = str(int(c))
            break;
        except:
            continue
    
    literals = []
    for c in l[::-1]:
        literals, converted = searchLiteral(literals, c, reverse=True)
        if converted != '':
            value += converted
            break
        try:
            value += str(int(c))
            break;
        except:
            continue
    
    output += int(value)

print(output)