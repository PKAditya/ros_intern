import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
l_TRIG = 4
l_ECHO = 27
l_led = 19

f_TRIG = 23
f_ECHO = 24
f_led = 19

b_TRIG = 22
b_ECHO = 5
b_led = 19

r_TRIG = 6
r_ECHO = 26
r_led = 19

en1 = 12
en2 = 13
in1 = 25
in2 = 16
in3 = 20
in4 = 21

GPIO.setup(l_TRIG, GPIO.OUT)
GPIO.setup(l_ECHO, GPIO.IN)
GPIO.setup(l_led, GPIO.OUT)

GPIO.setup(f_TRIG, GPIO.OUT)
GPIO.setup(f_ECHO, GPIO.IN)
GPIO.setup(f_led, GPIO.OUT)

GPIO.setup(b_TRIG, GPIO.OUT)
GPIO.setup(b_ECHO, GPIO.IN)
GPIO.setup(b_led, GPIO.OUT)

GPIO.setup(r_TRIG, GPIO.OUT)
GPIO.setup(r_ECHO, GPIO.IN)
GPIO.setup(r_led, GPIO.OUT)

GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
p1 = GPIO.PWM(en1,1)
p2 = GPIO.PWM(en2,1)
p1.start(100)
p2.start(100)

def stop():
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.LOW)
	GPIO.output(in4, GPIO.LOW)
def forward():
	GPIO.output(in1, GPIO.HIGH)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.HIGH)
	GPIO.output(in4, GPIO.LOW)
def right():
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.HIGH)
	GPIO.output(in4, GPIO.LOW)
def left():
	GPIO.output(in1, GPIO.HIGH)
	GPIO.output(in2, GPIO.LOW)
	GPIO.output(in3, GPIO.LOW)
	GPIO.output(in4, GPIO.LOW)
def backward():
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.HIGH)
	GPIO.output(in3, GPIO.LOW)
	GPIO.output(in4, GPIO.HIGH)
stop()
try:
	while True:
        #front sensor
		GPIO.output(f_TRIG, 0)
		time.sleep(0.1)
		GPIO.output(f_TRIG, 1)
		time.sleep(0.00001)
		GPIO.output(f_TRIG, 0)

		while GPIO.input(f_ECHO)==0:
			GPIO.output(f_led, False)
		f_pulse_start = time.time()
		while GPIO.input(f_ECHO)==1:
			GPIO.output(f_led, True)
		f_pulse_end = time.time()
		f_pulse_duration = f_pulse_end - f_pulse_start
		f_distance = f_pulse_duration*17150
		f_distance = round(f_distance, 2)
		#print(distance)


        #right sensor
		GPIO.output(r_TRIG, 0)
		time.sleep(0.1)
		GPIO.output(r_TRIG, 1)
		time.sleep(0.00001)
		GPIO.output(r_TRIG, 0)

		while GPIO.input(r_ECHO)==0:
			GPIO.output(r_led, False)
		r_pulse_start = time.time()
		while GPIO.input(r_ECHO)==1:
			GPIO.output(r_led, True)
		r_pulse_end = time.time()
		r_pulse_duration = r_pulse_end - r_pulse_start
		r_distance = r_pulse_duration*17150
		r_distance = round(r_distance, 2)


        #left sensor
		GPIO.output(l_TRIG, 0)
		time.sleep(0.1)
		GPIO.output(l_TRIG, 1)
		time.sleep(0.00001)
		GPIO.output(l_TRIG, 0)

		while GPIO.input(l_ECHO)==0:
			GPIO.output(l_led, False)
		l_pulse_start = time.time()
		while GPIO.input(l_ECHO)==1:
			GPIO.output(l_led, True)
		l_pulse_end = time.time()
		l_pulse_duration = l_pulse_end - l_pulse_start
		l_distance = l_pulse_duration*17150
		l_distance = round(l_distance, 2)


        #back sensor
		GPIO.output(b_TRIG, 0)
		time.sleep(0.1)
		GPIO.output(b_TRIG, 1)
		time.sleep(0.00001)
		GPIO.output(b_TRIG, 0)

		while GPIO.input(b_ECHO)==0:
			GPIO.output(b_led, False)
		b_pulse_start = time.time()
		while GPIO.input(b_ECHO)==1:
			GPIO.output(b_led, True)
		b_pulse_end = time.time()
		b_pulse_duration = b_pulse_end - b_pulse_start
		b_distance = b_pulse_duration*17150
		b_distance = round(b_distance, 2)
		if f_distance < 30.00:
			print("There is an object towards front at a distance of ",f_distance," cms")
			if r_distance < 20.00:
				print("There is an object right at a distance of ",r_distance," cms")
				if l_distance < 20.00:
					print("There is an object towards left at a distance of ",l_distance," cms")
					if b_distance < 30.00:
						print("There is an object towards back at a distance of ",b_distance," cms")
					else:
						stop()
						time.sleep(0.5)
						backward()
				else:
					stop()
					time.sleep(0.5)
					print("Turning left")
					left()
					time.sleep(2.3)
					forward()
			else:
				stop()
				time.sleep(0.5)
				print("Turning right")
				right()
				time.sleep(2.3)
				forward()
		else:
			forward()
		if b_distance < 30.00:
			print("There is an object towards back at a distance of ",b_distance," cms")
			forward()
			if f_distance < 30.00:
				print("There is an object towards front at a distance of ",f_distance," cms")
				if r_distance < 20.00:
					print("There is an object towards right at a distance of ",r_distance," cms")
					if l_distance < 20.00:
						print("There is an object towards left at a distance of",l_distance," cms")
						if b_distance < 30.00:
							print("There is an object towards backside at a distance of ",b_distance, " cms")
						else:
							backward()
					else:
						stop()
						time.sleep(0.5)
						print("turning left")
						left()
						time.sleep(2.3)
						forward()
				else:
					stop()
					time.sleep(0.5)
					print("Turning right")
					right()
					time.sleep(2.3)
					forward()
			else:
				print("Moving Forward")
				forward()

		if r_distance < 20.00:
			print("There is an object towards right at a distance of ",r_distance," cms")
			if l_distance < 20.00:
				print("There is a object towards left at a distance of ",l_distance," cms")
			else:
				stop()
				time.sleep(0.5)
				print("turning left")
				left()
				time.sleep(1)
				forward()
		if l_distance < 20.00:
			print("There is a object towards left at a distance of ",l_distance," cms")
			if r_distance < 20.00:
				print("There is a object towards right at a distance of ",r_distance," cms")
			else:
				stop()
				time.sleep(0.5)
				print("Turning right")
				right()
				time.sleep(1)
				forward()
		if f_distance < 30.00 and l_distance < 20.00 and r_distance < 20.00:
			backward()
finally:
	GPIO.cleanup()
	print(" Cleaned pins")
