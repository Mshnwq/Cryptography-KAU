`timescale 1 ps / 1 ps
module controlUnit
		(
	input clk, reset, go,
	output load , running, done,
	input over
	);
	
	wire [1:0] address;
	wire countLoad;
	wire [1:0] NSTw;
	wire [1:0] TESTw;
	
	counter counter0(clk, reset, ~countLoad, NSTw, address);
	ROM rom0(address, clk, TESTw, NSTw, load, running, done);
   mux4to1 mux0(~go, ~over, 1'b0, 1'b1, TESTw, countLoad); 
endmodule
