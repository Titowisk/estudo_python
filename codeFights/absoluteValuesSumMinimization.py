a = [0, 7, 9]

def absoluteValuesSumMinimization(a):
    # test all absoluteValueSums using each x possible
    
    smallest_av_sum = False
    for x in a:
        av_sum = 0
        for i in range(len(a)):
            av_sum += abs(a[i] - x) # x = 2
            
        if smallest_av_sum:
            if av_sum <= smallest_av_sum:
                best_x = x
        else:
            smallest_av_sum = av_sum
            best_x = x
    
    return best_x

absoluteValuesSumMinimization(a)