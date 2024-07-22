
from PIL import Image
import torch
import torchvision.models as models
import torchvision.transforms as transforms


def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0)  # Add batch dimension
    return image


def load_model():
    model = models.resnet50(pretrained=True)
    model.eval()  # Set model to evaluation mode
    return model

def predict(image_tensor, model):
    with torch.no_grad():
        outputs = model(image_tensor)
    return outputs

import argparse

def main():
    parser = argparse.ArgumentParser(description='Multi-label image classification CLI')
    parser.add_argument('image_path', type=str, help='Path to the image')
    args = parser.parse_args()

    # Preprocess the image
    image_tensor = preprocess_image(args.image_path)

    # Load the model
    model = load_model()

    # Make predictions
    outputs = predict(image_tensor, model)

    # Print the predictions (here, we'll print the raw outputs for simplicity)
    print('Predicted outputs:', outputs)

if __name__ == '__main__':
    main()
