from src.utils.path_utils import IMAGE_DIR, OUTPUT_DIR
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(str(IMAGE_DIR / "drone.jpg"))
img2 = cv2.imread(str(IMAGE_DIR / "drone2.jpg"))

if img1 is None:
    raise FileNotFoundError(f"Cannot find image: {IMAGE_DIR / 'drone.jpg'}")

if img2 is None:
    raise FileNotFoundError(f"Cannot find image: {IMAGE_DIR / 'drone2.jpg'}")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=500)
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

print(f"Total matches: {len(matches)}")

matched_img = cv2.drawMatches(
    img1, kp1, img2, kp2, matches[:50], None,
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.figure(figsize=(16, 8))
plt.title(f"Feature Matches: {len(matches[:50])}")
plt.imshow(cv2.cvtColor(matched_img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.savefig(str(OUTPUT_DIR / "feature_matching_result.png"))
plt.show()
