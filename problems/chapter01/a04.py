# from typing import Tuple
N = int(input())
s = ""
for i in range(10):
    wari = (1 << i)
    s = str((N // wari) % 2) + s
print(s)


# def hex_to_bin(x: int, s: str) -> Tuple[int, str]:
#     if x == 0:
#         if len(s) < 10:
#             return x, str(x % 2) + s
#         else:
#             return x, s
    
#     return hex_to_bin(x // 2, str(x % 2) + s)

# print(hex_to_bin(N, "")[1].zfill(10))