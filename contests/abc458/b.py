import numpy as np

def main():
    h, w = map(int, input().split())
    count = np.zeros((h, w), dtype=np.int32)
    count[1:,:] += 1
    count[:-1,:] += 1
    count[:,1:] += 1
    count[:,:-1] += 1
    matrix = count.tolist()
    print("\n".join(map(lambda arr: " ".join(map(str, arr)), matrix)))

if __name__ == "__main__":
    main()
