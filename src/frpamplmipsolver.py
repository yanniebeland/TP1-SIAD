import solver
import fastroute_problem as frp
import amplpy
import os
import sys



class FrpAmplMipSolver(solver.Solver):

    def __init__(self, prob=frp.FastRouteProb()):

        pass

    def solve(self):
        try:
            ampl_env = amplpy.Environment()
            ampl = amplpy.AMPL(ampl_env)

            ampl.setOption('solver', 'gurobi')

            model_dir = os.path.normpath('./tp1_ampl')
            ampl.read(os.path.join(model_dir, 'Question2.mod'))






