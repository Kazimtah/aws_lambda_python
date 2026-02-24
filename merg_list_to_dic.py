def change_two_lists_to_one_dict(list1,list2):
    """
    Docstring for change_two_lists_to_one_dict
    This function takes two seperate list and convert it to one dictionary 
    :param list1: list[]
    :param list2: list[]
    """
    # the following function will sue zip method to convert two #given list into Dict
    list_to_dict = dict(zip(list1,list2))
    return list_to_dict
    

list4= ["Jhone", "Softwaredeveloper", 25]
list3 = ["Name","Job","age"]

print(change_two_lists_to_one_dict(list3,list4))