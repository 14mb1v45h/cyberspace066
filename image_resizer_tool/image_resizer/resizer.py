import os
from PIL import Image

def resize_images(input_folder, output_folder, size):
    """Resize all images in input_folder to specified size and save to output_folder."""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Supported image formats
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    
    # Counter for processed images
    processed = 0
    errors = 0
    
    # Iterate through files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            try:
                # Open image
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)
                
                # Resize image while maintaining aspect ratio
                img.thumbnail(size, Image.LANCZOS)
                
                # Save resized image to output folder
                output_path = os.path.join(output_folder, f"resized_{filename}")
                img.save(output_path)
                print(f"Resized: {filename}")
                processed += 1
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                errors += 1
        else:
            print(f"Skipped: {filename} (unsupported format)")
    
    # Summary
    print(f"\nCompleted! Processed {processed} images, {errors} errors.")
    return processed, errors  # Explicitly return the tuple