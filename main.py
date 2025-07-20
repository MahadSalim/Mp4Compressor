import subprocess
import os

def compress_video(input_path, crf, preset):
    if not os.path.isfile(input_path):
        print(f"Input file does not exist: {input_path}")
        return

    # Get the input video file name (without extension)
    video_name = os.path.splitext(os.path.basename(input_path))[0]

    # Get the current working directory (where the script is running)
    current_dir = os.getcwd()

    # Create the new folder inside the current working directory
    output_folder = os.path.join(current_dir, video_name)
    os.makedirs(output_folder, exist_ok=True)

    # Create full output path inside that new folder
    output_path = os.path.join(output_folder, "compressed_output.mp4")

    command = ["ffmpeg","-i", input_path,"-vcodec", "libx264","-crf", str(crf),"-preset",
               preset,"-acodec", "aac","-b:a", "128k",output_path]

    print("Running compression with command:")
    print(" ".join(command))

    subprocess.run(command)

# Input video path:
video_path = r'C:\Users\Mahad\Desktop\badmintonVideo.mp4'

# Compression settings:
# crf value = 1-51
# presets = ultrafast, superfast, fast, medium, slow, veryslow
crf = 28  
preset = "medium"

# Run program:
compress_video(video_path, crf, preset)
