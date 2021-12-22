
function [t, y] = f1(f,g,t0,tN,x0,h)
n = round(((tN-t0)/h),0);
t = linspace(t0,tN,n);
y = zeros(2,n);
y(1,1) = x0(1,1);
y(2,1) = x0(2,1);

for i = 1:n-1
    x0_SL = f(t(i),y(1,i),y(2,i));
    x0_SR = f(t(i),y(1,i),y(2,i))*h + y(1,i);
    x1_SL = g(t(i),y(1,i),y(2,i));
    x1_SR = g(t(i),y(1,i),y(2,i))*h + y(2,i);
    y(1,i+1) = y(1,i)+(h/2)*(x0_SL+f((t(i)+h),x0_SR,x1_SR));
    y(2,i+1) = y(2,i)+(h/2)*(x1_SL+g((t(i)+h),x0_SR,x1_SR));
end
