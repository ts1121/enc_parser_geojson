import os
import json
from enc_parser.geojson_exporter import GeoJSONExporter

def test_geojson_exporter():
    # Create dummy features
    sample_features = [
        {
            "geometry": {
                "type": "Point",
                "coordinates": [-70.0, 42.0]
            },
            "properties": {
                "name": "Test Buoy",
                "category": "Special Purpose"
            }
        },
        {
            "geometry": {
                "type": "Point",
                "coordinates": [-71.0, 43.0]
            },
            "properties": {
                "name": "Test Wreck",
                "depth": 25
            }
        }
    ]

    # Specify output path
    output_path = "data/output/test_output/test_output.geojson"

    # Export
    exporter = GeoJSONExporter(sample_features, output_path)
    exporter.export()

    # Load the written file and validate
    with open(output_path, "r") as f:
        data = json.load(f)

    assert data["type"] == "FeatureCollection"
    assert len(data["features"]) == 2
    assert data["features"][0]["geometry"]["type"] == "Point"
    assert data["features"][1]["properties"]["name"] == "Test Wreck"

    print("GeoJSONExporter test passed successfully.")


test_geojson_exporter()
