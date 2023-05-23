import os
import json
from epistemictree import rules
from epistemictree import parser

# Test list

test_list = {
        # 'lotrec1':['(Ka-Ka-Ka(p||q))&&((Ka-Kap) && (-Ka-Ka-r))']
    # 'paperexample':['-KaKb-(-Kb-p&&q)&&-Kb-((Kb-KaKb-p&&-KaKb-q)&&(-Kb-q &&r))', "kt4"], 
    # 'paperexamplemonoagente':['-KaKa-(-Ka-p&&q)&&-Ka-((Ka-KaKa-p&&-KaKa-q)&&(-Ka-q &&r))', "kt4"], 
    # 'paper2':['Ka(Kap => Kaq) || Ka(Kaq => Kap)', "kt4"], 

    # 'lotrec1':['Ka(-Ka-(Ka(p||q)))&&Ka(-Ka-(-p))','kt4'],
    # 'lotrec2':['Ka(-Ka- (Ka (p || q))) && Ka(-Ka- (- p)) && -Ka-(Ka (- r))','kt4'],
    # 'lotrec3':['Ka(-Ka- (Ka (p || q))) && Ka(-Ka- (- s)) && -Ka-(Ka (- r))','kt4'],
    # 'lotrec4':['Ka(Ka p => p) && (Ka (Ka (p => Ka p) => p) => -Ka- (Ka p) => p => Ka (Ka (p => Ka p) => p) => -Ka- (Ka p) => p)','kt4'],
    # 'lotrec5':['Ka (-Ka- (Ka p) => p) => Ka (Ka (-Ka- (Ka p) => p))','kt4'],
    #
    #  'alfredo1':['Ka-Ka-p => -Ka-Kap','kt4'],
    #  'alfredo2':[' (-Ka-p && -Ka-q) && ((-Ka-p && -Ka-q) && (-Ka-p && -Ka-q))','kt4'],
    #
    #  'custom1':['Ka-Ka-Kap && -Ka-Ka-r','kt4'],
    #  'custom2': [' (-KaKa-p &&-Ka-(-Ka-(-Ka-p&&q)&&-Ka-((-Ka-p&&q) && Kar))) && (-Ka-(q&&-KaKa-r)&&-Ka-(q && -Ka-r))','kt4']
     # 'custom3': ['Ka(-Ka-p && -Ka-q) && ( Ka Ka(-Ka-p && -Ka-q) && Ka Ka Ka(-Ka-p && -Ka-q))','kt4']
      # 'custom4': [' -Ka--Ka-(-Ka-p && q)&&-Ka-((Ka-Ka--Ka-p && -Ka--Ka-q)&&(-Ka-q && r))','kt4']
      'custom5': [' (-Ka-Ka-Ka-p && -Ka--Ka-((p&&q)&&r))&&(-Ka--Ka-p &&Ka-Ka-(q&&r))', 'kt4']

 


    # "random0":["Kc-KcKdp||r", 'kt4'],
    # "random1":["p||-Kd--KcKdq", 'kt4'],
    # "random2":["p||p&&q||r=>r", 'kt4'],
    # "random3":["KdKbr||KaKcq", 'kt4'],
    # "random4":["-Kd-Kc--Kbp", 'kt4'],
    # "random5":["p=>p=>Kd-Kaq", 'kt4'],
    # "random6":["r=>-Kc-Kaq=>r", 'kt4'],
    # "random7":["KbKdr&&q=>r", 'kt4'],
    # "random8":["p&&Kbq=>-r&&r", 'kt4'],
    # "random9":["r||p&&Kc-Kdp", 'kt4'],
    # "random10":["Kc---Kd-Kcr", 'kt4'],
    # "random11":["q||-KaKbq||q", 'kt4'],
    # "random12":["r=>q||-Kbq||p", 'kt4'],
    # "random13":["-KaKcp||KdKap", 'kt4'],
    # "random14":["Kb-KbKd-Kc-Kap", 'kt4'],
    # "random15":["r&&-KbKaKdp", 'kt4'],
    # "random16":["q&&-Kdq&&-Kcq", 'kt4'],
    # "random17":["p=>-Kbr||p||r", 'kt4'],
    # "random18":["-Kb-Kbr||r||q", 'kt4'],
    # "random19":["q||Kc-Ka-Kbr", 'kt4'],
    # "random20":["r&&-Kdp&&q=>q", 'kt4'],
    # "random21":["r=>q=>p&&-Kdr", 'kt4'],
    # "random22":["-KaKdr&&Kdr", 'kt4'],
    # "random23":["r||-Kbp&&Kar", 'kt4'],
    # "random24":["q&&q||-q||-Kbp", 'kt4'],
    # "random25":["-KbKdq||-Kcp", 'kt4'],
    # "random26":["r=>p&&-r||p", 'kt4'],
    # "random27":["r&&-Kc-q||q", 'kt4'],
    # "random28":["-KcKdKcKbKaq", 'kt4'],
    # "random29":["r&&p=>-Kaq||q", 'kt4'],
    # "random30":["p||r||-KaKcq", 'kt4'],
    # "random31":["r||-Kc-KbKcr", 'kt4'],
    # "random32":["-Kc-Kb-Kb-Kdq", 'kt4'],
    # "random33":["q&&-Kbr||Kap", 'kt4'],
    # "random34":["q&&Kb-KbKd-Kdp", 'kt4'],
    # "random35":["p||KbKbKcq=>r", 'kt4'],
    # "random36":["Kd-KcKaKdr", 'kt4'],
    # "random37":["r&&r&&-Kb-Kbr", 'kt4'],
    # "random38":["-Kd-Kdr||Kbq", 'kt4'],
    # "random39":["KaKd-p=>p", 'kt4'],
    # "random40":["p&&-Kdp||r||p", 'kt4'],
    # "random41":["Ka-Kb-Ka-Kdq", 'kt4'],
    # "random42":["p||Kcp=>KdKbr", 'kt4'],
    # "random43":["-Kd-Kc-Kd-Kdq", 'kt4'],
    # "random44":["-Kap||q||-Kaq", 'kt4'],
    # "random45":["-Kb-Kc-Ka-Kbr", 'kt4'],
    # "random46":["q&&-Kb-Ka-Kdp", 'kt4'],
    # "random47":["KaKc-q||-Kar", 'kt4'],
    # "random48":["q||q=>Kb-Kdp", 'kt4'],
    # "random49":["Kdq=>r&&p||p", 'kt4'],
    # "random50":["Kdr=>-KdKb-Kdq", 'kt4'],
    # "random51":["-KcKcp&&r&&r", 'kt4'],
    # "random52":["Kcr||Kc-q||r", 'kt4'],
    # "random53":["-KbKdp=>Kc-Kcr", 'kt4'],
    # "random54":["r&&Kaq=>-Kbq", 'kt4'],
    # "random55":["q=>-Kbq&&Kbp", 'kt4'],
    # "random56":["-KdKbKd-Ka-Kaq", 'kt4'],
    # "random57":["p||KcKcq=>q", 'kt4'],
    # "random58":["r&&--p=>p||p", 'kt4'],
    # "random59":["q=>p||-KdKbp", 'kt4']
    # "random1":["KbKd-Kb-Kb-Kd-Kap", "kt4"],
    # "random2":["r||-Kd-Kc-Kd-Kc-Kap", "kt4"],
    # "random3":["Ka-Kb-Kc-Ka-Ka-Kbr", "kt4"],
    # "random4":["-Kd-KaKd-Kc-Kd--Kdr", "kt4"],
    # "random5":["Kb-Kc-Kd-Kb-Kc-Kbp", "kt4"],
    # "random6":["Kc-Kc-Kc-Kb-Ka-Kaq", "kt4"],
    # "random7":["Kbr||Kd-Kd-Kb--Kdr", "kt4"],
    # "random8":["Kb-Kc-Kar=>-Kd-Kdp", "kt4"],
    # "random9":["-Kb-Ka-Ka--Kd-Kdq", "kt4"],
    # "random10":["q&&-KdKd-Kb-Kd-Kdr", "kt4"],
    # "random11":["-KdKd-Kc-Kd-KdKbp", "kt4"],
    # "random12":["Kb-Kb-Ka-Kb-Kd-Kcq", "kt4"],
    # "random13":["-Kb-Ka-Kc-Kc-Kb-Kdp", "kt4"],
    # "random14":["r=>Ka-Kdp||-Kc-Kdr", "kt4"],
    # # "random15":["Kb--Kd-Kb-Kc-Kcq", "kt4"],
    # "random16":["-Kc-Kd-Kc-Kb-Kd-Kap", "kt4"],
    # "random17":["Ka-Kb-Kc-Kc-Ka-Kap", "kt4"],
    # "random18":["p||-Kb-KaKb-Kb-Kar", "kt4"],
    # "random19":["-Kd-Kc-Kd-Ka-Kd-Kdr", "kt4"],
    # "random20":["-Kd-Kc-Ka-Ka-Kb-Kar", "kt4"],
    # "random21":["r||--Ka-Kd-Ka-Kcp", "kt4"],
    # "random22":["p&&r=>-Kb-Kc-Kc-Kbr", "kt4"],
    # "random23":["KdKb-Kd-Ka-Kb-Kar", "kt4"],
    # "random24":["Kb-Kc-Kc-Kc-Kd-Kbr", "kt4"],
    # "random25":["q&&Kb-Kd-Kbq&&Kdp", "kt4"],
    # "random26":["-Kb-Kc-Kd-Kc-Kd-Kdp", "kt4"],
    # "random27":["Kc-Ka-Ka-Kc-Kd-Kbq", "kt4"],
    # "random28":["Kc-Kb-Kd-Kb-KdKbr", "kt4"],
    # "random29":["r=>Kb-Kc-Kc-Kb-Kcr", "kt4"],
    # "random30":["Ka-Kc-Kb-Kd-Ka-Kar", "kt4"],
    # "random31":["-Kc-Kc-Ka-Ka-Kd-Kap", "kt4"],
    # "random32":["-KaKd-Kb-Kb-Kc-Kbp", "kt4"],
    # "random33":["Kc-Ka-Ka-Ka-Kd-Kdp", "kt4"],
    # "random34":["Kd-Kcp||r=>Kb-Kdr", "kt4"],
    # "random35":["r=>Kd-Kcp=>Kd-Kaq", "kt4"],
    # "random36":["-Kd-Ka-Kc-Kb-Kcp", "kt4"],
    # "random37":["-Kd-Ka-Kdr||q||p", "kt4"],
    # "random38":["-Kd-Kd-Kc-Kbr&&Kcq", "kt4"],
    # "random39":["Kc-Kc-Ka-Kb-Kb-Kbp", "kt4"],
    # "random40":["q||Kc-Ka-KcKc-Kcp", "kt4"],
    # "random41":["Kc-Kc-Ka-Kc-Kd-Kdr", "kt4"],
    # "random42":["Kc-Kc-Kc-Kc-Kd-Kcq", "kt4"],
    # "random43":["r&&KaKb-Kd-Kb-Kcq", "kt4"],
    # "random44":["-Kb-Kd-Kc-Ka-Kc-Kdp", "kt4"],
    # "random45":["p||q&&--Kd-Kc-Kbp", "kt4"],
    # "random46":["q&&-Kc-Ka-KcKa-Kar", "kt4"],
    # "random47":["-Kb-Kb-Kdr&&-Kb-Kdq", "kt4"],
    # "random48":["p||Kd-Kd-Ka-Kd-Kdp", "kt4"],
    # "random49":["Kc-Kd-Ka-KbKc-Kdp", "kt4"],
    # "random50":["-Ka-Ka-Kd-Kc-Ka-Kcr", "kt4"],
    # "random51":["-Kd-Kc-Kd-Ka-Kc-Kap", "kt4"],
    # "random52":["-Kb-Kb-Kb-Kb-Kd-Kbp", "kt4"],
    # "random53":["q&&-Kc--Kc-Kd-Kbp", "kt4"],
    # "random54":["q&&-Ka-Ka-Kd-Kd-Kbr", "kt4"],
    # "random55":["p=>r&&--Ka-Kd-Kcp", "kt4"],
    # "random56":["q&&-Kc-Kd-Kc-Kb-Kdp", "kt4"],
    # "random57":["q=>-Kb-Kd-Kc-Kd-Kcr", "kt4"],
    # "random58":["p&&Kc-Ka-Kb-Ka-Kar", "kt4"],
    # "random59":["Kar||Kc-Kb-Kb-Kdq", "kt4"],
    # "random60":["q||Kc-Ka-Kc-KbKdq", "kt4"],
    # "random61":["-Ka-Kbq&&-Kb-Kdr", "kt4"],
    # "random62":["r=>Ka-Kb-Ka-Kc-Kdp", "kt4"],
    # "random63":["p&&-Kd-Kc-Ka-Kb-Kbr", "kt4"],
    # "random64":["q&&-Ka-Kc-Kc-Kd-Kcr", "kt4"],
    # "random65":["-Kc-Kb-Ka-Kc-Kc-Kdq", "kt4"],
    # "random66":["Kb-Kd-Kb-Kar=>Kdr", "kt4"],
    # "random67":["q||Ka-Kc-Ka-Kd-Kar", "kt4"],
    # "random68":["Ka-Kb-Kc-Kd-Kc-Kbp", "kt4"],
    # "random69":["-Kc-Kb-Kd-Ka-Kd-Kcr", "kt4"],
    # "random70":["-Kd-Kb-Kc-Ka-Kc-Kap", "kt4"],
    # "random71":["Kb-Kd-Kar=>-Kb-Kcr", "kt4"],
    # "random72":["Ka-Kd-Kb-Kdq||-Kbr", "kt4"],
    # "random73":["Kd-Ka-Ka-Kc-KaKdr", "kt4"],
    # "random74":["Kd-Kd-Kb-Kd-Ka-Kaq", "kt4"],
    # "random75":["p&&Ka-Kc-Kd-Kc-Kbr", "kt4"],
    # "random76":["-Kdp||-Kd-Kd-Kc-Kcq", "kt4"],
    # "random77":["-Kdq=>-Kb-Ka-Kb-Kcq", "kt4"],
    # "random78":["p||-Kb-Ka-Ka-Kc-Kbp", "kt4"],
    # "random79":["q=>p||Kb-Kd-Kdq&&q", "kt4"],
    # "random80":["-Kb-Ka-Kb-Kc-Kb-Kbq", "kt4"],
    # "random81":["q||-Ka-Kd-Kb-Kd-Kdp", "kt4"],
    # "random82":["-Kd-Ka-Kb-Kd-Kdp", "kt4"],
    # "random83":["r||-Kd-Kb-Kc-Kb-Kbp", "kt4"],
    # "random84":["-Kap=>Kd--Kdp||r", "kt4"],
    # "random85":["q||p||-Ka-Ka-Kc-Kbr", "kt4"],
    # "random86":["-Kb-Kap&&--Kdq=>r", "kt4"],
    # "random87":["p=>Ka-Kd-KaKb-Kcr", "kt4"],
    # "random88":["q||--Ka-Kc-Kc-Kdq", "kt4"],
    # "random89":["p&&q&&q||Kd-Kc-Kaq", "kt4"],
    # "random90":["Kb-Kc-Kb-Kd-Kb-Kdp", "kt4"],
    # "random91":["-Kc-Ka-Kap||--Kcq", "kt4"],
    # "random92":["Kc-Kd-Kd-Kb-Kc-Kcq", "kt4"],
    # "random93":["-Kc-Ka-Ka-Ka-Kd-Kcq", "kt4"],
    # "random94":["-Ka-Kd-KbKd-Ka-Kdp", "kt4"],
    # "random95":["-Kc-Kd-Kd-Ka-Ka-Kdp", "kt4"],
    # "random96":["-Kc-Ka-Kb-Ka-Kc-Kdr", "kt4"],
    # "random97":["-Kb-Kd-Kd-Ka-Ka-Kap", "kt4"],
    # "random98":["Kc-Kcq||Kbq||Kd-Kcr", "kt4"],
    # "random99":["-Kb-KdKc-Ka-Kd-Kdq", "kt4"],
    }
    

 # Data to be written
