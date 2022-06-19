from epistemictree import rules as rl
from epistemictree import tui as t
from epistemictree.parser import Formula

def main():
    t.run()

def test():
    formula1 = Formula("Kap")
    formula2 = Formula("-Kap")
    formula3 = Formula("-KapKaq")
    formula4 = Formula("--Kap-Kbq")
    formula5 = Formula("Kap")
        

if __name__ == '__main__':
    main()
