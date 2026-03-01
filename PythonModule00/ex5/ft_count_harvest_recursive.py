def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(1, days)


def helper(current, total):
    if current > total:
        print("Harvest time!")
        return
    print("Day", current)
    helper(current + 1, total)
