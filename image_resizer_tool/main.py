import argparse
import sys
from image_resizer.resizer import resize_images
import os

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Bulk Image Resizer Tool")
    parser.add_argument("input_folder", help="Path to folder containing images")
    parser.add_argument("output_folder", help="Path to save resized images")
    parser.add_argument("--width", type=int, default=1080, help="Desired width in pixels (default: 1080)")
    parser.add_argument("--height", type=int, default=1080, help="Desired height in pixels (default: 1080)")
    
    args = parser.parse_args()
    
    # Validate input folder
    if not os.path.isdir(args.input_folder):
        print(f"Error: {args.input_folder} is not a valid directory")
        sys.exit(1)
    
    # Call resize function
    size = (args.width, args.height)
    processed, errors = resize_images(args.input_folder, args.output_folder, size)

if __name__ == "__main__":
    main()