# Dual-Robot-Kivy

## Introduction

Last time I used Flask and Guizero to run my robots Linus and Torvalds. This time I'm going to show you how I used Kivy, a multi-platform Python library used for user interfaces, such as multi-touch apps for robotics control. Kivy can run natively on Windows, Mac, Linux, Android and iOS with no change in code. 

## Getting Started

### Hardware

* My Robots Linus and Torvalds
* My Ubuntu PC for developing the App
* My Phone and Tablet to run the App and to SSH into both Robots

### Software

* Raspberry Pi OS on Torvalds
* Raspberry Pi OS Lite on Linus
* Python Modules `gpiozero`, `pigpio` and `kivy`
* PyDroid3 to run the app on my Phone and Tablet.
* An SSH utility like JuiceSSH to SSH into my robots

To install Kivy on any machine use `pip install kivy[base] kivy_examples` or`pip3 install kivy[base]`. For Android and iOS you will use the python-for-android project. However for new users it's recommended to use buildozer. For iOS this link will show how you can create a package for iOS. To follow the Android guide click on ![this](https://kivy.org/doc/stable/guide/android.html) link. For iOS click on ![this](https://kivy.org/doc/stable/guide/packaging-ios.html) link.

However, a much easier and temporary way to get the app running on both is to use IDEs available for both platform. On Android, I found that PyDroid3 works best with Kivy and I ran my app using that IDE. On iOS I recommend using something like Pythonista and StaSh in order to get packages installed. 

## Code explanation

* `dual_robot_kivy.py` creates a grid layout with five columns. The green buttons control Linus's movement and its LED eye and the red buttons control Torvald's movement and its LED eye as well. The first two sliders control Linus's servo arm while the last two sliders control the speed of Linus's motors using PWM. This app can be run with only a phone or tablet making it very portable

## Pictures

* App design running on Ubuntu
* ![Ubuntu](https://github.com/sentairanger/Dual-Robot-Kivy/blob/main/Screenshot%20from%202021-04-28%2018-16-52.png)
* App design running on Windows
* ![Windows](https://github.com/sentairanger/Dual-Robot-Kivy/blob/main/2021-04-29.png)
* Final App running on Android
* ![Android](https://github.com/sentairanger/Dual-Robot-Kivy/blob/main/Screenshot_20210428-155135.png)


