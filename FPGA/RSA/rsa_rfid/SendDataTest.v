`timescale 1ns / 1ps
module SendDataTest;

reg clk;
reg  [31:0] cipher;
reg  start, rdreq_in, reset;
wire empty_sig ,full_sig, wrreq_sig, done;
wire [7:0] data_out;
wire [9:0] usedw_sig;

 send_data my_module_instance (
  .clock(clk),
  .reset(reset),
  .data_in(cipher),
  .start(start),
  .out(data_out),
  .req_wr(wrreq_sig),
  .done(done)
);

  always #10 clk = ~clk;
  initial begin
		clk <= 0;
		reset <= 1;
		#20
		reset <= 0;
		#20
		reset <= 1;
		#50
		@(posedge clk);
		cipher <= 32'h1E3470FB;
		@(posedge clk);
		start=1;
		@(posedge clk);
		start=0;
		
		#10000; // let ir run for 10000 cycles
		$stop;
end		
endmodule
