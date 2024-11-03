import os
import sys

dir = "wtv"
directory_name = "images"

full_path = os.path.join(dir, directory_name)

if os.path.exists(dir):
    try:
        os.mkdir(full_path)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"Directory '{dir}' does not exist. Please check the path.")



