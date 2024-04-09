# EarthAI System Architecture

Welcome to the EarthAI System Architecture repository. This repository contains the codebase for a cutting-edge system designed to process and analyze AIRS data using the Prithvi model, a foundation model for generalist geospatial artificial intelligence. Inspired by the principles from the ORCA project, our architecture is crafted to enhance the efficiency and scalability of distributed computing environments.

## Introduction

EarthAI System Architecture integrates dynamic scheduling and selective batching to process Atmospheric Infrared Sounder (AIRS) data effectively. AIRS data, known for its detailed atmospheric temperature and humidity information, when paired with the Prithvi model's advanced capabilities, offers unparalleled potential in climate and sustainability applications.

## Repository Structure

- `config/` - Configuration settings for system deployment and environment setup.
- `docs/` - Documentation detailing system design, technology selection, and operational guidelines.
- `scripts/` - Utility scripts to support data management tasks.
- `src/` - Source code of the system, including data processing and model serving components.
- `tests/` - Test suites to verify the system's functionality and performance.

## Getting Started

1. Clone the repository and navigate to its directory:

```bash
git clone https://github.com/rabiakonuk/EarthAI.git
cd EarthAI-System-Architecture
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```
## Configuring the System

Edit files within the "config/" directory to customize the system according to your deployment environment.

## Usage

1. Execute the data processing pipeline with:
```bash
python src/data_processing/pipeline.py
```

2. Launch the model serving server using:
```bash
python src/model_serving/server.py
```

3. Verify system stability and correctness (testing):
```bash
python -m unittest discover -s tests
```