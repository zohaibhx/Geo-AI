import rasterio
import numpy as np
import os
from processor import calculate_ndvi

def run_real_raster_workflow(red_path, nir_path, output_path):
    """
    Execution-ready pipeline for processing real satellite imagery.
    """
    print(f"🚀 Loading Real Data: {os.path.basename(red_path)}")
    
    with rasterio.open(red_path) as red_src:
        red_band = red_src.read(1).astype('float32')
        # We copy the metadata (CRS, transform) to ensure the output is georeferenced
        meta = red_src.meta 

    with rasterio.open(nir_path) as nir_src:
        nir_band = nir_src.read(1).astype('float32')

    # Run the core logic we built
    print("🧪 Calculating NDVI...")
    ndvi = calculate_ndvi(red_band, nir_band)

    # Update metadata for the output file
    # NDVI is a float between -1 and 1
    meta.update(dtype=rasterio.float32, count=1, driver='GTiff')

    with rasterio.open(output_path, 'w', **meta) as dst:
        dst.write(ndvi.astype(rasterio.float32), 1)
    
    print(f"✅ Success! Raster saved to: {output_path}")

# TO RUN: Replace these with your actual downloaded file paths
run_real_raster_workflow(r"C:\Users\user\Downloads\S2A_MSIL2A_20260513T063321_N0512_R077_T40QGL_20260513T112322.SAFE\S2A_MSIL2A_20260513T063321_N0512_R077_T40QGL_20260513T112322.SAFE\GRANULE\L2A_T40QGL_A056874_20260513T063934\IMG_DATA\R10m\T40QGL_20260513T063321_B04_10m.jp2",
                          r"C:\Users\user\Downloads\S2A_MSIL2A_20260513T063321_N0512_R077_T40QGL_20260513T112322.SAFE\S2A_MSIL2A_20260513T063321_N0512_R077_T40QGL_20260513T112322.SAFE\GRANULE\L2A_T40QGL_A056874_20260513T063934\IMG_DATA\R10m\T40QGL_20260513T063321_B08_10m.jp2", 
                          'output.tif')