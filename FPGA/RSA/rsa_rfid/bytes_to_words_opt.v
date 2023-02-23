module bytes_to_words_opt(
  input clock,        // Clock signal input
  input reset,        // Asynchronous reset input
  input [7:0] data_in,   // 8-bit data input
  input rdreq_in,     // Read request input to start operation
  output reg [31:0] key,  // 32-bit data output
  output reg [31:0] mod,  // 32-bit data output
  output reg [31:0] plaintext,  // 32-bit data output
  output reg rdreq_out,   // Read request output
  input empty,
  output reg done
);

  // Define parameter values for each state
  localparam IDLE	= 4'd0;
  localparam READ_0 = 4'd1;
  localparam READ_1 = 4'd2;
  localparam READ_2 = 4'd3;
  localparam READ_3 = 4'd4;
  localparam STORE_KEY = 4'd5;
  localparam STORE_MOD = 4'd6;
  localparam STORE_TEXT = 4'd7;
  localparam STORE_SELECT = 4'd8;
  localparam ADVANCE = 4'd9;

  reg [3:0] state = IDLE;    // Register to hold the current state
  reg [31:0] word_buffer;    // Register to hold the 32-bit word
  reg [3:0] next_state = 0;  // Register to keep track of the next state 
  reg [3:0] CURRENT_WORD = 0;  // Register to keep track of the next state 
  
  always @(posedge clock) begin
    if (!reset) begin
      state <= IDLE;
      next_state <= 0;
      rdreq_out <= 0;
		CURRENT_WORD <= 0;
		done <= 0;
    end 
	 else begin
		  case (state)
			IDLE: begin
				done <= 0;
			  if (rdreq_in) begin   // Check if read request 
				CURRENT_WORD = 0;
				state <= READ_0;      // Move to READ_0 state to read first byte
			  end 
			end
			READ_0: begin
				if(empty)begin
					word_buffer[7:0] = 0;
				end
				else begin
					word_buffer[7:0] = data_in;   // Store first byte of word
			  end
			  CURRENT_WORD = CURRENT_WORD+1;          // Move to ADVANCE state to move the fifo
			  next_state = READ_1;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_1: begin
				if(empty)begin
				word_buffer[15:8] = 0;
				end
				else begin
			  word_buffer[15:8] = data_in;   // Store second byte of word
			  end
			  next_state = READ_2;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_2: begin
				if(empty)begin
					word_buffer[23:16] = 0;
				end
				else begin
					word_buffer[23:16] = data_in;   // Store third byte of word
			  end
			  next_state = READ_3;
			  rdreq_out <= 1;       // Set read request output high
			  state <= ADVANCE;          // Move to ADVANCE state to move the fifo
			end
			READ_3: begin
				if(empty)begin
					word_buffer[31:24] = 0;
				end
				else begin
					word_buffer[31:24] = data_in;   // Store fourth byte of word
			  end
			  rdreq_out <= 1;       // Set read request output high
			  state <= STORE_SELECT;          // Move to ADVANCE state to move the fifo
			end
			STORE_KEY: begin
				key <= word_buffer;  // Set output to the complete 32-bit word
				state <= READ_0;          // Move to ADVANCE state to move the fifo
			end
			STORE_MOD: begin
				mod <= word_buffer;  // Set output to the complete 32-bit word
				state <= READ_0;          // Move to ADVANCE state to move the fifo
			end
			STORE_TEXT: begin
				plaintext <= word_buffer;  // Set output to the complete 32-bit word
				done <= 1;       // Set read request output high
				state <= IDLE;          // Move to ADVANCE state to move the fifo
			end
			STORE_SELECT: begin
				rdreq_out = 0;
				case(CURRENT_WORD)
					1: begin
						state <= STORE_KEY;
					end
					2: begin
						state <= STORE_MOD;
					end
					3: begin 
						state <= STORE_TEXT;
					end
				endcase
			end
			
			ADVANCE: begin
			  rdreq_out = 0;       // Set read request output high
			  state <= next_state;          // Move to ADVANCE state to move the fifo
			end
			
		  endcase
		  
		end
  end

endmodule
