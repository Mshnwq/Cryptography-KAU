transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/rsa_rfid.v}
vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/mux2to1.v}
vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/datapath.v}
vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/staticvalue.v}
vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/encrypt_decrypt.v}
vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/divider64.v}
vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/controlunit.v}

vlog -vlog01compat -work work +incdir+C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid {C:/Users/Abdallah/Desktop/RSA/FPGA_RSA_UHF_RFID/rsa_rfid/testRSA.v}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L altera_lnsim_ver -L fiftyfivenm_ver -L rtl_work -L work -voptargs="+acc"  testRSA

add wave *
view structure
view signals
run -all
