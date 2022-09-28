print('Welcome to the tip calculator.')
total = float(input('What was the total bill? '))
people = int(input('How many people to split the bill? '))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
total_percentage = total*(percentage/100)
result = (total_percentage + total)/people
result = "{:.2f}".format(result)

print(f'Each pearson Should pay: ${result}')

############################################################################
# # two digit adding
# two_digit_number = input('Type a two digit number: ') 
# new_input = str(two_digit_number)
# result1 = new_input[0] 
# result2 = new_input[1]
# print(int(result1)+int(result2))

##############################################################################
# # remaining time until 90
# age = input("What is your current age? ")
# age_as_int = int(age)
# years_rem = 90 - age_as_int
# month_rem = years_rem*12
# week_rem = years_rem*52
# days_rem = years_rem*365
# print(f"You have {years_rem} years, {month_rem} months, {week_rem} weeks and {days_rem} days")