def test_json(dict, name,  formulas, system, models, tree):
    if dict is None:
        dict = []
    data = open("/home/caguiler/tests/sample.json")
    if len(formulas) == 1:
        f = parser.Formula(formulas[0])
    model_dict_list = {
            "Name": name,
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
    with open("/home/caguiler/tests/sample.json", "w") as outfile:
        outfile.write("")
    for key in test_list:
        file_path = "/home/caguiler/tests/"+key
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        formulas = test_list[key][0].split(',')
        system = test_list[key][1]
        print("====== Current test: "+ key + " ==========")
        print("Formula: "+str(formulas))
        print("System: "+system)
        models = rules.epistemic_tableau(formulas, system, file_path, True, True, False)[2]
        tree = rules.epistemic_tableau(formulas, system, file_path, True, True, False)[1]        
        test_json(dict, key, formulas, system, models, tree)
    json_object = json.dumps(dict, indent=4)
    with open("/home/caguiler/tests/sample.json", "a") as outfile:
        outfile.write(json_object)

    for key in test_list:
        file_path = "/home/caguiler/tests/"+key+"simulated"
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        formulas = test_list[key][0].split(',')
        system = test_list[key][1]
        print("====== Current test: "+ key + " ==========")
        print("Formula: "+str(formulas))
        print("System: "+system)
        models = rules.epistemic_tableau(formulas, system, file_path, True, True, True)[2]
        tree = rules.epistemic_tableau(formulas, system, file_path, True, True, True)[1]        
        test_json(dict, key, formulas, system, models, tree)
    #
    json_object = json.dumps(dict, indent=4)
    with open("/home/caguiler/tests/samplebisi.json", "a") as outfile:
        outfile.write(json_object)

