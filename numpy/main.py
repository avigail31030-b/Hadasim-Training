from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("RGB")
arr = np.array(img)

print("Image shape:", arr.shape)

r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]

print("Red channel shape:", r.shape)
print("Green channel shape:", g.shape)
print("Blue channel shape:", b.shape)

r_flat = r.ravel()
g_flat = g.ravel()
b_flat = b.ravel()

r_hist = np.bincount(r_flat, minlength=256)
g_hist = np.bincount(g_flat, minlength=256)
b_hist = np.bincount(b_flat, minlength=256)

x = np.arange(256)

plt.figure()
plt.title("RGB Histogram")
plt.plot(x, r_hist, label = "Red")
plt.plot(x, g_hist, label = "Green")
plt.plot(x, b_hist, label = "Blue")

plt.xlabel("Color value (0-256)")
plt.ylabel("Pixel count")
plt.legend()

plt.show()
