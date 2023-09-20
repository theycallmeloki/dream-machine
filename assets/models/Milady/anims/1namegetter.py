import os

def list_fbx_files():
    # List all files in the current directory
    fbx_files = [filename.replace(".fbx", "") for filename in os.listdir(".") if filename.endswith(".fbx")]
    return fbx_files

if __name__ == "__main__":
    files = sorted(list_fbx_files())
    formatted_list = ', '.join(['"' + f + '"' for f in files])
    print(f"[{formatted_list}]")

