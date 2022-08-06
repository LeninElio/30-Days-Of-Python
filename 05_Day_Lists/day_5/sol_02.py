companies = ['SU PTA MADRE MARK', 'Google', 'Microsoft', 'Apple', 'PremiumSoft', 'IBM', 'Oracle', 'Amazon', 'JetBrains',
             '#;  ']

#  Solución 16
#  Sort the list using sort() method
del companies[-1]
companies[0] = 'Meta'
print(companies)
companies.sort()
print(companies)

#  Solución 17
#  Reverse the list in descending order using reverse() method
companies.sort(reverse=True)
print(companies)

#  Solución 18
#  Slice out the first 3 companies from the list
print(companies[:3])

#  Solución 19
#  Slice out the last 3 companies from the list
print(companies[-3:])

#  Solución 20
#  Slice out the middle IT company or companies from the list
# print(len(companies))
medio = len(companies) / 2
print(companies[int(medio)])

#  Solución 21
#  Remove the first IT company from the list
del companies[0]
print(companies)

#  Solución 22
#  Remove the middle IT company or companies from the list
medio = len(companies) / 2
del companies[int(medio)]
print(companies)

#  Solución 23
#  Remove the last IT company from the list
del companies[-1]
print(companies)

#  Solución 24
#  Remove all IT companies from the list
companies.clear()
print(companies)

#  Solución 25
#  Destroy the IT companies list
del companies
# print(companies)

#  Solución 26
#  Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print(front_end)
front_end.extend(back_end)
print(back_end)
print(front_end)

#  Solución 27
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert
# Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)
busca_red = full_stack.index('Redux')

full_stack.insert(busca_red, 'Python')
full_stack.insert(busca_red, 'SQL')
print(full_stack)
