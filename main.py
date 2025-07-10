from enc_parser.enc_directory import ENCDirectory
from enc_parser.enc_file import ENCFile
from enc_parser.layer_extractor import LayerExtractor
from enc_parser.geojson_exporter import GeoJSONExporter

import os

def main():
    # === CONFIGURATION ===
    input_directory_list = ["data/raw/Case_1_NY_BlockIslandNorth",
                            "data/raw/Case_2_NY_BlockIslandSouth","data/raw/Case_3_NY_LongIslandSound"]  #List of directory names containing ENC files
    target_layer = "all"  # Use "all" to extract from all layers
    feature_filter = None    # Optional: ["CATSPM", "COLOUR"]
    verbose = True

    for input_directory in input_directory_list:
        #Set output directory based on input directory
        # This will create a new output directory under 'data/output' with the same name as the input directory
        output_directory = os.path.join("data/output", os.path.basename(input_directory))
        print(f"\nProcessing directory: {input_directory}")
        print(f"Output will be saved to: {output_directory}")
        
        # === Step 1: Find ENC files in directory ===
        directory = ENCDirectory(input_directory)
        enc_files = directory.find_enc_files()

        if not enc_files:
            print("No ENC files found in the directory.")
            return

        print(f"\nFound {len(enc_files)} ENC file(s).")

        for enc_file_path in enc_files:
            print(f"\nProcessing: {enc_file_path}")
            try:
                # Step 2: Open the ENC file
                enc = ENCFile(enc_file_path, verbose=verbose)
                enc.open()

                features_all = []
                filename_stub = os.path.splitext(os.path.basename(enc_file_path))[0]

                # Step 3: Loop over desired layers
                if target_layer == "all":
                    layer_names = enc.list_layers()
                else:
                    layer_names = [target_layer]

                for layer_name in layer_names:
                    try:
                        layer = enc.get_layer(layer_name)
                        extractor = LayerExtractor(layer)
                        features = extractor.extract_features(feature_filter)

                        features_all.extend(features)
                        if verbose:
                            print(f"Extracted {len(features)} features from layer '{layer_name}'")
                    except Exception as e:
                        print(f"Could not process layer '{layer_name}': {e}")

                # Step 4: Export to GeoJSON
                if features_all:
                    os.makedirs(output_directory, exist_ok=True)
                    output_path = os.path.join(output_directory, f"{filename_stub}_{target_layer}.geojson")
                    exporter = GeoJSONExporter(features_all, output_path)
                    exporter.export()
                    print(f"Exported to: {output_path}")
                else:
                    print("No features extracted.")

            except Exception as e:
                print(f"Failed to process {enc_file_path}: {e}")

if __name__ == "__main__":
    main()
