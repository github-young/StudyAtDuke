e = 1.6e-19;
k = 1.38e-23;
T = 300;
VTN = -0.35;
ni = 1.5e10;
eps0 = 8.85e-14;
Cox = (3.9*eps0)./(e*180e-8);
Qss = 4e10;

syms Nd;
solve(VTN == sqrt(4*11.7*eps0*Nd*k*T*log(Nd/ni)/e)/Cox + 0.51 - Qss/Cox + k*T*log(Nd/ni)/e,Nd)