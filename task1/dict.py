''' Expression A and B '''
q1 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

res1 = q1['A'] + q1['B']
print(res1)


''' Expression A and C '''
q2 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

res2 = q1['A'] + q1['C']
print(res2)

''' Expression D and B '''
q3 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

r1 = q3.get('D','')
r2 = q3.get('B','')

res3 = r1 + r2
print(res3)


''' Expression A or B '''
q4 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

if(q4['A']):
    res4 = q4['A']
    print(res4)

else:
    res4 = q4['B']
    print(res4)


''' Expression A and B and C '''
q5 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}


r1 = q3.get('A','')
r2 = q3.get('B','')
r3 = q3.get('C','')


res5 = r1 + r2 +r3
print(res5)


''' Expression A and (B or C) '''
q6 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

r1=""
if (q6['B']):
    r1 = q6['B']
else:
    r1 = q6['C']
r2 = q6.get('A')
result6 = r2 + r1
print(result6)



''' Expression A and (C or D) '''
q7 = {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

r1=""
if (q7['C']):
    r1 = q7['C']
else:
    r1 = q7['D']
r2 = q7.get('A')
result7 = r2 + r1
print(result7)


''' Expression A and (B or C) and D '''
q8 = {'A':'Hello', 'C': 'Buddy', 'D': 'Welcome'}

r1=""
if "B" in q8:
    r1 = q8['B']
else:
    r1 = q8.get('C','')
r2 = q8.get('A')
r3 = q8.get('D')
result8 = r2 + r1 + r3
print(result8)









