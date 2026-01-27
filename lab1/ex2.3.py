import json
import math

def find_size(input_dict):
	if "size" in input_dict:
		input_dict["size"] = 42
		#print(input_dict["size"])
	for i in input_dict:
		if type(input_dict[i]) == dict:
			#print(i)
			find_size(input_dict[i])

## Reversing Json #####
def	reverse_json(output_dict):
	output_dict = reverse(output_dict)
	for i in output_dict:
		if type(output_dict[i]) == dict:
			#print(i)
			reverse_json(output_dict[i])
	return output_dict

def reverse(input_dict):
	#print(type(input_dict))
	keys = list(reversed(input_dict.keys()))
	new_dict ={}
	i = 0
	for k in keys:
		test = keys[i]
		new_dict[keys[i]] = input_dict[keys[i]]
		i = i + 1
	#print(new_dict)
	return new_dict
#######


f = open("large-file.json", "r")
data = f.read()
json_data = json.loads(data)

a = 0
#print(len(json_data))
for i in json_data:
	#print()
	find_size(i) 

new_list = []
for i in json_data:
	#print(i.keys())
	new_list.append(reverse_json(i))

reversed(new_list)
g =open("output.2.3.json", "w")
json.dump(new_list,g,indent=2)
f.close()
	
