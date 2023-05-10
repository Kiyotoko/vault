U0 = 10; % Quellspannung
R = 47; % Widerstand
I0 = U0 / R; % maximale Stromstärke
L = 100; % Induktivität
dt = 0.001; % deltaT
n = 1; % Index

X0 = [];
Y0 = [];
I = 0;

for t=0:dt:20
  X0(n) = t;
  Y0(n) = I;
  dI = dt * (U0 - R * I) / L;
  I += dI;
  n += 1;
endfor

n = 1;
X1 = [];
Y1 = [];

for t=0:dt:20
  X1(n) = t;
  Y1(n) = I;
  dI = -dt * (R * I) / L;
  I += dI;
  n += 1;
endfor

grid on
set(gca, "Fontsize", 18)

subplot(1, 2, 1)
plot(X0, Y0, "-b")
title("Einschaltvorgang")
xlabel("Zeit t [s]")
ylabel("Stromstärke I [A]")
legend(legend("Simulation"), "location", "southeast")

subplot(1, 2, 2)
plot(X1, Y1, "-b")
title("Ausschaltvorgang")
xlabel("Zeit t [s]")
ylabel("Stromstärke I [A]")
legend(legend("Simulation"), "location", "southeast")

