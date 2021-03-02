import sys
import solution as sol
import fastroute_problem as frp

class Route(sol.Solution):

    def __init__(self, solvedProblem=frp.FastRouteProb()):
        super(Route, self).__init__()
        self.visit_sequence = []
        self.problem = solvedProblem

    def __str__(self):
        tmp_str = ', '.join([str(i) for i in self.visit_sequence])
        
        return str(tmp_str)
    
    def validate(self):
        locations_list = list(range(0, self.problem.count_locations()))
        if sorted(self.visit_sequence) == locations_list:
            return True
        
        return False

    def evaluate(self):
        if self.validate() == False:
            return sys.float_info.max

        obj_val = 0
        for i in range(0, self.problem.count_locations() - 1):
            curr_source = self.visit_sequence[i]
            curr_destination = self.visit_sequence[i + 1]
            curr_distance = self.problem._dist_matrix[curr_source][curr_destination]
            obj_val = obj_val + curr_distance

        return obj_val
            

