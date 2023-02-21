module ControlUnit
	(
	input clk, reset, go,
	output done, load ,incFreq, running, incAdd,
	input equal, over
	);
	
	wire [2:0] address;
	wire countLoad;
	wire [2:0] NSTw;
	wire [1:0] TESTw;
	wire Loadw, Runningw, incAddrw, incFreaqw;
	
	counter counter0(clk, reset, countLoad, ~countLoad, NSTw, address);
	ROM rom0(address, clk, TESTw, NSTw, load, running, incAdd, incFreq, done);
	mux4to1 mux0(~go, over, ~equal, 1'b1, TESTw, countLoad); 
endmodule
