from parsing import ts_manager as ts

f1 = ts.Formula("Ka2p")
parser = ts.TSManager(f1.formula)

print(f1.parse())
print(f1.get_agent())
# for i in f1.get_subformulas():
#     print(i.formula)



