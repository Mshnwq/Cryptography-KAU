transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/rsa_rfid.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/bytes_to_words_opt.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/send_data.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/hex_to_7seg.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/datapath.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/staticvalue.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/encrypt_decrypt.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/divider64.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/controlunit.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/counter.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/rom.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/mux4to1.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/uart.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/baud_timer.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/uart_rx.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/fiforsa.v}
vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/uart_tx.v}

vlog -vlog01compat -work work +incdir+C:/Users/Perux/Documents/KAU/5th\ year/Trimester\ 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Perux/Documents/KAU/5th year/Trimester 1/EE460/project/FPGA_RSA_UHF_RFID/rsa_rfid/testRSA2.v}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L fiftyfivenm_ver -L rtl_work -L work -voptargs="+acc"  testRSA2

add wave *
view structure
view signals
run -all
