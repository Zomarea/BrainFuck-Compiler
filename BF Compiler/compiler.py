# BF Compiler by Kian Acaster v1.0 [No loops] #
limit = 10**3 # The size of the cell array
cells = [] # The cell array
pointer = 0 # The index pointer for the cell array
instructions = [] # An array of each instruction from the code file
string = [] # An array of characters from each cell's ASCII value (if printed)
final_string = "" # A string of every character from the string array (joined)

# A loop to predefine each index in the cell array (between 0 and the limit) to be 0
for i in range(limit): 
    cells.append(0) 
# A function to traverse through the file loaded to the compiler and push each individual character to the instructions array    
def parse_instructions(inst, arr):
    for i in range(len(inst)):
        arr.append(inst[i])
# Loads the file into the compiler        
file = input()
instruction = open(file,"r")
# Allows the user to type in specific instructions to the compiler (right now only "compile")
console_instruction = input()
# Runs the function "parse_instructions" 
parse_instructions(instruction.read(), instructions)

# This only happens if the user types "compile" into the console, this will run the program
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
