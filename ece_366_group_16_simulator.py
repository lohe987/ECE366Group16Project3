def simulate(I,Nsteps):
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
        fetch = fetch.replace("R","")       # Delete all the 'R' to make things simpler
        if (fetch[0:4] == "INIT "):
            fetch = fetch.replace("INIT ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = imm
            PC += 1
        elif (fetch[0:4] == "ADDI"):
            fetch = fetch.replace("ADDI ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[0:4] == "ADDN"):
            fetch = fetch.replace("ADDN ","")
            fetch = fetch.split(",")
            R = int(fetch[0])
            imm = int(fetch[1])
            Reg[R] = Reg[R] + imm
            PC += 1
        elif (fetch[0:4] == "ADD "):
            fetch = fetch.replace("ADD ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] + Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "SUB0 "):
            fetch = fetch.replace("SUB0 ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] - Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "XO  "):    # why "XO  " instead of "XOR " ?
                                        # --> because all the 'R' is deleted at fetch to make things simplier. 
            fetch = fetch.replace("XO  ","")
            fetch = fetch.split(",")      
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Reg[Rx] ^ Reg[Ry]
            PC += 1
        elif (fetch[0:4] == "LWD "):
            fetch = fetch.replace("LWD ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Reg[Rx] = Memory[Ry]
            PC += 1
        elif (fetch[0:4] == "SWD "):
            fetch = fetch.replace("SWD ","")
            fetch = fetch.replace("(","")
            fetch = fetch.replace(")","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            Memory[Ry] = Reg[Rx]
            PC += 1
        elif (fetch[0:4] == "SLE "):  
                                    
            fetch = fetch.replace("SLE ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if( Reg[Rx] < Reg[Ry] ):
                Reg[0] = 1
            else:
                Reg[0] = 0
            PC += 1
        elif (fetch[0:4] == "SLE0"):  # why "SLE0" instead of "SLER0" ? 
                                    # --> because all the 'R' is deleted at fetch to make things simplier. 
            fetch = fetch.replace("SLE0 ","")
            fetch = fetch.split(",")
            Rx = int(fetch[0])
            Ry = int(fetch[1])
            if( Reg[Rx] < Reg[Ry] ):
                Reg[0] = 1
            else:
                Reg[0] = 0
            PC += 1
        elif (fetch[0:4] == "CNT0"):     # why "CNT0" instead of "CNTR0" ?
                                        # --> because all the 'R' is deleted at fetch to make things simplier. 
            fetch = fetch.replace("CNT0 ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            PC = PC + imm
        elif (fetch[0:4] == "JIF "):
            fetch = fetch.replace("JIF ","")
            fetch = fetch.split(",")
            imm = int(fetch[0])
            PC = PC + imm
        elif(fetch[0:4] == "HLT "):
            finished = True
        if ( (DIC % Nsteps) == 0):
            print("Registers R0-R3: ", Reg)
            print("Memory: ",Memory)
            print()
        
    print("******** Simulation finished *********")
    print("Dynamic Instr Count: ",DIC)
    print("Registers R0-R3: ",Reg)
    print("Memory :",Memory)
