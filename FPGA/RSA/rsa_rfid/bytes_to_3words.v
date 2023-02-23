module bytes_to_3words(
  input clock,        // Clock signal input
  input reset,        // Asynchronous reset input
  input [7:0] data_in,   // 8-bit data input
  input rdreq_in,     // Read request input to start operation
  output reg [31:0] key,  // 32-bit data output
  output reg [31:0] mod,  // 32-bit data output
  output reg [31:0] plaintext,  // 32-bit data output
  output reg rdreq_out,   // Read request output
  input empty
);

  // Define parameter values for each state
  localparam IDLE	= 4'd0;
  localparam READ_0 = 4'd1;
  localparam READ_1 = 4'd2;
  localparam READ_2 = 4'd3;
  localparam READ_3 = 4'd4;
  localparam READ_4 = 4'd5;
  localparam READ_5 = 4'd6;
  localparam READ_6 = 4'd7;
  localparam READ_7 = 4'd8;
  localparam READ_8 = 4'd9;
  localparam READ_9 = 4'd10;
  localparam READ_10 = 4'd11;
  localparam READ_11 = 4'd12;
  localparam SHOW    = 4'd13;
  localparam ADVANCE = 4'd14;

  reg [3:0] state = IDLE;    // Register to hold the current state
  reg [31:0] word_buffer_k;    // Register to hold the 32-bit word
  reg [31:0] word_buffer_m;    // Register to hold the 32-bit word
  reg [31:0] word_buffer_p;    // Register to hold the 32-bit word
  reg [3:0] next_state = 0;  // Register to keep track of the next state 
  reg START = 1'b1;
  reg clear;
  always @(posedge clock) begin
    if (!reset) begin
      state <= IDLE;
      next_state <= 0;
      rdreq_out <= 0;
    end 
	 else begin
		  case (state)
			IDLE: begin
				clear <= 0;
			  if (rdreq_in&&!empty) begin   // Check if read request 
				state <= READ_0;      // Move to READ_0 state to read first byte
				START <= 0;
			  end 
			end
			READ_0: begin
			  word_buffer_k[7:0] = data_in;   // Store first byte of word
			  next_state <= 2;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_1: begin
			  word_buffer_k[15:8] = data_in;  // Store second byte of word
			  next_state <= 3;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_2: begin
			  word_buffer_k[23:16] = data_in; // Store third byte of word
			  next_state <= 4;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_3: begin
			  word_buffer_k[31:24] = data_in; // Store fourth byte of word
			  next_state <= 5;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_4: begin
			  word_buffer_m[7:0] <= data_in;   // Store first byte of word
			  next_state <= 6;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_5: begin
			  word_buffer_m[15:8] <= data_in;  // Store second byte of word
			 next_state <= 7;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_6: begin
			  word_buffer_m[23:16] <= data_in; // Store third byte of word
			  next_state <= 8;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_7: begin
			  word_buffer_m[31:24] <= data_in; // Store fourth byte of word
			  next_state <= 9;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_8: begin
			  word_buffer_p[7:0] <= data_in;   // Store first byte of word
			  next_state <= 10;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_9: begin
			  word_buffer_p[15:8] <= data_in;  // Store second byte of word
			  next_state <= 11;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_10: begin
			  word_buffer_p[23:16] <= data_in; // Store third byte of word
			  next_state <= 12;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_11: begin
			  word_buffer_p[31:24] <= data_in; // Store fourth byte of word
			  next_state <= 13;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			SHOW: begin
				key <= word_buffer_k;  // Set output to the complete 32-bit word
				mod <= word_buffer_m;  // Set output to the complete 32-bit word
				plaintext <= word_buffer_p;  // Set output to the complete 32-bit word
			  next_state <= 0;
			  clear <= 1;
			  state <= IDLE;          // Move to IDLE state to move the fifo
			end
			ADVANCE: begin
			  rdreq_out <= 0;       // Set read request output high
			  state <= next_state;          // Move to ADVANCE state to move the fifo
			end
		  endcase
		end
  end

endmodule
