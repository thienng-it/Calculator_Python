from tkinter import *
import playsound
import pygame

pygame.init()

sound = pygame.mixer.Sound("beep.wav")
# Các hàm tự định nghĩa cho calculator
# Hàm nhấn nút
def button_Click(numbers):
	global operator
	pygame.mixer.Sound.play(sound)
	# playsound.playsound("beep.wav", block=False)
	operator = operator + str(numbers)
	text_Input.set(operator)
# Hàm xóa
def button_Clear():
	global operator
	pygame.mixer.Sound.play(sound)
	# playsound("beep.wav", block=False)
	operator = ""
	text_Input.set("")
# Hàm đưa ra kết quả
def button_Equal():
	global operator # Biến global
	pygame.mixer.Sound.play(sound)
	# playsound("beep.wav", block=False) # block=False để phát ra âm thanh cùng lúc khi bấm nút
	result = str(eval(operator)) # Sử dụng eval() để tính một chuỗi biểu thức
	text_Input.set(result) # Hàm set() để hiển thị trên màn hình 

cal = Tk() # tạo frame cho ứng dụng
cal.title("Calculator") # Tiêu đề của frame

operator = ""
text_Input = StringVar() # Phần nhập vào là biến kiểu string
# Entry() phần nhập dữ liệu vào trên khung
txtDisplay = Entry(cal, width=30, font=("arial", 20, "bold"), textvariable = text_Input, bd=30, insertwidth=4, bg="aqua", justify="right").grid(columnspan=4)

# Tạo các nút trên úng dụng
""" 
cal: nút hiển thị trên khung ứng dụng
padx: kích cỡ của nút
bd: viền của nút
fg: màu chữ
font: kiểu chữ (kích cỡ và định dạng)
text: nội dung hiển thị trên nút
command: chức năng của nút dựa trên hàm def
bg: màu của nút
grid(): phân cột, hàng cho nút trên khung 
columnspan: một ô phân chia ra n cột
"""
button7 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="7", command=lambda:button_Click(7), bg="silver").grid(row=1, column=0)
button8 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="8", command=lambda:button_Click(8), bg="silver").grid(row=1, column=1)
button9 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="9", command=lambda:button_Click(9), bg="silver").grid(row=1, column=2)
button_Multiplication = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="x", command=lambda:button_Click("*"), bg="silver").grid(row=1, column=3)
# ----------------------------------------------------------------------------------------------------------------------------------
button4 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="4", command=lambda:button_Click(4), bg="silver").grid(row=2, column=0)
button5 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="5", command=lambda:button_Click(5), bg="silver").grid(row=2, column=1)
button6 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="6", command=lambda:button_Click(6), bg="silver").grid(row=2, column=2)
button_Division = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text=":", command=lambda:button_Click("/"), bg="silver").grid(row=2, column=3)
# ----------------------------------------------------------------------------------------------------------------------------------
button1 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="1", command=lambda:button_Click(1), bg="silver").grid(row=3, column=0)
button2 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="2", command=lambda:button_Click(2), bg="silver").grid(row=3, column=1)
button3 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="3", command=lambda:button_Click(3), bg="silver").grid(row=3, column=2)
button_Addition = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="+", command=lambda:button_Click("+"), bg="silver").grid(row=3, column=3)
# ----------------------------------------------------------------------------------------------------------------------------------
button_LeftParathesis = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="(", command=lambda:button_Click("("), bg="silver").grid(row=4, column=0)
button0 = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="0", command=lambda:button_Click(0), bg="silver").grid(row=4, column=1)
button_RightParathesis = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text=")", command=lambda:button_Click(")"), bg="silver").grid(row=4, column=2)
button_Subtraction = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="-", command=lambda:button_Click("-"), bg="silver").grid(row=4, column=3)
# ----------------------------------------------------------------------------------------------------------------------------------
button_Clear = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text="C", command=button_Clear, bg="silver").grid(row=5, column=0)
button_Dot = Button(cal, padx=30, bd=8, fg="black", font=("arial", 20, "bold"), text=".", command=lambda:button_Click("."), bg="silver").grid(row=5, column=1)
button_Equal = Button(cal, padx=90, bd=8, fg="black", font=("arial", 20, "bold"), text="=", command=button_Equal, bg="silver").grid(row=5, column=2, columnspan=2)

# mainloop(): tạo vòng lặp hiển thị cho khung ứng dụng
cal.mainloop()
