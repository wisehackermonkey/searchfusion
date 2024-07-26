# from transformers import ViTImageProcessor, ViTForImageClassification
# from PIL import Image
# import requests
# import sys
# import cProfile

# # Load the imagenet21k_wordnet_lemmas.txt file
# def load_labels(file_path):
#     with open(file_path, 'r') as f:
#         labels = [line.strip() for line in f.readlines()]
#     return labels

# # Define a function to process and classify an image
# def classify_image(image_path, labels):
#     processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
#     model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224-in21k')

#     image = Image.open(image_path)
#     inputs = processor(images=image, return_tensors="pt")
#     outputs = model(**inputs)
#     logits = outputs.logits

#     # Get the predicted class index
#     predicted_class_idx = logits.argmax(-1).item()

#     # Map the predicted index to the corresponding label
#     predicted_label = labels[predicted_class_idx]
    
#     return predicted_label

# # Load the labels from the file
# labels = load_labels('./imagenet21k_wordnet_lemmas.txt')

# # Example usage
# image_path = './images/tor.png'
# predicted_label = classify_image(image_path, labels)
# print(f'Predicted label: {predicted_label}')


# this doenst work because the oupt is super geneartic and not pretrained DAM.
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import sys
import glob

# Initialize processor and model at the top of the file
processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224-in21k')

# Load the imagenet21k_wordnet_lemmas.txt file
def load_labels(file_path):
    with open(file_path, 'r') as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

# Define a function to process and classify an image
def classify_image(image_path, labels):
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # Get the predicted class index
    predicted_class_idx = logits.argmax(-1).item()

    # Map the predicted index to the corresponding label
    predicted_label = labels[predicted_class_idx]
    
    return predicted_label

# Load the labels from the file
labels = load_labels('./imagenet21k_wordnet_lemmas.txt')

# Get the list of image paths from the command line arguments
image_paths = glob.glob(sys.argv[1])

# Iterate over each image path and classify the image
for image_path in image_paths:
    predicted_label = classify_image(image_path, labels)
    print(f'{image_path}: {predicted_label}')
