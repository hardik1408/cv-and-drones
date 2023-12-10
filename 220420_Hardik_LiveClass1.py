import numpy as np
import cv2
import matplotlib.pyplot as plt

def solve(s):
    img = cv2.imread(s, 0)
    M, N = img.shape
    foo = np.zeros((M, N), dtype=np.complex128) 

    for u in range(M):
        for v in range(N):
            sum_val = 0
            for x in range(M):
                for y in range(N):
                    sum_val += img[x, y] * np.exp(-1j * 2 * np.pi * ((u * x / M) + (v * y / N)))

            foo[u, v] = sum_val

    plt.figure(figsize=(12, 6))
    plt.subplot(122), plt.imshow(foo, cmap='gray')
    plt.title('Fourier Transform'), plt.axis('off')

    plt.show()


