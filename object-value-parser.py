import json
from pprint import pprint
# https://github.com/akesterson/dpath-python
import dpath.util

def get_object_value( test_object, path):
    test_object_dict = json.loads(test_object)
    result_value = dpath.util.get(test_object_dict, path)
    return result_value

test_object_1 = '{"a":{"b":{"c":"d"}}}'
path_1 = 'a/b/c'
#value = d

print(get_object_value(test_object_1,path_1))

test_object_2 = '{"x":{"y":{"z":"a"}}}'
path_2 = 'x/y/z'
#value = a

print(get_object_value(test_object_2,path_2))

# To run a fully functional and comprehensive test suite, a python unit test suite such as nose2 should be used
# Nose2: https://pypi.org/project/nose2/
