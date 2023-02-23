module dataPath
	#(parameter WordSize = 32)
	(  
	input clk, reset,
	
	// Data Path I/O	
	input  [7:0] uart_in,
	output [7:0] output_text,
	output [WordSize-1:0] cipherFull,
	output nextByte_in,
	output nextByte_out,
	input empty_fifo,
	input wire [9:0] usedw, 
	
	// Controller I/O
	input wire load, running,   // enablers
	output wire over            // flags
	);
	
	wire [WordSize-1:0]  inText; // from input
	wire [WordSize-1:0]  inKey; // from input
	wire [WordSize-1:0]  inMod; // from input
	wire [WordSize-1:0]  Cipher_Text; // to output
	wire [WordSize-1:0] ground; 
	wire start_Sending, start_Encrypting;
	staticValue outDefValue(ground);
	assign cipherFull[7:0] = inKey[7:0];
	assign cipherFull[15:8] = inMod[7:0];
	assign cipherFull[23:16] = inText[7:0];
	assign starting = (usedw == 9'd12) ? 1'b1 : 1'b0;
//	mux2to1 loadInpMux(ground, input_text, load, inMux);       // to get input from MUX
//	mux2to1 loadKeyMux(ground, key,        load, keyMux);      // to get input from MUX
//	mux2to1 loadModMux(ground, mod,        load, modMux);      // to get input from MUX
//	mux2to1 loadOutMux(ground, outMux,     over, output_text); // to get output from MUX
	

	
//	The bytes_to_words_opt module takes the the recived bytes in the uart module fifo combines them into 32-bit words and stores
// them in three differen registers in the following order: Key register, modulos register and plaintext register
bytes_to_words_opt bytes_to_words_opt_instance(
  .clock(clk),
  .reset(reset),
  .data_in(uart_in),
  .rdreq_in(starting),
  .key(inKey),
  .mod(inMod),
  .plaintext(inText),
  .rdreq_out(nextByte_in),
  .empty(empty_fifo),
  .done(start_Encrypting)
);



//	The encrypt_decrypt module takes the key, mod, and plain text from the bytes_to_words_opt and use them to encrypt or
// decrypt the message
	encrypt_decrypt encrypt_decrypt_state_machine(
	.base(inText),
	.modulo(inMod),
	.exponent(inKey),
	.clk(clk),
	.reset(start_Encrypting),
	.finish(start_Sending),
	.result(Cipher_Text)
);


//	The send_data module takes the resulting ciphertext from the encrypting module and send it to the uart module byte by byte
 send_data send_data_instance (
  .clock(clk),
  .reset(reset),
  .data_in(Cipher_Text),
  .start(start_Sending),
  .out(output_text),
  .req_wr(nextByte_out),
  .done(over)
);


	
endmodule 