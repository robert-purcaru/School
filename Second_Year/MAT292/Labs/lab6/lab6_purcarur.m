%% Laplace Transform Lab: Solving ODEs using Laplace Transform in MATLAB
% This lab will teach you to solve ODEs using a built in MATLAB Laplace transform 
% function |laplace|.
% 
% There are five (5) exercises in this lab that are to be handed in. Write your 
% solutions in a separate file, including appropriate descriptions in each step.
% 
% Include your name and student number in the submitted file.
%% Student Information
%%
% 
%  Student Name: Robert Purcaru
%
%%
% 
%  Student Number: 1007019842
%
%% Using symbolic variables to define functions
% In this exercise we will use symbolic variables and functions.

syms t s x y

f = cos(t)
h = exp(2*x)
%% Exercise 1
% Objective: Compute the Laplace transform and use it to show that MATLAB 'knows' 
% some of its properties.
% 
% Details: 
% 
% (a) Define the function |f(t)=exp(2t)*t^3|, and compute its Laplace transform 
% |F(s)|. (b) Find a function |f(t)| such that its Laplace transform is  |(s - 
% 1)*(s - 2))/(s*(s + 2)*(s - 3)| (c) Show that MATLAB 'knows' that if |F(s)| 
% is the Laplace transform of  |f(t)|, then the Laplace transform of |exp(at)f(t)| 
% is |F(s-a)| 
% 
% (in your answer, explain part (c) using comments). 
% 
% Observe that MATLAB splits the rational function automatically when solving 
% the inverse Laplace transform.
% 
% (a)    

clc; 
close all; 
clear;

syms f t;
f = exp(2*t) * t^3;

F = laplace(f)
%% 
% (b)

syms g G s;
G = ((s-1)*(s-2))/(s*(s+2)*(s-3));
g = ilaplace(G)
%% 
% (c)

syms F(t) f(t) a t
g(t) = exp(a*t)*f(t);
F=laplace(f(t))
G=laplace(g(t))
% f(t) is a non specific function with laplace transfrom F(s) as a fucntion
% of (t,s, f(t)). Since g is a function of (a, t f(t)), MATLAB shows that G
% is a function of (f(t), t, s - a) implying that G is a function of
% F(s-a), since the (s) term in the G arguments is replaced by (s - a)
%% Exercise 2
% Objective: Find a formula comparing the Laplace transform of a translation 
% of |f(t)| by |t-a| with the Laplace transform of |f(t)|
% 
% Details: 
%% 
% * Give a value to |a|
% * Let |G(s)| be the Laplace transform of |g(t)=u_a(t)f(t-a)| and |F(s)| is 
% the Laplace transform of |f(t)|, then find a formula relating |G(s)| and |F(s)|
%% 
% In your answer, explain the 'proof' using comments.

clc; 
close all; 
clear;

syms a s t;

a = 10;

ua(t) = heaviside(t-a);

f(t) = t*exp(t);
F = laplace(f(t))

g(t) = ua(t)*f(t-a);
G = laplace(g(t))


% The laplace transform of a function u_a(t)*f(t-a) = exp(-c*s) * F(s)
% where F(s) is the laplace transform of f(t). This is confirmed here as
% the laplace transform of f(t) is F(s) = 1/(s-1)^2 and G(s) is e^(-a*s) * F(s) 

%% Exercise 3
% Objective: Solve an IVP using the Laplace transform
% 
% Details: Explain your steps using comments
%% 
% * Solve the IVP
% * |y'''+2y''+y'+2*y=-cos(t)|
% * |y(0)=0|, |y'(0)=0|, and |y''(0)=0|
% * for |t| in |[0,10*pi]|
% * Is there an initial condition for which |y| remains bounded as |t| goes 
% to infinity? If so, find it.

clc; 
close all; 
clear;

% Declaring variables to be used
syms y(t) t Y s

% define the ODE

ODE=diff(y(t),t,3) + 2*diff(y(t),t,2) + diff(y(t),t,1) + 2*y(t) + cos(t) == 0

% laplace transform of the ODE.

L_ODE = laplace(ODE)

% initial conditions

L_ODE=subs(L_ODE,y(0),0)
L_ODE=subs(L_ODE,subs(diff(y(t), t), t, 0),0)
L_ODE=subs(L_ODE,subs(diff(y(t), t, 2), t, 0),0)

% factor out the Laplace transform of |y(t)|

L_ODE = subs(L_ODE,laplace(y(t), t, s), Y)
Y=solve(L_ODE,Y)

% Assign y the solution to the inverse laplace transform

y = ilaplace(Y)

% plot the solution

ezplot(y,[0,10*pi])
title("y'''+2y''+y'+2*y=-cos(t), y(0) = 0, y'(0)=0, y''(0)=0");
ylabel('y');
xlabel('t');

% there is no solution that bounds y as t goes to infinty, the function
% oscillates with increasing magnitude regardless of where it starts.

%% Exercise 4
% Objective: Solve an IVP using the Laplace transform
% 
% Details: 
%% 
% * Define 
% * |g(t) = 3 if 0 < t < 2|
% * |g(t) = t+1 if 2 < t < 5|
% * |g(t) = 5 if t > 5|
% * Solve the IVP
% * |y''+2y'+5y=g(t)|
% * |y(0)=2 and y'(0)=1|
% * Plot the solution for |t| in |[0,12]| and |y| in |[0,2.25]|.
%% 
% In your answer, explain your steps using comments.

clc; 
close all; 
clear;

% Declaring variables to be used
syms y(t) t Y s

% defining g(t) using heaviside functions, each subsequent 
% function needs to account for thevalue set by the previous;
% the last term is the sum of previous terms that gives a constant 5
u0(t) = heaviside(t);
u2(t) = heaviside(t-2);
u5(t) = heaviside(t-5);

g(t) = 3*u0(t)+(t-2)*u2(t)+(-t+4)*u5(t);

% define the ODE

ODE = diff(y(t),t,2) + 2*diff(y(t),t) + 5*y(t) - g(t) == 0

% laplace transform of the ODE.

L_ODE = laplace(ODE)

% initial conditions

L_ODE=subs(L_ODE,y(0),2)
L_ODE=subs(L_ODE,subs(diff(y(t), t), t, 0),1)

% factor out the Laplace transform of |y(t)|

L_ODE = subs(L_ODE,laplace(y(t), t, s), Y)
Y=solve(L_ODE,Y)

% Assign y the solution to the inverse laplace transform

y = ilaplace(Y)

% plot the solution

ezplot(y, [0,12, 0, 2.25])

% there is no solution that bounds y as t goes to infinty, the function
% oscillates with increasing magnitude regardless of where it starts.
%% Exercise 5
% Objective: Use the Laplace transform to solve an integral equation
% 
% Verify that MATLAB knowns about the convolution theorem by explaining why 
% the following transform is computed correctly.

clc; 
close all; 
clear;

syms t tau y(tau) s
I=int(exp(-2*(t-tau))*y(tau),tau,0,t)
laplace(I,t,s)

% By definition, I is the convolution of e^(2\tau - 2t) and y(\tau) 
% so the laplace transfrom of I is the product of the laplace transform 
% of y(\tau) and e^(2\tau - 2t). The laplace transfrom of y is given on the
% numerator and the laplace transform of e^(2\tau - 2t) is 1/(s+2).