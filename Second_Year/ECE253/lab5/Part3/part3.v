module part3(ClockIn, Resetn, Start, Letter, DotDashOut);
	input ClockIn, Resetn, Start;
	input [2:0] Letter;
	output reg DotDashOut;

	parameter A = 12'b101110000000;
    parameter B = 12'b111010101000;
    parameter C = 12'b111010111010;
    parameter D = 12'b111010100000;
    parameter E = 12'b100000000000;
    parameter F = 12'b101011101000;
    parameter G = 12'b111011101000;
    parameter H = 12'b101010100000;
	
	
	reg clk2;
	reg [11:0] counter;
	reg [11:0] curr;
	reg [11:0] code;
	
	// 2Hz clock generated on clk2
	
	always @(negedge Resetn)
	begin
		counter <= 12'b0;
		clk2 <= 1'b0;
		//curr <= 12'b0;
		code <= 12'b0;
	end
	
	always @(posedge ClockIn)
	begin
		if(~Resetn)
		begin
			counter <= 12'b0;
			clk2 <= 1'b0;
			code <= 12'b0;
		end
		else if(Start)
		begin
			code = curr;
			counter <= 8'd249;	
		end	
		
		else if(counter == 0)
		begin
			counter <= 8'd249;
			clk2 <= ~clk2;
			DotDashOut <= code[11];
			code <= {code[10:0], code[11]};
		end
		else counter <= counter - 1'b1;	
		

	end
	
	// assigning letter to curr register, happens whenever

	always @(*)
	begin
	    case (Letter)
            3'b000: curr = A;
            3'b001: curr = B;
            3'b010: curr = C;
            3'b011: curr = D;
            3'b100: curr = E;
            3'b101: curr = F;
            3'b110: curr = G;
            3'b111: curr = H; 
        endcase 
	end
	

endmodule

















