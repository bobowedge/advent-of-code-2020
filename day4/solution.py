
required_fields = set(['byr', 'iyr', 'eyr', 'hgt',
                       'hcl', 'ecl', 'pid'])
optional_fields = set(['cid'])

def eval_passport1(p:dict):
    fields = set(p.keys())
    xset = fields.intersection(required_fields)
    return xset == required_fields

def eval_passport2(p:dict):
    if not eval_passport1(p):
        return False
    try:
        byr = int(p['byr'])
        if byr < 1920 or byr > 2002:
            return False
        iyr = int(p['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False
        eyr = int(p['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False
        hgt = p['hgt']
        val = int(hgt[:-2])
        unit = hgt[-2:]
        if unit == "cm":
            if val < 150 or val > 193:
                return False
        elif unit == "in":
            if val < 59 or val > 76:
                return False
        else:
            return False
        hcl = p['hcl']
        values = set(list(hcl[1:]))
        valids = set(list("0123456789abcdef"))
        if hcl[0] != "#" or not values.issubset(valids):
            return False
        if p['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            return False
        pid = p['pid']
        values = set(list(pid))
        valids = set(list("0123456789"))
        if len(pid) != 9 or not values.issubset(valids):
            return False
        return True
    except:
        return False

testData1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".splitlines()

testData2 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".splitlines()

valids1 = 0
valids2 = 0
passport = {}
with open("passports.txt") as file:
    for line in file:
    #for line in testData2:
        line = line.strip()
        if len(line) == 0:
            if eval_passport1(passport):
                valids1 += 1
                if eval_passport2(passport):
                    valids2 += 1
            passport = {}
        else:
            line = line.split()
            for field in line:
                (x, y) = field.split(":")
                passport[x] = y

if eval_passport1(passport):
    valids1 += 1
    if eval_passport2(passport):
        valids2 += 1

print(valids1, valids2)