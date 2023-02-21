module rsa_rfid
	#(parameter WordSize = 32) 
	(  
	// Top Level  I/O
	input clk, reset,
	
	// Data Path  I/O	
	output [WordSize-1:0] output_text,
	output tx,
	input rx,
	output [7:0] sev_segment,
	output [7:0] sev_segment1,
	output [7:0] sev_segment2,
	output [7:0] sev_segment3,
	output [7:0] sev_segment4,
	output [7:0] sev_segment5,
	// Controller I/O
	input wire go,       // enablers
	output wire done     // flags
	);
	
	wire load, running, over, rd_uart, wr_uart, tx_full, rx_empty;
	wire  [7:0] r_data;
	wire 	[7:0] w_data;
	wire  [9:0]	usedw_wire;
	wire  [WordSize-1:0] input_text;
	wire  [WordSize-1:0] key;
	wire  [WordSize-1:0] mod;
	wire 	[WordSize-1:0] output__text;
	
	
//	dataPath DP(clk, reset, input_text, key, mod, output_text, load, running, over);
dataPath dataPath_rsa (
    .clk(clk),
    .reset(reset),
    .uart_in(r_data),
    .output_text(w_data),
	 .cipherFull(output__text),
    .nextByte_in(rd_uart),
    .nextByte_out(wr_uart),
	 .empty_fifo(rx_empty),
	 .usedw(usedw_wire),
    .load(!go),
    .running(running),
    .over(over)
  );
	controlUnit CU_rsa(clk, reset, !go, load, running, done, over);
	uart #(
    .DBIT(8), 
    .SB_TICK(16)
  ) uart_rsa (
    .clk(clk),
    .reset_n(reset),
    .r_data(r_data),
    .rd_uart(rd_uart),
    .rx_empty(rx_empty),
    .rx(rx),
    .w_data(w_data),
    .wr_uart(wr_uart),
    .tx_full(tx_full),
    .tx(tx),
	 .rx_usedw(usedw_wire),
    .TIMER_FINAL_VALUE(324)
  );

hex_to_7seg my_converter (
    .hex_value (output__text[3:0]),
    .seg_out (sev_segment)
);
hex_to_7seg my_converter1 (
    .hex_value (output__text[7:4]),
    .seg_out (sev_segment1)
);
hex_to_7seg my_converter2 (
    .hex_value (output__text[11:8]),
    .seg_out (sev_segment2)
);
hex_to_7seg my_converter3 (
    .hex_value (output__text[15:12]),
    .seg_out (sev_segment3)
);
hex_to_7seg my_converter4 (
    .hex_value (output__text[19:16]),
    .seg_out (sev_segment4)
);
hex_to_7seg my_converter5 (
    .hex_value (output__text[23:20]),
    .seg_out (sev_segment5)
);

endmodule 