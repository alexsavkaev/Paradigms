def numbers_share_declarative(arr):
    pos_cnt = len(list(filter(lambda x: x > 0, arr)))
    neg_cnt = len(list(filter(lambda x: x < 0, arr)))
    zero_cnt = len(list(filter(lambda x: x == 0, arr)))
    counts = [pos_cnt, neg_cnt, zero_cnt]
    shares = list(map(lambda x: x/len(arr), counts))
    return shares
print(numbers_share_declarative([0,0,1,1,1,-10,-9,-8]))