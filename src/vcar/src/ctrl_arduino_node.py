#!/usr/bin/python3.8
import rospy
import serial
from std_msgs.msg import String

## Variables globales del auto

# servo_1 = 60;
# servo_2 = 60;
# servo_3 = 60;
# servo_4 = 60;

GO_FORWARD = bytearray('#010$', encoding='utf-8')
GO_BACK = bytearray('#020$', encoding='utf-8')
GO_LEFT = bytearray('#030$', encoding='utf-8')
GO_RIGHT = bytearray('#040$', encoding='utf-8')
GO_STOP = bytearray('#000$', encoding='utf-8')
PANTILT_UP = bytearray('#05Z$', encoding='utf-8')
PANTILT_DOWN = bytearray('#05%$', encoding='utf-8')
PANTILT_LEFT = bytearray('#06Z$', encoding='utf-8')
PANTILT_RIGHT = bytearray('#06%$', encoding='utf-8')
# ARM_RIGHT = bytearray('#07%$', encoding='utf-8')
# ARM_LEFT = bytearray('#07Z$', encoding='utf-8')
# ARM_UPDOWN = bytearray('#08%$', encoding='utf-8')
# ARM_EXTEND = bytearray('#09%$', encoding='utf-8')
# ARM_CATCH = bytearray('#0A%$', encoding='utf-8')wwddddaa
SET_VEL_1 : bytearray = bytearray('#V10$', encoding='utf-8')
SET_VEL_2 : bytearray = bytearray('#V20$', encoding='utf-8')
SET_VEL_3 : bytearray = bytearray('#V30$', encoding='utf-8')
SET_VEL_4 : bytearray = bytearray('#V40$', encoding='utf-8')
SET_VEL_5 : bytearray = bytearray('#V50$', encoding='utf-8')

last_key : str

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS
)

""""
  
        if key == ord('i'):
            if(servo1 >= 0 and servo1 < 90):
                servo1 = servo1 + 5;
                PANTILT_UP[3]= servo1;
                ser.write(PANTILT_UP)
                #print(time_stamp() + ' ' + 'Pantilt Up');
        if key == ord('k'):
            if(servo1 > 0 and servo1 <= 90):
                servo1 = servo1 - 5;
                PANTILT_DOWN[3]= servo1;
                ser.write(PANTILT_DOWN)
                #print(time_stamp() + ' ' + "Pantilt Down");
        if key == ord('j'):
            if(servo2 >= 0 and servo2 < 90):
                servo2 = servo2 + 5;
                PANTILT_LEFT[3]= servo2;
                ser.write(PANTILT_LEFT)
                #print(time_stamp() + ' ' + "Pantilt Left" + str(PANTILT_LEFT));
        if key == ord('l'):
            if(servo2 > 0 and servo2 <= 170):
                servo2 = servo2 - 5;
                PANTILT_RIGHT[3]= servo2;
                ser.write(PANTILT_RIGHT)
                #print(time_stamp() + ' ' + "Pantilt Right" + str(PANTILT_RIGHT));

        if key == ord('t'):
            if(servo3 >= 0 and servo3 < 90):
                servo3 = servo3 + 5;
                #ARM_RIGHT[3]= servo3;
                #ser.write(ARM_RIGHT)
                #print(time_stamp() + ' ' + "Arm Right/Left" + str(ARM_RIGHT));
        if key == ord('g'):
            if(servo3 > 0 and servo3 <= 90):
                servo3 = servo3 - 5;
                ARM_LEFT[3]= servo3;
                ser.write(ARM_LEFT)
                #print(time_stamp() + ' ' + "Arm Left" + str(ARM_LEFT));
        """

def callback(data):

    global last_key
    #c = str(data.data).split(" ")
    #key = c[0]
    key : str = str(data.data)
    print(str)

    if last_key != key or True:
        last_key = key
        #rospy.loginfo(key)
        if key == "w down":
            ser.write(GO_FORWARD)
            rospy.loginfo("RPI: %s" + " - forward", GO_FORWARD)
        if key == "s down":
            ser.write(GO_BACK)
            rospy.loginfo("RPI: %s" + " - back", GO_BACK)
        if key == "left down":
            ser.write(GO_LEFT)
            rospy.loginfo("RPI: %s" + " - left", GO_LEFT) 
        if (key.startswith("s") or key.startswith("w") or key.startswith("left") or key.startswith("right")) and key.endswith("up"):
            ser.write(GO_STOP)
            rospy.loginfo("RPI: %s" + " - right", GO_STOP)
        
        if key == "right down":
            ser.write(GO_RIGHT)
            rospy.loginfo("RPI: %s" + " - right", GO_RIGHT)
        
        """
        Falta implementar del lado de arduino
        if key == "k down":
            ser.write(PANTILT_DOWN)
            rospy.loginfo("RPI: %s" + " - pantilt down", PANTILT_DOWN)
        if key == "i down":
            ser.write(PANTILT_UP)
            rospy.loginfo("RPI: %s" + " - pantilt up", PANTILT_UP)
        if key == "j down":
            ser.write(PANTILT_LEFT)
            rospy.loginfo("RPI: %s" + " - pantilt left", PANTILT_LEFT)
        if key == "l down":
            ser.write(PANTILT_RIGHT)
            rospy.loginfo("RPI: %s" + " - pantilt right", PANTILT_RIGHT)
        #rospy.loginfo("ARDUINO: " + ser.readline().decode("utf-8") )
        """

def listener():
    rospy.init_node("ctrl_arduino_node", anonymous=True)

    rospy.Subscriber('cmd_serial', String, callback)

    rospy.spin()

if __name__ =='__main__':

    last_key = '0'
    print("Ctrl Arduino Node inicialized")
    #rospy.loginfo("ARDUINO: " + ser.readline().decode("utf-8") )
    
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
