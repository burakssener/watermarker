import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def add_logo(video_path, logo_path, output_path, logo_size, logo_position):
    # Load the video
    video_clip = VideoFileClip(video_path)

    # Load the logo and resize it
    logo = (ImageClip(logo_path)
              .set_duration(video_clip.duration)
              .resize(height=logo_size * 6.6)  # Make the logo 10 times bigger
              .set_opacity(0.45))

    # Calculate the position to place the logo at the bottom of the middle
    logo_x = (video_clip.size[0] - logo.size[0]) // 2
    logo_y = 843
    # Add the logo in the desired position
    final_clip = CompositeVideoClip([video_clip, logo.set_position((logo_x, logo_y))])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264')

# Example usage
folder_path = "C:/Users/burak/Desktop/watermarker/"
logo_path = "C:/Users/burak/Desktop/watermarker/logo.png"
output_path = "C:/Users/burak/Desktop/watermarker/output"

# Get all files in the directory
files = os.listdir(folder_path)

# Filter out the video files
video_files = [file for file in files if file.endswith('.mp4')]

# Process each video file
for video_file in video_files:
    video_path = os.path.join(folder_path, video_file)
    output_path = os.path.join(folder_path, 'output', video_file)
    add_logo(video_path, logo_path, output_path, 50, "bottom-middle")
