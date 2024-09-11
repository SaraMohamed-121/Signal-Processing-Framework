import numpy as np
import matplotlib.pyplot as plt
#import points

file = open(r"C:\Users\user\Downloads\Term 9\Digital Signal Processing\Labs\Lab 1\Signals\signal1.txt","r")
l = file.readlines()
print("************************************************")
print("                  signal1 file                    ")
print("************************************************")
is_Freq = 0
is_Time = 0
SignalType = int(l[0])
if SignalType == 1:
    is_Freq = 1
    print("is Freq")
elif SignalType == 0:
    is_Time = 0
    print("is Time")

IsPeriodic = int(l[1])
if IsPeriodic == 1:
    print("Is Periodic")
elif IsPeriodic == 0:
    print("Is Not Periodic")
N1 = int(l[2])
print("SignalType: ",SignalType) # Time-->0/Freq-->1
print("IsPeriodic: ",IsPeriodic)
print("number of samples (N1): ",N1) # number of samples to follow or number of frequencies to follow

print("points: \n")
x=[]
y=[]
'''for i in l[3:]:
    x.append(float(i[0:2]))
    y.append(float(i[2:]))'''
for i in l[3:]:
        line_ = i.split(" ")
        x.append(float(line_[0]))
        y.append(float(line_[1]))
print("x= ",x)
print("y= ",y)
print("length of (x): ",len(x))
print("length of (y): ",len(y))


'''x = [p[0] for p in points]
y = [p[1] for p in points]'''
#'''for inx in len(x):

plt.title("Task 1 discrete")
plt.xlabel("Time")
plt.ylabel("Freq Amp PhaseShift")
dis = plt.scatter(x,y)
plt.show()

plt.title("Task 1 continuous")
plt.xlabel('Time')
plt.ylabel("Amp")
plt.axhline()
plt.colormaps()
con = plt.plot(x,y)
plt.show()

plt.title("Task 1 discrete an continuous")
plt.xlabel('Time')
plt.ylabel("Amp")
plt.scatter(x,y)
plt.plot(x,y)
plt.show()

print("___________________")
file.close()

#////////////////////task 2///////////////////////////
sin_cos_input = r'C:\Users\user\Downloads\Term 9\Digital Signal Processing\Labs\Lab 1\Signals\Sin_Cos\Inputs.txt'
sin_input = r'C:\Users\user\Downloads\Term 9\Digital Signal Processing\Labs\Lab 1\Signals\Sin_Cos\Inputs2.txt'

file2 = open(sin_cos_input, 'r')
linesf2 = file2.readlines()
print("************************************************")
print("                  input file                    ")
print("************************************************")
'''for o in linesf2[:]:
    if o == " " or o == "______________________________________" or o == None :
        continue
    else:
        lin2 = o.split("=")
        print(lin2[0], " : ", lin2[1])
'''
kv_pairsc = {}
kv_pairss = {}


'''with open(sin_input, 'r') as file:
    for line in file:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            kv_pairss[key] = value

with open(sin_cos_input, 'r') as file:
    for line in file:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            kv_pairsc[key] = value'''

'''cos_params = {}
sin_params = {}
for line in file:
    if line.strip() == "":
        continue
    parts = line.strip().split('=')
    if len(parts) == 2:
        key = parts[0].strip()
        value = parts[1].strip()
    if key == "type":
        cos_params[key] = value.strip()
    else:
        sin_params[key] = (value)
'''
for key, value in kv_pairss.items():
    print(f"Key: {key}, Value: {value}")

for key, value in kv_pairsc.items():
    print(f"Key: {key}, Value: {value}")

n_sin = 720
n_cos = 500
signals =[]
#kv_pairss["type"] = "sin"
#kv_pairsc["type"] = "cos"
#stype = kv_pairsc["type"]
#print(stype)
#stypes = kv_pairss["type"]
#print(stypes)

#----------------------------------------------
print("___________________")
l_c =[]
l_s =[]
#---------------------------------------------------------------------
from tkinter import *
pro = Tk()
pro.title("Signal processing")
sin_clk = 0
def sin_menu():
    sin_clk = 1
    cos_clk = 1
    kv_pairss["type"] = "sin"
    print("choose :",kv_pairss["type"])
    #filewin = Toplevel(pro)
    text_label = Label(pro, text="Amplitude")
    text_label.pack()
    text_A = Entry(pro)
    text_A.pack()

    text_label = Label(pro, text="Analog Frequency")
    text_label.pack()
    text_F = Entry(pro)
    text_F.pack()

    text_label = Label(pro, text="Sampling Frequency")
    text_label.pack()
    text_Fs = Entry(pro)
    text_Fs.pack()

    text_label = Label(pro, text="Phase Shift")
    text_label.pack()
    text_theta = Entry(pro)
    text_theta.pack()

    def save_value():
        A = float(text_A.get())
        print("Amplitude Value :", A)
        F = float(text_F.get())
        print("Analog Frequency Value :", F)
        Freqs = float(text_Fs.get())
        print("Sampling Frequency Value :", Freqs)
        theta = float(text_theta.get())
        print("Phase Shift Value :", theta)
        kv_pairss["A"] = A
        kv_pairss["AnalogFrequency"] = F
        kv_pairss["SamplingFrequency"] = Freqs
        kv_pairss["PhaseShift"] = theta
        print(type(Freqs))
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        for key, value in kv_pairss.items():
            print(f"Key: {key}, Value: {value}")


        if kv_pairss["type"] == "sin":
            #print("//////////////sin//////////////")
            if kv_pairss["SamplingFrequency"] == 0:
                t = np.linspace(0, 1, 1000)
                sin_signal = kv_pairss["A"] * np.sin(2 * np.pi * (kv_pairss["AnalogFrequency"]) * t + kv_pairss["PhaseShift"])
                print(sin_signal)
                kv_pairss["l_s"] = sin_signal
                plt.title("Task 1 sin Fs = 0")
                plt.xlabel('Time')
                plt.ylabel("Amp")
                plt.plot(t, sin_signal)
                plt.show()
            else:
                t = np.arange(0, 2, 0.5)
                sin_signal = kv_pairss["A"] * np.sin(2 * np.pi * (kv_pairss["AnalogFrequency"]/kv_pairss["SamplingFrequency"]) * t + kv_pairss["PhaseShift"])
                print(sin_signal)
                kv_pairss["l_s"] = sin_signal
                print("kv_pairss[l_s]",kv_pairss["l_s"])
                plt.title("Task 1 sin discrete an continuous ")
                plt.xlabel('Time')
                plt.ylabel("Amp")
                plt.plot(t, sin_signal)
                plt.scatter(t, sin_signal)
                plt.show()




    save_button = Button(pro, text="Save", command=save_value)
    save_button.pack()



