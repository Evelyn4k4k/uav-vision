from src.utils.path_utils import IMAGE_DIR, OUTPUT_DIR
import cv2
import matplotlib.pyplot as plt

image = cv2.imread(str(IMAGE_DIR / "drone.jpg"))

if image is None:
    raise FileNotFoundError(f"Cannot find image: {IMAGE_DIR / 'drone.jpg'}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Gray")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.savefig(str(OUTPUT_DIR / "edge_detection_result.png"))
plt.show()