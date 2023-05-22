import random
formula = "♢a♢b(♢bp∧q)∧♢b(□b♢a♢bp∧♢a♢bq)∧(♢bq ∧r)"
formula = "[] (<> ([] (P v Q))) & [] (<> (~ P)) & <> ([] (~ Q))"
formula = "[] (<> ([] (P v Q))) & [] (<> (~ P))"
formula="[] (<> ([] (P v Q))) & [] (<> (~ P)) & <> ([] (~ R))"
formula="[] (<> ([] (P v Q))) & [] (<> (~ S)) & <> ([] (~ R))"
formula="[] ([] P -> P) & ([] ([] (P -> [] P) -> P) -> <> ([] P) -> P -> [] ([] (P -> [] P) -> P) -> <> ([] P) -> P)"
formula="[] (<> ([] P) -> P) -> [] ([] (<> ([] P) -> P))"

k4="<> P & [] (P -> <> Q) & <> (~ P)"

result = k4.replace("[]","Ka").replace("<>","-Ka-").replace("&","&&").replace("v", '||').replace("~","-").replace("P","p").replace("Q",'q').replace("R",'r').replace("S",'s').replace("->","=>")

print(result)
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
    print('"random0":["'+formula+'", "kt4"],')

def new_element(last_char):
    if last_char in conector["type0"]:
        new_char = conector['type2'][random.randint(0, 2)]
    elif last_char in conector["type1"]: 
        my_list = ['A'] * 5 + ['B'] * 5 + ['C'] * 90
        typ = random.choice(my_list)
        if typ == 'A':
            new_char = conector['type0'][random.randint(0, 2)]
        elif typ == 'B':
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


# i = 0
# while i < 100:
#     random_formula(15)
#     i=i+1;


f1= "[] (<> ([] (P v Q))) & [] (<> (~ P))"
f2= "[] (<> ([] (P v Q))) & [] (<> (~ P)) & <> ([] (~ R)) "
f3= "[] (<> ([] (P v Q))) & [] (<> (~ S)) & <> ([] (~ R))"
f4= "[] ([] P -> P) & ([] ([] (P -> [] P) -> P) -> <> ([] P) -> P -> [] ([] (P -> [] P) -> P) -> <> ([] P) -> P) "
f5= "[] (<> ([] P) -> P) -> [] ([] (<> ([] P) -> P)) "
f6= "[] ([] P -> [] ([] P)) & ([] ([] P -> P) -> <> ([] P) -> [] P) -> [] ([] (P -> [] P) -> P) -> <> ([] P) -> [] P "

f1 = f4.replace("[]","\\square_a").replace("<>","\\lozenge_a").replace("&","\\land").replace("v", '\\lor').replace("~","\\lnot").replace("P","p").replace("Q",'q').replace("R",'r').replace("S",'s').replace("->","\\to")
print(f1)
