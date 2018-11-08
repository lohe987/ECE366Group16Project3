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
        elif (fetch[1:4] == '101'):  #INIT
            print("*INIT*")
            Rx = int(fetch[4:6], 2)
            print("R = ", Rx)
            imm = int(fetch[6:8], 2)
            print("imm = ", imm)
            Reg[Rx] = imm
            print("R", Rx, "=", Reg[Rx])
            PC += 1
        elif (fetch[1:4] == '111'):    #ADDI
            print("*ADDI*")
            Rx = int(fetch[4:6], 2)
            imm = int(fetch[6:8], 2)
            Reg[Rx] = Reg[Rx] + imm
            PC += 1
        elif (fetch[1:8] == '1111100'):    #ADDN
            print("*ADDN*")
            Reg[3] = Reg[3] - 1
            PC += 1
        elif (fetch[1:4] == '100'):    #ADD
            print("*ADD*")
            Rx = int(fetch[4:6],2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            print("R",Rx, " = R",Rx, " + ", "R",Ry)
            print("R",Rx, " = ", Reg[Rx])
            PC += 1
        elif (fetch[1:6] == '00000'):   #SUBR0
            print("*SUBR0*")
            Ry = int(fetch[6:8],2)
            Reg[0] = Reg[0] - Reg[Ry]
            PC += 1
        elif (fetch[1:5] == '0001'):    #XOR
            print("*XOR*")
            Rx = int(fetch[5:6], 2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[1:4] == '001'):    #LWD
            print("*LWD*")
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            Reg[Rx] = Memory[Ry]
            print("Load from memory slot mem[", Ry,"]")
            print("R ", Rx, " equals ", Reg[Rx])
            PC += 1
        elif (fetch[1:4] == '011'):    #SWD
            print("*SWD*")
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[1:4] == '110'):    #SLE
            print("*SLE*")
            Rx = int(fetch[4:6], 2)
            Ry = int(fetch[6:8], 2)
            if( Reg[Rx] < Reg[Ry] ):
                Reg[3] = 1
                print(Rx, "<", Ry, " so R3 = 1")
            else:
                Reg[3] = 0
                print(Rx, " is not < ", Ry, " so R3 = 0")
            PC += 1
        elif (fetch[1:6] == '00001'):    #SLER Need to double check
            print("*SLER*")
            Rx = 0
            Ry = int(fetch[6:8], 2)
            if( Reg[Ry] < Reg[0] ):
                Reg[3] = 1
            else:
                Reg[3] = 0
            PC += 1
        elif (fetch[1:8] == '0001000'):    #CNTR0
            count = 0
            n = Reg[0]
            while(n):
                count += n & 1
                n>>=1
            Reg[0] = count
            PC = PC + imm
        elif (fetch[1:4] == '010'):    #JIF
            print("*JIF*")
            sign = fetch[4]
            const = int(fetch[5:8],2)
            print("R3 equals ", Reg[3])
            if(Reg[3] == 1):
                print("R3 equals 1 therefore ")
                if(sign == '1'):
                    const = -(0b111 - int(const) + 1)
                    PC = PC + const
                    print("Jump back ", const)
                else:
                    PC = PC + const
                    print("Jump forward ", const)
            else:
                PC = PC + 1
                print("R3 does not equal 1 therefore ")
                print("PC = PC + 1")

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
        Instruction.append(line)                      # Copy all instruction into a list
        Nlines +=1

    print(Instruction[0])
    for line in data_file:  # Read in data memory
        if (line == "\n" or line[0] =='#'):              # empty lines,comments ignored
            continue
        Memory.append(int(line,2))
        print("Memory :",Memory)
    simulate(Instruction, Memory)

    
    instr_file.close()
    data_file.close()
    
if __name__ == "__main__":
    main()
