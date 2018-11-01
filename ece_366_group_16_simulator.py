def simulate(Instruction,Memory):
    print("ECE366 Fall 2018 ISA Design: Simulator")
    print()
    PC = 0              # Program-counter
    DIC = 0
    Reg = [0,0,0,0]     # 4 registers, init to all 0
    Memory = [0 for i in range(10)] # data memory, 10 spaces all init to 0.
    print("******** Simulation starts *********")
    finished = False
    while(not(finished)):
        fetch = Instruction[PC]
        DIC += 1
        
        if(fetch[1:8] == "0000000"): #HLT
            finished = True
            print("*HLT*")
        elif (fetch[1:4] == "101"):  #INIT
            print("*INIT*")
            R = format(int(fetch[4:6], 2))
            print("R = ", R)
            imm = format(int(fetch[6:8], 2))
            Reg[R] = imm
            PC += 1
        elif (fetch[1:4] == "111"):    #ADDI
            print("*ADDI*")
            R = format(int(fetch[4:6], 2))
            imm = format(int(fetch[6:8], 2))
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[1:8] == "1111100"):    #ADDN
            print("*ADDN*")
            Reg[3] = Reg[3] - 1
            PC += 1
        elif (fetch[1:4] == "100"):    #ADD
            print("*ADD*")
            Rx = format(int(fetch[4:6]),2)
            Ry = format(int(fetch[6:8), 2])
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[1:6] == "00000"):   #SUBR0
            print("*SUBR0*")
            Ry = format(int(fetch[6:8]),2)
            Reg[0] = Reg[0] - Reg[Ry]
            PC += 1
        elif (fetch[1:5] == "0001"):    #XOR
            print("*XOR*")
            Rx = format(int(fetch[5:6]), 2)
            Ry = format(int(fetch[6:8), 2))
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[1:4] == "001"):    #LWD
            print("*LWD*")
            Rx = format(int(fetch[4:6]), 2)
            Ry = format(int(fetch[6:8]), 2)
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[1:4] == "011"):    #SWD
            print("*SWD*")
            Rx = format(int(fetch[4:6]), 2)
            Ry = format(int(fetch[6:8]), 2)
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[1:4] == "110"):    #SLE
            print("*SLE*")
            Rx = format(int(fetch[4:6]), 2)
            Ry = format(int(fetch[6:8]), 2)
            if( Reg[Rx] < Reg[Ry] ):
                Reg[3] = 1
            else:
                Reg[3] = 0
            PC += 1
        elif (fetch[1:6] == "00001"):    #SLER Need to double check
            print("*SLER*")
            Rx = 0
            Ry = format(int(fetch[6:8]), 2)
            if( Reg[Ry] < Reg[0] ):
                Reg[3] = 1
            else:
                Reg[3] = 0
            PC += 1
        elif (fetch[1:8] == "0001000"):    #CNTR0
            print("*CNTR0*")
            fetch = fetch.replace("0001000","")
            #not done
            PC = PC + imm
        elif (fetch[1:4] == "010"):    #JIF
            print("*JIF*")
            imm = format(int(4:8]), 2)
            if(R[3] == 1):
                PC = PC + imm
            else:
                PC = PC + 1

    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    #print("Memory :",Memory)

    data = open("d_mem.txt","w")    # Write data back into d_mem.txt
    for i in range(len(Memory)):
        
        data.write(format(Memory[i],"016b"))
        data.write("\n")
    data.close()

def main():
    instr_file = open("i_mem.txt","r")
    data_file = open("d_mem.txt","r")
    Memory = []
    Nlines = 0          # How many instrs total in input.txt  
    Instruction = []    # all instructions will be stored here

    for line in instr_file: # Read in instr 
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        line = line.replace("\n","")
        Instruction.append(line)                        # Copy all instruction into a list
        Nlines +=1

    for line in data_file:  # Read in data memory
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        Memory.append(int(line,2))
    
        simulate(Instruction,Memory)


    
    instr_file.close()
    data_file.close()
    
if __name__ == "__main__":
    main()
