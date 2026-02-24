def simple_sort(cards):
    """
    Docstring for simple_sort
    
    :param cards: It will take a list as an argument and sort the list in a ascending orders
    """
    sorted_cards = []
    while cards:
        lowest_cards = min(cards)
        sorted_cards.append(lowest_cards)
        cards.remove(lowest_cards)
    return sorted_cards

cards_list = [5,1,9,20,8,10,15,18]
sort_function = simple_sort(cards_list)
print(sort_function)