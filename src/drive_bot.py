
# from machine import Pin, PWM
# import time
# 
# # Initialize PWM on GPIO 0
# servo_pin = PWM(Pin(0))
# servo_pin.freq(50)  # Set frequency to 50Hz for servo
# 
# 
# 
# # Define pins
# step_pin = Pin(12, Pin.OUT)
# dir_pin = Pin(13, Pin.OUT)
# en_pin = Pin(10, Pin.OUT)
# ms1_pin = Pin(14, Pin.OUT)
# ms2_pin = Pin(15, Pin.OUT)
# 
# # Setup pins
# en_pin.value(0)         # Enable motor driver (LOW to enable)
# ms1_pin.value(1)        # Microstepping setting (adjust if needed)
# ms2_pin.value(0)
# dir_pin.value(1)        # Set rotation direction: 1 = CW, 0 = CCW
# 
# # Set speed (steps per second)
# speed = 100
# delay = 1 / speed       # Time between steps
# 
# # Motor config
# degrees_to_move = 90
# steps_per_rev = 200     # Full steps per revolution (typical)
# microsteps = 2          # 1/2 step mode (adjust if needed)
# 
# # Calculate number of steps for 90°
# steps = int((degrees_to_move / 360) * steps_per_rev * microsteps)
# 
# # Function to move servo to a specific angle (0 to 180 degrees)
# def move_servo(angle):
#     # Convert angle to duty cycle (duty_u16 value between 1638 and 8192)
#     duty = int((angle / 180) * 6553 + 1638)  # Maps 0-180 deg to approx 2.5%-12.5% duty
#     servo_pin.duty_u16(duty)
# 
# # Test movement: 0° → 90° → 180° → 90° → 0°
# 
# for angle in [90, 0]:
#     print(f"Moving to {angle}°")
#     move_servo(angle)
#     time.sleep(1)
#     
# # Move 90 degrees
# for _ in range(steps):
#     step_pin.value(1)
#     time.sleep_us(500)
#     step_pin.value(0)
#     time.sleep(delay - 0.0020)  # subtract high pulse time
# 
# 
# 
#

from machine import Pin, PWM
import time

# Initialize servo on GPIO 0
servo = PWM(Pin(4))
servo.freq(50)

# Initialize PWM on GPIO 0
servo_pin = PWM(Pin(0))
servo_pin.freq(50)  # Set frequency to 50Hz for servo
# Define pins
step_pin = Pin(12, Pin.OUT)
dir_pin = Pin(13, Pin.OUT)
en_pin = Pin(10, Pin.OUT)
ms1_pin = Pin(14, Pin.OUT)
ms2_pin = Pin(15, Pin.OUT)

step_pin1 = Pin(5, Pin.OUT)
dir_pin1 = Pin(6, Pin.OUT)
en_pin1 = Pin(1, Pin.OUT)
ms1_pin1 = Pin(2, Pin.OUT)
ms2_pin1 = Pin(3, Pin.OUT)

# Setup pins
en_pin.value(0)         # Enable motor driver (LOW to enable)
ms1_pin.value(1)        # Microstepping setting (adjust if needed)
ms2_pin.value(0)
dir_pin.value(1)        # Set rotation direction: 1 = CW, 0 = CCW

# Setup pins1
en_pin1.value(0)         # Enable driver (LOW = enabled)
ms1_pin1.value(1)        # Set microstepping mode
ms2_pin1.value(0)        # Example: 1/2 step mode
dir_pin1.value(1)        # 1 = CW, 0 = CCW

# Set speed (steps per second)
speed = 100
delay = 1 / speed       # Time between steps

# Motor config
degrees_to_move = 90
steps_per_rev = 200     # Full steps per revolution (typical)
microsteps = 2          # 1/2 step mode (adjust if needed)
tray_correction = 7

# Calculate number of steps for 90°
steps = int((degrees_to_move / 360) * steps_per_rev * microsteps)

# Sweep slowly from 0° to 180°, then back
step_size = 2           # Smaller step size = smoother motion
delay_per_step = 0.02    # Increase delay = slower motion

def move_servo(angle):
    min_duty = 1638    # 0° (0.5ms pulse)
    max_duty = 8192    # 180° (2.5ms pulse)
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)
    
    # Function to move servo to a specific angle (0 to 180 degrees)
def move_servo1(angle):
    # Convert angle to duty cycle (duty_u16 value between 1638 and 8192)
    duty = int((angle / 180) * 6553 + 1638)  # Maps 0-180 deg to approx 2.5%-12.5% duty
    servo_pin.duty_u16(duty)

