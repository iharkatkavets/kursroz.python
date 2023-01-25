
def select_item(items, date):
    sorted_items = sorted(items, key=lambda item: item.pub_date, reverse=True)
    for item in sorted_items:
        if item.pub_date.date() <= date.date(): 
            return item

    return None

