
def godal_numbers(number):
    number += 1
    x = 0
    while number % 2 == 0:
        number //= 2
        x += 1
    number -= 1
    y = 0
    if number % 2 == 0 and number != 0:
        y = number // 2
    return x, y

def godal_to_code(label, instruct, variable):

    # Create List of Labels
    label_list = ['']
    for i in range(1, label+2):
        label_list.append(f'A{i}')
        label_list.append(f'B{i}')
        label_list.append(f'C{i}')
        label_list.append(f'D{i}')
        label_list.append(f'E{i}')

    # Create List of Labels
    variable_list = ['Y']
    for i in range(1, variable+2):
        variable_list.append(f'X{i}')
        variable_list.append(f'Z{i}')

    # Create Instruction roles
    if instruct == 0:
        instruction = f'{variable_list[variable]} <- {variable_list[variable]}'
    elif instruct == 1:
        instruction = f'{variable_list[variable]} <- {variable_list[variable]} + 1'
    elif instruct == 2:
        instruction = f'{variable_list[variable]} <- {variable_list[variable]} - 1'
    else:
        next_label = instruct - 2
        instruction = f'IF {variable_list[variable]}≠0 GOTO {label_list[next_label]}'

    if label != 0:

        return f"[{label_list[label]}] " + instruction

    else:
        return instruction




def decoding(inp):
    list_godel_number = []
    list_program = []
    for number in inp.split(" "):
        number = eval(number)
        a, y = godal_numbers(number)
        b, c = godal_numbers(y)
        # print("<{}, <{}, {}>".format(a, b, c))
        list_godel_number.append([a, b, c])
        list_program.append(godal_to_code(a, b, c))
        print(godal_to_code(a, b, c))
    return list_godel_number, list_program
