# Geo-AI
# GeoAI Wildfire Risk & Scalability Engine
A production-level Raster Workflow engine built to automate vegetation health analysis using Sentinel-2 satellite imagery. This project focuses on **Software Engineering best practices**, **Reliability**, and **Cloud Scalability**.

## 🚀 Key Features
- **Vectorized Raster Processing:** High-performance NDVI calculations using NumPy and Rasterio.
- **Production-Grade Stability:** Built-in protection against edge cases like division-by-zero and null pixel values.
- **Automated Quality Assurance:** Multi-stage CI/CD pipeline (GitHub Actions) for linting and unit testing.
- **Containerized Deployment:** Fully Dockerized environment ensuring cross-platform compatibility and zero-dependency setup.

## 🛠 Tech Stack
- **Languages:** Python 3.11
- **Geospatial:** Rasterio, NumPy, GDAL
- **Engineering:** Docker, Pytest, GitHub Actions, Flake8

## 📂 Project Structure
- `/src`: Core logic for raster processing.
- `/tests`: Unit and Scalability test suites.
- `/data`: Sentinel-2 satellite granules (Bands 4 & 8).
- `Dockerfile`: Container configuration.
- `.github/workflows`: CI/CD automation instructions.

## 🚦 Getting Started
### Using Docker (Recommended)
1. Build the image:
   `docker build -t esri-engine .`
2. Run the processing engine:
   `docker run -v "${PWD}:/app" esri-engine`

### Local Setup
1. Create venv: `python -m venv .venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
