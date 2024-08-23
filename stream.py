import cv2
import subprocess
import threading

# Hardcoded IP and port for streaming
UDP_IP = "127.0.0.1"  # localhost for testing
UDP_PORT = 9999

# Function to list available video sources (webcams)
def list_video_sources():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

# Function to stream video from the selected source using FFmpeg
def stream_video(source_index, stop_event):
    cap = cv2.VideoCapture(source_index)
    if not cap.isOpened():
        print(f"Error: Could not open video source {source_index}")
        return

    # FFmpeg command to stream via UDP
    ffmpeg_command = [
        'ffmpeg',
        '-f', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', '640x480',
        '-r', '30',
        '-i', '-',  # input from stdin
        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-f', 'mpegts',
        'output.ts'
    ]

    process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize frame if needed
        frame = cv2.resize(frame, (640, 480))

        # Write the frame to the FFmpeg process
        process.stdin.write(frame.tobytes())

    cap.release()
    process.stdin.close()
    process.wait()
    print("Stopped streaming.")

def main():
    # Step 2: List available video sources
    sources = list_video_sources()
    if not sources:
        print("No video sources found. Exiting.")
        return

    while True:
        print("Available video sources:")
        for i, source in enumerate(sources):
            print(f"{i}: Video Source {source}")

        # Step 3: Allow the user to select one
        choice = input("Select a video source by number (or 'q' to quit): ")
        if choice.lower() == 'q':
            break

        try:
            source_index = sources[int(choice)]
        except (IndexError, ValueError):
            print("Invalid selection. Please try again.")
            continue


        save_frames_to_file(0, 'output.avi')  # Replace 0 with your webcam index if needed

        """
        # Step 4: Stream the output of that source
        stop_event = threading.Event()
        stream_thread = threading.Thread(target=stream_video, args=(source_index, stop_event))
        stream_thread.start()

        # Step 5: Allow stopping the transmission at any time
        input("Press Enter to stop streaming...")
        stop_event.set()
        stream_thread.join()

        # Step 6: Go back to step 2 after stopping
        print("Streaming stopped.")
        """

    # Step 7: Allow stopping the script safely
    print("Exiting. Freeing resources.")
    cv2.destroyAllWindows()

def save_frames_to_file(source_index, output_file):
    cap = cv2.VideoCapture(source_index)
    if not cap.isOpened():
        print(f"Error: Could not open video source {source_index}")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Write the frame to file
        out.write(frame)

        cv2.imshow('Webcam Test', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
