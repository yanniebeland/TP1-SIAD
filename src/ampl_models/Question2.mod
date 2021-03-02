set D;
set A;

param L;
param X {D, A};

var Y {D, A} binary;

minimize Z: sum {d in D, a in A} X[d,a]*Y[d,a];

subject to Nombre_voyages: sum {d in D, a in A} Y[d,a]=L-1;
subject to Arriver_une_fois {a in A}: sum{d in D} Y[d,a]<=1;
subject to Depart_une_fois {d in D}: sum{a in A} Y[d,a]<=1;
subject to Chemin_realiste {d in D, a in A: d==a}: Y[d,a]=0;

