import os
import json
from epistemictree import rules
from epistemictree import parser

# Test list

test_list = {
        # 'lotrec1':['(Ka-Ka-Ka(p||q))&&((Ka-Kap) && (-Ka-Ka-r))']
    # 'paperexample':['-KaKb-(-Kb-p&&q)&&-Kb-((Kb-KaKb-p&&-KaKb-q)&&(-Kb-q &&r))', "kt4"], 
    # 'paper2':['Ka(Kap => Kaq) || Ka(Kaq => Kap)', "kt4"], 
    # 'lotrec1':['Ka-Kap', "kt4"], 
    "random0":["Kc-KcKdp||r", 'kt4'],
    "random1":["p||-Kd--KcKdq", 'kt4'],
    "random2":["p||p&&q||r=>r", 'kt4'],
    "random3":["KdKbr||KaKcq", 'kt4'],
    "random4":["-Kd-Kc--Kbp", 'kt4'],
    "random5":["p=>p=>Kd-Kaq", 'kt4'],
    "random6":["r=>-Kc-Kaq=>r", 'kt4'],
    "random7":["KbKdr&&q=>r", 'kt4'],
    "random8":["p&&Kbq=>-r&&r", 'kt4'],
    "random9":["r||p&&Kc-Kdp", 'kt4'],
    "random10":["Kc---Kd-Kcr", 'kt4'],
    "random11":["q||-KaKbq||q", 'kt4'],
    "random12":["r=>q||-Kbq||p", 'kt4'],
    "random13":["-KaKcp||KdKap", 'kt4'],
    "random14":["Kb-KbKd-Kc-Kap", 'kt4'],
    "random15":["r&&-KbKaKdp", 'kt4'],
    "random16":["q&&-Kdq&&-Kcq", 'kt4'],
    "random17":["p=>-Kbr||p||r", 'kt4'],
    "random18":["-Kb-Kbr||r||q", 'kt4'],
    "random19":["q||Kc-Ka-Kbr", 'kt4'],
    "random20":["r&&-Kdp&&q=>q", 'kt4'],
    "random21":["r=>q=>p&&-Kdr", 'kt4'],
    "random22":["-KaKdr&&Kdr", 'kt4'],
    "random23":["r||-Kbp&&Kar", 'kt4'],
    "random24":["q&&q||-q||-Kbp", 'kt4'],
    "random25":["-KbKdq||-Kcp", 'kt4'],
    "random26":["r=>p&&-r||p", 'kt4'],
    "random27":["r&&-Kc-q||q", 'kt4'],
    "random28":["-KcKdKcKbKaq", 'kt4'],
    "random29":["r&&p=>-Kaq||q", 'kt4'],
    "random30":["p||r||-KaKcq", 'kt4'],
    "random31":["r||-Kc-KbKcr", 'kt4'],
    "random32":["-Kc-Kb-Kb-Kdq", 'kt4'],
    "random33":["q&&-Kbr||Kap", 'kt4'],
    "random34":["q&&Kb-KbKd-Kdp", 'kt4'],
    "random35":["p||KbKbKcq=>r", 'kt4'],
    "random36":["Kd-KcKaKdr", 'kt4'],
    "random37":["r&&r&&-Kb-Kbr", 'kt4'],
    "random38":["-Kd-Kdr||Kbq", 'kt4'],
    "random39":["KaKd-p=>p", 'kt4'],
    "random40":["p&&-Kdp||r||p", 'kt4'],
    "random41":["Ka-Kb-Ka-Kdq", 'kt4'],
    "random42":["p||Kcp=>KdKbr", 'kt4'],
    "random43":["-Kd-Kc-Kd-Kdq", 'kt4'],
    "random44":["-Kap||q||-Kaq", 'kt4'],
    "random45":["-Kb-Kc-Ka-Kbr", 'kt4'],
    "random46":["q&&-Kb-Ka-Kdp", 'kt4'],
    "random47":["KaKc-q||-Kar", 'kt4'],
    "random48":["q||q=>Kb-Kdp", 'kt4'],
    "random49":["Kdq=>r&&p||p", 'kt4'],
    "random50":["Kdr=>-KdKb-Kdq", 'kt4'],
    "random51":["-KcKcp&&r&&r", 'kt4'],
    "random52":["Kcr||Kc-q||r", 'kt4'],
    "random53":["-KbKdp=>Kc-Kcr", 'kt4'],
    "random54":["r&&Kaq=>-Kbq", 'kt4'],
    "random55":["q=>-Kbq&&Kbp", 'kt4'],
    "random56":["-KdKbKd-Ka-Kaq", 'kt4'],
    "random57":["p||KcKcq=>q", 'kt4'],
    "random58":["r&&--p=>p||p", 'kt4'],
    "random59":["q=>p||-KdKbp", 'kt4'],
    }

 # Data to be written
