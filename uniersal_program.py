from decoder import decoding


def find_variable(programs, inp_var):
    lst_x = []
    lst_z = []
    for program in programs:
        if program.find('X') != -1:
            lst_x.append(eval(program[program.find('X')+1]))
            lst_x_var = [0] * max(lst_x)
        elif program.find('Z') != -1:
            lst_z.append(eval(program[program.find('Z') + 1]))
            lst_z_var = [0] * max(lst_z)
        else:
            lst_x_var = [0]*len(inp_var)
            if 'lst_z_var' not in locals():
                lst_z_var = []

            return lst_x_var, lst_z_var

    return lst_x_var, lst_z_var

def find_label(programs):
    lst_label = []

    for program in programs:
        # A -> 1
        if program.find('A') != -1:
            lst_label.append([1, eval(program[program.find('A') + 1]), 'A'])

        # B -> 2
        elif program.find('B') != -1:
            lst_label.append([2, eval(program[program.find('B') + 1]), 'B'])

        # C -> 3
        elif program.find('C') != -1:
            lst_label.append([3, eval(program[program.find('C') + 1]), 'C'])

        # D -> 4
        elif program.find('D') != -1:
            lst_label.append([4, eval(program[program.find('D') + 1]), 'D'])

        # E -> 5
        elif program.find('E') != -1:
            lst_label.append([5, eval(program[program.find('E') + 1]), 'E'])

        else:
            lst_label.append([0, 0, 'End'])

    lst_char_label = [num[0] for num in lst_label]
    lst_number_label = [num[1] for num in lst_label]

    lst_based_on_char = [0] * max(lst_char_label)
    lst_based_on_num = [0] * (5 * (max(lst_number_label) - 1))

    lst_label_program = lst_based_on_char + lst_based_on_num

    for label in lst_label:
        if label[0] > 0:
            index = label[0]-1 + (5*(label[1] - 1))
            lst_label_program[index] = 1

    return lst_label_program


def label_couner(program_line, lst_label):
    line_of_program_label = find_label([program_line])
    line_of_program_label += [0] * (len(lst_label) - len(line_of_program_label))
    return line_of_program_label


if __name__ == "__main__":
    # inp = str(input("input number: "))
    inp_program = input("program number: ")
    inp_var = input("input variable: ")

    lst_inpt_var = inp_var.split(" ")

    list_godal_number, list_program = decoding(inp_program)
    print("\n")
    dict_program = {}
    for idx, item in enumerate(list_program):
        dict_program[idx+1] = item

    dict_godal_number = {}
    for idx, item in enumerate(list_godal_number):
        dict_godal_number[idx+1] = item

    lst_x_var, lst_z_var = find_variable(list_program, inp_var)
    lst_label = find_label(list_program)

    Y = 0

    # initialized prime variables
    for idx, X_inp in enumerate(lst_inpt_var):
        lst_x_var[idx] += eval(X_inp)

    i = 1

    line_of_program_label = {}
    while i <= len(dict_program):
        print(i, lst_x_var, lst_z_var, Y)
        # print(i, lst_x_var[0], lst_x_var[1], lst_x_var[2], lst_z_var[0], lst_z_var[1], Y)

        # V <- V
        if dict_godal_number[i][1] == 0:
            line_of_program_label[i] = label_couner(dict_program[i], lst_label)
            i += 1

        # V <- V + 1
        elif dict_godal_number[i][1] == 1:
            if dict_program[i].find('X') != -1:
                lst_x_var[eval(dict_program[i][dict_program[i].find('X')+1]) - 1] += 1
            elif dict_program[i].find('Z') != -1:
                lst_z_var[eval(dict_program[i][dict_program[i].find('Z') + 1]) - 1] += 1
            elif dict_program[i].find('Y') != -1:
                Y += 1
            line_of_program_label[i] = label_couner(dict_program[i], lst_label)
            i += 1

        # V <- V - 1
        elif dict_godal_number[i][1] == 2:
            if dict_program[i].find('X') != -1:
                lst_x_var[eval(dict_program[i][dict_program[i].find('X')+1]) - 1] -= 1
            elif dict_program[i].find('Z') != -1:
                lst_z_var[eval(dict_program[i][dict_program[i].find('Z') + 1]) - 1] -= 1
            elif dict_program[i].find('Y') != -1:
                Y -= 1
            line_of_program_label[i] = label_couner(dict_program[i], lst_label)
            i += 1


        # IF GOTO
        else:
            if dict_program[i].find('X') != -1:
                if lst_x_var[eval(dict_program[i][dict_program[i].find('X')+1]) - 1] != 0:
                    go_to_label = label_couner(dict_program[i], lst_label)

                    for key, val in line_of_program_label.items():
                        if val == go_to_label:
                            line_of_program_label[i] = label_couner(dict_program[i], lst_label)
                            i = key
                            break
                        else:
                            break

                else:
                    line_of_program_label[i] = label_couner(dict_program[i], lst_label)
                    i += 1

            elif dict_program[i].find('Z') != -1:
                if lst_z_var[eval(dict_program[i][dict_program[i].find('Z')+1]) - 1] != 0:
                    go_to_label = label_couner(dict_program[i], lst_label)

                    for key, val in line_of_program_label.items():
                        if val == go_to_label:
                            line_of_program_label[i] = label_couner(dict_program[i], lst_label)
                            i = key
                        else:
                            break
                else:
                    break
            else:
                break