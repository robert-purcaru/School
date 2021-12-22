module part1(Clock, Enable, Clear_b, CounterValue);
	input Clock, Enable, Clear_b;
	output reg [7:0] CounterValue;
	
	always @(posedge Clock)
	begin
		if(Clear_b == 1'b0) CounterValue <= 8'b0;
		else if (Enable) CounterValue <= CounterValue + 1'b1;
	end

endmodule