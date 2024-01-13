def numbers_share(arr):
    pos_cnt, neg_cnt, zero_cnt = 0,0,0
    for el in arr:
        if el > 0: pos_cnt += 1
        elif el < 0: neg_cnt += 1
        else: zero_cnt += 1
    pos_shr, neg_shr, zero_shr = pos_cnt/len(arr), neg_cnt/len(arr), zero_cnt/len(arr)
    return pos_shr, neg_shr, zero_shr
print(numbers_share([0,0,1,1,1,-10,-9,-8]))