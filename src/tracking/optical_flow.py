from src.utils.path_utils import IMAGE_DIR, OUTPUT_DIR
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread(str(IMAGE_DIR / "drone.jpg"))
img2 = cv2.imread(str(IMAGE_DIR / "drone2.jpg"))

if img1 is None:
    raise FileNotFoundError(f"Cannot find image: {IMAGE_DIR / 'drone.jpg'}")

if img2 is None:
    raise FileNotFoundError(f"Cannot find image: {IMAGE_DIR / 'drone2.jpg'}")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

p0 = cv2.goodFeaturesToTrack(
    gray1,
    maxCorners=100,
    qualityLevel=0.3,
    minDistance=7,
    blockSize=7
)

p1, st, err = cv2.calcOpticalFlowPyrLK(gray1, gray2, p0, None)

good_new = p1[st == 1]
good_old = p0[st == 1]

mask = np.zeros_like(img2)

for new, old in zip(good_new, good_old):
    a, b = new.ravel().astype(int)
    c, d = old.ravel().astype(int)
    cv2.line(mask, (c, d), (a, b), (0, 255, 0), 2)
    cv2.circle(img2, (a, b), 4, (0, 0, 255), -1)

result = cv2.add(img2, mask)

plt.figure(figsize=(10, 8))
plt.title("Optical Flow Tracking")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.savefig(str(OUTPUT_DIR / "optical_flow_result.png"))
plt.show()