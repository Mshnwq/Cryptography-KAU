module send_data(
  input clock,        		// Clock signal input
  input reset,       		//  reset input
  input [31:0] data_in,   	// 32-bit data input
  input start,     			// input to start operation
  output [7:0] out,  	// 8-bit data output
  output reg req_wr,			// signal to allow fifo to store current byte 
  output reg done		// done with operation
);

  // Define parameter values for each state
  localparam IDLE	= 4'd0;
  localparam SEND = 4'd1;
  localparam SHIFT = 4'd2;
  localparam DONE = 4'd3;

  reg [1:0] state = IDLE;    // Register to hold the current state
  reg [31:0] data_reg = 0;		// Register to hold the data input
  reg [3:0] current_byte = 0;
  assign out = data_reg[7:0];
  
  always @(posedge clock) begin
    if (!reset) begin
      state <= IDLE;
		current_byte <= 0;
      data_reg <= 0;
		done <= 0;
    end 
	 else begin
		  case (state)
			IDLE: begin
				done <= 0;
			  if (start) begin   // Check if read request 
				data_reg <= data_in;
				state <= SEND;      // Move to SEND state to send the byte
			  end 
			end
			SEND: begin
				if ( current_byte < 4) begin
				  current_byte <= current_byte+1;
				  req_wr <= 1;
				  state <= SHIFT;          // Move to SHIFT state to shift 1 byte
				end
				else begin
					 state <= DONE;
				end
			end
			SHIFT: begin
				data_reg <= {8'd0, data_reg[31:8]};
				req_wr <= 0;       // Set read request output high
				state <= SEND;          // Move to SEND state to move the fifo
			end
			DONE: begin
			  done <= 1;
			  current_byte <= 0;
			  req_wr <= 0;  
			  state <= IDLE;          // Move to IDLE state 
			end

		  endcase
		  
		end
  end

endmodule
