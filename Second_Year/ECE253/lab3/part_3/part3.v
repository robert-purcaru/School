
module part3(A, B, Function, ALUout);
	input [3:0] A, B;
	input [2:0] Function;
	output reg [7:0] ALUout;
	wire [4:0] added;
	
	always @(*)
	begin
		case(Function)
			3'b000: ALUout = {added};
			3'b001: ALUout = {A+B};
			3'b010: ALUout = { {4{B[3]}}, B };
			3'b011: ALUout = {| {A,B}};
			3'b100: ALUout = {& {A,B}};
			3'b101: ALUout = {A,B};
				
			default: ALUout = 2'h00;
		endcase
	end
	
	part2_a u0(
	.a(A),
	.b(B),
	.c_in(1'b0),
	.s(added[3:0]),
	.c_out(added[4])
	);

endmodule

module part2_a(a, b, c_in, s, c_out);
	input [3:0] a,b;
	input c_in;
	output c_out;
	output [3:0] s;
	wire w0, w1, w2;
	
	FullAdder u0(
		.a(a[0]),
		.b(b[0]),
		.c_in(c_in),
		.s(s[0]),
		.c_out(w0)
	);
	
	FullAdder u1(
		.a(a[1]),
		.b(b[1]),
		.c_in(w0),
		.s(s[1]),
		.c_out(w1)
	);
	
	FullAdder u2(
		.a(a[2]),
		.b(b[2]),
		.c_in(w1),
		.s(s[2]),
		.c_out(w2)
	);
	
	FullAdder u3(
		.a(a[3]),
		.b(b[3]),
		.c_in(w2),
		.s(s[3]),
		.c_out(c_out)
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