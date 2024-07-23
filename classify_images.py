# import argparse
# import os
# import subprocess
# from pathlib import Path

# def classify_images(directory, jobs, output_file):
#     # Get all PNG files in the specified directory
#     image_files = list(Path(directory).glob('*.png'))
    
#     if not image_files:
#         print(f"No PNG files found in the directory {directory}")
#         return

#     # Create the command for GNU parallel
#     parallel_command = f"ls {directory}/*.png | parallel -j {jobs} 'cat {{}} | python blip.py --text \"photo of \" --verbose >> {output_file}'"
    
#     # Execute the command
#     result = subprocess.run(parallel_command, shell=True, text=True)
    
#     if result.returncode == 0:
#         print(f"Image classifications have been written to {output_file}")
#     else:
#         print("An error occurred during the classification process.")

# def main():
#     parser = argparse.ArgumentParser(description="Classify images in a directory using a Python script and GNU parallel.")
#     parser.add_argument('directory', nargs='?', default='.', help='Directory containing the images (default: current directory)')
#     parser.add_argument('-j', '--jobs', type=int, default=1, help='Number of parallel jobs (default: 1)')
#     parser.add_argument('-o', '--output', default='image_classifications.txt', help='Output file (default: image_classifications.txt)')
    
#     args = parser.parse_args()
    
#     classify_images(args.directory, args.jobs, args.output)

# if __name__ == "__main__":
#     main()

import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Classify images in a directory using blip.py")
    parser.add_argument('-d', '--directory', type=str, default='-', help="Directory containing images")
    parser.add_argument('-j', '--jobs', type=int, default=1, help="Number of parallel jobs")
    parser.add_argument('-o', '--output', type=str, default='image_classifications.txt', help="Output file")
    parser.add_argument('-f', '--formats', type=str, default='png,jpg,webp,gif', help="Comma-separated list of image formats")

    args = parser.parse_args()

    # Handle directory input from stdin
    if args.directory == '-':
        directory = input("Enter directory name: ").strip()
    else:
        directory = args.directory

    # Generate the list of image files
    formats = args.formats.split(',')
    format_str = ' '.join([f'{directory}/*.{fmt}' for fmt in formats])

    # Create the command string
    command = f"ls {format_str} | parallel -j {args.jobs} 'cat {{}} | python blip.py --text \"photo of \" --verbose >> {args.output}'"

    # Execute the command
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    main()
