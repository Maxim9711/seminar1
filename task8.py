n = int(3)
m = int(2)
k = int(4)
if ((k % n == 0) or (k % m == 0)) and (k < n * m) :
    print(f"Можно отломить {k} долек")
else:
    print(f"Нельзя отломить {k} долек")