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
        fetch = I[PC]
        DIC += 1
        print(fetch)
    
        if (fetch[0:2] == "101"):  #INIT
            fetch = fetch.replace("101 ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = imm
            PC += 1
        elif (fetch[0:2] == "111"):    #ADDI
            fetch = fetch.replace("111","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[0:6] == "1111100"):    #ADDN
            fetch = fetch.replace("1111100","")
            R = 3
            Reg[R] = Reg[R] - 1
            PC += 1
        elif (fetch[0:2] == "100"):    #ADD
            fetch = fetch.replace("100","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "00000"):   #SUBR0
            fetch = fetch.replace("00000","")
            Ry = int(fetch[0])
            Reg[0] = Reg[0] - Reg[Ry]
            PC += 1
        elif (fetch[0:3] == "0001"):    #XOR
            fetch = fetch.replace("0001","")
            fetch = fetch.split(",")      
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[0:2] == "001"):    #LWD
            fetch = fetch.replace("001","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[0:2] == "011"):    #SWD
            fetch = fetch.replace("011","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[0:2] == "110"):    #SLE                       
            fetch = fetch.replace("110","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if( Reg[Rx] < Reg[Ry] ):
                Reg[3] = 1
            else:
                Reg[3] = 0
            PC += 1
        elif (fetch[0:4] == "00001"):    #SLER 
            fetch = fetch.replace("00001","")
            Rx = 0
            Ry = int(fetch[0])
            if( Reg[Ry] < Reg[0] ):
                Reg[3] = 1
            else:
                Reg[3] = 0
            PC += 1
        elif (fetch[0:6] == "0001000"):    #CNTR0
            fetch = fetch.replace("0001000","")
            imm = int(fetch[0])
            PC = PC + imm
        elif (fetch[0:2] == "010"):    #JIF
            fetch = fetch.replace("010","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            PC = PC + imm
        elif(fetch[0:6] == "0001111"): #HLT
            finished = True
            
        
    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    print("Memory :",Memory)

    def main():
    instr_file = open("i_mem.txt","r")
    data_file = open("d_mem.txt","r")
    Memory = []
    Nlines = 0          # How many instrs total in input.txt  
    Instruction = []    # all instructions will be stored here
    print("Welcome to ECE366 ISA sample programs")
        print("Simulator")
        print("Normal execution")

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
