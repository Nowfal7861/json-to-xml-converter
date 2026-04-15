import sys
import json


def handle_object(data, name, indent):
    space = "    " * indent
    xml = ''
    if name:
        xml += f'{space}<object name = "{name}">\n'
    else:
        xml += f'{space}<object>\n'
    for key,value in data.items():
        xml += json_to_xml(value,key,indent + 1)
    xml += f'{space}</object>\n'
    return xml

def handle_array(data, name, indent):
    space = "    " * indent
    xml = f'{space}<array name = "{name}">\n'
    for item in data:
        xml += json_to_xml(item, None, indent + 1)
    xml += f'{space}</array>\n'
    return xml

def json_to_xml(data,name = None, indent = 0):
    space = "    " * indent
    if isinstance(data,dict):
        return handle_object(data,name,indent)
    elif isinstance(data,list):
        return handle_array(data,name,indent)
    elif isinstance(data,str):
        if name:
            return f'{space}<string name = "{name}">{data}</string>\n'
        else:
            return f'{space}<string>{data}</string>\n'
    elif isinstance(data, bool):
        if name:
            return f'{space}<boolean name = "{name}">{str(data).lower()}</boolean>\n'
        else:
            return f'{space}<boolean>{str(data).lower()}</boolean>\n'
    elif isinstance(data, (int,float)):
        if name:
            return f'{space}<number name = "{name}">{data}</number>\n'
        else:
            return f'{space}<number>{data}</number>\n'
    else:
        if name:
            return f'{space}<null name = "{name}"/>\n'
        else:
            return f'{space}<null/>\n'
    

# MAIN
if len(sys.argv) != 3:
    print("Usage: python script.py input.json output.xml")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file,"r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error FIle '{input_file}'not Found")
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON forat")
    sys.exit(1)

if not isinstance(data, (dict,list)):
    print("Top level json must be object or array")
    sys.exit(1)

xml_output = json_to_xml(data)

try:
    with open(output_file, "w") as f:
        f.write(xml_output)
except Exception as e:
    print(f"Error : {e}")
    sys.exit(1)
print("conversion seccessfull")


# print(json_to_xml({"age": 25}))










# import sys
# import json
# print(sys.argv)


# if len(sys.argv) != 3:
#     print("Usage: python script.py input.json output.xml")
#     sys.exit(1)


# input_file = sys.argv[1]

# with open(input_file,"r") as f:
#     data = json.load(f)

