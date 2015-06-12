import csv

# constraints make cost scores

# find minimum cost


# advisor - [student student ... student] matches

#types of constraints:
# advisor: acceptable number of students range - outside range cost = 99999
# advisor: name students they want - cost = -99999 if student names as poss
# students: rank project preference list - cost = 99999 off list?
# groups: average student gpa > (3?)
# not all projects need to be filled

def diff_weight(goal, value, damp, weight):
    return weight*(1+abs(goal-value)/damp)

def optimize_groups

class Constraint(object):
    def __init__(self,penalty_damping=1e6,penalty_weight=1e3):
        self.func = None
        self.pen = penalty_damping
        self.weight = penalty_weight
        return

    def func(self,group,advisor):
        raise ValueError, 'No cost function for constraint defined'
        return #cost

class MinimumGPA(Constraint):
    def __init__(self, min_gpa=3.0, **kwargs):
        super(Constraint,self).__init__(**kwargs)
        self.min_gpa = min_gpa
        return
        
    def func(self, group, advisor):
        gpas = [s.gpa for s in group.students]
        avg_gpa = sum(gpas)/float(len(gpas))
        cost = 0.
        if avg_gpa < self.min_gpa:
            cost += diff_weight(self.min_gpa,avg_gpa,self.pen,self.weight)
        return cost

class GroupSize(Constraint):
    def __init__(self, **kwargs):
        super(Constraint,self).__init__(**kwargs)
        return
        
    def func(self, group, advisor):
        numstu = len(group.students)
        advnum = advisor.num_students
        assert type(advnum)==list, 'Group size limits must be list'
        if len(advnum) == 2:
            minsize = advnum[0]
            maxsize = advnum[1]
        elif len(advnum) == 1:
            minsize = advnum[0]
            maxsize = advnum[0]
        else:
            raise IOError, 'list of group size limits too long'
        cost = 0.
        if numstu < minsize:
            cost += diff_weight(minsize,numstu,self.pen,self.weight)
        elif numstu > maxsize:
            cost += diff_weight(maxsize,numstu,self.pen,self.weight)
        return cost
            
    
class Advisor(object):
    def __init__(self,info):
        self.name = info['name']
        self.student_preferences['student_preferences']
        self.num_students['num_students']
        return

class Group(object):
    def __init__(self,students):
        self.students = students
        return

class Students(object):
    def __init__(self, info):
        self.name = info['name']
        self.preferences = info['preferences']
        self.gpa = info['gpa']
        return

class Match(object):
    def __init__(self,group,advisor):
        self.group = group
        self.advisor = advisor
        self.cost = 0.
        self.constraints = []
        return
    
    def set_constraint(self,constraint):
        self.constraints.append(constraint)
        return

    def calculate_cost(self,):
        cc = 0.
        for constraint in self.constraints:
            cc += constraint.func(group, advisor)
        return cc


if __name__=='__main__':
    data = load_csv()
    

    total_cost = sum(matches)









