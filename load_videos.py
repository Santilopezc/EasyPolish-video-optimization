import os
from typing import List
from videos import VideoCollection  # Assuming this is the module where we defined our classes

def load_videos_from_folder(folder_path: str) -> VideoCollection:
    collection = VideoCollection()
    
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder {folder_path} does not exist.")
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            # The title is the filename without the .txt extension
            title = os.path.splitext(filename)[0]
            
            # Read the content of the file
            with open(file_path, 'r') as file:
                transcript = file.read()
            
            # Add the video to our collection
            collection.add_video(title, transcript)
    
    return collection

# Usage example:
folder_path = 'Polish Transcripts'
video_collection = load_videos_from_folder(folder_path)
print(f'Amount of videos: {video_collection.total_videos()}')