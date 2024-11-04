import os
import shutil

main_dir = input("Paste the directory path of the folder you want to organize: ")

file_categories = {
    "Images": ['.png', '.jpg', '.jpeg'],
    "Documents": ['.doc', '.docx', '.txt', '.xls', '.xlsx', '.pdf'],
    "Videos": ['.mp4', '.avi', '.mov'],
    "Audio": ['.mp3', '.wav'],
}

if os.path.exists(main_dir):
    
    for category, extensions in file_categories.items():

        destination_folder = os.path.join(main_dir, category)
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
            print(f"Directory '{category}' created successfully.")
        else:
            print(f"Directory '{category}' already exists.")

        # Iterate over files in the main directory
        for filename in os.listdir(main_dir):
            if filename.endswith(tuple(extensions)): 
                source_file = os.path.join(main_dir, filename)
                try:
                    # Move the file to the destination folder
                    shutil.move(source_file, destination_folder)
                    print(f"File '{filename}' moved to '{destination_folder}' successfully.")
                except PermissionError:
                    print(f"Permission denied: Unable to move '{filename}'.")
                except Exception as e:
                    print(f"An error occurred while moving '{filename}': {e}")
else:
    print(f"Directory '{dir}' does not exist. Please check the path.")



