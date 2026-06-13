import numpy as np
import math

def main():
    for l in range(1, 15):
        s = "a"*l
        left_patterns = np.array([
            [math.comb(i, k) for k in range(len(s))]
            for i in range(len(s))
        ])
        right_patterns = np.array([
            [math.comb(len(s)-1-i, k) for k in range(len(s))]
            for i in range(len(s))
        ])
        print(np.sum(left_patterns * right_patterns, axis=1))

if __name__ == "__main__":
    main()
