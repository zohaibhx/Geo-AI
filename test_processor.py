import numpy as np
from processor import calculate_ndvi

def test_ndvi_logic():
    # Create mock raster data (2x2 pixels)
    # NIR (high value = healthy plants), Red (low value)
    mock_red = np.array([[0.1, 0.2], [0.1, 0.1]])
    mock_nir = np.array([[0.8, 0.7], [0.9, 0.9]])
    
    result = calculate_ndvi(mock_red, mock_nir)
    
    # 1. Test Range: NDVI must be between -1 and 1
    assert np.all(result <= 1.0)
    assert np.all(result >= -1.0)
    
    # 2. Test Expected Value: (0.8-0.1)/(0.8+0.1) = ~0.77
    assert round(result[0,0], 2) == 0.78

print("✅ Unit Test Script Ready")