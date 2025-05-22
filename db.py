import json
py_data = {'name': '''Himanshu''', "age": True, "active": False, "other": None}
json_data= json.dumps(py_data)
print(json_data)
print(type(json_data))
# ans 
# {"name": "Himanshu", "age": true, "active": false, "other": null}
# <class 'str'>

j_data =  '{"name": "Himanshu", "age": true, "active": false, "other": null}'
print(type(j_data))
py_data = json.loads(j_data)    # this is the function because it come from file and by paranthesis it written anythin so it not a method or variable
print(py_data)
print(type(py_data))

# {"name": "Himanshu", "age": true, "active": false, "other": null}
# <class 'str'>
# {'name': 'Himanshu', 'age': True, 'active': False, 'other': None}
# <class 'dict'>

# api to restapi , type of api like softapi etc 