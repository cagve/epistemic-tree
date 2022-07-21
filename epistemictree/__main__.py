from epistemictree import rules as rl
import os
from epistemictree import tui as tui
from epistemictree import utils


def main():
    examples()

def examples():
    tree = exe['tree8']
    value = rl.run_tableau('kt4',tree[0],tree[1])
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" Existe contramodelo > "+ str(value[0]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if value[0]:
        print(" Contramodelo:")
        print(value[2].print_model())
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(value[1].print_tree(value[1].root,2))
    print(value[1].print_label_tree(value[1].root,2))
    utils.dot_to_latex()

exe = {
        # Pag 126. Fig 5.1
        'tree1' : ['-(-KaKa-p&&Ka-p)', None], 
        'tree2' : ['-(p&&-Kap)', None], 
        'tree3' : ['-(-Ka-p && Ka-Ka-p)', None ],
        'tree4' : ['-(-KaKa-p && Ka-p)', None ],
        'tree5' : ['-(Kap && (-Ka-q && -Ka-(r||-p)))', None ],
        'tree6' : ['-(-Ka-p)', ['Ka(p =>(-Ka-q))','-Kap']],
        'tree7' : ['-(-Ka-p)', ['Ka(p =>(-Ka-q))','Ka-q']],
        'tree8' : ['-(Ka-Ka-p)', None], # CONTRAMODELO EN S4
        'axioma4' : ['Kap=>KaKap', None], 
        'axioma5' : ['-Kap=>Ka-Kap', None], 
        }



if __name__ == '__main__':
    main()
