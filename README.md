# ENC Parser GeoJSON

**ENC Parser GeoJSON** is a Python package for parsing
**S-57 Electronic Navigational Chart (ENC)** files and exporting
selected layers and features as **GeoJSON**.

The project is designed for:

- Marine spatial applications
- ENC preprocessing pipelines
- Geospatial machine learning workflows
- Semantic feature extraction from S-57 data

---

# Features

- Parse S-57 ENC `.000` files using GDAL/OGR
- Automatically discover ENC files in directories
- Extract ENC layers and features with metadata
- Export extracted features to GeoJSON
- Modular architecture for reuse and extension
- Command-line configurable workflow

---

# Repository Structure

```text
enc_parser_geojson/
│
├── enc_parser/
│   ├── enc_directory.py
│   ├── enc_file.py
│   ├── layer_extractor.py
│   └── geojson_exporter.py
│
├── data/
│   ├── raw/
│   └── output/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ts1121/enc_parser_geojson.git
cd enc_parser_geojson
```

---

## 2. Install Dependencies

### Option A — Install from requirements.txt

```bash
pip install -r requirements.txt
```

### Option B — Install as a package

```bash
pip install .
```

---

# Running the Parser

## Default Batch Processing

Runs the parser using the default hardcoded ENC directories:

```bash
python main.py
```

---

## Process a Specific ENC Directory

```bash
python main.py --input data/raw/Case_1_NY_BlockIslandNorth
```

---

## Process Multiple ENC Directories

```bash
python main.py --input \
data/raw/Case_1_NY_BlockIslandNorth \
data/raw/Case_2_NY_BlockIslandSouth
```

---

## Extract a Specific Layer

Example using the `DEPARE` layer:

```bash
python main.py \
--input data/raw/Case_1_NY_BlockIslandNorth \
--layer DEPARE
```

---

## Specify Output Directory

```bash
python main.py \
--input data/raw/Case_1_NY_BlockIslandNorth \
--output data/custom_output
```

---

# Output

GeoJSON outputs are exported to:

```text
data/output/<input_directory_name>/
```

Example:

```text
data/output/Case_1_NY_BlockIslandNorth/
```

---

# Dependencies

Main dependencies include:

- GDAL / OGR
- Python 3.12+
- argparse

---

# Future Development

Planned future capabilities include:

- Semantic grounding of S-57 attributes
- Ontology mapping
- Spatio-semantic feature grouping
- Graph-based ENC representations
- Integration with LLM workflows
- Validation and QA pipelines

---

# License

MIT License
