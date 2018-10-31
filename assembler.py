#!/usr/bin/env python

input_file = open("LIS_machine_code_program2.txt", "r")
output_file = open("program2_disassembled.lis", "w")

output = "\n"

for line in input_file:
	print output
	output_file.write(output)

	wrongOp = False
	if (line == "\n"):
		continue

	line = line.replace("\n", "")
	print "Machine code: ", line

	op_bin = line[1:8]
	if (op_bin == "0000000"):
		op = "HLT"
		output = op + " //Stop program\n" 
		continue

	elif (op_bin == "1111100"):
		op = "ADDN"
		output = op + "//r3 = r3 - 1\n" 
		continue

	elif (op_bin == "0001000"):
		op = "CNTR0"
		output = op + " //Count the number of 1's in r0\n"
		continue
	
	op_bin = line[1:6]

	if (op_bin == "00000"):
		op = "SUBR0"
		ry = str(int(line[6:8], 2)) 
		if (ry == '1'):
			wrongOp = True
		if (wrongOp == False):
			output = op + " r" + ry + " //r0 = r0 - ry\n"
			continue

	op_bin = line[1:5]
	
	if (op_bin == "0001"):
		op = "XOR"
		rx = str(int(line[5:6], 2))
		ry = str(int(line[6:8], 2)) 
		output = op + " r" + rx + ", r" + ry + " //rx = rx XOR ry\n"
		continue

	elif (op_bin == "0000"):
		op = "SLER"
		rx = str(int(line[5:7], 2))
		ry = str(int(line[7], 2))
		output = op + " r" + rx + ", r" + ry + " //If rx < r0 then r3 = 1\n\t//Else r3 = 0\n"
		continue

	op_bin = line[1:4]

	if (op_bin == "100"):
		op = "ADD"	
		rx = str(int(line[4:6], 2))
		ry = str(int(line[6:8], 2))
		output = op + " r" + rx + ", " + ry + " //rx = rx + ry\n"
		continue

	elif (op_bin == "111"):
		op = "ADDI"
		rx = str(int(line[4:6], 2))
		const = str(int(line[6:8], 2))
		output = op + " r" + rx + ", " + const + " //rx = rx + imm\n"
		continue

	elif (op_bin == "001"):
		op = "LWD"
		rx = str(int(line[4:6], 2))
		ry = str(int(line[6:8], 2))
		output = op + " r" + rx + ", r" + ry + " //rx = M[ry]\n"
		continue

	elif (op_bin == "011"):
		op = "SWD"
		rx = str(int(line[4:6], 2))
		ry = str(int(line[6:8], 2))
		output = op + " r" + rx + ", r" + ry + " //M[ry] = rx\n"
		continue

	elif (op_bin == "110"):
		op = "SLE"
		rx = str(int(line[4:6], 2))
		ry = str(int(line[6:8], 2))
		output = op + " r" + rx + ", " + ry + " //If rx < ry then r3 = 1\n\t//Else r3 = 0\n"
		continue

	elif (op_bin == "101"):
		op = "INIT"
		rx = str(int(line[4:6], 2))
		const = str(int(line[6:8], 2))
		output = op + " r" + rx + ", " + const + " //rx = imm\n"
		continue
	
	elif (op_bin == "010"):
		op = "JIF"
		sign = line[4] 
		const = int(line[5:8], 2)
		if (sign == '1'):
			const = -(0b111 - int(const) + 1)

		const = str(const)

		output = op + " " + const + " //If r3 = 1 then jump (PC = PC + imm)\n\t//Else do nothing\n"
		
	print output
	output_file.write(output)
