name = "prasath"
is_active = True
age=20
lists = {
        'Alice': {'age': 25, 'city': 'New York'},
        'Bob': {'age': 30, 'city': 'San Francisco'},
    }

# methods
get_all = ["prasath" , "prem" , "sam"]

get_all.append("srini")

get_all.insert(4 , "vasant")

get_all.remove("prasath")

get_all.clear()

specific_names = get_all[0:2] # get_all[-1]

# sets
unique = {1,2,3,3}

is_occur  = 'pa' in name

not 1 == 1 or 1 == "1"


# disclear functions
def get_a_record():
    input_name = input("Insert person name: ")
    
    if input_name in lists:
        return lists[input_name]
    else:
        return f"Record for {input_name} not found."

# while loop
def while_function():
    i = 0
    while i <= 5:
        print(i)
        i += 1 

# for loop
def for_loop():
    for item in get_all:
        print(item)

# if loop
def if_condition():
    temperature = 30
    if temperature > float(input("get a temeraturew: ")):
        return "its very hot"
    elif temperature > 20:
       return "weater is good"
    else:
      return "weater is good"
    
