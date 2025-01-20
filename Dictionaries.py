# dict_name = {key : value} ;general syntax ;no duplicates allowed
# ordered since 3.7 version; unordered before that 
phone_no = {
    'Sovan': 7479297329,
    'Ashutosh': 9334534984,
    'Amlan': 7205011243,
    'Pratyush': 7205421832
}
print(phone_no)
print(phone_no['Pratyush'])

ph_no = dict({
    'Jango':1232,
    'Kaniga':3425,
    'Lincoln':2132,
    0:'Harem'
})
print(ph_no)
del ph_no['Kaniga']
print(ph_no)
print(ph_no.pop('Lincoln'))
print(ph_no)
print(ph_no[0])
print(ph_no)
ph_no['Jango']=6765
print(ph_no)

phone_no['Ashutosh'] = {'Ashutosh home':43234, 'Ashutosh office':54345, 'Ashutosh child':21612} # type: ignore
print(phone_no['Sovan'])
print(phone_no.get('Ashutosh'))

data = {
    3:'Hemant',
    1:'Jayant',
    4:'Kartik'
}
print(data)
print(data[3])
print(data.keys()) #returns keys in the dictionary
print(data.values())
print(data.items())
print(data.popitem())
print(data)
print(data.clear())
print(data)

grunt = { 
    2:'Quinton',
    45:'Mclafy',
    543:'Theodre Roosevelt',
    0:'Connor'
}
print(len(grunt))
for i in grunt:
    print(i)
    print(grunt[i])

for j in grunt.items():
    print(j)
dormant = grunt.copy()
print(dormant)

