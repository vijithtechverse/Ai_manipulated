from PIL import Image
from PIL.ExifTags import TAGS

def analyze_metadata(image):
    exif_data = image.getexif()
    suspicious = False
    reasons = []

    if not exif_data:
        suspicious = True
        reasons.append("No EXIF metadata found")

    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag in ["Software", "ProcessingSoftware"]:
            suspicious = True
            reasons.append(f"Edited using: {value}")

    return suspicious, reasons
