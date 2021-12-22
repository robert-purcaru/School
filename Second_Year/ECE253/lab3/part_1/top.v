module top(LEDR, SW);
    input [9:0] SW;
    output [9:0] LEDR;
	
	part1 u0(
		.MuxSelect(SW[9:7]),
		.Input(SW[6:0]),
		.Out(LEDR[0])
	);
	
endmodule