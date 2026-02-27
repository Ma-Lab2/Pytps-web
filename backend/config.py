"""
config.py - Environment variable configuration.
"""

import os

IMAGE_DIR = os.environ.get("PYTPS_IMAGE_DIR", "/data/images")
OUTPUT_DIR = os.environ.get("PYTPS_OUTPUT_DIR", "/data/output")
WORKERS = int(os.environ.get("PYTPS_WORKERS", "4"))
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SESSION_MAX_AGE = int(os.environ.get("PYTPS_SESSION_MAX_AGE", "3600"))
