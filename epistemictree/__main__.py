from epistemictree import rules as rl
import os
from epistemictree import tui as tui
from epistemictree import utils


def main():
    examples()

def examples():
    tree = exe['tree2']
    print("SISTEMA K4")
    value = rl.run_tableau('k4',tree[0],tree[1])
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" Existe contramodelo > "+ str(value[0]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if value[0]:
        print(" Contramodelo:")
        print(value[2].print_model())
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    utils.dot_to_latex()

exe = {
        # Pag 126. Fig 5.1
        'tree1' : ['-(-KaKa-p&&Ka-p)', None], 
        'tree2' : ['-(p&&-Kap)', None], 
        'tree3' : ['-(-Ka-p && Ka-Ka-p)', None ],
        'tree4' : ['-(-KaKa-p && Ka-p)', None ],
        'tree5' : ['-(Kap && (-Ka-q && -Ka-(r||-p)))', None ],
        'tree6' : ['-(-Ka-p)', ['Ka(p =>(-Ka-q))','-Kap']],
        'tree7' : ['-(-Ka-p)', ['Ka(p =>(-Ka-q))','Ka-q']]
        }



if __name__ == '__main__':
    main()
