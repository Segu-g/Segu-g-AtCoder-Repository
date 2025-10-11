import numpy as np
t = int(input())

for _ in range(t):
    sx_t, sy_t, gx_t, gy_t = map(int, input().split())
    sx_a, sy_a, gx_a, gy_a = map(int, input().split())
    
    s_t = np.array((sx_t - sy_t))
    g_t = np.array((gx_t - gy_t))
    s_a = np.array((sx_a - sy_a))
    g_a = np.array((gx_a - gy_a))


    if np.sum(np.square(g_t - s_t)) < np.sum(np.square(g_a - s_a)):
        s_t, g_t, s_a, g_a = s_a, g_a, s_t, g_t
    
    direc_t = g_t - s_t
    norm_t = np.linalg.norm(direc_t)
    v_t = direc_t / norm_t if norm_t != 0 else direc_t

    direc_a = g_a - s_a
    norm_a = np.linalg.norm(direc_a)
    v_a = direc_a / norm_a if norm_a != 0 else direc_a

    s_r = s_a - s_t
    v_r = v_a - v_t

    

            

