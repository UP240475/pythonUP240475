# Day 5 lvl 1 - Lists  in Python

#punto 1

el = list()
print(el)

#punto 2

list_nums= ["1", "2", "3", "4", "5", "6"]

#punto 3

print(len(list_nums))

#punto 4

print(list_nums[0])
print(list_nums[-1])
middle = len(list_nums)//2
print(list_nums[middle])

#punto 5

mixed_data_types = ["patricio", 19, 1.72, "single", "Aguascalientes"]

#punto 6

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#punto 7

print(it_companies)

#punto 8

print(len(it_companies))

#punto 9

print(it_companies[0])
print(it_companies[-1])
middle = len(it_companies)//2
print(it_companies[middle])

#punto 10

it_companies[1] = "gogle"
print(it_companies)

#punto 11

it_companies.append("apple")
print(it_companies)

#punto 12

middle = len(it_companies)//2
it_companies.insert(middle,"intel")
print(it_companies)

#punto 13

it_companies[4] = it_companies[4].upper()
print(it_companies)

#punto 14

print("#; ".join(it_companies))

#punto 15

print("IBM" in it_companies)
print("Google" in it_companies)

#punto 16

it_companies.sort()
print(it_companies)

#punto 17

it_companies.reverse()
print(it_companies)

#punto 18

first_3 = it_companies[:3]
print(first_3)

#punto 19

last_3 = it_companies[-3:]
print(last_3)

#punto 20
middle = len(it_companies)//2
print(it_companies[middle:middle+1])

#punto 21

del it_companies[0]
print(it_companies)

#punto 22

middle = len(it_companies)//2
del it_companies [middle:middle+1]
print(it_companies)

#punto 23

del it_companies[-1]
print(it_companies)

#punto 24

del it_companies[:]
print(it_companies)

#punto 25

del it_companies

#punto 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
print(f"{front_end} + {back_end}\n= {join}")

#punto 27

full_stack = join
redux = full_stack.index("Redux")
position = redux+1
full_stack[position:position] = ["Python", "SQL"]
print(full_stack)


