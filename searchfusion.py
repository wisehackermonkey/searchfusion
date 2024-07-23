
# from PIL import Image
# import torch
# import torchvision.models as models
# import torchvision.transforms as transforms


# def preprocess_image(image_path):
#     image = Image.open(image_path).convert('RGB')
#     transform = transforms.Compose([
#         transforms.Resize((224, 224)),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#     ])
#     image = transform(image).unsqueeze(0)  # Add batch dimension
#     return image


# def load_model():
#     model = models.resnet50(pretrained=True)
#     model.eval()  # Set model to evaluation mode
#     return model

# def predict(image_tensor, model):
#     with torch.no_grad():
#         outputs = model(image_tensor)
#     return outputs

# import argparse

# def main():
#     parser = argparse.ArgumentParser(description='Multi-label image classification CLI')
#     parser.add_argument('image_path', type=str, help='Path to the image')
#     args = parser.parse_args()

#     # Preprocess the image
#     image_tensor = preprocess_image(args.image_path)

#     # Load the model
#     model = load_model()

#     # Make predictions
#     outputs = predict(image_tensor, model)

#     # Print the predictions (here, we'll print the raw outputs for simplicity)
#     print('Predicted outputs:', outputs)

# if __name__ == '__main__':
#     main()

import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import json
import argparse
import torch.nn.functional as F

# Load ImageNet class labels
with open('./imagenet_labels.json') as f:
    IMAGE_NET_LABELS = json.load(f)

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
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        top5_prob, top5_catid = torch.topk(probabilities, 5)
        top5_prob = top5_prob.numpy()
        top5_catid = top5_catid.numpy()
        predicted_labels = [(IMAGE_NET_LABELS[catid], prob) for catid, prob in zip(top5_catid, top5_prob)]
    return predicted_labels

def main():
    parser = argparse.ArgumentParser(description='Multi-label image classification CLI')
    parser.add_argument('image_path', type=str, help='Path to the image')
    args = parser.parse_args()

    # Preprocess the image
    image_tensor = preprocess_image(args.image_path)

    # Load the model
    model = load_model()

    # Make predictions
    predicted_labels = predict(image_tensor, model)

    # Print the predicted labels
    for label, prob in predicted_labels:
        print(f'Label: {label}, Probability: {prob:.4f}')

if __name__ == '__main__':
    main()
