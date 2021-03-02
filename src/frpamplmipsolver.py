import solver
import fastroute_problem as frp
import amplpy
import os


class FrpAmplMipSolver(solver.Solver):

    def __init__(self, prob=frp.FastRouteProb()):
        self.prob = prob
        self.matrix = prob.__str__()
        pass

    def solve(self):
        try:
            ampl_env = amplpy.Environment()
            ampl = amplpy.AMPL(ampl_env)

            ampl.setOption('solver', 'gurobi')

            model_dir = os.path.normpath('../ampl_models')
            ampl.read(os.path.join(model_dir, 'Question2.mod'))

            starts=['1','2','3','4']
            ends=['1','2','3','4']

            df = amplpy.DataFrame('start')
            df.setColumn(self,'start')
            ampl.setData(df,starts)

            df = amplpy.DataFrame('end')
            df.setColumn(self,'end')
            ampl.setData(df, ends)

            df = amplpy.DataFrame(('start','end'),'dst')

            df.setValues({
                (start, end): self.matrix[i][j]
                for i, start in enumerate(starts)
                for j, end in enumerate(ends)})


            ampl.setData(self, df)
            ampl.solve()


            print('Objective: {}'.format(ampl.getObjective('Total_Cost').value()))
            solution = ampl.getVariable('Buy').getValues()
            print('Solution: \n' + str(solution))

        except Exception as e:
            print(e)
            raise








