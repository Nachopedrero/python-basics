
citizens = [{ 'First Name': 'Preston' , 'Last Name': 'Cunningham', 'Age': 49 , 'Education': 'Doctoral', 'Occupation':' Teacher' ,'Experience (Years)': 6, 'Salary': 62499}, 
 { 'First Name': 'Madaline', 'Last Name': 'Farrell', 'Age': 41, 'Education': 'Bachelor', 'Occupation': 'Insurer','Experience (Years)': 16, 'Salary': 50190},
 { 'First Name': 'Eleanor', 'Last Name': 'Carter', 'Age': 49, 'Education': 'Lower secondary', 'Occupation': 'Programmer','Experience (Years)': 18, 'Salary': 189716},
 { 'First Name': 'Adison', 'Last Name': 'Hall', 'Age': 42 , 'Education': 'Bachelor', 'Occupation': 'Florist','Experience (Years)': 21, 'Salary': 34517},
 { 'First Name': 'Grace', 'Last Name': 'Cooper', 'Age': 49, 'Education': 'Master', 'Occupation': 'Singer','Experience (Years)': 9, 'Salary': 51994},
 { 'First Name': 'Alford', 'Last Name': 'Kelley', 'Age': 49, 'Education': 'Bachelor', 'Occupation': 'Aeroplane Pilot','Experience (Years)': 9, 'Salary': 170466},
 { 'First Name': 'Vincent', 'Last Name': 'Anderson', 'Age': 47, 'Education': 'Master', 'Occupation': 'Botanist','Experience (Years)': 6, 'Salary': 71617},
 { 'First Name': 'Myra', 'Last Name': 'Wright', 'Age': 45, 'Education': 'Master', 'Occupation': 'Geologist' ,'Experience (Years)': 18, 'Salary': 48786},
 { 'First Name': 'Chester', 'Last Name':'Bennett', 'Age': 42, 'Education': 'Doctoral', 'Occupation': 'Astronomer','Experience (Years)': 13, 'Salary': 44826},
 { 'First Name': 'Blake', 'Last Name': 'Tucker', 'Age': 42, 'Education': 'Doctoral', 'Occupation': 'Firefighter','Experience (Years)': 21, 'Salary': 36761},
 { 'First Name': 'Paige', 'Last Name': 'Ryan', 'Age': 43, 'Education': 'Primary', 'Occupation': 'Fine Artist','Experience (Years)': 19, 'Salary': 28181},
 { 'First Name': 'Natalie', 'Last Name': 'Ellis', 'Age': 45, 'Education': 'Bachelor', 'Occupation': 'Baker','Experience (Years)': 0, 'Salary': 31194},
 { 'First Name': 'Martin', 'Last Name': 'Thompson', 'Age': 47, 'Education': 'Bachelor', 'Occupation': 'Journalist','Experience (Years)': 21, 'Salary': 90183},
 { 'First Name': 'Alan', 'Last Name': 'Sullivan', 'Age': 46, 'Education': 'Doctoral', 'Occupation': 'Singer','Experience (Years)': 2, 'Salary': 18440},
 { 'First Name': 'Inga', 'Last Name': 'Bergman', 'Age': 41, 'Education': 'Bachelor', 'Occupation': 'Producer','Experience (Years)': 22, 'Salary': 80029},
 { 'First Name': 'Freddy', 'Last Name': 'Brown', 'Age': 48, 'Education': 'Bachelor', 'Occupation': 'Economist','Experience (Years)': 18, 'Salary': 146217},
 { 'First Name': 'Adelaide', 'Last Name': 'Farrell', 'Age': 42, 'Education': 'Bachelor', 'Occupation': 'Mechanic','Experience (Years)': 9, 'Salary':19414},
 { 'First Name': 'Luke', 'Last Name': 'Cooper', 'Age': 40, 'Education': 'Upper secondary', 'Occupation': 'Producer','Experience (Years)': 17, 'Salary': 160541},
 { 'First Name': 'Sofia', 'Last Name': 'Hall', 'Age': 41, 'Education': 'Doctoral', 'Occupation': 'Baker','Experience (Years)': 1, 'Salary': 25904},
 { 'First Name': 'Ashton', 'Last Name': 'Kelly', 'Age': 49, 'Education': 'Master', 'Occupation': 'Chef','Experience (Years)': 6, 'Salary': 95533}
]

def media(ages):
  s=0
  for c in ages:
    s+=c
  return s/len(ages)

ages=[]
for c in citizens:
  ages.append(c['Age'])

print("The mean age of the citizens is:",round(media(ages),1),"years")

educationDuplicate =[]
for i in range(len(citizens)):
 for j in range(i+1,len(citizens)):
   if citizens[i]['Education']==citizens[j]['Education']:
     educationDuplicate.append(citizens[i]['Education'])
     break

education=[]
for c in citizens:
  if c['Education'] not in educationDuplicate:
   education.append(c['Education'])

print(education)

print(len(education))


occupationsDuplicate =[]
for i in range(len(citizens)):
 for j in range(i+1,len(citizens)):
   if citizens[i]['Occupation']==citizens[j]['Occupation']:
     occupationsDuplicate.append(citizens[i]['Occupation'])
     break

occupation=[]
for c in citizens:
  if c['Occupation'] not in occupationsDuplicate:
   occupation.append(c['Occupation'])

print(occupation)

print(len(occupation))

citizensReduce=[]
for c in citizens:
  citizensReduce.append({'First Name':c['First Name'], 'Last Name': c['Last Name'],'Starting age':c['Age']-c['Experience (Years)']})

print(citizensReduce)

educationStats=[]
for e in education:
  for c in citizens:
    if e==c['Education']:
      educationStats.append({e:c['Salary']})
print(educationStats)

occupationStats=[]
for o in occupation:
  for c in citizens:
    if o==c['Occupation']:
      occupationStats.append({o:c['Salary']})
print(occupationStats)


result = list(filter(lambda x: (x['Education'] == 'Doctoral'), citizens))

print(result)

def educationDoctoral(citizens):
  result=[]
  for c in citizens:
    if c['Education'] == 'Doctoral':
      result.append(c)
  return result

print(educationDoctoral(citizens))

result = list(map(lambda x : x['First Name']+" "+x['Last Name']+" is "+str(x['Age'])+" years old", citizens))

print(result)