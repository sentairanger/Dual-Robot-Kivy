# import libraries
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from gpiozero import LED, OutputDevice, PWMOutputDevice, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

#Define the factories
factory = PiGPIOFactory(host='192.168.0.22')
factory2 = PiGPIOFactory(host='192.168.0.18')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

#Define the eyes
linus_eye = LED(16, pin_factory=factory)
torvalds_eye = LED(25, pin_factory=factory2)

# Define the servo arm
angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=factory)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=factory)

# Button colors
red = [1,0,0,1]
green = [0,1,0,1]

class GridRobotApp(App):
    def build(self):
        # Create a layout of 5 columns
        layout = GridLayout(cols=5)
        # define the buttons, labels and sliders
        forward = Button(text="forward",background_color=green)
        backward = Button(text="backward", background_color=green)
        left = Button(text="left", background_color=green)
        right = Button(text="right", background_color=green)
        north = Button(text="north", background_color=red)
        south = Button(text="south", background_color=red)
        east = Button(text="east", background_color=red)
        west = Button(text="west", background_color=red)
        linus = Button(text="linus eye", background_color=green)
        torvalds = Button(text="torvalds eye", background_color=red)
        self.slider1 = Slider(min = -90,  max=90)
        self.slider2 = Slider(min=-90,  max=90)
        self.slider3 = Slider(min=0,  max=10)
        self.slider4 = Slider(min=0,  max=10)
        label_servo = Label(text="Servo Arm")
        label_pwm = Label(text="PWM control")
        self.l1 = Label(text='0')
        self.l2 = Label(text='0')
        self.l3 = Label(text='0')
        self.l4 = Label(text='0')
        # bind the buttons to their functions
        north.bind(on_press=self.torvalds_left)
        north.bind(on_release=self.stop)
        south.bind(on_press=self.torvalds_right)
        south.bind(on_release=self.stop)
        west.bind(on_press=self.torvalds_forward)
        west.bind(on_release=self.stop)
        east.bind(on_press=self.torvalds_backward)
        east.bind(on_release=self.stop)
        forward.bind(on_press=self.direction_one)
        forward.bind(on_release=self.stop_two)
        backward.bind(on_press=self.direction_two)
        backward.bind(on_release=self.stop_two)
        left.bind(on_press=self.direction_four)
        left.bind(on_release=self.stop_two)
        right.bind(on_press=self.direction_three)
        right.bind(on_release=self.stop_two)
        linus.bind(on_press=self.eye_on)
        linus.bind(on_release=self.eye_off)
        torvalds.bind(on_press=self.torvalds_on)
        torvalds.bind(on_release=self.torvalds_off)
        # row 1
        layout.add_widget(forward)
        layout.add_widget(backward)
        layout.add_widget(left)
        layout.add_widget(right)
        layout.add_widget(linus)
        # row 2
        layout.add_widget(north)
        layout.add_widget(south)
        layout.add_widget(east)
        layout.add_widget(west)
        layout.add_widget(torvalds)
        # row 3
        layout.add_widget(label_servo)
        layout.add_widget(self.slider1)
        layout.add_widget(self.l1)
        layout.add_widget(self.slider2)
        layout.add_widget(self.l2)
        # row 4
        layout.add_widget(label_pwm)
        layout.add_widget(self.slider3)
        layout.add_widget(self.l3)
        layout.add_widget(self.slider4)
        layout.add_widget(self.l4)
        # bind the sliders to their functions
        self.slider1.bind(value=self.angle_one)
        self.slider2.bind(value=self.angle_two)
        self.slider3.bind(value=self.pwm_one)
        self.slider4.bind(value=self.pwm_two)
        return layout
    # Define the functions for the sliders, labels and buttons
    def angle_one(self, instance, angle):
        self.l1.text = "%d"% angle
        angular_servo.angle = int(self.slider1.value)

    def angle_two(self, instance, angle):
        self.l2.text = "%d"% angle
        angular_servo2.angle = int(self.slider2.value)

    def pwm_one(self,instance, pwm):
        self.l3.text = "%d"% pwm
        en_1.value = int(self.slider3.value) / 10

    def pwm_two(self, instance, pwm):
        self.l4.text = "%d"% pwm
        en_2.value = int(self.slider4.value) / 10
    def torvalds_forward(self,event):
        pin1.on()
        pin2.off()
        pin3.on()
        pin4.off()
    def torvalds_backward(self, event):
        pin1.off()
        pin2.on()
        pin3.off()
        pin4.on()
    def torvalds_left(self, event):
        pin1.off()
        pin2.on()
        pin3.on()
        pin4.off()
    def torvalds_right(self, event):
        pin1.on()
        pin2.off()
        pin3.off()
        pin4.on()
    def stop(self, event):
        pin1.off()
        pin2.off()
        pin3.off()
        pin4.off()
    def direction_one(self, event):
        motor_in1.on()
        motor_in2.off()
        motor_in3.on()
        motor_in4.off()
    def direction_two(self, event):
        motor_in1.off()
        motor_in2.on()
        motor_in3.off()
        motor_in4.on()
    def direction_three(self, event):
        motor_in1.on()
        motor_in2.off()
        motor_in3.off()
        motor_in4.on()
    def direction_four(self, event):
        motor_in1.off()
        motor_in2.on()
        motor_in3.on()
        motor_in4.off()
    def stop_two(self, event):
        motor_in1.off()
        motor_in2.off()
        motor_in3.off()
        motor_in4.off()
    def eye_on(self, event):
        linus_eye.on()
    def eye_off(self, event):
        linus_eye.off()
    def torvalds_on(self, event):
        torvalds_eye.on()
    def torvalds_off(self, event):
        torvalds_eye.off()

# Define the root and then run the app
root = GridRobotApp()
root.run()
