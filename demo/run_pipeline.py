import os

print("Running edge detection...")
os.system("python -m src.detection.edge_detection")

print("Running ORB feature extraction...")
os.system("python -m src.feature.orb_features")

print("Running feature matching...")
os.system("python -m src.matching.feature_matching")

print("Running optical flow tracking...")
os.system("python -m src.tracking.optical_flow")

print("Running mini visual odometry...")
os.system("python -m src.vo.mini_visual_odometry")

print("Pipeline finished.")