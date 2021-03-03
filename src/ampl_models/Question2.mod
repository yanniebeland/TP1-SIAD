# Ensembles
set D;
set A;
set O;
# Param�tres
param L;
param X {d in D, a in A};

# Variables de d�cision
var Y {d in D, a in A} binary;

# Fonction objectif
minimize Z: sum {d in D, a in A} X[d,a]*Y[d,a];

# Contraintes
subject to Nombre_voyages: sum {d in D, a in A} Y[d,a]=L-1;
subject to Arriver_une_fois {a in A}: sum{d in D} Y[d,a]<=1;
subject to Depart_une_fois {d in D}: sum{a in A} Y[d,a]<=1;
subject to Chemin_realiste {d in D, a in A: d==a}: Y[d,a]=0;



