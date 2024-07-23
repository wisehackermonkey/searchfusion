import urllib.request
import json

# URL of the ImageNet labels JSON file
url = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'

# Download and save the JSON file
def download_imagenet_labels(filename='imagenet_labels.json'):
    urllib.request.urlretrieve(url, filename)
    print(f'Downloaded {filename}')

# Example usage
download_imagenet_labels()
