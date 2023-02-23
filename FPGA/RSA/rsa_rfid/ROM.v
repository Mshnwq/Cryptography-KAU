module ROM(
input[1:0] addr,
input CS,
output reg [1:0] TEST,
output reg [1:0] NST,
output reg Load,
output reg Running,
output reg Done		 
);

reg[6:0] out;
//integer cr;
reg [6:0] ROMs[3:0];
initial begin
ROMs[0]=7'b0000000; ROMs[1]=7'b1010100;
ROMs[2]=7'b0110010; ROMs[3]=7'b1100001;
TEST 		 = ROMs[0][6:5];
NST 		 = ROMs[0][4:3];
Load 		 = ROMs[0][2];
Running	 = ROMs[0][1];
Done		 = ROMs[0][0];
end
always @(negedge CS) begin
//cr=addr;
TEST 		 <= ROMs[addr][6:5];
NST 		 <= ROMs[addr][4:3];
Load 		 <= ROMs[addr][2];
Running	 <= ROMs[addr][1];
Done		 <= ROMs[addr][0];
end
endmodule
