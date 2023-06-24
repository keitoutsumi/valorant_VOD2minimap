import cv2

def read_frame(cap):
    ret, frame = cap.read()
    return ret, frame

def write_frame(video_writer, frame):
    video_writer.write(frame)

def create_video_writer(path, fourcc, fps, width, height):
    return cv2.VideoWriter(path, fourcc, fps, (width, height))

def release_video_writer(video_writer):
    video_writer.release()

def release_video_capture(cap):
    cap.release()
