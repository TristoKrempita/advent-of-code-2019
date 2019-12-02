from part_1 import calc_zeroth_value

def calc_values(opcode):
    for i in range(100):
        for j in range(100):
            opcode_copy = [int(n) for n in opcode.split(',')]
            opcode_copy[1] = i
            opcode_copy[2] = j
            if calc_zeroth_value(opcode_copy)[0] == 19690720:
                return i, j


with open("input", "r") as file:
    opcode = file.read()

if __name__ == '__main__':
    print(calc_values(opcode))
