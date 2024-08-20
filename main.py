"""this is a cheat script written by DrHaze for Counter Strike v1.6
personally I don't suggest using this cheat due to low efficiency compared to cheats like sv_cheats 1
this project is mainly educational and in it, I'm trying to implement object detection for further honing my
skills in this subject. another way to implement this cheat is choose the ally and enemy classes and train the object
detection model two times. I haven't tested it yet, but I am sure that this way you can run the cheat more smoothly and
on weaker systems due to having less classes, and you can use smaller CNNs,so it needs less computational power
for training.
updates will come for updating the guns coeffs for further accuracy
List of low coil guns for starting the project:
CT: KRIEG 550, BULLPUP
T: -
"""

# importing the required packages
import pyautogui
import cv2
import numpy as np

my_class = None

while my_class is None:
    team = input("Enter team number(0 for terrorists and 1 for counter terrorists): ")
    if team == '0':
        my_class = 't'
    elif team == '1':
        my_class = 'ct'
    else:
        print("Invalid input")

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Optional: Display the recording screen
    # cv2.imshow('Live', frame)

    # ------ getting the class and the coords of objects using YOLO ------
    classes = []
    coords = None
    for class_ in classes:
        if class_ == my_class:
            coords = [(1, 2, 4, 6)]  # get the coords

    # finding the gun and calibrating it based on its recoil(optional)
    """for this part I suggest cropping the image and try to find the gun using basic opencv functions
    the gun size is not going to change and if we don't find any gun, we will take the last gun as the gun at hand
    and we know that at the start of every match we are going to have at least a pistol so that gun will be our
    default value for finding the guns coeffs"""

    # since this is the first try we are going to use low recoil guns listed at the top of the file
    gun_coeffs = (1 / 2, 1 / 2)

    # calculating the coeffs of the mouse
    if coords is not None:
        for coord in coords:
            mouse_pos = coord[:2] + coord[2:] * gun_coeffs
            pyautogui.moveTo(mouse_pos[0], mouse_pos[1])
            pyautogui.click()

    # Stop showing the screen when we press 'q'
    # if cv2.waitKey(1) == ord('='):
    #     break

# Destroy all windows
# cv2.destroyAllWindows()
