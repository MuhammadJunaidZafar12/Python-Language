from operator import index

# marks = [12, 56, 32, 98, 12, 45, 1, 4]
#
# iNdex = 0
# for mark in marks:
#     print(mark)
#     if iNdex == 3:
#         print("Junaid, awesome")
#     iNdex =iNdex+1


marks = [12, 56, 32, 98, 12, 45, 1, 4]


for Index, mark in enumerate(marks, start=1):
    print(mark)
    if Index == 3:
        print("Junaid, awesome")
