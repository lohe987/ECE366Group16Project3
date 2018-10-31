#!/usr/bin/env python

input_file1 = open("program2.lis", "r")
output_file = open("LIS_machine_code_program2.txt", "w")

memSection = False
codeSection = False
commentHere = False
output = ""
memory = []
jumpMarkers = dict()

def TwosComplement(num, numBits):
	if (num < 0):
		num = (1 << numBits) + num
	else:
		if ((num & (1 << (numBits - 1))) != 0):
			num -= (1 << numBits)
	
	return num


for line in input_file1:
	if (line == "\n"):
		continue

	line = line.replace("\n", "")
	line = line.replace(" ", "")

	line = line.split('/')
	line = line[0]

	if (line == "*instructions"):
		memSection = False
		codeSection = True

	if (memSection == True):
		line = line.split('~')
		if (line[2][0] == '-'):
			line[2] = line[2].replace("-", "")
			line[2] = 0b1111111111111111 - int(line[2]) + 1

		memValue = format(int(line[2]), "016b")
		memory.append(memValue)

	if (line == "*memory"):
		memSection = True

	if (codeSection == True):
		line = line.replace("\t", "")
		line = line.replace("r", "")
		line = line.replace("[", "")
		line = line.replace("]", "")
		
		if (line[0:3] == 'LWD'):
			line = line.replace("LWD", "")
			line = line.split(',')

			op = "001"
			rx = format(int(line[0]), "02b")
		 	const = format(int(line[1]), "02b")
			
			output = op + rx + const + " //LWD: rx = M[ry]"

		elif (line[0:3] == 'SWD'):
			line = line.replace("SWD", "")
			line = line.split(',')

			op = "011"
			rx = format(int(line[0]), "02b")
		 	const = format(int(line[1]), "02b")

			output = op + rx + const + " //SWD: M[ry] = rx"

		elif (line[0:4] == 'SLER'):
			line = line.replace("SLER", "")
			line = line.split(',')

			op = "0000"
			rx = format(int(line[0]), "02b")
		 	ry = format(int(line[1]), "01b")
			ry = ry[0]

			output = op + rx + ry + " //SLER: If rx < r0, then r3 = 1, Else r3 = 0"

		elif (line[0:3] == 'SLE'):
			line = line.replace("SLE", "")
			line = line.split(',')

			op = "110"
			rx = format(int(line[0]), "02b")
		 	const = format(int(line[1]), "02b")

			output = op + rx + const + " //SLE: If rx < ry, then r3 = 1, Else r3 = 0"


		elif (line[0:4] == 'ADDN'):
			line = line.replace("ADDN", "")

			op = "1111"

			output = op + "100" + " //ADDN: r3 = r3 - 1"

		elif (line[0:4] == 'ADDI'):
			line = line.replace("ADDI", "")
			line = line.split(',')
	
			const = int(line[1])
			if (const < 0):
				const *= -1
				const = 0b1111111111111111 - const + 1
				const = format(const, "02b")
				const = const[14:16]
			else:
				const = format(int(line[1]), "02b")

			op = "111"
			rx = format(int(line[0]), "02b")
			output = op + rx + const + " //ADDI: rx = rx + imm"

		elif (line[0:3] == 'ADD'):
			line = line.replace("ADD", "")
			line = line.split(',')

			op = "100"
			rx = format(int(line[0]), "02b")
		 	ry = format(int(line[1]), "02b")

			output = op + rx + ry + " //ADD: rx = rx + ry"

		elif (line[0:4] == 'INIT'):
			line = line.replace("INIT", "")
			line = line.split(',')

			op = "101"
			rx = format(int(line[0]), "02b")
		 	ry = format(int(line[1]), "02b")

			output = op + rx + ry + " //INIT: rx = imm"

		elif (line[0:3] == 'XOR'):
			line = line.replace("XOR", "")
			line = line.split(',')

			op = "0001"
			rx = format(int(line[0]), "01b")
			rx = rx[0]
		 	ry = format(int(line[1]), "02b")

			output = op + rx + ry + " //XOR: rx = rx XOR ry"

		elif (line[0:3] == 'JIF'):
			line = line.replace("JIF", "")
			line = line.split(' ')
			op = "010"
			const = TwosComplement(int(line[0]), 4)
			const = format(const, "04b")

			output = op + const + " //JIF: If r3 = 1, then jump (PC = PC + imm), Else do nothing"

		elif (line[0:5] == 'CNTR0'):
			line = line.replace("CNTR0", "")

			op = "0001"

			output = op + "000" + " //CNTR0: Count the number of 1's in r0"

		elif (line[0:5] == 'SUBR0'):
			line = line.replace("SUBR0", "")

			op = "0000"
		 	ry = format(int(line[0]), "02b")

			output = op + '0' + ry + " //SUBR0: r0 = r0 - ry"


		elif (line[0:3] == 'HLT'):
			line = line.replace("HLT", "")

			op = "000"

			output = op + "00" + "00" + " //HLT: End the program"

		numOnes = output.count("1")
		if ((numOnes % 2) == 0 and output != ""):
			output = '0' + output
		elif (output != ""):
			output = '1' + output

		if (output != ""):
			output_file.write(output + "\n")
		output = ""
