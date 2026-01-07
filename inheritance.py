class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)}")


custom_list = ExtendedList([1,3,4])
print(custom_list)
custom_list.print_list_info()