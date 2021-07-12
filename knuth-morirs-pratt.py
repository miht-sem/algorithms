# t = 'лилила'
#
# p = [0] * len(t)
# j = 0
# i = 1
# while i < len(t):
#     if t[j] == t[i]:
#         p[i] = j + 1
#         i += 1
#         j += 1
#     else:
#         if j == 0:
#             p[i] = 0
#             i += 1
#         else:
#             j = p[j - 1]
#
# print(p)
#
# a = 'лилилось лилилась'
# m = len(t)
# n = len(a)
#
# i = 0
# j = 0
#
# while i < n:
#     if a[i] == t[j]:
#         i += 1
#         j += 1
#         if j == m:
#             print('Nice')
#             break
#     else:
#         if j > 0:
#             j = p[j - 1]
#         else:
#             i += 1
#
# if i == n and j != m:
#     print('Bad')


whatToFind = 'лилила'
masPrefix = [0] * len(whatToFind)

i = 0
j = 1

while j < len(whatToFind):
    if whatToFind[i] == whatToFind[j]:
        masPrefix[j] = i + 1
        i += 1
        j += 1
    else:
        if i == 0:
            masPrefix[j] = 0
            j += 1
        else:
            i = masPrefix[i-1]

print(masPrefix)

whereToFind = 'лилилось лилилась'

n = len(whereToFind)
m = len(whatToFind)

i = 0
j = 0

while i < n:
    if whereToFind[i] == whatToFind[j]:
        i += 1
        j += 1
        if j == m:
            print('Nice')
            break
    else:
        if j > 0:
            j = masPrefix[j - 1]
        else:
            i += 1

if i == n and j != m:
    print('Bad')