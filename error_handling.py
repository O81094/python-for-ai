# Wrong - same list for all calls!
def add_item(item, items=[]):
    items.append(item)
    return items

# Right - create new list each time
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Example usage
add_item('apple')  # ['apple']
add_item('banana') # ['banana']
add_item('orange') # ['orange']

fruits = add_item('apple')
fruits = add_item('banana')
fruits = add_item('orange', fruits)