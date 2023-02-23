`timescale 1 ps / 1 ps
module testRSA;

	//inputs
	reg [31:0] input_text;
	reg [31:0] key;
	reg [31:0] mod;
	reg go, reset, clk, divide;
	
	//outputs
	wire done;
	wire [31:0] output_text;
	
	//module to test
	rsa_rfid RSA(clk, reset, input_text, key, mod, output_text, go, done);
	
	always
		#5 clk = ~clk;
	
	initial begin
		// intilaizing data
		input_text = 0;
		go = 0;
		reset = 0;
		clk = 0;
		
		///////////////
		@(posedge clk);
		input_text = 'h00982af2;
		key        = 'ha51126c1;
		mod        = 'hae177305;
		
		@(posedge clk);
		go = 1;
	
		@(posedge clk);
		go = 0;
		
		
		
		#10000; // let ir run for 10000 cycles
		$stop;
		
		
	end
	
endmodule
		
		
		