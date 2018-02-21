a = [13, 20, 7, 4]

def inside_sum(number):
    # receive a number and return the sum between its individual numbers
    number_string = str(number)
    inside_sum = 0
    for n in number_string:
        inside_sum += int(n)
    return inside_sum

def digitalSumSort(a):

    sorted_numbers = []
    limit = len(a)
    while len(sorted_numbers) < limit:
        smallest = a[0]
        for i in range(len(a)):
            if inside_sum(smallest) > inside_sum(a[i]):
                smallest = a[i]
            elif inside_sum(smallest) == inside_sum(a[i]):
                if smallest <= a[i]:
                    smallest = a[i]
        sorted_numbers.append(smallest)
        a.remove(smallest)
    return sorted_numbers

digitalSumSort(a)