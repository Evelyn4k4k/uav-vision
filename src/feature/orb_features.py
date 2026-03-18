from src.utils.path_utils import IMAGE_DIR, OUTPUT_DIR
import cv2
import matplotlib.pyplot as plt

image = cv2.imread(str(IMAGE_DIR / "drone.jpg"))

if image is None:
    raise FileNotFoundError(f"Cannot find image: {IMAGE_DIR / 'drone.jpg'}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=500)
keypoints, descriptors = orb.detectAndCompute(gray, None)

output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    color=(0, 255, 0),
    flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
)

plt.figure(figsize=(10, 8))
plt.title(f"ORB Features: {len(keypoints)} keypoints")
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.savefig(str(OUTPUT_DIR / "orb_features_result.png"))
plt.show()