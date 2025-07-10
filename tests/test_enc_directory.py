import os
from enc_parser.enc_directory import ENCDirectory

def test_enc_directory():
    # Step 1: Define path to the ENC folder
    enc_root = "data/raw/test_input"  # Your directory with ENC files

    # Step 2: Initialize the ENCDirectory class
    directory = ENCDirectory(enc_root)

    # Step 3: Find ENC files
    enc_files = directory.find_enc_files()

    # Step 4: Print results
    print(f"Found {len(enc_files)} ENC file(s) in '{enc_root}'\n")
    for i, fpath in enumerate(enc_files, 1):
        print(f"{i}. {fpath}")

    # Step 5: Validate results
    assert isinstance(enc_files, list)
    assert all(f.endswith('.000') for f in enc_files)
    print("\nENCDirectory test passed successfully.")


test_enc_directory()

