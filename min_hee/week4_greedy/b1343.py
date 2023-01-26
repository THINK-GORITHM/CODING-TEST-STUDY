# 백준 1343 폴리오미노

poly = input().rstrip()

# 1. AAAA로 replace
# 2. BB로 replace
# 3. X가 남아있으면 -1 출력

poly = poly.replace("XXXX", "AAAA")
poly = poly.replace("XX", "BB")

print(poly if poly.count("X")==0 else -1)