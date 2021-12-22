

module part3(clock, reset, ParallelLoadn, RotateRight, ASRight, Data_IN, Q);
	input clock, reset, ParallelLoadn, RotateRight, ASRight;
	input [7:0] Data_IN;
	output reg [7:0] Q;
	
	always @(posedge clock) begin
		if(reset)
			Q <= 8'b00000000;
		else if (~ParallelLoadn)
			Q <= Data_IN;
		else if (RotateRight) begin
			if(ASRight) begin
				Q[6:0] <= Q >> 1;
				Q[7] <= Q[7];
			end
			else
				Q <= {Q[0], Q[7:1]};
		end
		else
			Q <= {Q[6:0], Q[7]};
	end
	
endmodule