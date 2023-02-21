module ROM(
input[2:0] addr,
input CS,
output reg [1:0] TEST,
output reg [2:0] NST,
output reg Load,
output reg Runningm,
output reg incAddrw,
output reg incFreaqw, 
output reg Done		 
);

reg[9:0] out;
integer cr;
reg [9:0] ROMs[7:0];
initial begin
ROMs[0]=10'b0000000000; ROMs[1]=10'b1101010000;
ROMs[2]=10'b1101101000; ROMs[3]=10'b0111000100;
ROMs[4]=10'b1001000000; ROMs[5]=10'b1101000010;
ROMs[6]=10'b1100000001; ROMs[7]= 10'b0000000000;
TEST 		 = ROMs[0][9:8];
NST 		 = ROMs[0][7:5];
Load 		 = ROMs[0][4];
Runningm	 = ROMs[0][3];
incAddrw  = ROMs[0][2];
incFreaqw = ROMs[0][1];
Done		 = ROMs[0][0];
end
always @(negedge CS) begin
cr=addr;
TEST 		 <= ROMs[cr][9:8];
NST 		 <= ROMs[cr][7:5];
Load 		 <= ROMs[cr][4];
Runningm	 <= ROMs[cr][3];
incAddrw  <= ROMs[cr][2];
incFreaqw <= ROMs[cr][1];
Done		 <= ROMs[cr][0];
end
endmodule
