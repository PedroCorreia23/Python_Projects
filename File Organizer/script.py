import os
import shutil

main_dir = r'C:\Users\pedro\OneDrive\Ambiente de Trabalho\file_organizer'

file_categories = {
    "Images": ['.png', '.jpg', '.jpeg'],
    "Documents": ['.doc', '.docx', '.txt', '.xls', '.xlsx', '.pdf'],
    "Videos": ['.mp4', '.avi', '.mov'],
    "Audio": ['.mp3', '.wav'],
}

destination_folder = os.path.join(main_dir, file_categories.items())

# Ensure the main directory exists
if os.path.exists(main_dir):
    
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
        print(f"Directory '{file_categories}' created successfully.")
    else:
        print(f"Directory '{file_categories}' already exists.")

    # Iterate over files in the main directory
    for filename in os.listdir(main_dir):
        if filename.endswith(('.png', '.jpg')):
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



