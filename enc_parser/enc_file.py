from osgeo import ogr

# A class to handle ENC files
# Uses the OSGEO library to read ENC files
# The class provides methods to open the file, list layers, and get a specific layer by name
# The class can be extended to include more functionality as needed
class ENCFile:
    
    # Initialize the ENCFile class with the file path and verbosity level
    # The verbosity level can be used to control the amount of logging or output
    def __init__(self, filepath, verbose=0):
        self.filepath = filepath
        self.verbose = verbose
        self.datasource = None

    # Open the ENC file using OGR
    # Raises an exception if the file cannot be opened
    def open(self):
           self.datasource = ogr.Open(self.filepath)
           if not self.datasource:
               raise Exception(f"Failed to open ENC file: {self.filepath}")
           
    # List all layers in the ENC file
    # Returns a list of layer names
    def list_layers(self):
         return [self.datasource.GetLayerByIndex(i).GetName() for i in range(self.datasource.GetLayerCount())]
    
    # Get a specific layer by name
    # Raises an exception if the layer is not found
    def get_layer(self, layer_name):
         for i in range(self.datasource.GetLayerCount()):
              layer = self.datasource.GetLayerByIndex(i)
              if layer.GetName() == layer_name:
                   return layer
              
         raise Exception(f"Layer '{layer_name}' not found in ENC file: {self.filepath}")