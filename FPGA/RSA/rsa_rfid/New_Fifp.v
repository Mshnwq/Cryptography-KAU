module fifo (
    input clk,
    input rst,
    input wr_en,
    input rd_en,
    input [7:0] data_in,
    output [7:0] data_out,
    output full,
    output empty,
    output reg [9:0] current_data_count
);

reg [7:0] mem [0:1023];
reg [9:0] head = 0;
reg [9:0] tail = 0;
reg [9:0] next_head;

assign data_out = mem[tail];
assign full = (current_data_count == 1024);
assign empty = (current_data_count == 0);

always @(posedge clk or negedge rst) begin
    if (!rst) begin
        current_data_count <= 0;
        head <= 0;
        tail <= 0;
    end else begin
        if (wr_en && !full) begin
            mem[head] <= data_in;
            next_head <= head + 1;
            if (next_head == 1024) begin
                next_head <= 0;
            end
            head <= next_head;
            current_data_count <= current_data_count + 1;
        end
        if (rd_en && !empty) begin
            tail <= tail + 1;
            if (tail == 1024) begin
                tail <= 0;
            end
            current_data_count <= current_data_count - 1;
        end
    end
end

endmodule
