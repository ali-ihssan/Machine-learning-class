import cv2
import os


# def video_to_frames(video_path, output_root_folder, start_time, end_time, interval_length=3):

#     video_name = os.path.splitext(os.path.basename(video_path))[0]

#     video_capture = cv2.VideoCapture(video_path)

#     os.makedirs(output_root_folder, exist_ok=True)

#     fps = int(video_capture.get(cv2.CAP_PROP_FPS))
#     total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
#     num_intervals = (end_time - start_time) // interval_length
#     print(f"Processing video: {video_name}")
#     print(f"Total frames: {total_frames}")
#     print(f"Frames per second: {fps}")
#     print(f"Number of intervals: {num_intervals}")

#     for interval in range(num_intervals):
#         # Calculate the start and end frames for the interval
#         start_frame = int((start_time + interval * interval_length) * fps)
#         end_frame = int((start_time + (interval + 1) * interval_length) * fps)

#         # Set the video capture to the start frame
#         video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

#         # Create the output folder for the interval
#         output_folder = os.path.join(
#             output_root_folder, f"{video_name}_start{start_time}_end{end_time}_interval{interval + 1}")
#         os.makedirs(output_folder, exist_ok=True)

#         for frame_number in range(start_frame, end_frame):
#             ret, frame = video_capture.read()
#             if not ret:
#                 print(f"Error reading frame {frame_number}")
#                 break

#             frame_filename = os.path.join(
#                 output_folder, f"{video_name}_interval{interval + 1}_frame{frame_number:04d}.png")
#             cv2.imwrite(frame_filename, frame)
#             print(f"Frame {frame_number} saved as {frame_filename}")

#     video_capture.release()

# def video_to_frames(video_path, output_root_folder, start_time, end_time, interval_length=3, output_fps=15):
#     if not os.path.isfile(video_path):
#         print(f"Error: video file {video_path} does not exist.")
#         return

#     video_name = os.path.splitext(os.path.basename(video_path))[0]
#     video_capture = cv2.VideoCapture(video_path)

#     if not video_capture.isOpened():
#         print(f"Error: could not open video file {video_path}.")
#         return

#     os.makedirs(output_root_folder, exist_ok=True)
#     fps = int(video_capture.get(cv2.CAP_PROP_FPS))
#     total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
#     num_intervals = (end_time - start_time) // interval_length

#     if num_intervals == 0:
#         print(f"Error: interval length {interval_length} is too large.")
#         return

#     print(f"Processing video: {video_name}")
#     print(f"Total frames: {total_frames}")
#     print(f"Frames per second: {fps}")
#     print(f"Number of intervals: {num_intervals}")

#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID'
#     for interval in range(num_intervals):
#         start_frame = int((start_time + interval * interval_length) * fps)
#         end_frame = int((start_time + (interval + 1) * interval_length) * fps)
#         output_folder = os.path.join(
#             output_root_folder, f"{video_name}_start{start_time}_end{end_time}_interval{interval + 1}")
#         os.makedirs(output_folder, exist_ok=True)
#         output_file = os.path.join(
#             output_folder, f"{video_name}_interval{interval + 1}.mp4")
#         out = cv2.VideoWriter(output_file, fourcc, output_fps, (int(
#             video_capture.get(3)), int(video_capture.get(4))))

#         if not out.isOpened():
#             print(f"Error: could not open output file {output_file}.")
#             return

#         for frame_number in range(start_frame, end_frame):
#             video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
#             ret, frame = video_capture.read()
#             if not ret:
#                 print(f"Error reading frame {frame_number}")
#                 break
#             out.write(frame)
#         out.release()
#     video_capture.release()

def video_to_frames(video_path, output_root_folder, start_time, end_time, interval_length=3, output_fps=14):
    if not os.path.isfile(video_path):
        print(f"Error: video file {video_path} does not exist.")
        return

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print(f"Error: could not open video file {video_path}.")
        return

    os.makedirs(output_root_folder, exist_ok=True)
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    num_intervals = (end_time - start_time) // interval_length

    if num_intervals == 0:
        print(f"Error: interval length {interval_length} is too large.")
        return

    print(f"Processing video: {video_name}")
    print(f"Total frames: {total_frames}")
    print(f"Frames per second: {fps}")
    print(f"Number of intervals: {num_intervals}")
    print(f"Output FPS: {output_fps}")
    print(fps)
    print(f"fps // output_fps: {fps // output_fps}")
    frame_skip = fps // output_fps
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID'
    for interval in range(num_intervals):
        start_frame = int((start_time + interval * interval_length) * fps)
        end_frame = int((start_time + (interval + 1) * interval_length) * fps)
        output_folder = os.path.join(
            output_root_folder, f"{video_name}_start{start_time}_end{end_time}_interval{interval + 1}")
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(
            output_folder, )
        out = cv2.VideoWriter(output_file, fourcc, output_fps, (int(
            video_capture.get(3)), int(video_capture.get(4))))

        # if not out.isOpened():
        #     print(f"Error: could not open output file {output_file}.")
        #     return

        for frame_number in range(start_frame, end_frame, frame_skip):
            video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = video_capture.read()
            if not ret:
                print(f"Error reading frame {frame_number}")
                break
            out.write(frame)
            # Save each frame as an image
            output_image_file = os.path.join(
                output_folder, f"{video_name}_frame{frame_number}.png")
            cv2.imwrite(output_image_file, frame)
        out.release()
    video_capture.release()


def process_videos_in_folder(input_folder, output_root_folder, video_info):

    if video_info is None:
        return
    if not os.path.exists(output_root_folder):
        os.makedirs(output_root_folder)
    for idx, (video_file, start_time, end_time) in enumerate(video_info, start=1):

        if end_time - start_time < 3:
            print(
                f"Skipping video {video_file} start: {start_time} end: {end_time} because the interval is less than 3 seconds")
            continue

        video_path = os.path.join(input_folder, video_file)
        video_to_frames(video_path, output_root_folder, start_time, end_time)


if __name__ == "__main__":
    # Set the path to the folder containing video files
    input_folder = "../content/XX"

    # Set the root folder for output frames
    output_root_folder = "../content/a"

    # Define video information as a list of tuples (video_file, start_time, end_time)
    video_info = [
        ("22.mp4", 0, 5),
        # Add more videos with their respective start and end times
    ]

    # Call the function to process videos in the folder and save frames within each 3-second interval
    process_videos_in_folder(input_folder, output_root_folder, video_info)
