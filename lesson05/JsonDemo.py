import json

score = '{"國文":100, "數學":90}'
students = '[{"name":"vincent", "age":18}, {"name":"mary", "age":17}]'

obj = json.loads(score) #將json字串轉為json物件
print(type(obj))
print(obj.get('國文'))

obj2 = json.loads(students) #將json字串轉為json物件
print(type(obj2))
for st in obj2:
    print(st.get('name'), st.get('age'))