module part2(ClockIn, Reset, Speed, CounterValue);
	input ClockIn, Reset;
	input [1:0] Speed;
	output reg [3:0] CounterValue;
	reg [11:0] RateDivider;
	
	always @(posedge ClockIn)
	begin 
		if (Reset)
		begin
			CounterValue <= 0;
			RateDivider <= 0;
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
		end
		else RateDivider <= RateDivider - 1;
	end
	
	
endmodule