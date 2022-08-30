import os

def dot_to_latex():
    file = open("/home/karu/model.dot", 'r')
    replaced_content = ""
    for line in file:
        line = line.strip()
        new_line = line.replace("->", "@").replace('-','¬').replace('&&', '∧').replace('=>','→').replace('v','∨').replace('@','->')
        replaced_content = replaced_content + new_line + "\n"
    file.close()
    file_write = open("/home/karu/model.dot",'w')
    file_write.write(replaced_content)
    file_write.close()
    os.system('dot -Tpng ~/model.dot > ~/model.png')