cos_clk = 0
def cos_menu():
        cos_clk = 1
        sin_clk = 1
        kv_pairsc["type"] = "cos"
        print("choose :", kv_pairsc["type"])

        text_label = Label(pro, text="Amplitude")
        text_label.pack()
        text_A = Entry(pro)
        text_A.pack()

        text_label = Label(pro, text="Analog Frequency")
        text_label.pack()
        text_F = Entry(pro)
        text_F.pack()

        text_label = Label(pro, text="Sampling Frequency")
        text_label.pack()
        text_Fs = Entry(pro)
        text_Fs.pack()

        text_label = Label(pro, text="Phase Shift")
        text_label.pack()
        text_theta = Entry(pro)
        text_theta.pack()

        def save_value():
            A = float(text_A.get())
            print("Amplitude Value :", A)
            F = float(text_F.get())
            print("Analog Frequency Value :", F)
            Freqs = float(text_Fs.get())
            print("Sampling Frequency Value :", Freqs)
            theta = float(text_theta.get())
            print("Phase Shift Value :", theta)

            kv_pairsc["A"] = A
            kv_pairsc["AnalogFrequency"] = F
            kv_pairsc["SamplingFrequency"] = Freqs
            kv_pairsc["PhaseShift"] = theta


            if kv_pairsc["type"] == "cos":
                if kv_pairsc["SamplingFrequency"] ==0:
                   t = np.linspace(0, 1, 1000)
                # print("//////////////cos//////////////")
                   cos_signal = kv_pairsc["A"] * np.sin(2 * np.pi * (kv_pairsc["AnalogFrequency"]) * t + kv_pairsc["PhaseShift"])
                   print(cos_signal)
                   plt.title("Task 1 cos Fs = 0")
                   plt.xlabel('Time')
                   plt.ylabel("Amp")
                   plt.plot(t, cos_signal)
                   plt.show()
                else:
                    t = np.arange(0, 2, 0.5)
                    cos_signal = kv_pairsc["A"] * np.sin(2 * np.pi * (kv_pairsc["AnalogFrequency"] / kv_pairsc["SamplingFrequency"]) * t + kv_pairsc["PhaseShift"])
                    print(cos_signal)
                    kv_pairsc["l_c"] = cos_signal
                    print("kv_pairsc[l_c] :", kv_pairsc["l_c"])
                    plt.title("Task 1 cos discrete an continuous ")
                    plt.xlabel('Time')
                    plt.ylabel("Amp")
                    plt.plot(t, cos_signal)
                    plt.scatter(t, cos_signal)
                    plt.show()
                    plot_2signal()



        save_button = Button(pro, text="Save", command=save_value)
        save_button.pack()

        save_button = Button(pro, text="Draw 2 signal", command=plot_2signal)
        save_button.pack()


#---------------------------------
def multi ():
    text_label = Label(pro, text="mul_num")
    text_label.pack()
    text_m = Entry(pro)
    text_m.pack()

    def save_value():
        m = float(text_m.get())
        print("mul_num Value :", m)
        signal1 = r'C:\Users\hp zook\Videos\dsp\task2\input signals (1)\Signal1.txt'
        s1 = open(signal1, 'r')

        r = []
        p = []
        w = s1.readlines()
        for i in w[3:]:
            line_ = i.split(" ")
            r.append(float(line_[0]))
            p.append(float(line_[1]))
        print("x= ", x)
        print("y= ", y)
        print("length of (x): ", len(r))
        print("length of (y): ", len(p))
        # Multiply the signal array by 5
        for j in p:
            signal1_multiplied_by_value = j * m
        #    Print the multiplied signal array
            print(signal1_multiplied_by_value)
    save_button = Button(pro, text="Save", command=save_value)
    save_button.pack()


menubar = Menu(pro)
f = Menu(menubar, tearoff=0)
f.add_command(label='Sin',command=sin_menu)
f.add_command(label='Cos',command=cos_menu)
f.add_separator()
f.add_command(label='Exit',command=pro.quit)
menubar.add_cascade(label='Signal Generation',menu=f)
pro.config(menu=menubar)
l_cc = []
l_ss = []
def plot_2signal():

    l_cc = kv_pairsc["l_c"]
    l_ss = kv_pairss["l_s"]
    print(l_ss,l_cc,"gggggg")
   # if sin_clk == 1 and cos_clk == 1:
    t = np.arange(0, 2, 0.5)
    plt.title("Task 1 sin and cos")
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(t, l_cc)
    plt.plot(t, l_ss)
    plt.tight_layout()
    plt.show()



pro.mainloop()