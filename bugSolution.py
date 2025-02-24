def function_with_uncommon_error(data):
    try:
        if isinstance(data, (str, bytes)):
            return []  # Handle strings and bytes explicitly
        result = [x for x in data if x > 10]
        return result
    except TypeError as e:
        print(f"Error: {e}")
        return []

data = (1, 2, 3, 4, 11, 12, 13)
result = function_with_uncommon_error(data) # tuple
print(result) 

data = {1, 2, 3, 4, 11, 12, 13}
result = function_with_uncommon_error(data) #set
print(result)

data = "not iterable"
result = function_with_uncommon_error(data) # string
print(result)

data = [1,2,3,4,11,12,13]
result = function_with_uncommon_error(data) #list
print(result)