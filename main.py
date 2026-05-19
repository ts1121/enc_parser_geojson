from enc_parser.enc_directory import ENCDirectory
from enc_parser.enc_file import ENCFile
from enc_parser.layer_extractor import LayerExtractor
from enc_parser.geojson_exporter import GeoJSONExporter

import os
import argparse


# === DEFAULT CONFIGURATION ===
DEFAULT_INPUT_DIRECTORIES = [
    "data/raw/Case_1_NY_BlockIslandNorth",
    "data/raw/Case_2_NY_BlockIslandSouth",
    "data/raw/Case_3_NY_LongIslandSound"
]

DEFAULT_TARGET_LAYER = "all"
DEFAULT_FEATURE_FILTER = None
DEFAULT_VERBOSE = True
DEFAULT_OUTPUT_ROOT = "data/output"


def process_directory(
    input_directory,
    output_root,
    target_layer="all",
    feature_filter=None,
    verbose=True
):
    """
    Process all ENC files in a directory and export GeoJSON outputs.
    """

    # Create output directory based on input directory name
    output_directory = os.path.join(
        output_root,
        os.path.basename(input_directory)
    )

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
            # === Step 2: Open ENC file ===
            enc = ENCFile(enc_file_path, verbose=verbose)
            enc.open()

            features_all = []

            filename_stub = os.path.splitext(
                os.path.basename(enc_file_path)
            )[0]

            # === Step 3: Determine layers ===
            if target_layer == "all":
                layer_names = enc.list_layers()
            else:
                layer_names = [target_layer]

            # === Step 4: Extract features from layers ===
            for layer_name in layer_names:

                try:
                    layer = enc.get_layer(layer_name)

                    extractor = LayerExtractor(layer)

                    features = extractor.extract_features(
                        feature_filter
                    )

                    features_all.extend(features)

                    if verbose:
                        print(
                            f"Extracted {len(features)} features "
                            f"from layer '{layer_name}'"
                        )

                except Exception as e:
                    print(
                        f"Could not process layer "
                        f"'{layer_name}': {e}"
                    )

            # === Step 5: Export GeoJSON ===
            if features_all:

                os.makedirs(output_directory, exist_ok=True)

                output_path = os.path.join(
                    output_directory,
                    f"{filename_stub}_{target_layer}.geojson"
                )

                exporter = GeoJSONExporter(
                    features_all,
                    output_path
                )

                exporter.export()

                print(f"Exported to: {output_path}")

            else:
                print("No features extracted.")

        except Exception as e:
            print(f"Failed to process {enc_file_path}: {e}")


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Parse S-57 ENC files and export GeoJSON."
    )

    parser.add_argument(
        "--input",
        nargs="+",
        help=(
            "One or more input directories "
            "containing ENC files."
        )
    )

    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_ROOT,
        help=(
            "Root output directory. "
            f"Default: {DEFAULT_OUTPUT_ROOT}"
        )
    )

    parser.add_argument(
        "--layer",
        default=DEFAULT_TARGET_LAYER,
        help=(
            "Target ENC layer to extract. "
            "Use 'all' for all layers."
        )
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Disable verbose console output."
    )

    return parser.parse_args()


def main():

    args = parse_arguments()

    # Use CLI input if provided,
    # otherwise fall back to defaults
    input_directory_list = (
        args.input
        if args.input
        else DEFAULT_INPUT_DIRECTORIES
    )

    verbose = not args.quiet

    for input_directory in input_directory_list:

        process_directory(
            input_directory=input_directory,
            output_root=args.output,
            target_layer=args.layer,
            feature_filter=DEFAULT_FEATURE_FILTER,
            verbose=verbose
        )


if __name__ == "__main__":
    main()
