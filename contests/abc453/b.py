def main():
    t, x = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    
    last_saved_time = 0
    last_saved_a = a_arr[0]
    results = [(last_saved_time, last_saved_a)]
    for i, a in zip(range(1, t+1), a_arr[1:]):
        if abs(last_saved_a - a) >= x:
            last_saved_time = i
            last_saved_a = a
            results.append((last_saved_time, last_saved_a))
    print("\n".join(map(lambda saved: f"{saved[0]} {saved[1]}", results)))


if __name__ == "__main__":
    main()
