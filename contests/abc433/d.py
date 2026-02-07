import bisect

def main():
    n, m = map(int, input().split())
    a_arr = tuple(map(int, input().split()))

    digit_a_matrix = [[] for _ in range(11)]
    for a in a_arr:
        digit = len(str(a))
        digit_a_matrix[digit].append(a)

    count = 0
    for digit in range(11):
        digit_a_arr = digit_a_matrix[digit]
        digit_a_arr.sort()
        
        modulation_factor =  pow(10, digit, m)
        modulated_a_arr = [(a * modulation_factor) % m for a in a_arr]
        modulated_a_arr.sort()

        for a in digit_a_arr:
            neg_a = (m - a) % m
            count += bisect.bisect_right(modulated_a_arr, neg_a) - bisect.bisect_left(modulated_a_arr, neg_a)
    
    print(count)

            

    

if __name__ == "__main__":
    main()
