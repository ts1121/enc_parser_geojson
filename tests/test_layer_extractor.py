from enc_parser.enc_file import ENCFile
from enc_parser.layer_extractor import LayerExtractor

def test_layer_extractor():
    filepath = "data/raw/test_input/US5CT1EY.000"  # Replace with your ENC file path
    target_layer_index = 2

    enc = ENCFile(filepath, verbose=True)
    enc.open()

    layers = enc.list_layers()
    print("Layers in ENC file:")
    for i, layer in enumerate(layers):
        print(f"{i+1}: {layer}")

    if layers:
        layer_name = layers[target_layer_index]
        print(f"\nExtracting features from layers: '{layer_name}'")

        layer = enc.get_layer(layer_name)
        extractor = LayerExtractor(layer)
        features = extractor.extract_features()

        print(f"\nExtracted {len(features)} features from layer '{layer_name}':")
        for i, feat in enumerate(features[:5]):
            print(f"Feature {i+1}:")
            print(f"  Geometry: {feat['geometry']}")
            print(f"  Properties: {feat['properties']}")

test_layer_extractor()
   