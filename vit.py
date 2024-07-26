

# from transformers import ViTImageProcessor, ViTForImageClassification
# from PIL import Image
# import requests
# import cProfile
# url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
# image = Image.open(requests.get(url, stream=True).raw)

# processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
# model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
# def main():
#     inputs = processor(images=image, return_tensors="pt")
#     outputs = model(**inputs)
#     logits = outputs.logits
#     # model predicts one of the 1000 ImageNet classes
#     predicted_class_idx = logits.argmax(-1).item()
#     print("Predicted class:", model.config.id2label[predicted_class_idx])

# if __name__== "__main__":
#     cProfile.run("main()")


from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import sys
import cProfile
processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224-in21k')
# Define a function to process and classify an image
def process_and_classify_image(image_path):
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    # Model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx]

def main(image_paths):

    for image_path in image_paths:
        predicted_class = process_and_classify_image(image_path)
        print(f"Image: {image_path} - Predicted class: {predicted_class}")

if __name__ == "__main__":
    # Pass a list of image file paths as arguments to the script
    with open("photos.txt","r", encoding="utf-8") as file: 
        
        # image_paths = sys.argv[1:].split("\n")
        image_paths = file.read().split("\n")[:4]

        if not image_paths:
            print("Please provide image file paths as arguments.")
        else:
            cProfile.run("main(image_paths)")
            