def loadData(day):
	return [l.strip() for l in open('input', 'r')] + ['']

def getFields(line):
    result = {}
    parts = line.split(' ')
    for p in parts:
        k, v = p.split(':')
        result[k] = v
    
    return result

def checkFields(fields, required, opt):
    return all(r in fields for r in required)

def checkNumber(payload, min, max):
    try:
        num = int(payload)
    except Exception:
        return False

    return min <= num <= max

def checkBirth(payload):
    return checkNumber(payload, 1920, 2002)

def checkIssue(payload):
    return checkNumber(payload, 2010, 2020)

def checkExpiration(payload):
    return checkNumber(payload, 2020, 2030)

def checkHeight(payload):
    if len(payload) < 3:
        return False

    unit = payload[-2:]
    if unit == 'in':
        return checkNumber(payload[:-2], 59, 76)
    elif unit == 'cm':
        return checkNumber(payload[:-2], 150, 193)
    
    return False
    
def checkHair(payload):
    chars = '0123456789abcdef'
    if len(payload) != 7:
        return False

    return all(c in chars for c in payload[1:]) and payload[0] == '#'

def checkEye(payload):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return payload in valid

def checkID(payload):
    if len(payload) != 9:
        return False

    chars = '0123456789'
    return all(c in chars for c in payload)
    
def checkPassport(data, required):
    return checkFields(data, required.keys(), []) and all(required[k](v) for k, v in data.items() if k in required)

def solve_1():
    required = {
        'byr': checkBirth,
        'iyr': checkIssue,
        'eyr': checkExpiration,
        'hgt': checkHeight,
        'hcl': checkHair,
        'ecl': checkEye,
        'pid': checkID,
    }

    result = 0
    current_fields = {}
    for line in loadData('04'):
        if len(line) == 0:
            if checkPassport(current_fields, required):
                result += 1
            current_fields = {}
        else:
            current_fields.update(getFields(line))
    
    return result
    
print(solve_1())