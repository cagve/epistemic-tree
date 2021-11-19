from parsing import ts_manager as ts

f1 = ts.Formula("--q&&(p=>-r)")
parser = ts.TSManager(f1.formula)

# f1.get_subformulas()
for i in f1.get_subformulas():
    print(i.formula)



