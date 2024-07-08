import os
import shutil

def move_files_with_warning(src_folder, dest_folder):
    # Makes sure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Iterate over files in source folder
    for filename in os.listdir(src_folder):
        # Check if file contains "content_warning" and ends with .webm
        if "content_warning" in filename and filename.endswith(".webm"):
            # Construct full file path
            src_file_path = os.path.join(src_folder, filename)
            dest_file_path = os.path.join(dest_folder, filename)
            
            # Moves file
            shutil.move(src_file_path, dest_file_path)
            print(f"Moved: {filename}")

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    destination_folder = os.path.join(desktop_path, "Moved_Warning_Files")
    
    move_files_with_warning(desktop_path, destination_folder)
