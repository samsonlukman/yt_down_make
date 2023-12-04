import os
from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips
import random

# Output directory for downloaded videos
output_dir = 'C:\\Users\\dell\\Videos\\output_videos'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List of YouTube video links
youtube_links = [
     ""
]

# Download YouTube videos
downloaded_files = []
for link in youtube_links:
    try:
        yt = YouTube(link)
        video = yt.streams.filter(file_extension="mp4", res="720p").first()
        downloaded_file = video.download(output_dir)
        downloaded_files.append(downloaded_file)
    except Exception as e:
        print(f"Error downloading video from {link}: {e}")

# Cut random 5 seconds from each downloaded video (excluding the first 20 seconds)
cut_videos = []
for file_path in downloaded_files:
    try:
        video_clip = VideoFileClip(file_path)
        start_time = random.uniform(20, max(20, video_clip.duration - 5))
        cut_clip = video_clip.subclip(start_time, start_time + 5)
        cut_videos.append(cut_clip)
    except Exception as e:
        print(f"Error processing video file {file_path}: {e}")

# Concatenate the cut videos into one final output
final_output = concatenate_videoclips(cut_videos)

# Set the output file path
output_path = os.path.join(output_dir, "final_output.webm")

# Write the final output to file
final_output.write_videofile(output_path, codec="libvpx", audio_codec="libvorbis", bitrate="8M", remove_temp=True)

# Print information about the final output
print(f"Final output saved at: {output_path}")
print(f"Total duration of the final output: {final_output.duration} seconds")
