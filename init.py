from parsing import ts_manager as ts

f1 = ts.Formula("--q&&p")
parser = ts.TSManager(f1.formula)

print(f1.parse())
# for i in f1.get_subformulas():
#     print(i.formula)



