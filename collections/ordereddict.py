from collections import OrderedDict
string = "pradeep"
# we can get the unique characters of a string using OrderedDict preserving the order.
print(''.join(OrderedDict.fromkeys(string).keys()))