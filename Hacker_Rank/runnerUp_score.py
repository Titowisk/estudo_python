# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


arr = map(int, "2 3 6 6 5".split())
arr = list(arr)

def max_score(array):
    biggest_score = ""
    for s in array:
        if not biggest_score:
            biggest_score = s
            
        if s >= biggest_score:
            biggest_score = s
    return biggest_score

biggest_score = max_score(arr)
while True:    
    if biggest_score in arr:
        arr.remove(biggest_score)
    else:
        break
if arr:
    runner_up = max_score(arr)
    print(runner_up)