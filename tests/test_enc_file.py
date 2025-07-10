from enc_parser.enc_file import ENCFile

def test_enc_file():
    filepath = "data/raw/test_input/US5CT1EY.000"  # Replace with your ENC file path

    enc = ENCFile(filepath, verbose=True)

    enc.open()

    layers = enc.list_layers()
    print("Layers in ENC file:")
    for i, layer in enumerate(layers):
        print(f"{i+1}: {layer}")

    if layers:
        print(f"\nAccessing layer '{layers[2]}'")
        layer = enc.get_layer(layers[2])
        print(f"Number of features: '{layer.GetFeatureCount()}'.")

test_enc_file()
