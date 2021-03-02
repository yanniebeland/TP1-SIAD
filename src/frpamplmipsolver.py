import solver
import fastroute_problem as frp
import amplpy
import os
import sys



class FrpAmplMipSolver(solver.Solver):

    def __init__(self, prob=frp.FastRouteProb()):
        self.prob = prob
        pass

    def solve(self):
        try:
            ampl_env = amplpy.Environment()
            ampl = amplpy.AMPL(ampl_env)

            ampl.setOption('solver', 'gurobi')

            model_dir = os.path.normpath('./ampl_models')
            ampl.read(os.path.join(model_dir, 'Question2.mod'))
            ampl.setData(self, prob)
            ampl.solve()

            print('Objective: {}'.format(ampl.getObjective('Total_Cost').value()))
            solution = ampl.getVariable('Buy').getValues()
            print('Solution: \n' + str(solution))

        except Exception as e:
            print(e)
            raise








