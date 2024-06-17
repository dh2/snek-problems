# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#  Sort the list
#  Skip all values that are greater than or equal to the k value
#  Starting with the largest elligible number, attempt to add it to all other available numbers from the back forward
#def_list = [20,100,6,6,5,1, 15, 3, 7]
def GetData():
    input_list = []
    data_value = ''
    def loop_input():
        nonlocal data_value
        nonlocal input_list
        while data_value is not None or len(input_list) < 2:
            data_value = input('Enter values [%s]: ' % len(input_list))
            if len(data_value) > 0:
                input_list.append(int(data_value))
                print("Current Values: %s" % input_list)
            else:
                data_value = None

    print("Enter values to build the list.")
    print("Values must be numeric and greater than or equal to zero (0)")
    print("You must enter at least two values")
    print("Enter a blank line to finish input")
    print("-------------------------------------------------------------------")

    try:
        loop_input()
    except ValueError as e:
        print('%s is not a valid input:' % data_value)
        data_value = ''
        loop_input()

    return input_list

def GetValue():
    value = 0

    while int(value) <= 0:
        value = input('Enter desired value: ')

    return int(value)

def DoMath(data, k: int):
    list_s = sorted(data, reverse=True)
    found = False
    for item in list_s:
        if item >= k:
            continue
        last = -1
        sum = 0
        
        while sum < k:
            num = list_s[last]
            sum = item +  num
            print("Item({0}): num: {1} | sum: {2}".format(item, num, sum))
            if sum == k:
                print("Found: {0} + {1} = {2}".format(item, num, k))
                found = True
                break
            else:
                last = last - 1
        
        if found:
            break

    if not found:
        print("I dunno")

list_data = GetData()
k_val = GetValue()
DoMath(list_data, k_val)