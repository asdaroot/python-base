d = {1 : "one", 1.01: "one dot zero one", "1" : "one str"}

for k, v in d.items(): # (1, "one"), (1.01, "one dot.."), ("1", "one_str")
    print(k, v)

for k in d:
    print(k, d[k])
print(d.items())