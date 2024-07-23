import clip
import torch
from PIL import Image

model, preprocess = clip.load("ViT-B/32", device="cpu")
image = preprocess(Image.open("./image.jpg")).unsqueeze(0)
text = clip.tokenize(["a photo of a cat", "a photo of a dog"]).to("cpu")

with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)

    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(1)

print(f"Predicted label: {text[indices[0]].decode('utf-8')}, Probability: {values[0]:.4f}")
# //nope!