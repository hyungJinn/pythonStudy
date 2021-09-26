s = input()
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatian:
    s = s.replace(i, "#")

print(len(s))