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

# ORB features
orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Feature matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Simplified camera intrinsics
h, w = gray1.shape
focal = 800
cx, cy = w / 2, h / 2

K = np.array([
    [focal, 0, cx],
    [0, focal, cy],
    [0, 0, 1]
])

E, mask = cv2.findEssentialMat(
    pts1, pts2, K,
    method=cv2.RANSAC,
    prob=0.999,
    threshold=1.0
)

if E is None:
    print("Essential matrix estimation failed.")
    raise SystemExit

_, R, t, mask_pose = cv2.recoverPose(E, pts1, pts2, K)

print("Estimated Rotation R:")
print(R)

print("\nEstimated Translation t:")
print(t)

print(f"\nNumber of matches: {len(matches)}")

# ----------------------------
# Simple trajectory visualization
# ----------------------------
# Frame 1 at origin
p0 = np.array([0.0, 0.0, 0.0])

# Frame 2 uses recovered translation direction
p1 = t.flatten()

# Build a tiny 2-point trajectory
xs = [p0[0], p1[0]]
ys = [p0[2], p1[2]]   # use x-z plane for visualization

plt.figure(figsize=(6, 6))
plt.plot(xs, ys, marker="o", linewidth=2)
plt.scatter(xs[0], ys[0], s=80, label="Frame 1")
plt.scatter(xs[1], ys[1], s=80, label="Frame 2")

plt.text(xs[0], ys[0], " Start", fontsize=10)
plt.text(xs[1], ys[1], " End", fontsize=10)

plt.title("Mini Visual Odometry Trajectory")
plt.xlabel("X")
plt.ylabel("Z")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.tight_layout()
plt.savefig(str(OUTPUT_DIR / "trajectory_result.png"))
plt.show()