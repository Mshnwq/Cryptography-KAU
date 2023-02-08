module staticValue 
	#(parameter bits = 32, parameter value = 32'd0 )
	(output [bits-1:0] out);
	
	assign out = value;
	
endmodule 