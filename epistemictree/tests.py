import os
from json2html import *
import json
from epistemictree import rules

# Test list

test_list = {
    # 'test1':['-Ka((-KaKb-q)&&(Kb-KaKb-r))&&-KbKa(-Kb-r&&q)', "k4"], 
    # 'test2':['-Ka((-KaKb-q)&&(Kb-KaKb-r))&&-KbKa(-Kb-r&&q)', "kt4"], 
    # 'test3':['-KaKb-(p&&-Kb-q)&&-KbKb-(p&&-Kb-q)', "k4"], 
    'test4':['-KaKb-(p&&-Kb-q)&&-KbKb-(p&&-Kb-q)', "kt4"], 
    # 'test5':['-KaKb-(-Kb-r&&q)&&-Kb-((-KaKb-q&&Kb-KaKb-r) && (p&&-Kb-q))', "k4"], 
    'test6':['-KaKb-(-Kb-r&&q)&&-Kb-((-KaKb-q&&Kb-KaKb-r) && (p&&-Kb-q))', "kt4"], 
        }

 # Data to be written
def test_json(dict, formula, system, models, tree):
    if dict is None:
        dict = []
    data = open("/home/karu/tests/sample.json")
    model_dict_list = {
        "Formula": ' '.join(formula),
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
        models = rules.epistemic_tableau(formulas, system, file_path, True, True, True)[2]
        tree = rules.epistemic_tableau(formulas, system, file_path, True, True, True)[1]        
        test_json(dict, formulas, system, models, tree)

    json_object = json.dumps(dict, indent=4)
    html_object = json2html.convert(json = json_object)
    print(html_object)
    with open("/home/karu/tests/sample.json", "a") as outfile:
        outfile.write(json_object)
    with open("/home/karu/tests/sample.html", "a") as outfile:
        outfile.write(html_object)
