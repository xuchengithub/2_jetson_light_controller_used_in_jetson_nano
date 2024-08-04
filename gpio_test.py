
import Jetson.GPIO as GPIO
import time
import cv2

# Initialize the camera capture object with the USB camera.
# Often, the first connected camera is at index 0.

cam = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)
if not cam.isOpened():
    print("Cannot open camera")
    exit()
cam.set(cv2.CAP_PROP_FPS, 10) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_EXPOSURE,1000)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)
cam.set(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U, False)


if not cam.isOpened():
    print("Cannot open camera")
    exit()
frame_resized =[]

# Pin Definitions
output_pin = 38  # Output pin
input_pin = 40   # Input pin connected to the switch
output_pin_light_1 = 11
output_pin_light_2 = 12
output_pin_all = 16
# Set up the pins
GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
GPIO.setup(output_pin, GPIO.OUT)
GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(output_pin_light_1, GPIO.OUT)
GPIO.setup(output_pin_light_2, GPIO.OUT)
GPIO.setup(output_pin_all, GPIO.OUT)
# Function to drive the output pin and monitor the input pin for changes
def monitor_input_and_output():
    last_state = None
    change_detected = False
    now_change = None
    old_now = None
    GPIO.output(output_pin_all, GPIO.HIGH)
    try:
        while True:

            
            # Drive the output pin high (3.3V)
            GPIO.output(output_pin, GPIO.HIGH)
            time.sleep(0.01)  # Sleep for 0.01 seconds
            
            # Check input state
            current_state = GPIO.input(input_pin)
            if current_state != last_state:
                change_detected = True  # Detect any change
            
            # Drive the output pin low (0V)
            GPIO.output(output_pin, GPIO.LOW)
            time.sleep(0.01)  # Sleep for 0.01 seconds
            
            # Check input state again
            current_state = GPIO.input(input_pin)
            if current_state != last_state:
                change_detected = True  # Detect any change

            # Reset last_state for the next loop
            last_state = current_state






            # Output result based on whether a change was detected
            if change_detected:
                # print("1 - Alternating signal detected")
                change_detected = False  # Reset change detection flag
                now_change = 1
            else:
                # print("0 - No alternating signal detected")
                now_change = 0

            if old_now != now_change:
                print("light on 111111111111111111111111")
                
                GPIO.output(output_pin_light_1,GPIO.HIGH)
                GPIO.output(output_pin_light_2,GPIO.HIGH)
                time.sleep(2)
                ret, frame = cam.read()
                
                now_frame =frame
                time.sleep(1)
                
                
                # If frame is read correctly, ret is True.
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                # Resize the frame.
                # width = 640  # Set desired width.
                # height = 480  # Set desired height.
                # frame_resized = cv2.resize(frame, (width, height))

                # Save the resulting frame to a file.
                cv2.imwrite('captured_frame.jpg', now_frame)
                print("Image saved as 'captured_frame.jpg'")

                time.sleep(0.3)
                # time.sleep(0.5)
                # Press 'q' to exit the loop.
                if cv2.waitKey(1) == ord('q'):
                    break

                frame = []
                now_frame = []





                time.sleep(0.05)
                print("light off")
                GPIO.output(output_pin_light_1,GPIO.LOW)
                GPIO.output(output_pin_light_2,GPIO.LOW)

                old_now = now_change
           
    finally:
        GPIO.cleanup()
        cam.release()
        cv2.destroyAllWindows()

# Run the function
monitor_input_and_output()




