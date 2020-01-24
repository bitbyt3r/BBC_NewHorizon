import rasterio
from rasterio.transform import Affine

img = rasterio.open("color.tif")
angle = -85
res = 360/5928
transform = Affine.translation(0,angle) * Affine.scale(res, res)
new = rasterio.open(f"out_neg85.tif", "w", driver="GTiff", height=2963, width=5926, count=3, transform=transform, crs="+proj=latlong", dtype=img.read().dtype, nodata=None, interleave="pixel", compress="lzw")
new.write(img.read())
new.close()