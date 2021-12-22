module part3(ClockIn, Resetn, Start, Letter, DotDashOut);
    input ClockIn, Resetn, Start;

    input [2:0] Letter; 
    parameter A = 12'b101110000000;
    parameter B = 12'b111010101000;
    parameter C = 12'b111010111010;
    parameter D = 12'b111010100000;
    parameter E = 12'b100000000000;
    parameter F = 12'b101011101000;
    parameter G = 12'b111011101000;
    parameter H = 12'b101010100000;

    reg [11:0] pattern;
    always@(*)
    begin 
        case (Letter)
            3'b000: pattern <= A;
            3'b001: pattern <= B;
            3'b010: pattern <= C;
            3'b011: pattern <= D;
            3'b100: pattern <= E;
            3'b101: pattern <= F;
            3'b110: pattern <= G;
            3'b111: pattern <= H; 
        endcase 
    end

    output reg DotDashOut;
    reg [11:0] patternReg;
    reg [11:0] RawCounter;
    parameter dividerStartVal = 11'd249;

    always@(negedge Resetn)
    begin
        RawCounter <= dividerStartVal;
        patternReg <= 12'b0; 
    end 

    always@(posedge ClockIn)
    begin
        if(!Resetn)
        begin
            RawCounter <= dividerStartVal;
            patternReg <= 12'b0; 
        end 
        else if (Start)
        begin
            RawCounter <= dividerStartVal;
            patternReg <= pattern;
			RawCounter <= RawCounter - 1; 
        end 
        else if (RawCounter == 0)
        begin 
            RawCounter <= dividerStartVal;
            DotDashOut <= patternReg[11];
            patternReg <= {patternReg[10:0], patternReg[11]};
        end
        else 
            RawCounter <= RawCounter - 1; 
    end 
endmodule