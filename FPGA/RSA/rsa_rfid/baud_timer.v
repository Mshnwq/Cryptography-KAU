module baud_timer
	#(parameter bits = 4)( 
	input clk,
	input reset_n,
	input enable,
	input [bits - 1:0] FINAL_VALUE,
	output done
	);
	
	reg [bits -1:0] Q_reg, Q_next;
	
	 // output (BITS - 1:07 0, output done ); 

	always @(posedge clk, negedge reset_n) 
	begin 
		if (!reset_n) begin
			Q_reg <= 'b0; 
			end
		else if(enable) begin
			Q_reg <= Q_next;
			end
		else begin
			Q_reg <= Q_reg; 
			end
	end
	
	// Next state logic 
	assign done = (Q_reg == FINAL_VALUE); 

	
	always @(*) begin
		Q_next = done ? 'b0 : (Q_reg + 1); 
		end
		
endmodule 
