import matplotlib.pyplot as plt
from src.utils.path_utils import OUTPUT_DIR

steps = [
    "Input Image",
    "Edge Detection",
    "ORB Features",
    "Feature Matching",
    "Optical Flow",
    "Visual Odometry"
]

fig, ax = plt.subplots(figsize=(12, 2.8))
ax.set_xlim(0, len(steps))
ax.set_ylim(0, 1)
ax.axis("off")

for i, step in enumerate(steps):
    x = i + 0.5
    rect = plt.Rectangle((x - 0.4, 0.35), 0.8, 0.3, fill=False, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, 0.5, step, ha="center", va="center", fontsize=11)
    if i < len(steps) - 1:
        ax.annotate(
            "",
            xy=(i + 1.1, 0.5),
            xytext=(i + 0.9, 0.5),
            arrowprops=dict(arrowstyle="->", linewidth=2)
        )

plt.tight_layout()
plt.savefig(str(OUTPUT_DIR / "pipeline_diagram.png"), dpi=200, bbox_inches="tight")
plt.show()