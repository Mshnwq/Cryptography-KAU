module counter (  input clk,               // Declare input port for clock to allow counter to count up
                  input rstn,              // Declare input port for reset to allow the counter to be reset to 0 when required
						input load,
						input count,
						input  [2:0] current,
                  output reg[2:0] out);    // Declare 4-bit output port to get the counter values

  // This always block will be triggered at the rising edge of clk (0->1)
  // Once inside this block, it checks if the reset is 0, if yes then change out to zero
  // If reset is 1, then design should be allowed to count up, so increment counter
  initial begin
  out = 0;
  end
  always @ (posedge clk) begin
    if (rstn==1)
      out <= 0;
    else if(count)
      out <= out + 1;
		else 
		out <= current;
  end
endmodule
