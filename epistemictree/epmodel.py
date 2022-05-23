class Model():
    def __init__(self, worlds = None, relations = None):
        if worlds == None:
            self.worlds=[]
        else:
            self.worlds=worlds
        if relations == None:
            self.relations=[]
        else:
            self.relations=relations
    
    def add_world(self, world):
        self.worlds.append(world)

    def print_worlds(self):
        for i in self.worlds:
            print(i.to_string(), end=", ")

    def print_relations(self):
        for i in self.relations:
            print(i.to_string(), end=", ")

    def add_relation(self, relation):
        self.relations.append(relation)

    def get_world_by_name(self, name:str):
        for world in self.worlds:
            if world.name == name:
                return world
        return None
    
    def print_model(self):
        print("W = {", end="") 
        self.print_worlds()
        print("}")
        print("R = {", end="") 
        self.print_relations()
        print("}")
        for world in self.worlds:
            print("V("+world.name+")={", end=" ")
            for literal in world.evaluation:
                print(literal.formula, end=", ")
            print("}")

    def print_dot(self):
        file = open("/home/karu/model.dot", 'w')
        file.write("digraph G {\n")
        for world in self.worlds:
            file.write(world.name+'[label="'+world.name+' \\n '+world.evaluation_to_string()+'"];\n')
        for relation in self.relations:
            file.write(relation.world1.name+' -> '+relation.world2.name+'[label="'+relation.agent+'"];\n')
        file.write("}")
        file.close



class Relation():
    def __init__(self, world1, world2, agent):
        self.world1=world1
        self.world2 = world2
        self.agent = agent

    def to_string(self):
        return '<'+self.world1.name+self.agent+self.world2.name+'>'


class World():
    def __init__(self, name:str, relations = None, evaluation = None):
        if evaluation == None:
            self.evaluation=[]
        else:
            self.evaluation=evaluation
        self.name=name
        self.relations = relations

    def to_string(self):
        return self.name

    def get_accesible_worlds(self):
        return self.relations

    def add_true_formula(self, formula):
        self.evaluation.append(formula)

    def add_true_formula_list(self, formula_list):
        for formula in formula_list:
            for f in self.evaluation:
                if formula.formula == f.formula:
                    return 
            self.evaluation.append(formula)

    def evaluation_to_string(self):
        formula_list  = ""
        for ev in self.evaluation:
            if formula_list=="":
                formula_list = ev.formula
            else:
                formula_list = formula_list+','+ev.formula
        return formula_list
