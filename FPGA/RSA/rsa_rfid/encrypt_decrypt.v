//module that performs encryption and decryption
//modulo exponentiation is performed using the algorithm in Applied Cryptography by Bruce Schneier
module encrypt_decrypt
   #(parameter WORDSIZE = 16)
	(
	input [WORDSIZE*2-1:0] base,
	input [WORDSIZE*2-1:0] modulo,
	input [WORDSIZE*2-1:0] exponent,
	input clk,
	input reset,
	output finish,
	output [WORDSIZE*2-1:0] result
	);

	//localparam WORDSIZE = 8;
	localparam DIVIDE_LATENCY = 5'd20;
	//state definitions
	localparam DIVIDING = 3'd1;
	localparam UPDATE = 3'd2;
	localparam HOLD =	3'd3;
	localparam DONE =	3'd4;
	
	reg [WORDSIZE*4-1:0] base_reg = 0;
	reg [WORDSIZE*4-1:0] modulo_reg = 0;
	reg [WORDSIZE*4-1:0] exponent_reg = 0;
	reg [WORDSIZE*2-1:0] result_reg = 0;
	reg [4:0] divide_latency_counter;
	reg [2:0] state;

	wire [WORDSIZE*4-1:0] result_mul_base;	
	wire [WORDSIZE*2-1:0] result_next;
	wire [WORDSIZE*4-1:0] base_squared;
	wire [WORDSIZE*2-1:0] base_next;
	wire [WORDSIZE*2-1:0] exponent_next = exponent_reg >> 1;
	assign base_squared = base_reg * base_reg;
	assign result_mul_base = result_reg * base_reg;
	assign finish = (state == HOLD) ? 1'b1 : 1'b0;
	assign result = result_reg;
	
	divider64 base_squared_mod_modulo(
		.clock(clk),
		.denom(modulo_reg),
		.numer(base_squared),
		.quotient(),
		.remain(base_next)
	);
	
	divider64 result_mul_base_mod_modulo(
		.clock(clk),
		.denom(modulo_reg),
		.numer(result_mul_base),
		.quotient(),
		.remain(result_next)
	);
	
	always @ (posedge clk) begin
		if (reset) begin
			base_reg <= base;
			modulo_reg <= modulo;
			exponent_reg <= exponent;
			result_reg <= 32'd1;
			divide_latency_counter <= DIVIDE_LATENCY;
			state <= DIVIDING;
		end
		else case (state)
			DIVIDING: 
				begin
				
					//stall until dividers are done, since division takes DIVIDE_LATENCY cycles
					if (divide_latency_counter == 5'd0) state <= UPDATE;
					else divide_latency_counter <= divide_latency_counter - 5'd1;
					
				end
			UPDATE: 
				begin
				
					if (exponent_reg != 64'd0) 
					begin
					
						if (exponent_reg[0]) result_reg <= result_next;
						base_reg <= base_next;
						exponent_reg <= exponent_next;
						divide_latency_counter <= DIVIDE_LATENCY;
						state <= DIVIDING;
						
					end
					else state <= HOLD;
					
				end
			HOLD: 
				begin
				base_reg <= 64'd0;
				modulo_reg <= 64'd0;
				exponent_reg <= 64'd0;
				state <= DONE;
				end
			DONE: 
				begin

				end	
		endcase
	end
	
endmodule
