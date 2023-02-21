module uart_rx 
	#(parameter DBIT = 8, // # data bits 
					SB_TICK = 16 // # stop bit ticks 
	)
	(
		input clk, reset_n, 
		input rx, s_tick, 
		output reg rx_done_tick,
		output [DBIT - 1:0] rx_out 
	);
	localparam 	idle = 0, start = 1, 
					data = 2, stop = 3;
					
	reg [1:0] state_reg,state_next;
	reg [3:0] s_reg, s_next; 						// keep track of the baud rate ticks (16 total) 
	reg [$clog2(DBIT) - 1:0] n_reg, n_next; 	// keep track of the number of data bits recieved 
	reg [DBIT - 1:0] b_reg, b_next; 				// stores the recieved data bits 
	
	// State and other registers 
	always @(posedge clk, negedge reset_n) 
	begin 
		if (!reset_n) 
		begin 
			state_reg <= idle;
			s_reg <= 0; n_reg <= 0; 
			b_reg <= 0; 
		end 
		else begin 
			state_reg <= state_next; 
			s_reg <= s_next; 
			n_reg <= n_next; 
			b_reg <= b_next; 
		end 
	end 
	
	// Next state logic 
	always @(*)
	begin 
		state_next = state_reg; 
		s_next = s_reg; 
		n_next = n_reg; 
		b_next = b_reg; 
		rx_done_tick = 1'b0; 
		case (state_reg) 
			idle:
			begin
				if (!rx) begin 
					s_next = 0; 
					state_next = start; 
				end 
			end
			start:
			begin
				if (s_tick) begin
					if (s_reg == 7) begin 
						s_next = 0;
						n_next = 0;
						state_next = data; 
					end
					else begin
						s_next = s_reg + 1; 
					end
				end
			end
			data:
			begin
				if (s_tick) begin
					if(s_reg == 15) begin
						s_next = 0; 
						b_next = {rx, b_reg[DBIT - 1:1]}; // Right shift 
						if (n_reg == (DBIT - 1))
							state_next = stop; 
						else
							n_next = n_reg + 1; 
					end 
					else 
						s_next = s_reg + 1; 
				end
			end
			stop:
			begin
				if (s_tick) begin
					if(s_reg == (SB_TICK - 1)) begin 
						rx_done_tick = 1'b1; 
						state_next = idle; 
					end
					else
						s_next = s_reg + 1;
				end
			end
			default:
				state_next = idle;
		endcase
	end
	
	//output
	assign rx_out = b_reg;
endmodule

			
