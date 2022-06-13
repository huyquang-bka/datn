lp_list = ["123", "123", "456"]
lp_most_dict = {}
lp_set = set(lp_list)
for lp in lp_set:
    lp_most_dict[lp_list.count(lp)] = lp
lp_final = lp_most_dict[max(lp_most_dict.keys())]
print(lp_final)