def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    ## create lists of the numbers and signs that are used
    first_numbers = []
    second_numbers = []
    solution_numbers = []
    sign_symbols = []
    for problem in problems:
        # isolate problem numbers and convert to int
        problem_numbers = problem.split(" ")
        
        if [x for x in problem_numbers if x.isalpha()]:
            return "Error: Numbers must only contain digits."
        
        problem_numbers = [int(number) for number in problem_numbers if number.isnumeric()]
        #_
        
        # create first_numbers list
        first_numbers.append(problem_numbers[0])
        #_
        
        # create second_numbers list
        second_numbers.append(problem_numbers[1])
        #_
        
        # calculate and create the solutions list and the sign list
        if "+" in problem:
            solved_problem = sum(problem_numbers)
            sign_symbols.append("+")
        elif "-" in problem:
            solved_problem = problem_numbers[0] - problem_numbers[1]
            sign_symbols.append("-")
        else:
            return "Error: Operator must be '+' or '-'."
        
        solution_numbers.append(solved_problem)
        #_
    ##_
    
    ## create the string that will be displayed
    max_length_list = []
    for number in first_numbers:
        index = first_numbers.index(number)
        max_length_list.append(max(len(str(number)), len(str(second_numbers[index])))+2)
    
    if [x for x in max_length_list if x > 6]:
        return "Error: Numbers cannot be more than four digits."
    
    # create the lines
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    space = "    "
    for number in first_numbers:
        
        index = first_numbers.index(number)
        
        first_line += " " * (max_length_list[index] - len(str(first_numbers[index]))) + str(first_numbers[index]) + space
        second_line += sign_symbols[index] + " " * ((max_length_list[index] - len(str(second_numbers[index]))) -1) + str(second_numbers[index]) + space
        third_line += "-" * max_length_list[index] + space
        fourth_line += " " * (max_length_list[index] - len(str(solution_numbers[index]))) + str(solution_numbers[index]) + space
    
    first_line += "\n"
    second_line += "\n"
    third_line += "\n"
    fourth_line += "\n"
    #_
    
    final_string = first_line + second_line + third_line + fourth_line
    ##_
    if show_answers:
        print(final_string)
    return final_string

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')