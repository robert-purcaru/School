function [x,y] = f1(f, t0,tN,y0,h) 
num_terms = int32((tN-t0)/h);
x = zeros(1, num_terms);
y = zeros(1, num_terms);
x(1) = t0;
y(1) = y0;
for i=1:num_terms
    x(i+1) = x(i)+h;
    m_here = f(x(i), y(i));
    y(i+1) = y(i) + (h/2) * (m_here + f(x(i) + h, y(i) + h*m_here)); 
end
end