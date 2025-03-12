from PIL import Image, ImageGrab
import numpy
import cv2 
import time
from threading import Thread
from fishing.fishing_agent import FishingAgent 


class MainAgent:
    def __init__(self):
        self.agents = []
        self.fishing_thread = None
        
        self.current_image = None #BGR
        self.current_image_hsv = None #HSV
        
        self.zone = "Silverpine Forest"
        self.time = "day"
        
        print("MainAgent Setup complete...")


def update_screen(agent):
    
    initial_time = time.time()
    fps_report_delay = 5
    fps_report_time = time.time()
    
    while True:
        agent.current_image = ImageGrab.grab()
        agent.current_image = numpy.array(agent.current_image)
        agent.current_image = cv2.cvtColor(agent.current_image, cv2.COLOR_RGB2BGR)
        agent.ccurrent_image_hsv = cv2.cvtColor(agent.current_image, cv2.COLOR_BGR2HSV)
        
        #cv2.imshow("Screenshot", agent.current_image)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        execution_time = time.time() - initial_time
        if time.time() - fps_report_time >= fps_report_delay:
            print("FPS: " + str(1 / (execution_time)))
            fps_report_time = time.time()
        initial_time = time.time()
        time.sleep(0.005)
    
def print_menu():
    print("Enter a command:")
    print("\tS\tStart the main agent.")
    print("\tZ\tSet zone.")
    print("\tF\tStart the fishing agent.")
    print("\tQ\tQuit wowzer.")
    
    
if __name__ == "__main__":
    main_agent = MainAgent()
    
    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()
        
        if user_input == "s":
            update_screen_thread = Thread(
            target=update_screen,
            args=(main_agent,),
            name="update screen thread",
            daemon=True)
            update_screen_thread.start()
            print("Thread started...")
            
        elif user_input == "z":
            pass
        elif user_input == "f":
            fishing_agent = FishingAgent(main_agent)
            fishing_agent.run()
            
        elif user_input == "q":
            cv2.destroyAllWindows()
            break
        else:
            print("Input Error!")
            print_menu()

    print("Exiting application")