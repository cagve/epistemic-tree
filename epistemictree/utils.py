from os import wait


def superfluo_test(branch, label1,label2):
    base1 = branch.get_base_set(label1)
    list1=[formula.formula for formula in base1]

    base2 = branch.get_base_set(label2)
    list2=[formula.formula for formula in base2]

    flag=False
    for i in list1:
        flag = False;
        for j in list2:
            if i==j:
                flag = True
                break ;
    if flag:
        return (list1, list2)
    else:
        for i in list2:
            flag = False;
            for j in list1:
                if i==j:
                    flag = True
                    break ;
        if flag: 
            return(list2,list1)
        else:
            return None

def superfluo(branch, label1, label2):
    # Etiqueta la misma return false
    if label1.label == label2.label:
        return False

    base1 = branch.get_base_set(label1)
    list1=[formula.formula for formula in base1]

    base2 = branch.get_base_set(label2)
    list2=[formula.formula for formula in base2]

    count=0
    flag=True
    while flag and count < len(list1):
        for i in list1:
            if i not in list2:
                flag = False
            count = count+1

    if flag and len(set(list1)) == len(set(list2)):
        # Si son iguales
        if label1.simplify_label()>label2.simplify_label():
            return True
        else:
            return False
    return flag
