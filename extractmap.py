import argparse
import cv2
from video_utils import *
from image_processing import *
from ocr import *
from buffer_utils import *

parser = argparse.ArgumentParser(description='Process video file.')
parser.add_argument('video_file_path', type=str, help='Path to the video file to process.')
parser.add_argument('output_folder_path', type=str, help='Path to the output folder.')
args = parser.parse_args()

video_file_path = args.video_file_path
output_folder_path = args.output_folder_path

ocr_roi = (979, 10, 999, 25)
crop_roi = (30, 50, 410, 410)

cap = cv2.VideoCapture(video_file_path)

if (cap.isOpened()== False): 
    print("Error opening video stream or file")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 3
width = crop_roi[2] - crop_roi[0]
height = crop_roi[3] - crop_roi[1]

video_writers = {}
current_number = 1
frame_counter = 0

buffer_size = 10
buffer = deque(maxlen=buffer_size)

def numbercheck(number):
    number = number.strip()
    if number.isdigit():
        num = int(number)
        return 0 <= num - int(current_number) <= 1
    return False

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_counter += 1
    if ret == True:
        if frame_counter % 10 == 0:
            roi = frame[ocr_roi[1]:ocr_roi[3], ocr_roi[0]:ocr_roi[2]]
            gray_roi = convert_to_gray(roi)
            gray_roi_processed = preprocess_image(gray_roi)
            number = extract_text(gray_roi_processed, config='--psm 6 -c tessedit_char_whitelist=0123456789')

            if numbercheck(number):
                append_to_buffer(buffer,number.strip())
            
            if buffer:
                most_common_number, count = get_most_common(buffer)
                
                if count/buffer_size >= 0.5:
                    current_number = most_common_number
                
                if current_number not in video_writers:
                    print("round" + str(current_number) + "extraction started")
                    video_writers[current_number] = create_video_writer(output_folder_path + '/round' + str(current_number).strip() + '.mp4', fourcc, fps, width, height)

                cropped_frame = frame[crop_roi[1]:crop_roi[3], crop_roi[0]:crop_roi[2]]
                write_frame(video_writers[current_number],cropped_frame)
    else:
        break

cap.release()
for writer in video_writers.values():
    writer.release()

# cv2.destroyAllWindows()
