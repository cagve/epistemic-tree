from epistemictree import rules as rl
from epistemictree import tui as tui
from epistemictree import utils

def main():
    tree = herzig['tree2']
    print("SISTEMA K4")
    value = rl.run_tableau('k4',tree[0],tree[1])
    value[1].print_tree(value[1].root, 2)
    value[1].print_label_tree(value[1].root, 2)
    print(value[0])
    value[2].print_model()
    utils.dot_to_latex()

herzig = {
        # Pag 126. Fig 5.1
        'tree1' : ['-(-KaKa-p&&Ka-p)', None], 
        'tree2' : ['-(-Ka-p && Ka-Ka-p)', None ],
        'tree3' : ['-(-Ka-p && Ka-Ka-p)', None ]
        }


herzig = {
        # Pag 126. Fig 5.1
        'tree1' : ['-(-KaKa-p&&Ka-p)', None], 
        'tree2' : ['-(-Ka-p && Ka-Ka-p)', None ],
        'tree3' : ['-(-KaKa-p && Ka-p)', None ],
        'tree4' : ['-(Kap && (-Ka-q && -Ka-(r||-p)))', None ],
        'tree5' : ['-(-Ka-p)', ['Ka(p =>(-Ka-q))','-Kap']]
        }
if __name__ == '__main__':
    main()
