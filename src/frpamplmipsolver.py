import solver
import fastroute_problem as frp
import amplpy
import os
from importlib import reload
reload(solver)



class FrpAmplMipSolver(solver.Solver):

    def __init__(self):
        super(FrpAmplMipSolver, self).__init__()
        self.prob = frp.FastRouteProb(dist_matrix=None)
        self.dist_matrix = frp.FastRouteProb.give_dist_matrix(self.prob)

    def solve(self, prob=None):
        try:
            ampl_env = amplpy.Environment()
            ampl = amplpy.AMPL(ampl_env)

            ampl.setOption('solver', 'gurobi')

            model_dir = os.path.normpath('./ampl_models')
            ampl.read(os.path.join(model_dir, 'Question2.mod'))

            nb_locations = frp.FastRouteProb.count_locations(self.prob)
            location_list = list(range(nb_locations))

            L = ampl.getParameter('L')
            L.set(nb_locations)

            D = amplpy.DataFrame('D')
            D.setColumn('D', location_list)
            ampl.setData(D, 'D')

            A = amplpy.DataFrame('A')
            A.setColumn('A', location_list)
            ampl.setData(A, 'A')

            df = amplpy.DataFrame(('D', 'A'), 'X')

            df.setValues({
                (start, end): self.dist_matrix[i][j]
                for i, start in enumerate(location_list)
                for j, end in enumerate(location_list)})
            print(df)

            ampl.setData(df)
            ampl.solve()
            results = ampl.getVariable('Y').getValues()
            print(results)

            return results

        except Exception as e:
            print(e)
            raise




