import os
import plac
from epistemictree import rules as rl
from epistemictree import tui as t

@plac.opt('premises', "Premises", type=str)
@plac.opt('conclusion', "Conclusion", type=str)
@plac.flg('tui', "Terminal interface")

def main(premises, conclusion, tui=False):
    """A script for run epistemic tableaux"""
    if tui:
        t.run()
    else:
        val = rl.test_theorem(conclusion,premises.split())
        if val:
            print("Open tree")
        else:
            print("Closed tree")
    pass
        

if __name__ == '__main__':
    plac.call(main)
