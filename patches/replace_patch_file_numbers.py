import os
import re

def rename_patch_files(directory):
    """Renames .patch files to have sequential numbers as their first 4 characters, replacing existing numbers."""
    patch_files = []

    # Regular expression to match and remove the first 4 characters if they are numbers
    number_pattern = re.compile(r'^\d{4}')

    # Recursively find all .patch files in the given directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.patch'):
                patch_files.append(os.path.join(root, file))
    
    # Sort files by path to maintain a consistent order
    patch_files.sort()

    # Rename each file with a sequential number
    for i, old_path in enumerate(patch_files, start=1):
        # Generate new filename with sequential numbering
        dir_name = os.path.dirname(old_path)
        old_filename = os.path.basename(old_path)
        
        # Remove the first 4 characters if they are numbers
        new_filename = number_pattern.sub(f"{i:04d}", old_filename, count=1)
        new_path = os.path.join(dir_name, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_filename} -> {new_filename}")

def main():
    directory = "server"  # Replace with the path to your patch directory
    rename_patch_files(directory)

if __name__ == "__main__":
    main()
