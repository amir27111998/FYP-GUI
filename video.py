import cv2
import re
import json

SETTINGS_PATH = './settings.json'
BASE_PATH = './videos'
def stream_video(filename):
    cv2.destroyAllWindows()
    delay=1
    if re.search("^carla*", filename):
        delay = 200
    video = cv2.VideoCapture(BASE_PATH+'/'+filename)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        resized = cv2.resize(frame, (720, 480))
        cv2.imshow('Playing', resized)
        if cv2.waitKey(delay) == 27:
            break
    cv2.destroyAllWindows()
    return

def save_settings(settings_dict):
    try:
        with open(SETTINGS_PATH,'w') as file:
            json.dump(settings_dict, file)
        return True
    except Exception as e:
        return False


def read_settings():
    settings={}
    with open(SETTINGS_PATH, 'r') as file:
        settings=json.load(file)
    return settings
