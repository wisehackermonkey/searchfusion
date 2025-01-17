import argparse
import sys
import os
from os import path 
import logging
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


def main():
    parser = argparse.ArgumentParser(description='Image captioning using BLIP.')
    parser.add_argument('--text', type=str, default='A ', help='Text prompt for image captioning.')
    parser.add_argument('--input_file', type=str, default='-', help='Path to the input image file (default: stdin).')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode for warnings.')

    args = parser.parse_args()

    # Configure logging
    if args.verbose:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.CRITICAL)
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    logging.warning("Loading models and processor...")
    
    # Load the model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    logging.warning("Reading the image...")
    
    # Read the image
    if args.input_file == '-':
        # Read image from stdin
        raw_image = Image.open(sys.stdin.buffer).convert('RGB')
    else:
        # Read image from the provided file path
        raw_image = Image.open(args.input_file).convert('RGB')
        logging.warning(f"Processed Image {args.input_file}")


    logging.warning("Processing the image and generating caption...")

    # Process the image and generate caption
    inputs = processor(raw_image, args.text, return_tensors="pt")
    out = model.generate(**inputs)

    if not args.verbose:
        sys.stdout = sys.__stdout__
    # Print the generated caption
    if not args.input_file == '-':
        cur_file = path.abspath(path.expanduser(args.input_file))
        print(cur_file,",", processor.decode(out[0], skip_special_tokens=True))

if __name__ == '__main__':
    main()
