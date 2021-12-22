function [t, y] = DE2_purcarur(f,t0,tN,y0,y1,h)
nums = round(((tN-t0)/h),0);
t = t0:h:tN;

y = zeros(1,nums);
y(1) = y0;
y(2) = y0+y1*h;

for j = 1:nums-1
    y_p = (y(j+1)-y(j))/h;
    y_dp = f(t(j+2),y_p,y(j+1));
    y(j+2) = (h^2)*y_dp+2*y(j+1)-y(j);
end