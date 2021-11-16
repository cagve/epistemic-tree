from parsing import ts_manager as ts

f1 = ts.Formula("--q&&q")
parser = ts.TSManager(f1.formula)

for i in f1.get_subformulas():
    print(i.formula)



