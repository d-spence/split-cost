PROMPT = '> '
NAMES = ['Dan', 'Mattie']

def get_name(i): return NAMES[i] if (0 <= i < len(NAMES)) else f'Person {i+1}'

print('Enter $ total')
total_cost_input = input(PROMPT).strip()

try:
    total_cost = float(total_cost_input)

    if total_cost <= 0: raise ValueError
except ValueError:
    print('Total must be an integer or decimal value greater than 0.')
    exit(1)

print('How many ways do you want to split? Press [ENTER] for default of 2.')
split_by_input = input(PROMPT).strip()

try:
    split_by = 2 if (split_by_input == '') else int(split_by_input)

    if not 2 <= split_by < 10: raise ValueError # accepted split_by range
except ValueError:
    print('Split value must be an integer greater than 1 and less than 10.')
    exit(1)

individual_deductions = [0 for i in range(split_by)] # [0, 0, ...]

# get deductions (e.g. cost of items not being shared) for each person
for i in range(split_by):
    print(f'Enter deductions for {get_name(i)}. Separate multiple $ values by a space.')
    deductions_input = input(PROMPT).strip()

    for val in deductions_input.split(' '):
        try:
            individual_deductions[i] += 0 if (val == '') else float(val)
        except ValueError:
            print('Deduction values must be integers or decimals separated by a space.')
            exit(1)

total_cost_minus_deductions = total_cost - sum(individual_deductions)
split_cost = total_cost_minus_deductions / split_by
print('')

# display totals
for i in range(split_by):
    individual_total = split_cost + individual_deductions[i]
    print(f'{get_name(i):>8}: ${individual_total:>6.2f} (deductions: ${individual_deductions[i]:>6.2f})')

print('-' * 40)
print(f'{"TOTAL":>8}: ${total_cost:>6.2f} ({split_by}-way split)')
input('\nPress [ENTER] to exit script...')
