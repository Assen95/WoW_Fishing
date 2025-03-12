from PIL import Image, ImageGrab
import numpy
import cv2 
import time

def update_screen():
    
    initial_time = time.time()
    
    while True:
        screenshot = ImageGrab.grab()
        screenshot = numpy.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        
        cv2.imshow("Screenshot", screenshot)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        execution_time = time.time() - initial_time
        print("FPS: " + str(1 / (execution_time)))
        initial_time = time.time()
        
        
# This will tell python file to be run as the main file. So whenver I "run" it will run this.
if __name__ == "__main__":
    update_screen()