import numpy as np

def calculate_ndvi(red_channel, nir_channel):
    """
    Calculates the Normalized Difference Vegetation Index.
    This is a standard Raster workflow used at Esri.
    """
    # Convert to float for math
    red = red_channel.astype(float)
    nir = nir_channel.astype(float)
    
    # Formula: (NIR - Red) / (NIR + Red)
    denominator = nir + red
    
    # Product Engineering: Handle division by zero (crucial for stability)
    denominator[denominator == 0] = 1e-9
    
    ndvi = (nir - red) / denominator
    return ndvi