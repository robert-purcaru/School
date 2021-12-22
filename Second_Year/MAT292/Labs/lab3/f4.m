function [x,y] = f4(f, t0,tN,y0,h);
num_terms = int32((tN-t0)/h);
x = zeros(1, num_terms);
y = zeros(1, num_terms);
x(1) = t0;
y(1) = y0;

tol=1e-8;
i = 1;

while x(i) < tN
    x(i+1) = x(i)+h;
    m_here = f(x(i), y(i));
    D = 1;
    
    while abs(D) > tol
    
        Y = y(i) + (h/2) * (m_here + f(x(i) + h, y(i) + h*m_here)); 

        half_step1 = y(i) + (h/4) * (m_here + f(x(i) + h / 2, y(i) + h*m_here / 2));
        m_half = f(x(i) + h/2, half_step1);
        Z = half_step1 + (h/4) * (m_half + f(x(i) + h/2 + h/2, half_step1 + h*m_half / 2));
        
        D = Z-Y;
        if abs(D) > tol
            h = 0.9*h*min(max(tol/abs(D),0.3),2);
        end
    end
    y(i+1) = Z-D;
    
    i = i+1;
end
end