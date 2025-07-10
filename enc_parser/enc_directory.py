import os
import fnmatch

#The ENCDirectory class is designed to find all ENC files in a specified directory.
#It recursively searches through the directory and its subdirectories for files matching the ENC file pattern.
class ENCDirectory:
    # Initializes the ENCDirectory with a root path.
    # The root path is the directory where the search for ENC files will begin.
    def __init__(self, root_path):
        self.root_path = root_path

    # Finds all ENC files in the directory and its subdirectories.
    # It returns a list of file paths that match the ENC file pattern 'US*.000
    def find_enc_files(self):
        enc_files = []
        for root, _, filenames in os.walk(self.root_path):
            for filename in fnmatch.filter(filenames, 'US*.000'):
                enc_files.append(os.path.join(root, filename))
        return enc_files
