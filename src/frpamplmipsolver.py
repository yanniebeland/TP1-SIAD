import solver
import amplpy
import os
from route_solution import Route


class FrpAmplMipSolver(solver.Solver):

    def __init__(self, ):
        super(FrpAmplMipSolver, self).__init__()

    def solve(self, prob):
        ampl_env = amplpy.Environment()
        ampl = amplpy.AMPL(ampl_env)

        ampl.setOption('solver', 'gurobi')
        ampl.setOption('gurobi_options',
                       "improvetime 3600 "
                       #"impstartnodes 100 "
                       #"iterlim 1000000 "
                       "mipfocus 1 "
                       #"nodelim 1000 "
                       "timelim 7200 "
                       "tunetimelimit 60 "
                       "relax 0")

        model_dir = os.path.normpath('./ampl_models')
        ampl.read(os.path.join(model_dir, 'Question2.mod'))

        nb_locations = prob.count_locations()
        location_list = list(range(1, nb_locations+1))

        L = ampl.getParameter('L')
        L.set(nb_locations)

        D = amplpy.DataFrame('D')
        D.setColumn('D', location_list)
        ampl.setData(D, 'D')

        A = amplpy.DataFrame('A')
        A.setColumn('A', location_list)
        ampl.setData(A, 'A')

        nodes = nb_locations-1
        nodes_list = list(range(1, nodes+1))
        Z = amplpy.DataFrame('Z')
        Z.setColumn('Z', nodes_list)
        ampl.setData(Z, 'Z')

        df = amplpy.DataFrame(('D', 'A'), 'X')

        df.setValues({
            (start, end): prob._dist_matrix[i][j]
            for i, start in enumerate(location_list)
            for j, end in enumerate(location_list)})
        # print(df)

        ampl.setData(df)
        ampl.solve()

        y = ampl.getVariable('Y')
        dfy = y.getValues()

        chosen = {int(row[0]): int(row[1]) for row in dfy if row[3] == 1}

        x = ampl.getParameter('X')
        dfx = x.getValues()
        dist_list = []
        for row in dfx:
            for i in chosen:
                to_append = [row[2]]
                if i == (row[0], row[1]):
                    dist_list.append(to_append)

        solution = Route(prob)

        solution.visit_sequence = generate_order(location_list, chosen)

        return solution


def generate_order(location_list, chosen):
    start_point = None
    for candidate in location_list:
        if candidate not in chosen.values():
            start_point = candidate

    if start_point is None:
        raise Exception("No start point found")

    order = []
    next = start_point

    while next is not None:
        order.append(next)
        next = chosen.get(next)

    start_points = set(chosen.keys())
    arrival_points = set(chosen.values())
    all_points = set(location_list)

    #print(location_list)
    print(f"No start from: {all_points-start_points}")
    print(f"No arrival from: {all_points - arrival_points}")

    return order




