student = (
    ("s001","王玲",87,55,75),
    ("s002","玲解耦",87,55,75),
    ("s003","王三",87,45,75),
    ("s004","王玲啊",87,55,75),
    ("s005","金的",82,55,45),
    ("s006","王df玲",81,55,75),
    ("s007","王fe玲",97,65,75),
    ("s008","王分时玲",47,55,75),
    ("s009","王额玲",67,55,75),
    ("s010","王额玲",67,25,75),
    ("s011","去的玲",77,55,75),
)


for s in student:
    total = s[2]+s[3]+s[4]
    avg = total/3
    print(f"{total} {avg:.1f}")

china_scroe = [s[2] for s in student]
math_scroe = [s[3] for s in student]
english_scroe = [s[4] for s in student]
print(min(china_scroe))

