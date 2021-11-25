from parsing import ts_manager as ts

f1 = ts.Formula("Ka(p&&q)")
f2 = ts.Formula("(p&&q)")
f3 = ts.Formula("p&&q")
f4 = ts.Formula("-q")

parser = ts.TSManager(f1.formula)

print("la lóngitud de la fórmula " + str(f1.get_len()))
print("la lóngitud de la fórmula " + str(f2.get_len()))
print("la lóngitud de la fórmula " + str(f3.get_len()))
print("la lóngitud de la fórmula " + str(f4.get_len()))

for i in f1.get_subformulas():
    print(i.formula, end=" ")



