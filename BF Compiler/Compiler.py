# BF Compiler by Kian Acaster v1.0 [No loops] #
limit = 10**3
cells = []
pointer = 0 
instructions = []
string = []
final_string = ""

for i in range(limit): 
    cells.append(0) 
def parse_instructions(inst, arr):
    for i in range(len(inst)):
        arr.append(inst[i])
file = input()
instruction = open(file,"r")
console_instruction = input()
parse_instructions(instruction.read(), instructions)
if console_instruction == "compile":
    for i in range(len(instructions)):
        if instructions[i] == "+": 
            cells[pointer] = cells[pointer] + 1
        if instructions[i] == "-": 
            cells[pointer] = cells[pointer] - 1    
        if instructions[i] == ">": 
            if pointer == limit:
                pointer= 0
            else:
                pointer = pointer + 1            
        if instructions[i] == "<": 
            if pointer == 0:
                pointer = limit - 1
            else:    
                pointer = pointer - 1
        if instructions[i] == ".":
            string.append(chr(cells[pointer]))         
    for i in range(len(string)):
        final_string += string[i]
    print(final_string)
