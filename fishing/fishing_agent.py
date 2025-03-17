import cv2
import numpy
import pyautogui
import time


class FishingAgent:
    def __init__(self, main_agent):
        self.main_agent = main_agent
        #using absolute path, because im lazy
        self.fishing_target = cv2.imread("fishing/assets/fishing_target.png") 
        self.fishing_thread = None
        
        
    def cast_fishing_bobber(self):
        print("Casting...")
        # TODO: After done free it
        # pyautogui.press('1')
        time.sleep(2)
        self.find_fishing_bobber()
    
    def find_fishing_bobber(self):
        if self.main_agent.current_image is not None:
            current_image = self.main_agent.current_image
            bobber_location = cv2.matchTemplate(
                current_image,
                self.fishing_target,
                method=cv2.TM_CCOEFF_NORMED)
            bobber_location_array = numpy.array(bobber_location)
            
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(bobber_location_array)
            print(max_loc)
            
            self.move_mouse_to_fishing_bobber(max_loc)
        # cv2.imshow("Match Template View", bobber_location_array)
        # cv2.waitKey(0)
        
    def move_mouse_to_fishing_bobber(self, max_loc):
        pyautogui.moveTo(max_loc[0], max_loc[1], 0.5, pyautogui.easeOutQuad)
        self.watch_fishing_bobber(max_loc)
    
    def watch_fishing_bobber(self, max_loc):
        watch_time = time.time()
        while True:
            pixel = self.main_agent.current_image_hsv[max_loc[1], max_loc[0]]
            
            if self.main_agent.zone == "Silverpine Forest" and self.main_agent.time == "day":
                # TODO: Change this shit, when necessary
                if pixel[0] >= 60:
                    print("Bite detected!")
                    break
            
            
            if time.time() - watch_time >= 30:                      #TODO: Change it later.
                break

    def pull_line(self):
        print("Pulling line!")
        pyautogui.keyDown("shift")
        time.sleep(0.005)
        pyautogui.click(button="right")
        time.sleep(0.010)
        pyautogui.keyUp('shift')
    
    def run(self):
        while True:
            self.cast_fishing_bobber()
            time.sleep(5)