import fastroute_problem as frp
import frpamplmipsolver as amplsolve

dist_matrix = [[0,  20,  30, 40],
               [20,  0,  30,  5],
               [30, 30,   0, 10],
               [40,  5,  10,  0]]




frp_inst = frp.FastRouteProb(dist_matrix)

# Run
print('Problème actuel:')
print(str(frp_inst))

print('Résoudre le problème...')
frp_solver = amplsolve.FrpAmplMipSolver()
frp_sol = frp_solver.solve(frp_inst)

print('Solution retournée:')
print(frp_sol)
print(str(frp_sol.evaluate()))

