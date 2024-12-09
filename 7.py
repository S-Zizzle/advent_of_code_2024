problems = {}

with open('7_input.txt', 'r') as file:
    for line in file:
        line = line.split(':')

        if line[0] in problems:
            problems[int(line[0])].append(list(map(int, line[1].strip('\n').strip().split(' '))))
        else:
            problems[int(line[0])] = [list(map(int, line[1].strip('\n').strip().split(' ')))]

def recurse(equation, answer):
    if len(equation) == 1:
        if equation[0] == answer:
            return True
        else:
            return False
            
    this = equation[:2]

    p = this[0] + this[1]
    m = this[0] * this[1]

    equation = equation[2:]

    p_equation = equation.copy()
    m_equation = equation.copy()

    p_equation.insert(0, p)
    m_equation.insert(0, m)

    p_result = recurse(p_equation, answer)
    m_result = recurse(m_equation, answer)

    return True in [p_result, m_result]

count = 0

for answer, numbersets in problems.items():
    for numbers in numbersets:
        print(numbers)
        
        found = recurse(numbers, answer)

        if found:
            count += answer

print(count)