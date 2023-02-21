module mux4to1 (input a,                 // input called a
					 input b,                 // input called b
					 input c,                 // input called c
					 input d,                 // input called d
					 input [1:0] sel,         // input sel used to select between a,b,c,d
					 output out);             // output based on input sel

   // When sel[1] is 0, (sel[0]? b:a) is selected and when sel[1] is 1, (sel[0] ? d:c) is taken
   // When sel[0] is 0, a is sent to output, else b and when sel[0] is 0, c is sent to output, else d
   assign out = sel[1] ? (sel[0] ? d : c) : (sel[0] ? b : a); 
   
endmodule