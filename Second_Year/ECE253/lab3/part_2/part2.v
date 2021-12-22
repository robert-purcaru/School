
module part2(a, b, c_in, s, c_out);
	input [3:0] a,b;
	input c_in;
	output [3:0] s, c_out;
	
	FullAdder u0(
		.a(a[0]),
		.b(b[0]),
		.c_in(c_in),
		.s(s[0]),
		.c_out(c_out[0])
	);
	
	FullAdder u1(
		.a(a[1]),
		.b(b[1]),
		.c_in(c_out[0]),
		.s(s[1]),
		.c_out(c_out[1])
	);
	
	FullAdder u2(
		.a(a[2]),
		.b(b[2]),
		.c_in(c_out[1]),
		.s(s[2]),
		.c_out(c_out[2])
	);
	
	FullAdder u3(
		.a(a[3]),
		.b(b[3]),
		.c_in(c_out[2]),
		.s(s[3]),
		.c_out(c_out[3])
	);
	
endmodule

module FullAdder(a,b,c_in,s,c_out);
	input a,b,c_in;
	output s,c_out;
	wire w0;
	
	assign w0 = a ^ b;
	assign s = w0 ^ c_in;
	
	Mux u0 (
		.x(b),
		.y(c_in),
		.s(w0),
		.f(c_out)
	);
	
endmodule
	

module Mux(x,y,s,f);
	input x,y,s;
	output reg f;
	
	always @(*)
	begin
		case(s)
			1'b0: f = x;
			1'b1: f = y;
			default f = 1'bx;
		endcase
	end
endmodule