import RPi.GPIO as GPIO
import curses
from time import sleep

en = 12
in1 = 25
in2 = 16
en1 = 13
in3 = 20
in4 = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in1,GPIO.LOW)
GPIO.setup(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.LOW)
GPIO.setup(in4,GPIO.LOW)

p1 = GPIO.PWM(en,1)
p2 = GPIO.PWM(en1,1)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1.start(100)
p2.start(100)
print("working")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2,GPIO.LOW)

def forward():
	print("UP ARROW KEY IS PRESSED")
	print("MOVING FORWARD")
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
def backward():
	print("DOWN ARROW KEY IS PRESSED")
	print("MOVING BACKWARD")
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
def right():
	print("RIGHT ARROW KEY IS PRESSED")
	print("TURNING RIGHT")
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
def left():
	print("LEFT ARROW KEY IS PRESSED")
	print("TURNING LEFT")
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
def back_right():
	print("RIGHT ARROW KEY IS PRESSED")
	print("TURNING RIGHT BACKWARDS")
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
def back_left():
	print("LEFT ARROW KEY IS PRESSED")
	print("TURNING LEFT BACKWARDS")
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
def brake():
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)

try:
	while True:
		char = screen.getch()
		if char == ord('A'):
			import obstacle_avoidance
		if char == curses.KEY_UP:
			forward()
			char2 = screen.getch()
			if char2 == curses.KEY_DOWN:
				brake()
				sleep(0.5)
				backward()
				char3 = screen.getch()
				if char3 == ord(' '):
					brake()
					print("STOPPED")
			if char2 == curses.KEY_RIGHT:
				brake()
				sleep(0.5)
				right()
				char4 = screen.getch()
				if char4 == ord(' '):
					brake()
					print("STOPPED")
			if char2 == curses.KEY_LEFT:
				brake()
				sleep(0.5)
				left()
				char5 = screen.getch()
				if char5 == ord(' '):
					brake()
					print("STOPPED")
			if char2 == ord(' '):
				brake()
				print("STOPPED")
		if char == curses.KEY_RIGHT:
			right()
			char6 = screen.getch()
			if char6 == curses.KEY_UP:
				brake()
				sleep(0.5)
				forward()
				char7 = screen.getch()
				if char7 == ord(' '):
					brake()
					print("STOPPED")
			if char6 == curses.KEY_DOWN:
				brake()
				sleep(0.5)
				backward()
				char8 = screen.getch()
				if char8 == ord(' '):
					brake()
					print("STOPPED")
			if char6 == curses.KEY_LEFT:
				brake()
				sleep(0.5)
				left()
				char9 = screen.getch()
				if char9 == ord(' '):
					brake()
					print("STOPPED")
			if char6 == ord(' '):
				brake()
				print("STOPPED")
		if char == curses.KEY_LEFT:
			left()
			char10 = screen.getch()
			if char10 == curses.KEY_UP:
				brake()
				sleep(0.5)
				forward()
				char11 = screen.getch()
				if char11 == ord(' '):
					brake()
					print("STOPPED")
			if char10 == curses.KEY_DOWN:
				brake()
				sleep(0.5)
				backward()
				char12 = screen.getch()
				if char12 == ord(' '):
					brake()
					print("STOPPED")
			if char10 == curses.KEY_RIGHT:
				brake()
				sleep(0.5)
				right()
				char13 = screen.getch()
				if char13 == ord(' '):
					brake()
					print("STOPPED")
			if char10 == ord(' '):
				brake()
				print("STOPPED")
		if char == curses.KEY_DOWN:
			backward()
			char14 = screen.getch()
			if char14 == curses.KEY_UP:
				brake()
				sleep(0.5)
				forward()
				char15 = screen.getch()
				if char15 == ord(' '):
					brake()
					print("STOPPED")
			if char14 == curses.KEY_RIGHT:
				brake()
				sleep(0.5)
				back_right()
				char16 = screen.getch()
				if char16 == curses.KEY_LEFT:
					brake()
					sleep(0.5)
					back_left()
					char17 = screen.getch()
					if char17 == ord(' '):
						brake()
						print("STOPPED")
				if char16 == ord(' '):
					brake()
					print("STOPPED")
			if char14 == curses.KEY_LEFT:
				brake()
				sleep(0.5)
				back_left()
				char17 = screen.getch()
				if char17 == curses.KEY_RIGHT:
					brake()
					sleep(0.5)
					back_right()
					char18 = screen.getch()
					if char18 == ord(' '):
						brake()
						print("STOPPED")
				if char17 == ord(' '):
					brake()
					print("STOPPED")
			if char14 == ord(' '):
				brake()
				print("STOPPED")
finally:
	curses.nocbreak();screen.keypad(0);curses.echo()
	curses.endwin()
