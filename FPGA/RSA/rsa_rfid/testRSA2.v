`timescale 1ns / 1ps
module testRSA2;

	//inputs
	wire tx;
	reg go, reset, clk;
	reg rx;
	//outputs
	wire done;
	wire [31:0] output_text;
	wire [7:0] sevn, sevn1, sevn2, sevn3, sevn4, sevn5;
//	reg [119:0] rx_combo = {1'b1,8'b00000000,1'b0,1'b1,8'b10011000,1'b0,1'b1,8'b00101010,1'b0,1'b1,8'b11110010,1'b0,1'b1,8'b10101110,1'b0,1'b1,8'b00010111,1'b0,1'b1,8'b01110011,1'b0,1'b1,8'b00000101,1'b0,1'b1,8'b10100101,1'b0,1'b1,8'b00010001,1'b0,1'b1,8'b00100110,1'b0,1'b1,8'b11000001,1'b0};
//	reg [119:0] rx_combo = {1'b1,8'b00000000,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000101,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b10001101,1'b0,1'b1,8'b11111101,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000001,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000001,1'b0};
//	reg [119:0] rx_combo = {1'b1,8'b01100000,1'b0,1'b1,8'b10010000,1'b0,1'b1,8'b10011101,1'b0,1'b1,8'b11101101,1'b0,1'b1,8'b01110011,1'b0,1'b1,8'b11110010,1'b0,1'b1,8'b00010001,1'b0,1'b1,8'b01101011,1'b0,1'b1,8'b01101001,1'b0,1'b1,8'b01000010,1'b0,1'b1,8'b10011101,1'b0,1'b1,8'b11100001,1'b0};
//reg [119:0] rx_combo = {1'b1,8'h46,1'b0,1'b1,8'hba,1'b0,1'b1,8'hfa,1'b0,1'b1,8'h74,1'b0,1'b1,8'h79,1'b0,1'b1,8'h28,1'b0,1'b1,8'hb8,1'b0,1'b1,8'h5b,1'b0,1'b1,8'h21,1'b0,1'b1,8'hc4,1'b0,1'b1,8'hd8,1'b0,1'b1,8'h61,1'b0};
//reg [119:0] rx_combo = {1'b1,8'h00,1'b0,1'b1,8'h8a,1'b0,1'b1,8'h04,1'b0,1'b1,8'hed,1'b0,1'b1,8'h73,1'b0,1'b1,8'h15,1'b0,1'b1,8'h36,1'b0,1'b1,8'hd5,1'b0,1'b1,8'h00,1'b0,1'b1,8'h01,1'b0,1'b1,8'h00,1'b0,1'b1,8'h01,1'b0};
//  reg [119:0] rx_combo = {1'b1,8'h56,1'b0,1'b1,8'h91,1'b0,1'b1,8'hba,1'b0,1'b1,8'h33,1'b0,1'b1,8'h57,1'b0,1'b1,8'h1a,1'b0,1'b1,8'h82,1'b0,1'b1,8'h31,1'b0,1'b1,8'h00,1'b0,1'b1,8'hff,1'b0,1'b1,8'hff,1'b0,1'b1,8'hff,1'b0};
  reg [119:0] rx_combo = 	{1'b1,8'h00,1'b0,1'b1,8'h8a,1'b0,1'b1,8'h04,1'b0,1'b1,8'hed,1'b0,1'b1,8'h73,1'b0,1'b1,8'h15,1'b0,1'b1,8'h36,1'b0,1'b1,8'h5d,1'b0,1'b1,8'h00,1'b0,1'b1,8'h01,1'b0,1'b1,8'h00,1'b0,1'b1,8'h01,1'b0};

  // reg [119:0] rx_combo = 0 ;

	//module to test
	
	rsa_rfid RSA(
    .clk(clk),
    .reset(reset),
    .output_text(output_text),
    .tx(tx),
	 .rx(rx),
	 .sev_segment(sevn),
	 .sev_segment1(sevn1),
	 .sev_segment2(sevn2),
	 .sev_segment3(sevn3),
	 .sev_segment4(sevn4),
	 .sev_segment5(sevn5),
	 
    .go(go),
    .done(done)
  );
	
	always
		#10 clk = ~clk;
	
	initial begin
		// intilaizing data
		go = 1;
		reset = 1;
		clk = 0;
		#20
		reset = 0;
		#20
		reset = 1;
		rx = 1;
		#104000
		///////////////
		
		repeat (120) begin
	  // Code to be executed in the loop
			@(posedge clk) begin
			 rx = rx_combo[0];
			 rx_combo = {1'b1, rx_combo[119:1]};
			 #104166;
			 end	
		end	


//		@(posedge clk);
//		go = 0;
//		@(posedge clk);
//		go = 1;
		
		
		
		#5000000; // let ir run for 10000 cycles
		$stop;
		
		
	end
	
endmodule
		
		
		