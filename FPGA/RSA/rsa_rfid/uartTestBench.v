`timescale 1ns / 1ps

module uartTestBench;

  // Parameters
  parameter DBIT = 8;
  parameter SB_TICK = 16;

  // Inputs
  reg clk;
  reg reset_n;
  reg rx;
  wire done;

  // Outputs
  wire rx_done_tick;
  wire [DBIT - 1:0] rx_out;

  // Instantiate the DUT
  baud_timer #(9) baud_timer_inst (
    .clk(clk),
    .reset_n(reset_n),
    .enable(1'b1),
    .FINAL_VALUE(324),
    .done(done)
  );

  uart_rx #(
    .DBIT(DBIT),
    .SB_TICK(SB_TICK)
  ) uart_rx_inst (
    .clk(clk),
    .reset_n(reset_n),
    .rx(rx),
    .s_tick(done),
    .rx_done_tick(rx_done_tick),
    .rx_out(rx_out)
  );

  // Clock generation
  always #10 clk = ~clk;

  // Reset generation

  // Test case 1: Receive a byte
  initial begin
    // Send a byte
		reset_n <= 1;
		clk <= 0;
		rx<= 1;
		#50
		reset_n <= 0;
		#50
		reset_n <= 1;
		#50
		#40000
	 @(posedge clk);
	 rx <= 0;
	 #104166
	 @(posedge clk);
    rx <= 1;
	 #104166
    @(posedge clk);
    rx <= 1;
	 #104166
    @(posedge clk);
    rx <= 0;
	 #104166
    @(posedge clk);
    rx <= 1;
	 #104166
    @(posedge clk);
    rx <= 0;
	 #104166
    @(posedge clk);
    rx <= 0;
	 #104166
    @(posedge clk);
    rx <= 1;
	 #104166
	 @(posedge clk);
    rx <= 0;
	 #104166
	 @(posedge clk);
    rx <= 1;
	 #104166
    #20
	 #1000
	 $stop;
	 
  end

endmodule