def degs_to_steps(degs):
    steps_per_rev = 200     # Full steps per revolution (typical)
    microsteps = 2          # 1/2 step mode (adjust if needed)
    steps = int((degs / 360) * steps_per_rev * microsteps)
    return steps

def tray_clockwise(n):
    if n == 0:
        return
    elif n < 0:
        dir_val = 0
    else:
        dir_val = 1
    
    steps = degs_to_steps(abs(n) * (90+tray_correction))
    
    dir_pin.value(dir_val)
    for _ in range(steps):
        step_pin.value(1)
        time.sleep_us(400)
        step_pin.value(0)
        time.sleep(delay) #- 0.0020)  # subtract high pulse time
    
    time.sleep(0.1)
    steps = tray_correction
    dir_pin.value(int(not dir_val))
    for _ in range(steps):
        step_pin.value(1)
        time.sleep_us(400)
        step_pin.value(0)
        time.sleep(delay) #- 0.0020)  # subtract high pulse time
    
def fork_clockwise():
    dir_pin1.value(1)
    for _ in range(steps):
        step_pin1.value(1)
        time.sleep_us(500)
        step_pin1.value(0)
        time.sleep(delay) #- 0.0020)  # subtract high pulse time    

def fork_counter_clockwise():
    dir_pin1.value(0)
    for _ in range(steps):
        step_pin1.value(1)
        time.sleep_us(1000)
        step_pin1.value(0)
        time.sleep(delay) #- 0.0020)  # subtract high pulse time    


def hand_up():
    # move hand up
    for angle in [0, 90]:
        move_servo1(angle)

def hand_down():
    # Move lower hand
    for angle in [90, 0]:
        move_servo1(angle)

def fork_in():
    # Forward sweep
    for angle in range(175, 0, -step_size):
        move_servo(angle)
        time.sleep(delay_per_step)
    time.sleep(0.1)
        
def fork_out():
    for angle in range(0, 175, step_size):
         move_servo(angle)
         time.sleep(delay_per_step)
    time.sleep(0.1)


action_dict = {
    "extend_fork" : fork_in,
    "retract_fork" : fork_out,
    "rotate_fork_cw_90": fork_clockwise,
    "rotate_fork_ccw_90" : fork_counter_clockwise,
    "lower_hand" : hand_down,
    "raise_hand" : hand_up,
    "rotate_tray_cw_90" : lambda: tray_clockwise(1),
    "rotate_tray_ccw_90": lambda: tray_clockwise(-1),
}


scramble = [
    #BCW
    "lower_hand",
    "rotate_tray_cw_90",
    "raise_hand",

    #FCW
    "extend_fork",
    "rotate_fork_cw_90",
    "retract_fork",

    #WCCW
    "rotate_tray_ccw_90",

    #FCCW
    "extend_fork",
    "rotate_fork_ccw_90",
    "retract_fork",

    #BCCW
    "lower_hand",
    "rotate_tray_ccw_90",
    "raise_hand",

    #WCCW
    "rotate_tray_ccw_90",

    #FCCW
    "extend_fork",
    "rotate_fork_ccw_90",
    "retract_fork",

    #BCCW
    "lower_hand",
    "rotate_tray_ccw_90",
    "raise_hand",


    #FCCW
    "extend_fork",
    "rotate_fork_ccw_90",
    "retract_fork",

    #BCW
    "lower_hand",
    "rotate_tray_cw_90",
    "raise_hand",
]

solve = [
    #BCCW
    "lower_hand",
    "rotate_tray_ccw_90",
    "raise_hand",

    #FCW
    "extend_fork",
    "rotate_fork_cw_90",
    "retract_fork",

    #BCW
    "lower_hand",
    "rotate_tray_cw_90",
    "raise_hand",

    #FCW
    "extend_fork",
    "rotate_fork_cw_90",
    "retract_fork",

    #WCW
    "rotate_tray_cw_90",

    #BCW
    "lower_hand",
    "rotate_tray_cw_90",
    "raise_hand",

    #FCW
    "extend_fork",
    "rotate_fork_cw_90",
    "retract_fork",

    #WCW
    "rotate_tray_cw_90",

    #FCCW
    "extend_fork",
    "rotate_fork_ccw_90",
    "retract_fork",

    #BCCW
    "lower_hand",
     "rotate_tray_ccw_90",
    "raise_hand",
]

fork_in()
fork_out()

time.sleep(2)

for move in scramble:
    print(move)
    action_dict[move]()
    time.sleep(0.1)
    
time.sleep(10)

for move in solve:
    print(move)
    action_dict[move]()
    time.sleep(0.1)
    


