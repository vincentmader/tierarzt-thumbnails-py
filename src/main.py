import os
from pathlib import Path

import PIL
from PIL import Image

# Loop over all "Quartal" directories.
path_to_gallery = Path("../../../static/gallery/")
for entry in sorted(os.listdir(path_to_gallery)):
    path_to_quarter = Path(path_to_gallery, entry)

    # Consider only directories that start with "Images_"
    if not entry.startswith("Images_"):
        continue
    if not os.path.isdir(path_to_quarter):
        continue

    # Loop over all images in "Quartal" directory.
    print(f"{entry}")
    for entry in sorted(os.listdir(path_to_quarter)):
        if entry in [".DS_Store", "thumbnails"]:
            continue
        path_to_image = Path(path_to_quarter, entry)

        # Determine path to newly-created thumbnail file.
        split = entry.split('.')
        filename, ext = '.'.join(split[:-1]), split[-1]
        path_to_thumbnail = Path(path_to_quarter, "thumbnails", f"{filename}_100.jpg")

        # Save thumbnail if and only if file does not exist already.
        if os.path.exists(path_to_thumbnail):
            continue
        try:
            img = Image.open(path_to_image)
            img.thumbnail((100, 100)) #, Image.ANTIALIAS)
            img.save(path_to_thumbnail)
        except Exception:
            print(f"\t\tError:\t{entry}")
            continue
        print(f"\t\t\t{entry}")

        # Ask user for confirmation before writing thumbnail file.
        # input(f"{path_to_image} -> {path_to_thumbnail}")
