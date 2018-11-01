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
            fetch = fetch.replace("101 ","")
            fetch = fetch.split("101")
            R = int(fetch[0])
            print("R = ", R)
            imm = int(fetch[])
            Reg[R] = imm
            PC += 1
        elif (fetch[1:4] == "111"):    #ADDI
            print("*ADDI*")
            fetch = fetch.replace("111","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[1:8] == "1111100"):    #ADDN
            print("*ADDN*")
            fetch = fetch.replace("1111100","")
            R = 3
            Reg[R] = Reg[R] - 1
            PC += 1
        elif (fetch[1:4] == "100"):    #ADD
            print("*ADD*")
            fetch = fetch.replace("100","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[1:6] == "00000"):   #SUBR0
            print("*SUBR0*")
            fetch = fetch.replace("00000","")
            Ry = int(fetch[0])
            Reg[0] = Reg[0] - Reg[Ry]
            PC += 1
        elif (fetch[1:5] == "0001"):    #XOR
            print("*XOR*")
            fetch = fetch.replace("0001","")
            fetch = fetch.split(",")      
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[1:4] == "001"):    #LWD
            print("*LWD*")
            fetch = fetch.replace("001","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[1:4] == "011"):    #SWD
            print("*SWD*")
            fetch = fetch.replace("011","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[1:4] == "110"):    #SLE
            print("*SLE*")
            fetch = fetch.replace("110","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if( Reg[Rx] < Reg[Ry] ):
                Reg[3] = 1
            else:
                Reg[3] = 0
            PC += 1
        elif (fetch[1:6] == "00001"):    #SLER
            print("*SLER*")
            fetch = fetch.replace("00001","")
            Rx = 0
            Ry = int(fetch[0])
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
            fetch = fetch.replace("010","")
            imm = int(fetch[0])
            PC = PC + imm

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
