module uart 
	#(parameter DBIT = 8, 		// # data bits 
					SB_TICK = 16 	// # stop bit ticks 
	)
	(
		input clk, reset_n,
		
		// reciver ports
		output [DBIT - 1:0] r_data,
		input rd_uart,
		output rx_empty,
		input rx,
		
		// transmiter ports
		input [DBIT - 1:0] w_data,
		input wr_uart,
		output tx_full,
		output tx,
		output [9:0] rx_usedw,
		
		//baud rate
		input [10: 0] TIMER_FINAL_VALUE
		);
		
		wire tick;
		baud_timer #(.bits(11))	baud_rate_generator (
			.clk ( clk ),
			.reset_n ( reset_n ),
			.enable ( 1'b1 ),
			.FINAL_VALUE ( TIMER_FINAL_VALUE ),
			.done ( tick )
		);

		wire rx_done_tick;
		wire [DBIT - 1:0] rx_out;
		uart_rx #(.DBIT(DBIT), .SB_TICK(SB_TICK))	receiver (
			.clk ( clk ),
			.reset_n ( reset_n ),
			.rx ( rx ),
			.s_tick ( tick ),
			.rx_done_tick ( rx_done_tick ),
			.rx_out ( rx_out )
		);

		fifoRsa	rx_FIFO (
			.clock ( clk ),
			.data ( rx_out ),
			.rdreq ( rd_uart ),
			.sclr ( !reset_n ),
			.wrreq ( rx_done_tick ),
			.empty ( rx_empty ),
			.full (),
			.q ( r_data ),
			.usedw (rx_usedw)
		);
		
		wire tx_fifo_empty, tx_done_tick;
		wire [DBIT - 1:0] tx_din;
		uart_tx #(.DBIT(DBIT), .SB_TICK(SB_TICK))	transmitter (
			.clk ( clk ),
			.reset_n ( reset_n ),
			.tx_start ( !tx_fifo_empty ),
			.s_tick ( tick ),
			.tx_din ( tx_din ),
			.tx_done_tick ( tx_done_tick ),
			.tx ( tx )
		);

		fifoRsa	tx_FIFO (
			.clock ( clk ),
			.data ( w_data ),
			.rdreq ( tx_done_tick ),
			.sclr ( !reset_n ),
			.wrreq ( wr_uart ),
			.empty ( tx_fifo_empty ),
			.full (tx_full),
			.q ( tx_din ),
			.usedw ()
		);
	endmodule
