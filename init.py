from parsing import ts_manager as ts

f1 = ts.Formula("-p")
parser = ts.TSManager(f1.formula)

print(f1.get_term())




