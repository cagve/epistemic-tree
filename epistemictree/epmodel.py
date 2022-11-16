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

    def get_agents(self):
        agents = []
        for relation in self.relations:
            agents.append(relation.agent)
        return set(agents)

    def get_relations_by_agent(self, agent):
        """Return tuples for an agent"""
        relations = []
        for relation in self.relations:
            if relation.agent == agent:
                relations.append(relation.to_tuple())
        return relations

    def print_worlds(self):
        for i in self.worlds:
            print(i.to_string(), end=", ")

    def print_relations(self):
        for i in self.relations:
            print(i.to_string(), end=", ")

    def add_relation(self, relation):
        self.relations.append(relation)

    def contain_world(self, world):
        for r in self.worlds:
            if r.name == world.name:
                return True
        return False

    def contain_relation(self, relation):
        for r in self.relations:
            if r.world1.name == relation.world1.name and r.world2.name == relation.world2.name and r.agent == relation.agent:
                return True
        return False

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

    def print_dot(self, filedot:str):
        print("PRINTING "+filedot)
        file = open(filedot, 'w')
        file.write("digraph G {\n")
        file.write("node[shape=record]\n")
        print("Printing model dot")
        for world in self.worlds:
            evaluation = world.evaluation_to_string().replace('||','v').replace(',','\\n')
            if world.is_superfluo():
                file.write(world.name+'[style=dashed, color=blue, label="'+world.name+' | '+evaluation+'"];\n')
            else:
                file.write(world.name+'[label="'+world.name+' | '+evaluation+'"];\n')
        for relation in self.relations:
            if relation.type == "normal":
                file.write(relation.world1.name+' -> '+relation.world2.name+'[label="'+relation.agent+'"];\n')
            elif relation.type == "superfluo":
                file.write(relation.world1.name+' -> '+relation.world2.name+'[style=dashed,color=blue, label="'+relation.agent+'"];\n')
            elif relation.type == "closure":
                file.write(relation.world1.name+' -> '+relation.world2.name+'[ color=red, label="'+relation.agent+'"];\n')
        file.write("}")
        file.close

    def reflexive_closure(self, agent):
        print("Añadiendo reflexive closure")
        for world in self.worlds:
            relation = Relation( world, world, agent, "closure")
            if not self.contain_relation(relation):
                self.add_relation(relation)

    def transitive_closure(self,agent):
        """Method to make the model transitive. Only attends to the relation of the agent."""
        print("Añadiendo transitive closure")
        closure = set(self.get_relations_by_agent(agent))
        while True:
            new_relations = set((x,w) for x,y in closure for q,w in closure if q == y)
            for i in new_relations:
                world1 = World(str(i[0]))
                world2 = World(str(i[1]))
                relation = Relation( world1, world2,agent, "closure")
                if not self.contain_relation(relation):
                    print(relation.to_string()+" not in model")
                    self.add_relation(relation)
            closure_until_now = closure | new_relations
            if closure_until_now == closure:
                break
            closure = closure_until_now
        return closure

    def eq_bisimulate(self):
        bisimulate_W = []
        for world in self.worlds:
            if world.is_superfluo():
                print("============"+world.name+" is superfluos ================")
                originals = world.get_originals()
                for original in originals:
                    ori = self.get_world_by_name(original.name)
                    if not ori:
                        print("Error not originals in model") 
                        return 
                    world_evaluation = world.evaluation_to_list()
                    ori_evaluation = ori.evaluation_to_list()
                    print("Originals "+ori.name+" evaluation " + ori.evaluation_to_string())
                    print("World "+world.name+"evaluation " + world.evaluation_to_string())
                    eq_super = all(formula in ori_evaluation for formula in world_evaluation)
                    if eq_super:
                        print(world.name + " is equal superfluos of "+ ori.name)
                    else:  
                        print(world.name + " is not equal superfluos of "+ ori.name)
                        new_world = World(world.name)
                        new_world.add_true_formula_list(world.evaluation)
                        bisimulate_W.append(world)
            else:
                print(world.name+" no es superfluo, hay que incluirlo")
                new_world = World(world.name)
                new_world.add_true_formula_list(world.evaluation)
                bisimulate_W.append(world)

        bisimulate_Model = Model(bisimulate_W, None)
        for relation in self.relations:
            world1 = relation.world1
            world2 = relation.world2
            if bisimulate_Model.contain_world(world1) and bisimulate_Model.contain_world(world2):
                bisimulate_Model.add_relation(relation)

        return bisimulate_Model


    def bisimulate(self):
        print("Bisimulation...")
        bisimulate_W = []
        bisimulate_R = []
        for world in self.worlds:
            if not world.is_superfluo():
                print(world.name+" no es superfluo, hay que incluirlo")
                new_world = World(world.name)
                new_world.add_true_formula_list(world.evaluation)
                bisimulate_W.append(world)

        bisimulate_Model = Model(bisimulate_W, None)
        for relation in self.relations:
            world1 = relation.world1
            world2 = relation.world2
            if bisimulate_Model.contain_world(world1) and bisimulate_Model.contain_world(world2):
                bisimulate_Model.add_relation(relation)

        return bisimulate_Model




    def closures(self, agents, system):
        print(agents)
        if agents:
            for agent in agents:
                if "t" in system:
                    self.reflexive_closure(agent)
                if "4" in  system:
                    self.transitive_closure(agent)




class Relation():
    def __init__(self, world1, world2, agent, type):
        self.world1=world1
        self.world2 = world2
        self.agent = agent
        self.type = type

    def to_string(self):
        return '<'+self.world1.name+self.agent+self.world2.name+'>'

    def to_tuple(self):
        return(int(self.world1.name),int(self.world2.name))


class World():
    def __init__(self, name:str, relations = None, evaluation = None, originals = None):
        if evaluation == None:
            self.evaluation=[]
        else:
            self.evaluation=evaluation
        self.name=name
        self.relations = relations
        if originals == None:
            self.originals=[]
        else:
            self.originals=originals

    def add_original(self, world):
        self.originals.append(world)
    
    def filter_modal_formulas(self) -> list:
        formula_list = []
        for formula in self.evaluation:
            if formula.is_modal():
                formula_list.append(formula)
        return formula_list

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
                formula_list = formula_list+', '+ev.formula
        return formula_list.replace("=>","→")


    def evaluation_to_list(self):
        """LIST OF FORMULA IN STRING FORMAT"""
        formula_list  = []
        for ev in self.evaluation:
                formula_list.append(ev.formula)
        return formula_list

    def get_originals(self):
        return self.originals

    def is_superfluo(self):
        if(self.get_originals()):
            return True
        return False
        
