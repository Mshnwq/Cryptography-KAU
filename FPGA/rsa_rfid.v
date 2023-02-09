module rsa_rfid
	#(parameter WordSize = 32) 
	(  
	// Top Level  I/O
	input clk, reset,
	
	// Data Path  I/O	
	input  [WordSize-1:0] input_text,
	input  [WordSize-1:0] key,
	input  [WordSize-1:0] mod,
	
	output [WordSize-1:0] output_text,
	
	// Controller I/O
	input wire go,       // enablers
	output wire done     // flags
	);
	
	wire load, running, over;
	
	dataPath DP(clk, reset, input_text, key, mod, output_text, load, running, over);
	controlUnit CU(clk, reset, go, load, running, done, over);


endmodule 