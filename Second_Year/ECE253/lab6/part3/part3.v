module part3(Clock, Resetn, Go, Divisor, Dividend, Quotient, Remainder);
	input Clock, Resetn, Go;
	input [3:0] Divisor;
	input [3:0] Dividend;
	
	output [3:0] Remainder;
	output [3:0] Quotient;
	
	wire a4;
	wire ldr;
	wire [1:0] alu_sel;
	wire do_shift;
	wire set_q0;
	wire ldd;
	
	datapath u1(
		.clock(Clock),
		.resetn(Resetn),
		
		.Dr({1'b0, Divisor}),
		.external_dv(Dividend),
		
		.ldd(ldd),
		.do_shift(do_shift),
		.set_q0(set_q0),
		.alu_sel(alu_sel),
		.ldr(ldr),
		
		.a4(a4),
		.Quotient(Quotient),
		.Remainder(Remainder)
	);
	
	control u2(
		.clock(Clock),
		.resetn(Resetn),
		
		.go(Go),
		
		.a4(a4),
		
		.ldd(ldd),
		.ldr(ldr),
		.do_shift(do_shift),
		.set_q0(set_q0),
		.alu_sel(alu_sel)
	);

endmodule

module control(
	input clock,
	input resetn,
	
	input go,
	
	input a4,
	
	output reg ldd,
	output reg ldr,
	output reg do_shift,
	output reg set_q0,
	output reg [1:0] alu_sel
	);
	
	reg [4:0] curr_state, next_state;
	
	reg [2:0] count;
	
	localparam state_0 		= 5'd0,
			   state_1 		= 5'd1,
			   state_2 		= 5'd2,
			   state_3 		= 5'd3,
			   state_4 		= 5'd4,
			   state_5 		= 5'd5,
			   state_6		= 5'd6;

	always@(*)
	begin: state_table
		case (curr_state)
			state_0: begin
			next_state = go ? state_1 : state_0;
			end
			
			state_1: begin
			next_state = state_2;
			end
			
			state_2: begin
				if(a4 == 1)
					next_state = state_3;
				if(a4 == 0)
					next_state = state_4;
			end
			
			state_3: begin
			next_state = state_5;
			end
			
			state_4: begin
			next_state = state_5;
			end
			
			state_5: begin
			count = count - 1;
			if(count == 0)
				next_state = state_6;
			else
				next_state = state_1;
			end
			
		endcase
	end
	
	always@(*)
	begin: signals
		do_shift 	= 1'b0;
		set_q0 		= 1'b0;
		alu_sel 	= 2'b0x;
		ldr 		= 1'b0;
		ldd			= 1'b0;
		
		case(curr_state)
			state_0: begin
				count = 3'b100;
				ldd = 1'b1;
			end
			state_1:
				do_shift = 1'b1;
				
			state_2:
				alu_sel = 2'b10;
			
			state_3: begin
				alu_sel = 2'b11;
				set_q0 = 1'b1;
			end
			state_4: 
				set_q0 = 1'b1;
			state_5:
				ldr = 1'b0;
			state_6:
				ldr = 1'b1;
			endcase
	end
	
	always@(posedge clock)
	begin: state_FFs
		if(!resetn) begin
			curr_state <= 5'd0;
			next_state <= 5'd0;
		end
		else
			curr_state <= next_state;
	end
	
endmodule

module datapath(
    input clock,
    input resetn,

	input [4:0] Dr,
	input [3:0] external_dv,

	input ldd,
	input do_shift,
	input set_q0,
	input [1:0] alu_sel, 
	input ldr,

	output a4,
	output reg [3:0] Quotient,
	output reg [3:0] Remainder
    );
	
	reg [4:0] A;
	reg [3:0] Dv;
	
	always@(*)
	begin
		if(set_q0)
			Dv[0] = ~A[4];
		case(alu_sel)
			2'b11: 
				A = A + Dr;
			2'b10:
				A = A - Dr;
			default: 
				A = A;
		endcase
	end
	
	always@(*)
	begin
		if(do_shift) begin
			A = {A[3:0], Dv[3]};
			Dv = {Dv[2:0], 1'b0};
		end
	end
	
	always@(*)
	begin
		if(ldd == 1)
			Dv <= external_dv;
	end
	
	
	always@(posedge clock)
	begin
		if(!resetn) begin
			A <= 0;
			Dv <= 0;
			Remainder <= 0;
			Quotient <= 0;
		end
		else if(ldr) begin
			Remainder <= A[3:0];
			Quotient <= Dv;
		end
		
	end
	
	assign a4 = A[4];
			
endmodule
