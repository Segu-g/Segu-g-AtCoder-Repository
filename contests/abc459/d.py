import heapq

ORD_A = ord("a")

def main():
    t = int(input())
    s_arr = tuple(input() for _ in range(t))
    outputs = []
    for s in s_arr:
        
        counts = [0 for _ in range(ord("z") - ord("a") + 1)]
        for c in s:
            counts[ord(c) - ORD_A] += 1
        
        heap = [(-count, chr(ORD_A + i)) for i, count in enumerate(counts)]
        heapq.heapify(heap)
        
        text = []
        prev_char = (0, " ")
        success = False
        for _ in range(len(s)):
            mcount, c = heapq.heapreplace(heap, prev_char)
            if mcount == 0:
                break
            text.append(c)
            prev_char = (mcount + 1, c)
        else:
            success = True

        if success:
            outputs.append("Yes")
            outputs.append("".join(text))
        else:
            outputs.append("No")

    print("\n".join(outputs))   

if __name__ == "__main__":
    main()
