it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Las cantidad de compañias en it_commpanies es de: ', len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Intel', 'Nvidia', 'Amd', 'Radeon'])
print(it_companies)

it_companies.remove('Apple')
print(it_companies)

it_companies.remove('Amd')
it_companies.add('Qualcomm')
it_companies.remove('Qualcomm')
it_companies.discard('Samsung')
print(it_companies)