def test_json(dict, formulas, system, models, tree):
    if dict is None:
        dict = []
    data = open("/home/karu/tests/sample.json")
    if len(formulas) == 1:
        f = parser.Formula(formulas[0])
    model_dict_list = {
        "Formula": ' '.join(formulas),
        "Len": f.get_modal_len(),
        "System": system,
        "Num of models": len(models)
            }
    counter = 0
    for model in models:
        num = len(model.worlds)
        model_dict_list["Model "+str(counter)]= num
        counter = counter+1

    index = 0
    for branch in tree.get_open_branchs():
        model_dict_list["Branch "+str(index)]= len(branch) - 1
        index = index+1

    dict.append(model_dict_list)
    return dict


def run_test():
    dict = []
    with open("/home/karu/tests/sample.json", "w") as outfile:
        outfile.write("")
    for key in test_list:
        file_path = "/home/karu/tests/"+key
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        formulas = test_list[key][0].split(',')
        system = test_list[key][1]
        print("====== Current test: "+ key + " ==========")
        print("Formula: "+str(formulas))
        print("System: "+system)
        models = rules.epistemic_tableau(formulas, system, file_path, True, True, False)[2]
        tree = rules.epistemic_tableau(formulas, system, file_path, True, True, False)[1]        
        test_json(dict, formulas, system, models, tree)
    json_object = json.dumps(dict, indent=4)
    with open("/home/karu/tests/sample.json", "a") as outfile:
        outfile.write(json_object)

    for key in test_list:
        file_path = "/home/karu/tests/"+key+"simulated"
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        formulas = test_list[key][0].split(',')
        system = test_list[key][1]
        print("====== Current test: "+ key + " ==========")
        print("Formula: "+str(formulas))
        print("System: "+system)
        models = rules.epistemic_tableau(formulas, system, file_path, True, True, True)[2]
        tree = rules.epistemic_tableau(formulas, system, file_path, True, True, True)[1]        
        test_json(dict, formulas, system, models, tree)

    json_object = json.dumps(dict, indent=4)
    with open("/home/karu/tests/samplebisi.json", "a") as outfile:
        outfile.write(json_object)

# 'test1':['-Ka((-KaKb-q)&&(Kb-KaKb-r))&&-KbKa(-Kb-r&&q)', "k4"], 
# 'test2':['-Ka((-KaKb-q)&&(Kb-KaKb-r))&&-KbKa(-Kb-r&&q)', "kt4"], 
# 'test3':['-KaKb-(p&&-Kb-q)&&-KbKb-(p&&-Kb-q)', "k4"], 
# 'test4':['-KaKb-(p&&-Kb-q)&&-KbKb-(p&&-Kb-q)', "kt4"], 
# 'test5':['-KaKb-(-Kb-r&&q)&&-Kb-((-KaKb-q&&Kb-KaKb-r) && (p&&-Kb-q))', "k4"], 
# 'test6k4':['-KaKb-(-Kb-r&&q)&&-Kb-((-KaKb-q&&Kb-KaKb-r) && (p&&-Kb-q))', "k4"], 
# 'test6kt4':['-KaKb-(-Kb-r&&q)&&-Kb-((-KaKb-q&&Kb-KaKb-r) && (p&&-Kb-q))', "kt4"], 
# 'test7':['Ka(-Ka-(Ka(p||q))) && Ka(-Ka(s)) && (-Ka-Ka-r)', 'kt4']
