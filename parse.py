import random
formula = "♢a♢b(♢bp∧q)∧♢b(□b♢a♢bp∧♢a♢bq)∧(♢bq ∧r)"
result = formula.replace("♢a","-Ka-").replace("♢b","-Kb-").replace("□a","Ka").replace("□b","Kb").replace("∧","&&")
simple = result.replace("--", "")

conector  = {
        'type0':["p","q","r"],
        'type1':["Ka", "Kb", "Kc", "Kd", "-"],
        'type2':['&&', '||', '=>'],
        'type3':["-Ka", "-Kb", "-Kc", "-Kd"]
        }


def random_formula(n):
    formula = ''
    while len(formula)<=n:
        if formula == '':
            last_char = '&&'
        else:
            last_char = formula[-1:]
            if last_char not in ['p','q','r','-']:
                last_char = formula[-2:]
        formula = formula + new_element(last_char)

    last_char = formula[-1:]
    if last_char not in ['p','q','r']:
        new_char = conector['type0'][random.randint(0, 2)]
        formula = formula + new_char
    print('"random0":["'+formula+'"],')

def new_element(last_char):
    if last_char in conector["type0"]:
        new_char = conector['type2'][random.randint(0, 2)]
    elif last_char in conector["type1"]: 
        typ = random.randint(0, 2)
        if typ == 0:
            new_char = conector['type0'][random.randint(0, 2)]
        elif typ == 1:
            new_char = conector['type1'][random.randint(0, 4)]
        else:
            new_char = conector['type3'][random.randint(0, 3)]

    elif last_char in conector["type2"]: 
        typ = random.randint(0, 2)
        if typ == 0:
            new_char = conector['type0'][random.randint(0, 2)]
        elif typ == 1:
            new_char = conector['type1'][random.randint(0, 4)]
        else:
            new_char = conector['type3'][random.randint(0, 3)]
    else: 
        print("Not found")
    return new_char


i = 0
while i < 60:
    random_formula(10)
    i=i+1;


