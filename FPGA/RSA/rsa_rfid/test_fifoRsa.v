`timescale 1ns / 1ps
module test_fifoRsa;

reg clk;
reg [7:0] data_sig;
wire [31:0] key;
wire [31:0] mod;
wire [31:0] plaintext;
reg  sclr_sig, wrreq_sig, rdreq_in, reset;
wire empty_sig ,full_sig, rdreq_sig, done;
wire [7:0] q_sig;
wire [9:0] usedw_sig;

fifoRsa fifoRsa_inst (
	.clock ( clk ),
	.data ( data_sig ),
	.rdreq ( rdreq_sig ),
	.sclr ( !reset ),
	.wrreq ( wrreq_sig ),
	.empty (empty_sig ),
	.full ( full_sig ),
	.q ( q_sig ),
	.usedw ( usedw_sig )
);



bytes_to_words_opt my_instance(
  .clock(clk),
  .reset(reset),
  .data_in(q_sig),
  .rdreq_in(rdreq_in),
  .key(key),
  .mod(mod),
  .plaintext(plaintext),
  .rdreq_out(rdreq_sig),
  .empty(),
  .done(done)
);

  always #10 clk = ~clk;
  initial begin
    // Send a byte
		clk <= 0;
		reset <= 1;
		#20
		reset <= 0;
		#20
		reset <= 1;
		#50
		@(posedge clk);
		data_sig <= 8'd3;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd6;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd32;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd14;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd25;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd12;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd54;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd66;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd33;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd38;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd71;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		data_sig <= 8'd4;
		@(posedge clk);
		wrreq_sig = 1;
		@(posedge clk);
		wrreq_sig = 0;
		@(posedge clk);
		wrreq_sig <=0;
		@(posedge clk);
		rdreq_in=1;
		@(posedge clk);
		rdreq_in=0;
		
		#10000; // let ir run for 10000 cycles
		$stop;
end		
endmodule
