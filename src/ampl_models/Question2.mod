# Ensembles
set D;
set A;
set Z;
# Parametres
param L;
param nodes = L - 1 integer;
param suite = nodes - 1;

param X {d in D, a in A};

# Variables de decision
var Y {d in D, a in A, z in Z} binary;

# Fonction objectif
minimize total_distance: sum {d in D, a in A, z in Z} X[d,a]*Y[d,a,z];

# Contraintes
subject to Nombre_voyages: sum {d in D, a in A, z in Z} Y[d,a,z]=nodes;
subject to Arriver_une_fois {a in A}: sum{d in D, z in Z} Y[d,a,z]<=1;
subject to Depart_une_fois {d in D}: sum{a in A, z in Z} Y[d,a,z]<=1;
subject to Chemin_realiste {d in D, a in A, z in Z: d==a}: Y[d,a,z]=0;
subject to Single_Node {d in D, a in A, z in Z: d!=a}: Y[d,a,z] + Y[a,d,z]<=1;
subject to gotta_move {z in Z}: sum{d in D, a in A} Y[d,a,z] = 1;
subject to order {p in 1..L, s in 1..suite}: sum{d in D} Y[d,p,s] - sum{a in A} Y[p,a,s+1] = 0;


