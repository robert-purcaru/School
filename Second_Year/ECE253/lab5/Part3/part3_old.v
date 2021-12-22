module part3(ClockIn, Resetn, Start, Letter, DotDashOut);
	input ClockIn, Resetn, Start;
	input [2:0] Letter;
	output reg DotDashOut;
	
	reg [11:0] curr;
	
	parameter A = 12'b101110000000;
	parameter B = 12'b111010101000;
	parameter C = 12'b111010111010;
	parameter D = 12'b111010100000;
	parameter E = 12'b100000000000;
	parameter F = 12'b101011101000;
	parameter G = 12'b111011101000;
	parameter H = 12'b101010100000;
	
	wire clk2;
	
	part2 u2(
		.ClockIn(ClockIn), 
		.Reset(~Resetn),
		.Speed(2'b01),
		.clk2(clk2)
	);
	
	always @(*)
	begin
		case(Letter)
			3'b000: curr <= A;
			3'b001: curr <= 12'b111010101000;
			3'b010: curr <= C;
			3'b011: curr <= D;
			3'b100: curr <= E;
			3'b101: curr <= F;
			3'b110: curr <= G;
			3'b111: curr <= H;
			default: curr <= 12'b11111111111;
		endcase
	end
	
	always @(posedge clk2 or negedge Resetn)
	begin
		if(~Resetn)
		begin
			curr <= 12'b0;
			DotDashOut <= 1'b0;
		end
		else
		begin
			DotDashOut <= curr[11];
			curr <= curr << 1;
			curr[0] <= curr[11];
		end		
	end
endmodule



module part2(ClockIn, Reset, Speed, CounterValue, clk2);
	input ClockIn, Reset;
	input [1:0] Speed;
	output reg [3:0] CounterValue;
	output reg clk2;
	reg [11:0] RateDivider;
	
	always @(posedge ClockIn)
	begin 
		if (Reset)
		begin
			CounterValue <= 12'b0;
			RateDivider <= 12'b0;
		end
		else if(RateDivider == 0)
		begin
			case (Speed)
				0: RateDivider <= 12'd0;
				1: RateDivider <= 12'd499;
				2: RateDivider <= 12'd999;
				3: RateDivider <= 12'd1999;
			endcase
			CounterValue <= CounterValue + 1;
			clk2 <= CounterValue[1];
		end
		else RateDivider <= RateDivider - 1;
	end
	
	
endmodule