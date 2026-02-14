from collections import deque

def main():
    n = int(input())
    a_arr = list(map(int, input().split()))
    a_arr.sort()

    l_arr = []
    
    # 折れてないやつが存在するとき
    a_arr_l1 = a_arr.copy()
    l1 = a_arr_l1.pop()
    l1_is_valid = True
    while a_arr_l1 and a_arr_l1[-1] == l1:
        a_arr_l1.pop()
    if len(a_arr_l1) % 2 != 0:
        l1_is_valid = False
    for i in range(len(a_arr_l1)//2):
        if a_arr_l1[i] + a_arr_l1[-1-i] != l1:
            l1_is_valid = False
            break
    if l1_is_valid:
        l_arr.append(l1)

    # 折れてないやつが存在しないとき
    a_arr_l2 = a_arr
    l2 = a_arr_l2[0] + a_arr_l2[-1]
    l2_is_valid = True
    if len(a_arr_l2) % 2 != 0:
        l2_is_valid = False
    for i in range(len(a_arr_l2)//2):
        if a_arr_l2[i] + a_arr_l2[-1-i]!= l2:
            l2_is_valid = False
            break
    if l2_is_valid:
        l_arr.append(l2)

    l_arr.sort()
    print(" ".join(map(str, l_arr)))


if __name__ == "__main__":
    main()
