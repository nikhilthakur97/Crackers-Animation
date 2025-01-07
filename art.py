import os
import time
import sys

def display_usage():
    print("\nAnimate text art in your terminal\n")
    print("Usage: python3 animate_text.py <directory> <iterations>")
    print("    <directory>: Path to the folder containing text art frames")
    print("    <iterations>: Number of animation loops, or use -1 for infinite looping")
    print()
    sys.exit(1)

# Ensure correct argument count
if len(sys.argv) != 3:
    display_usage()

# Parse arguments
directory = sys.argv[1]
try:
    iterations = int(sys.argv[2])
except ValueError:
    print("<iterations> must be an integer.")
    sys.exit(1)

# Validate directory
if not os.path.isdir(directory):
    print(f"Error: Directory '{directory}' not found.")
    sys.exit(1)

# Load text art frames
frames = []
frame_index = 0
while True:
    frame_path = os.path.join(directory, f"{frame_index}.txt")
    if os.path.isfile(frame_path):
        with open(frame_path, "r") as file:
            frames.append(file.read())
        frame_index += 1
    else:
        break

if not frames:
    print(f"Error: No text art frames found in '{directory}'.")
    sys.exit(1)

# Animation loop
frame_count = len(frames)
lines_to_clear = len(frames[0].splitlines()) + 1
clear_sequence = "\033[A" * lines_to_clear

current_loop = 0
while iterations == -1 or current_loop < iterations:
    for frame in frames:
        if current_loop > 0 or frame != frames[0]:
            print(clear_sequence, end="")
        print(frame)
        time.sleep(0.05)
    current_loop += 1
