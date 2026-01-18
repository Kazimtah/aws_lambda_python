def quick_sort(cards):
    """
    Docstring for quick_sort
    
    :param cards: As an argument it will take a list and sorte in a scending orders. In a quick sorted  algorithum we choose a pivote from our list and then we divide the list into sub list of greater and less . and then we joint it through the truncate of list at the end of list
    """
    if len(cards) < 2:
        return cards
    else:
        pivot = cards[0]
        less = [i for i in cards[1:] if i <= pivot] 
        greater = [i for i in cards[1:] if i > pivot]
        return quick_sort(less) + [pivot]+ quick_sort(greater)

card_list = [25,17,12,0,14,1,2,8,6,7,25,17,48]
quick_sort1 = quick_sort(card_list)
print(quick_sort1)