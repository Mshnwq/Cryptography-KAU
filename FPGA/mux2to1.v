module mux2to1 
	#(parameter bits = 32)
	(  
	input [bits-1:0] inA, 
	input [bits-1:0] inB, 
	input select,
	output reg [bits-1:0] out
	);
	
	always @(*)
	
	case (select)
		2'b00: out = inA; //selectA
		2'b01: out = inB;	//selectB
		default out = {bits{1'b0}};
	endcase
	
endmodule 