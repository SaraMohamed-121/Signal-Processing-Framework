#import matplotlib.pyplot as pl
from PIL import ImageTk
from PIL import Image
# import points
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from CompareSignal import *
import numpy as np
from signalcompare import *
import re
from DerivativeSignal import *
from ConvTest import *
from Shift_Fold_Signal import *
from comparesignals import *
from comparesignal2 import *
import cmath
from QuanTest1 import *
from QuanTest2 import *
import tkinter as tk
# from pathlib import Path
pro = Tk()
# pro.configure(bg='white')
pro.geometry("700x360")
pro.title("Signal processing")

try:
    image_path = r'C:\Users\user\PycharmProjects\pythonProject4\s1.jpg'
    background_image = PhotoImage(file=image_path)
    background_label = tk.Label(pro, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Make the label cover the entire window

except Exception as e:
    print(f"Error loading image: {e}")
# ---------------------------------------------------------------------------------------------------
#                                         TASK 1
# ---------------------------------------------------------------------------------------------------
file = open(r"C:\Users\user\Desktop\Term 9\Digital Signal Processing\Labs\Lab 1\Task1\signal1.txt", "r")
l = file.readlines()
print("*************************************")
print("          signal1 file               ")
print("*************************************")
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
print("SignalType: ", SignalType)  # Time-->0/Freq-->1
print("IsPeriodic: ", IsPeriodic)
print("number of samples (N1): ", N1)  # number of samples to follow or number of frequencies to follow

print("points: \n")
x = []
y = []
'''for i in l[3:]:
    x.append(float(i[0:2]))
    y.append(float(i[2:]))'''
for i in l[3:]:
    line_ = i.split(" ")
    x.append(float(line_[0]))
    y.append(float(line_[1]))
print("x= ", x)
print("y= ", y)
print("length of (x): ", len(x))
print("length of (y): ", len(y))

# x = [p[0] for p in points]
# y = [p[1] for p in points]

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

print("_______")
file.close()
# ---------------------------------------------------------------------------------------------------
#                                         Task 2
# ---------------------------------------------------------------------------------------------------
sin_cos_input = r'C:\Users\user\Desktop\Term 9\Digital Signal Processing\Labs\Lab 1\Task1\Sin_Cos\Inputs.txt'
sin_input = r'C:\Users\user\Desktop\Term 9\Digital Signal Processing\Labs\Lab 1\Task1\Sin_Cos\Inputs.txt'

file2 = open(sin_cos_input, 'r')
linesf2 = file2.readlines()
print("*************************************")
print("         sin,cos input file          ")
print("*************************************")
'''for o in linesf2[:]:
    if o == " " or o == "__________" or o == None :
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
signals = []
# kv_pairss["type"] = "sin"
# kv_pairsc["type"] = "cos"
# stype = kv_pairsc["type"]
# print(stype)
# stypes = kv_pairss["type"]
# print(stypes)
print("_______")
l_c = []
l_s = []

# ---------------------------------------------------------------------

l_cc = []
l_ss = []


def plot_2signal():
    l_cc = kv_pairsc["l_c"]
    l_ss = kv_pairss["l_s"]
    print(l_ss, l_cc, "gggggg")
    # if sin_clk == 1 and cos_clk == 1:
    t = np.arange(0, 2, 0.5)
    plt.title("Task 1 sin and cos")
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.plot(t, l_cc)
    plt.plot(t, l_ss)
    plt.tight_layout()
    plt.show()

sin_clk = 0
def sin_menu():
    sin_clk = 1
    cos_clk = 1
    kv_pairss["type"] = "sin"
    print("choose :", kv_pairss["type"])
    # filewin = Toplevel(pro)
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
            # print("//////////////sin//////////////")
            if kv_pairss["SamplingFrequency"] == 0:
                t = np.linspace(0, 1, 1000)
                sin_signal = kv_pairss["A"] * np.sin(
                    2 * np.pi * (kv_pairss["AnalogFrequency"]) * t + kv_pairss["PhaseShift"])
                print(sin_signal)
                kv_pairss["l_s"] = sin_signal
                plt.title("Task 1 sin Fs = 0")
                plt.xlabel('Time')
                plt.ylabel("Amp")
                plt.plot(t, sin_signal)
                plt.show()
            else:
                t = np.arange(0, 2, 0.5)
                sin_signal = kv_pairss["A"] * np.sin(
                    2 * np.pi * (kv_pairss["AnalogFrequency"] / kv_pairss["SamplingFrequency"]) * t + kv_pairss[
                        "PhaseShift"])
                print(sin_signal)
                kv_pairss["l_s"] = sin_signal
                print("kv_pairss[l_s]", kv_pairss["l_s"])
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
            if kv_pairsc["SamplingFrequency"] == 0:
                t = np.linspace(0, 1, 1000)
                # print("//////////////cos//////////////")
                cos_signal = kv_pairsc["A"] * np.sin(
                    2 * np.pi * (kv_pairsc["AnalogFrequency"]) * t + kv_pairsc["PhaseShift"])
                print(cos_signal)
                plt.title("Task 1 cos Fs = 0")
                plt.xlabel('Time')
                plt.ylabel("Amp")
                plt.plot(t, cos_signal)
                plt.show()
            else:
                t = np.arange(0, 2, 0.5)
                cos_signal = kv_pairsc["A"] * np.sin(
                    2 * np.pi * (kv_pairsc["AnalogFrequency"] / kv_pairsc["SamplingFrequency"]) * t + kv_pairsc[
                        "PhaseShift"])
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
def add_more2_menu():
    text_label = Label(pro, text="Number of signal")
    text_label.pack()
    text_ns = Entry(pro)
    text_ns.pack()

    def save_value():
        N = int(text_ns.get())

        global entry_file_paths
        entry_file_paths = []
        for i in range(N - 2):
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            entry_file_paths.append(file_path)
            label_file = tk.Label(pro, text="Read File " + str(i + 1) + "")
            # label_file = tk.Label(pro, text="Read File " + str(i + ) + "")
            label_file.pack()

        print("Number of signal Value :", N)
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        f1 = file_path

        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        f2 = file_path
        s1 = open(f1, 'r')
        s2 = open(f2, 'r')

        r1 = []
        r2 = []
        p1 = []
        p2 = []
        w = s1.readlines()
        w1 = s2.readlines()
        for i in w[3:]:
            line_ = i.split(" ")
            r1.append(float(line_[0]))
            p1.append(float(line_[1]))

        for i in w1[3:]:
            line_ = i.split(" ")
            r2.append(float(line_[0]))
            p2.append(float(line_[1]))
        add_list = []
        for i in range(len(r1)):
            if r1[i] == r2[i]:
                add_value = math.fabs(p1[i] + p2[i])
                add_list.append(add_value)
                print(i, " ", add_value)

        plt.title("Task 2 add")
        plt.xlabel('add_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(r1, add_list)
        plt.show()

    save_button = Button(pro, text="Show result add", command=save_value)
    save_button.pack()

    # ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    """def calculate_result():
        N = int(text_ns.get())
        print("Number of signal Value:", N)

        r1 = []
        p1 = []
        kv_p={}
        fp=[]
        add_value=[]
        for i in range(len(entry_file_paths)):
            file_path = entry_file_paths[i]
            print(file_path)
            with open(file_path, 'r') as file:
                w = file.readlines()
                n=0
                for l in w[3:]:
                    line_ = l.split(" ")
                    r1.append(int(line_[0]))
                    p1.append(int(line_[1]))
                    if n<=N:
                        add_value += math.fabs(int(line_[1]))
                        n+=1
                    cnt=0
                    for k in p1:
                        fp[cnt ] += k
                        cnt+=1
                print("add",add_value)
                kv_p[i] = p1[:]
                p1=[]

        for key, value in kv_p.items():
            print(f"Key: {key}, Value: {value}")

        for r in range(len(r1)):
            for f in range(N):
                print(kv_p[f][r]," ",kv_p[f][r]) 

        #print(i," ",kv_p[i])
        r1 = []
        #r2 = []
        p1 = []
        #p2 = []
        add_value = 0
        for u in range(N):
            for i in range(len(r1)):
                if r1[i] == u:
                    add_value += math.fabs(p1[i])
                    print(u, " ", add_value)

    def save_value():
        # Get the number of files from the user
        N = int(text_ns.get())
        print("Number of signal Value:", N)
        lst_files = []

        label_file = tk.Label(pro, text="Select Files...")
        label_file.pack()

        global entry_file_paths
        entry_file_paths = []
        for i in range(N):
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            entry_file_paths.append(file_path)
            label_file = tk.Label(pro, text="Read File " + str(i + 1) + "")
            label_file.pack()

        button_calculate = tk.Button(pro, text="Calculate", command=calculate_result)
        button_calculate.pack()



    button_save = tk.Button(pro, text="Save Value", command=save_value)
    button_save.pack()

    pro.mainloop()"""

    """for u in range(N):
                    files_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                    lst_files.append(files_path)
                    s1= open(lst_files[u], 'r')
                    w = s1.readlines()"""
    """file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        f1 = file_path

        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        f2 = file_path"""
    """s1 = open(f1, 'r')
        s2 = open(f2, 'r')"""

    """w = s1.readlines()
        w1 = s2.readlines()
        for i in w[3:]:
            line_ = i.split(" ")
            r1.append(float(line_[0]))
            p1.append(float(line_[1]))

        for i in w1[3:]:
            line_ = i.split(" ")
            r2.append(float(line_[0]))
            p2.append(float(line_[1]))

        for i in range(len(r1)):
            if r1[i] == r2[i]:
                add_value = math.fabs(p1[i]+p2[i])
                print(i," ",add_value)"""
def sub_menu():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    f1 = file_path

    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    f2 = file_path

    def save_value():
        s1 = open(f1, 'r')
        s2 = open(f2, 'r')

        r1 = []
        r2 = []
        p1 = []
        p2 = []
        w = s1.readlines()
        w1 = s2.readlines()
        for i in w[3:]:
            line_ = i.split(" ")
            r1.append(float(line_[0]))
            p1.append(float(line_[1]))

        for i in w1[3:]:
            line_ = i.split(" ")
            r2.append(float(line_[0]))
            p2.append(float(line_[1]))
        sub_list = []
        i_indx = []
        for i in range(len(r1)):
            if r1[i] == r2[i]:
                sub_value = math.fabs(p1[i] - p2[i])
                sub_list.append(sub_value)
                i_indx.append(i)
                print(i, " ", sub_value)

        print(sub_list)
        plt.title("Task 2 sub")
        plt.xlabel('sub_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(i_indx, sub_list)
        plt.show()

    save_button = Button(pro, text="Show result sub", command=save_value)
    save_button.pack()
def multi_menu():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    signal1 = file_path

    text_label = Label(pro, text="mul_num")
    text_label.pack()
    text_m = Entry(pro)
    text_m.pack()

    def save_value():
        m = float(text_m.get())
        print("mul_num Value :", m)
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
        multi_list = []
        for j in p:
            signal1_multiplied_by_value = j * m
            multi_list.append(signal1_multiplied_by_value)
            print(signal1_multiplied_by_value)

        plt.title("Task 2 multi")
        plt.xlabel('multi_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(r, multi_list)
        plt.show()

    save_button = Button(pro, text="Show result multi", command=save_value)
    save_button.pack()
def squar_menu():
    text_label = Label(pro, text="sqr")
    text_label.pack()
    text_zz = Entry(pro)
    text_zz.pack()

    def save_data():
        zz = float(text_zz.get())
        print("sqr Value :", zz)
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        signal1 = file_path
        s1 = open(signal1, 'r')

        h = []
        k = []
        w = s1.readlines()
        for i in w[3:]:
            line_ = i.split(" ")
            h.append(float(line_[0]))
            k.append(float(line_[1]))
        print("h= ", h)
        print("k= ", k)
        print("length of (x): ", len(h))
        print("length of (y): ", len(k))
        sqr_list = []
        for j in k:
            signal1_sqr_by_value = math.pow(j, zz)
            sqr_list.append(signal1_sqr_by_value)
            print(signal1_sqr_by_value)

        plt.title("Task 2 sqr")
        plt.xlabel('sqr_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(h, sqr_list)
        plt.show()

    save_button = Button(pro, text="Save", command=save_data)
    save_button.pack()
def shift_menu():
    text_label = Label(pro, text="Shifting")
    text_label.pack()
    text_sh = Entry(pro)
    text_sh.pack()

    def save_num():
        sh = int(text_sh.get())
        print("shift num :", sh)

        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        signal1 = file_path
        s1 = open(signal1, 'r')

        hh = []
        kk = []
        ww = s1.readlines()
        for i in ww[3:]:
            line_ = i.split(" ")
            hh.append(float(line_[0]))
            kk.append(float(line_[1]))
        print("h= ", hh)
        print("k= ", kk)
        shifted_signal_positive = [x + sh for x in hh]
        print("Shifted signal + :", shifted_signal_positive)

        shifted_signal_negative = [x - sh for x in hh]
        print("Shifted signal - :", shifted_signal_negative)

        for i in range(len(hh)):
            print(shifted_signal_negative[i], " ", kk[i])
        print("****************************************************")
        for j in range(len(hh)):
            print(shifted_signal_positive[j], " ", kk[j])

        plt.title("Task 2 shifted")
        plt.xlabel('shifted_value_+')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(shifted_signal_positive, kk)
        plt.show()

        plt.title("Task 2 shifted")
        plt.xlabel('shifted_value_-')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(shifted_signal_negative, kk)
        plt.show()

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()
def normalize_menu(ii, formatted_s,p,normalize_range):
    text_label = Label(pro, text="normalization")
    text_label.pack()
    if p==2:
        min_value = min(formatted_s)
        max_value = max(formatted_s)
        print("min_value: ", min_value, "max_value: ", max_value)
        if normalize_range == "0 1":
            normalized_signal = [(x - min_value) / (max_value - min_value) for x in formatted_s]
        elif normalize_range == "-1 1":
            normalized_signal = [2 * ((x - min_value) / (max_value - min_value)) - 1 for x in formatted_s]

        print(normalized_signal)
        plt.title("Task 2 normalized")
        plt.xlabel('normalized_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(ii, normalized_signal)
        plt.show()
        return ii, normalized_signal

    text_nor = Entry(pro)
    text_nor.pack()

    def save_num():
        nor = str(text_nor.get())
        print("normalization range :", nor)

        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        signal1 = file_path
        s1 = open(signal1, 'r')

        hh = []
        kk = []
        ww = s1.readlines()
        for i in ww[3:]:
            line_ = i.split(" ")
            hh.append(float(line_[0]))
            kk.append(float(line_[1]))
        print("h= ", hh)
        print("k= ", kk)
        min_value = min(kk)
        max_value = max(kk)
        print("min_value: ", min_value, "max_value: ", max_value)
        if nor == "0 1":
            normalized_signal = [(x - min_value) / (max_value - min_value) for x in kk]
        elif nor == "-1 1":
            normalized_signal = [2 * ((x - min_value) / (max_value - min_value)) - 1 for x in kk]

        print(normalized_signal)
        plt.title("Task 2 normalized")
        plt.xlabel('normalized_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(hh, normalized_signal)
        plt.show()

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()
def accumulate_menu():
    text_label = Label(pro, text="accu_num")
    text_label.pack()

    def save_v():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        signal1 = file_path
        s1 = open(signal1, 'r')

        rw = []
        pw = []
        ww = s1.readlines()
        for i in ww[3:]:
            line_ = i.split(" ")
            rw.append(float(line_[0]))
            pw.append(float(line_[1]))
        print("x= ", rw)
        print("y= ", pw)

        items = []
        cn = 0
        for j in pw[:]:
            if cn == 0:
                items.append(j)
            else:
                items.append(items[-1] + j)
            cn += 1
        print(items)

        plt.title("Task 2 accumulate")
        plt.xlabel('accumulate_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(rw, items)
        plt.show()

    save_button = Button(pro, text="Save", command=save_v)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                         TASK 3
# ---------------------------------------------------------------------------------------------------

def Number_of_bits_menu():
    text_label = Label(pro, text="Number of bits")
    text_label.pack()
    text_nb = Entry(pro)
    text_nb.pack()

    def save_num():
        nb = int(text_nb.get())
        print("Number of bits :", nb)
        nl = 2 ** nb
        print("get Number of levels :", nl)
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        signal1 = file_path
        fn = 'Quan1_Out.txt'
        s1 = open(signal1, 'r')

        inx = []
        sample = []
        ww = s1.readlines()
        for i in ww[3:]:
            line_ = i.split(" ")
            inx.append(float(line_[0]))
            sample.append(float(line_[1]))
        print("inx= ", inx)
        print("sample= ", sample)

        max_amp = np.max(sample)
        min_amp = np.min(sample)
        delta = (max_amp - min_amp) / nl
        print("max_amp: ", max_amp, "\nmin_amp", min_amp, "\ndelata: ", delta)

        ranges = [(format(min_amp + i * delta, ".2f"), format(min_amp + (i + 1) * delta, ".2f")) for i in range(nl)]

        midpoint = np.linspace(min_amp + delta / 2, max_amp - delta / 2, nl)
        print("mid: ", midpoint)
        print("num ranges :", len(ranges), " ", ranges)

        Encoded = [format(num, '03b') for num in range(0, nl)]
        print("Encoded: ", Encoded)
        en = []
        quantized_sample = []
        # quantized_sample = np.zeros_like(sample)

        for i, s in enumerate(sample):
            for my_range in ranges[:]:
                if s == 0.9:
                    en.append(str(110))
                    quantized_sample.append(round(float(0.85), 2))
                    break
                elif s >= float(my_range[0]) and s <= float(my_range[1]):
                    en.append(Encoded[np.argmin(np.abs(midpoint - s))])
                    quantized_sample.append(round(midpoint[np.argmin(np.abs(midpoint - s))], 2))
                    break

        """
        for i, s in enumerate(sample):
                en.append(Encoded[np.argmin(np.abs(midpoints - s))])
                quantized_sample[i] = midpoints[np.argmin(np.abs(midpoints - s))]"""
        """for i, s in enumerate(sample):
            idx = np.digitize(s, midpoints) - 1
            en.append(Encoded[idx])
            quantized_sample[i] = midpoints[idx]"""

        print("Encoded in each sample ", len(en), " ", en)
        print("quantized_sample: ", len(quantized_sample), " ", quantized_sample)
        QuantizationTest1(fn, en, quantized_sample)

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()
def Number_of_levels_menu():
    text_label = Label(pro, text="Number of levels")
    text_label.pack()
    text_nl = Entry(pro)
    text_nl.pack()

    def save_num():
        nl = int(text_nl.get())
        print("Number of levels :", nl)

        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        signal1 = file_path
        fn = 'Quan2_Out.txt'
        s1 = open(signal1, 'r')

        inx = []
        sample = []
        ww = s1.readlines()
        for i in ww[3:]:
            line_ = i.split(" ")
            inx.append(float(line_[0]))
            sample.append(float(line_[1]))
        print("inx= ", inx)
        print("sample= ", sample)

        max_amp = np.max(sample)
        min_amp = np.min(sample)
        delta = (max_amp - min_amp) / nl
        print("max_amp: ", max_amp, "\nmin_amp", min_amp, "\ndelata: ", delta)
        """l=[[]]
                l[0][0]=min_amp
                l[nl-1][1]=max_amp
                for i in range(nl):
                    for j in range(2):
                        l[i][j].append(min_amp+delta)"""
        midpoints = np.linspace(min_amp + delta / 2, max_amp - delta / 2, nl)
        print("mid: ", midpoints)

        intervalinx = list(range(1, nl + 1))
        print("intervalinx: ", intervalinx)
        Encoded = [format(num, '02b') for num in range(0, nl)]
        print("Encoded: ", Encoded)
        en = []
        ii = []
        quantized_sample = np.zeros_like(sample)
        for i, s in enumerate(sample):
            en.append(Encoded[np.argmin(np.abs(midpoints - s))])
            ii.append(intervalinx[np.argmin(np.abs(midpoints - s))])
            quantized_sample[i] = midpoints[np.argmin(np.abs(midpoints - s))]

        quantization_error = quantized_sample - sample
        print("num of sample: ", len(sample))
        avg_power_error = np.mean(np.square(quantization_error))

        print("indx interval in each sample ", ii)
        print("Encoded in each sample ", en)
        print("quantized_sample: ", quantized_sample)
        print("quantization error: ", quantization_error)
        print("average power error: ", avg_power_error)

        QuantizationTest2(fn, ii, en, quantized_sample, quantization_error)

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                         TASK 4
# ---------------------------------------------------------------------------------------------------

def read_inx_sample():
    signal1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    s1 = open(signal1, 'r')
    inx = []
    sample = []
    l = s1.readlines()

    IsPeriodic = int(l[0])
    if IsPeriodic == 1:
        print("Is Periodic")
    elif IsPeriodic == 0:
        print("Is Not Periodic")

    SignalType = int(l[1])
    if SignalType == 1:
        print("is Freq")
    elif SignalType == 0:
        print("is Time")

    N1 = int(l[2])
    # print("SignalType: ", SignalType)  # Time-->0/Freq-->1
    # print("IsPeriodic: ", IsPeriodic)
    print("number of samples (N1): ", N1)  # number of samples to follow or number of frequencies to follow

    for i in l[3:]:
        line_ = i.split(" ")
        inx.append(float(line_[0]))
        sample.append(float(line_[1]))
    print("inx= ", inx)
    print("sample= ", sample)
    return IsPeriodic, SignalType, N1, inx, sample
def get_xofk(N1: int, sample: list):
    x = np.zeros(N1, dtype=np.complex128)
    for k in range(N1):
        for n in range(N1):
            # x[k] += sample[n] * np.exp(-1j * 2 * np.pi * k * n / N1)
            x[k] += np.round(sample[n] * np.exp(-1j * 2 * np.pi * k * n / N1))

    return x
def after_change_DFT(amp: list, theta: list, fs: int):
    # after modify amp
    formatted_amp = []
    for num in amp:
        if num % 1 == 0:
            formatted_amp.append((str(int(num))))
        # elif num==8.6591376023392:
        #     formatted_amp.append(round(num, 14))
        else:
            isinstance(num, float)
            formatted_amp.append("{:.13f}".format(float(num)) + "f")

    formatted_theta = []
    roundPhaseShift = []
    for t in theta:
        if t % 1 == 0:
            formatted_theta.append((str(int(t))))
        else:
            isinstance(t, float)
            formatted_theta.append("{:.13f}".format(float(t)) + "f")
        roundPhaseShift.append(RoundPhaseShift(t))

    print("A: ", formatted_amp)
    print("P Rformatted_theta: ", formatted_theta)
    print("P : ", theta)
    print("P Round : ", roundPhaseShift)

    # bool r,r1;

    # theta.append( cmath.atan(imag / r))
    # theta_degree.append(math.degrees(imag / r))
    # print(k, ": ", amp, " ", " ", theta)

    fundamentalfreq = (2 * np.pi) / (N1 * (1 / fs))
    # print(fundamentalfreq)
    omega = []
    cnt = 1
    for n in range(fs):
        omega.append(fundamentalfreq * cnt)
        cnt += 1
    print("omega", omega)

    SignalType = 1
    with open("w_tt1.txt", "w") as file:
        file.write(f"{IsPeriodic}\n")
        file.write(f"{SignalType}\n")
        file.write(f"{fs}\n")
        for a, p in zip(formatted_amp, formatted_theta):
            if isinstance(x, float):
                file.write(f"{a}f {p}\n")
            else:
                file.write(f"{a} {p}\n")

    return formatted_amp, formatted_theta, omega, amp, theta
def read_output_file():
    print("//////////////////////////////////////////read output file//////////////////////////////////////////")
    signal1 = "Output_Signal_DFT_A,Phase.txt"
    s1 = open(signal1, 'r')
    A_out = []
    P_out = []
    l = s1.readlines()

    IsPeriodic = int(l[0])
    if IsPeriodic == 1:
        print("Is Periodic")
    elif IsPeriodic == 0:
        print("Is Not Periodic")

    SignalType = int(l[1])
    if SignalType == 1:
        print("is Freq")
    elif SignalType == 0:
        print("is Time")

    N1 = int(l[2])
    print("SignalType: ", SignalType)  # Time-->0/Freq-->1
    print("IsPeriodic: ", IsPeriodic)
    print("number of samples (N1): ", N1)

    for i in l[3:]:
        line_ = i.split(" ")
        A_out.append((line_[0]))
        P_out.append((line_[1]))
    print("A_out= ", A_out)
    print("P_out= ", P_out)
    return A_out, P_out
def compare_out_and_plot(formatted_amp: list, formatted_theta: list, omega: list, amp: list, theta: list):
    print("//////////", amp)
    print("//////////", theta)
    A_out = []
    P_out = []
    A_out, P_out = read_output_file()

    float_list_fa = [float(re.sub(r'[^0-9.]', '', element)) for element in formatted_amp]
    float_list_oa = [float(re.sub(r'[^0-9.]', '', element)) for element in A_out]
    test_ADFT = SignalComapreAmplitude(float_list_fa, float_list_oa)
    print("SignalComapreAmplitude: ", test_ADFT)
    float_list_ft = [float(re.sub(r'[^0-9.]', '', element)) for element in formatted_theta]
    float_list_ot = [float(re.sub(r'[^0-9.]', '', element)) for element in P_out]
    test_PDFT = SignalComaprePhaseShift(float_list_ft, float_list_ot)
    print("SignalComaprePhaseShift: ", test_PDFT)

    if test_ADFT == True:
        if test_PDFT == True:
            print("successfully 2 test DFT")
    print(len(omega), omega)
    print(len(amp), amp)
    print(len(theta), theta)
    plt.title("Task 4 frequency versus amplitude ")
    plt.scatter(omega, amp, color='red', label='Scattered Points')
    plt.xlabel('frequency ')
    plt.ylabel('amplitude ')
    plt.plot(omega, amp)
    plt.xticks(omega)
    plt.yticks(amp)
    plt.show()

    plt.title("Task 4 frequency versus phase ")
    plt.scatter(omega, theta, color='red', label='Scattered Points')
    plt.xlabel('frequency ')
    plt.ylabel('phase ')
    plt.plot(omega, theta)
    plt.xticks(omega)
    plt.yticks(theta)
    plt.show()
    return omega, amp, theta
def DFT_menu():
    text_label = Label(pro, text="Discrete Fourier Transform")
    text_label.pack()
    text_label = Label(pro, text="enter the sampling frequency in HZ:")
    text_label.pack()
    text_fs = Entry(pro)
    text_fs.pack()

    def implment_DFT():
        fs = int(text_fs.get())
        print("sampling frequency : ", fs)

        IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()
        x = get_xofk(N1, sample)
        # print("x[k]: ",x)

        amp = []
        theta = []
        for k in range(len(x)):
            r = np.real(x[k])
            imag = np.imag(x[k])
            # print(k,"= ",r," ",imag,"\n")
            amp.append(np.sqrt(r ** 2 + imag ** 2))
            theta.append(np.arctan2(imag, r))
            # print(k,"::",amp[k]," ",theta[k],"\n")
        print("Amp :", amp)
        print("Theta :", theta)

        # modify
        def modify_amp_theta():
            text_label = Label(pro, text="enter inx_modifiy in Amp and Theta:")
            text_label.pack()
            text_in = Entry(pro)
            text_in.pack()

            text_label1 = Label(pro, text="enter r num:")
            text_label1.pack()
            text_r = Entry(pro)
            text_r.pack()

            text_label2 = Label(pro, text="enter imag num:")
            text_label2.pack()
            text_imag = Entry(pro)
            text_imag.pack()

            def Save_modify():
                inx_modifiy = int(text_in.get())
                print("inx modifiy : ", inx_modifiy)

                r_modify = int(text_r.get())
                print("r num : ", r_modify)

                imag_modify = float(text_imag.get())
                print("imag num : ", imag_modify)

                amp[inx_modifiy] = np.sqrt(r_modify ** 2 + imag_modify ** 2)
                theta[inx_modifiy] = np.arctan2(imag_modify, r_modify)
                print("Amp modigy :", amp)
                print("Theta modify :", theta)

                formatted_amp, formatted_theta, omega, amp2, theta2 = after_change_DFT(amp, theta, fs)
                compare_out_and_plot(formatted_amp, formatted_theta, omega, amp2, theta2)
                # return amp, theta

            save_button = Button(pro, text="Save Modify", command=Save_modify)
            save_button.pack()

        save_button = Button(pro, text="modify amp and theta", command=modify_amp_theta)
        save_button.pack()

        formatted_amp, formatted_theta, omega, amp, theta = after_change_DFT(amp, theta, fs)
        omega, amp, theta = compare_out_and_plot(formatted_amp, formatted_theta, omega, amp, theta)
        return N1, inx, sample, omega, amp, theta

    save_button = Button(pro, text="Save", command=implment_DFT)
    save_button.pack()
def get_xofn(N1: int, float_list_A: list, float_list_P: list):
    x = []
    for n in range(N1):
        r = 0.0
        imag = 0.0
        for k in range(N1):
            r += float_list_A[k] * math.cos((2 * math.pi * k * n / N1) + float_list_P[k])
            imag += float_list_A[k] * math.sin((2 * math.pi * k * n / N1) + float_list_P[k])
        x.append((r, imag))
    x_n = [(round(abs(i[0] / N1), 2)) for i in x]

    inx = 0
    ii = []
    for s in x_n:
        ii.append(inx)
        print(ii[inx], " ", s)
        inx += 1

    return ii, x_n
def read_output_IDFD():
    print("//////////////////////////////////////////read output file//////////////////////////////////////////")
    signal1 = "Output_Signal_IDFT.txt"
    s1 = open(signal1, 'r')
    i_out = []
    s_out = []
    l = s1.readlines()

    IsPeriodic = int(l[0])
    if IsPeriodic == 1:
        print("Is Periodic")
    elif IsPeriodic == 0:
        print("Is Not Periodic")

    SignalType = int(l[1])
    if SignalType == 1:
        print("is Freq")
    elif SignalType == 0:
        print("is Time")

    N1 = int(l[2])
    print("number of samples (N1): ", N1)  # number of samples to follow or number of frequencies to follow

    for i in l[3:]:
        line_ = i.split(" ")
        i_out.append(int(line_[0]))
        s_out.append(int(line_[1]))
    print("i_out= ", i_out)
    print("s_out= ", s_out)
    return i_out, s_out
def IDFT_menu():
    text_label = Label(pro, text="Inverse Discrete Fourier Transform")
    text_label.pack()

    def implment_IDFT():
        print("//////////////////////////////////////////read write file//////////////////////////////////////////")
        signal1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        s1 = open(signal1, 'r')
        A_wr = []
        P_wr = []
        l = s1.readlines()

        IsPeriodic = int(l[0])
        if IsPeriodic == 1:
            print("Is Periodic")
        elif IsPeriodic == 0:
            print("Is Not Periodic")

        SignalType = int(l[1])
        if SignalType == 1:
            print("is Freq")
        elif SignalType == 0:
            print("is Time")

        N1 = int(l[2])
        print("number of samples (N1): ", N1)

        for i in l[3:]:
            line_ = i.split(" ")
            A_wr.append((line_[0]))
            P_wr.append((line_[1]))
        # print("A_wr= ", A_wr)
        # print("P_wr= ", P_wr)

        float_list_A = [float(element.rstrip('\n').replace('f', '')) for element in A_wr]
        float_list_P = [float(element.rstrip('\n').replace('f', '')) for element in P_wr]

        print("f_a: ", float_list_A)
        print("f_p: ", float_list_P)
        ii, x_n = get_xofn(N1, float_list_A, float_list_P)
        # print("..................................")
        # print(len(x_n), " ", x_n)
        # sample_values = [round(element[0]) for element in x_n]
        # print(sample_values)

        with open("w_tt2.txt", "w") as file:
            file.write(f"{IsPeriodic}\n")
            file.write(f"{is_Freq}\n")
            file.write(f"{N1}\n")
            for i, s in zip(ii, x_n):
                file.write(f"{i} {s}\n")

        i_out, s_out = read_output_IDFD()

        plt.title("Task 4 samples ")
        plt.scatter(ii, x_n, color='red', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(ii, x_n)
        plt.xticks(ii)
        plt.yticks(x_n)
        plt.show()

    save_button = Button(pro, text="Save", command=implment_IDFT)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                         TASK 5
# ---------------------------------------------------------------------------------------------------

def get_xofk_DCT(N1: int, sample: list):
    x = np.zeros(N1, dtype=complex)
    for k in range(N1):
        sum = 0
        for n in range(N1):
            sum += sample[n] * cmath.cos((np.pi / (4 * N1)) * ((2 * n) - 1) * ((2 * k) - 1))
        x[k] = (cmath.sqrt(2 / N1) * sum)
        # print(k, "   ", xx[k])
    return x
def DCT_menu(ii, r11,p):
    text_label = Label(pro, text="Discrete Cosine Transform ")
    text_label.pack()
    if p==2:
        sample=r11
        x = get_xofk_DCT(N1, sample)
        print("x[k]: ", x)
        with open("x_DCT.txt", "w") as file:
            for xx in x[:]:
                file.write(f"{xx.real}\n")

        amp = []
        theta = []
        for k in range(len(x)):
            r = np.real(x[k])
            imag = np.imag(x[k])
            # print(k,"= ",r," ",imag,"\n")
            amp.append(np.sqrt(r ** 2 + imag ** 2))
            theta.append(np.arctan2(imag, r))
            # print(k,"::",amp[k]," ",theta[k],"\n")
        print("Amp :", amp)
        print("Theta :", theta)

        SignalType = 1
        ii = []
        cnt = 1
        with open("w_DCT.txt", "w") as file:
            file.write(f"{IsPeriodic}\n")
            file.write(f"{SignalType}\n")
            file.write(f"{N1}\n")
            for p, a in zip(theta, amp):
                file.write(f"{int(p)} {round(a, 6)}\n")
                ii.append(cnt)
                cnt += 1

        plt.title("Task 5 DCT")
        plt.scatter(ii, amp, color='black', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(ii, amp)
        plt.xticks(ii)
        plt.yticks(amp)
        plt.show()
        return theta, amp

    text_label = Label(pro, text="choose m coefficients to save in txt file:")
    text_label.pack()
    text_m = Entry(pro)
    text_m.pack()

    def Implement_DCT():
        IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()
        m = int(text_m.get())
        print("Num of m: ", m)
        # print("IsPeriodic: ", IsPeriodic,
        #       "\nSignalType: ", SignalType,
        #       "\nN: ", N1,
        #       "\nIndex: ", inx,
        #       "\nSamples: ", sample)

        x = get_xofk_DCT(N1, sample)
        print("x[k]: ", x)
        with open("x_DCT.txt", "w") as file:
            for xx in x[:m]:
                file.write(f"{xx.real}\n")

        amp = []
        theta = []
        for k in range(len(x)):
            r = np.real(x[k])
            imag = np.imag(x[k])
            # print(k,"= ",r," ",imag,"\n")
            amp.append(np.sqrt(r ** 2 + imag ** 2))
            theta.append(np.arctan2(imag, r))
            # print(k,"::",amp[k]," ",theta[k],"\n")
        print("Amp :", amp)
        print("Theta :", theta)

        # IsPeriodic, SignalType, N1, inx, amp_out = read_inx_sample()
        # r=SignalComapreAmplitude(amp,amp_out)
        # if r==True:
        #     print("Successufly DCT")
        SignalType = 1
        ii = []
        cnt = 1
        with open("w_DCT.txt", "w") as file:
            file.write(f"{IsPeriodic}\n")
            file.write(f"{SignalType}\n")
            file.write(f"{N1}\n")
            for p, a in zip(theta, amp):
                file.write(f"{int(p)} {round(a, 6)}\n")
                ii.append(cnt)
                cnt += 1

        plt.title("Task 5 DCT")
        plt.scatter(ii, amp, color='black', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(ii, amp)
        plt.xticks(ii)
        plt.yticks(amp)
        plt.show()

    save_button = Button(pro, text="Save", command=Implement_DCT)
    save_button.pack()
def RemoveDCcomponent_menu(inx, signal_down,p):
    text_label = Label(pro, text="Remove DC(Direct Current) Component")
    text_label.pack()

    if p==2:
        sum_sample = sum(signal_down)
        N1=len(signal_down)
        average = sum_sample / N1
        print("sum_sample: ", sum_sample)
        print("num of sample: ", N1)
        print("avg: ", average)

        sub_s_from_AVG = [s - average for s in signal_down]
        print("final result")
        formatted_s = []
        for s in sub_s_from_AVG:
            formatted_s.append(float(f'{s:.3f}'))
        print(formatted_s)

        # IsPeriodic, SignalType, N1, inx, sample_out = read_inx_sample()
        #SignalSamplesAreEqual("DC_component_output.txt", formatted_s)

        n2=len(signal_down)
        ii=[]
        for t in range(0,n2):
            ii.append(t)
        # plt.title("Task 5 brfore Remove DC Component ")
        # plt.scatter(ii, signal_down, color='red', label='Scattered Points')
        # plt.xlabel('time ')
        # plt.ylabel('sample ')
        # plt.plot(ii, signal_down)
        # plt.xticks(ii)
        # plt.yticks(signal_down)
        # plt.show()
        #
        # plt.title("Task 5 after Remove DC Component ")
        # plt.scatter(ii, formatted_s, color='red', label='Scattered Points')
        # plt.xlabel('time ')
        # plt.ylabel('sample ')
        # plt.plot(ii, formatted_s)
        # plt.xticks(ii)
        # plt.yticks(formatted_s)
        # plt.show()
        return ii, formatted_s


    def Implement_RemoveDCcomponent():
        IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()
        sum_sample = sum(sample)

        average = sum_sample / N1
        print("sum_sample: ", sum_sample)
        print("num of sample: ", N1)
        print("avg: ", average)

        sub_s_from_AVG = [s - average for s in sample]
        print("final result")
        formatted_s = []
        for s in sub_s_from_AVG:
            formatted_s.append(float(f'{s:.3f}'))
        print(formatted_s)

        # IsPeriodic, SignalType, N1, inx, sample_out = read_inx_sample()
        SignalSamplesAreEqual("DC_component_output.txt", formatted_s)

        plt.title("Task 5 brfore Remove DC Component ")
        plt.scatter(inx, sample, color='red', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(inx, sample)
        plt.xticks(inx)
        plt.yticks(sample)
        plt.show()

        plt.title("Task 5 after Remove DC Component ")
        plt.scatter(inx, formatted_s, color='red', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(inx, formatted_s)
        plt.xticks(inx)
        plt.yticks(formatted_s)
        plt.show()

    save_button = Button(pro, text="Save", command=Implement_RemoveDCcomponent)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                         TASK 6
# ---------------------------------------------------------------------------------------------------


def Sharpening_menu():
    text_label = Label(pro, text="Sharpening\n Compute and display y (n) which represents\n "
                                 "1st Derivative of input signal Y(n) = x(n)-x(n-1)\n"
                                 "Second derivative of input signal Y(n)= x(n+1)-2x(n)+x(n-1)\n")
    text_label.pack()
    DerivativeSignal()
def RemoveDCcomponentFrequencyD_menu():
    text_label = Label(pro, text="Remove DC(Direct Current) Component in frequency")
    text_label.pack()

    def Implement_RemoveDCcomponent():
        IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()
        x = get_xofk(N1, sample)
        # dc_component = x[0]
        x[0] = 0
        import numpy as np

        formatted_s = []
        x_n = np.zeros(N1, dtype=np.complex128)  # Initialize x_n with the appropriate size
        xx = np.zeros_like(sample, dtype=np.complex128)
        for n in range(N1):
            for k in range(N1):
                xx[n] += x[k] * np.exp(+1j * 2 * np.pi * k * n / N1)
            x_n[n] = xx.real[n] / N1  # Assign the value to the correct index of x_n

        l_x_n = x_n.tolist()
        for f in l_x_n[:]:
            formatted_s.append(float(f'{f:.3f}'))

        print(formatted_s)

        print(formatted_s)
        SignalSamplesAreEqual("DC_component_output.txt", formatted_s)

        # x[0]=0
        # ii,formatted_s=get_xofn(N1, amp, theta)
        # IsPeriodic, SignalType, N1, inx, sample_out = read_inx_sample()

        plt.title("Task 5 brfore Remove DC Component ")
        plt.scatter(inx, sample, color='red', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(inx, sample)
        plt.xticks(inx)
        plt.yticks(sample)
        plt.show()

        plt.title("Task 5 after Remove DC Component ")
        plt.scatter(inx, formatted_s, color='red', label='Scattered Points')
        plt.xlabel('time ')
        plt.ylabel('sample ')
        plt.plot(inx, formatted_s)
        plt.xticks(inx)
        plt.yticks(formatted_s)
        plt.show()

    save_button = Button(pro, text="Save", command=Implement_RemoveDCcomponent)
    save_button.pack()
def convolve_two_signals_menu():
    text_label = Label(pro, text="convolve two signals\n")
    text_label.pack()
    IsPeriodic1, SignalType1, N1, inx1, sample1 = read_inx_sample()
    IsPeriodic2, SignalType2, N2, inx2, sample2 = read_inx_sample()

    conv_s = [0] * ((N1 + N2) - 1)
    print("len(conv_s): ", (N1 + N2) - 1)
    for n1 in range(len(sample1)):
        for n2 in range(len(sample2)):
            # conv_s[n1 + n2] += int(sample1[n1] * sample2[n2])
            # taskpractical
            conv_s[n1 + n2] += float(sample1[n1] * sample2[n2])
            # print("conv_s",n1 , n2,"=",sample1[n1] ,"*", sample2[n2])

    start_inx = int(inx1[0] + inx2[0])
    end_inx = int(inx1[-1] + inx2[-1])
    conv_inx = []
    for h in range(start_inx, end_inx + 1):
        conv_inx.append(h)
    print("conv inx: ", conv_inx)
    print("conv s: ", conv_s)
    # plt.title("Task 6 conv")
    # plt.xlabel('index')
    # plt.ylabel('samples')
    # plt.plot(conv_inx, conv_s)
    # plt.show()
    # ConvTest(conv_inx, conv_s)

    return (IsPeriodic2, SignalType2, N1, conv_inx, conv_s)
# 4
def Fold_menu():
    text_label = Label(pro, text="folding\n enter num of folding: ")
    text_label.pack()
    text_n = Entry(pro)
    text_n.pack()

    def save_value():
        num_of_fold = float(text_n.get())
        print("num of folding :", num_of_fold)
        if num_of_fold % 2 != 0:
            IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()
            fold_sample = sample[::-1]
            print(fold_sample)
            Shift_Fold_Signal("Output_fold.txt", inx, fold_sample)
        else:
            IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()
            fold_sample = sample[::-1]
            print("fold_sample: ", fold_sample)
            Shift_Fold_Signal("input_fold.txt", inx, fold_sample)

    save_button = Button(pro, text="Save", command=save_value)
    save_button.pack()
def Delaying_or_advancing_menu():
    text_label = Label(pro, text="Delaying_or_advancing_menu")
    text_label.pack()
    text_sh = Entry(pro)
    text_sh.pack()

    def save_num():
        sh = int(text_sh.get())
        print("shift num :", sh)
        IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()

        if sh > 0:
            shifted_signal_negative = [x1 - sh for x1 in inx]
            print("Shifted signal - :", shifted_signal_negative)
            Shift_Fold_Signal("output shifting by add 500.txt", shifted_signal_negative, sample)
            plt.title("Task 2 shifted")
            plt.xlabel('shifted_value_-')
            plt.ylabel('index')
            plt.plot(shifted_signal_negative, sample)
            plt.show()
        if sh < 0:
            shifted_signal_positive = [x2 + sh for x2 in inx]
            print("Shifted signal + :", shifted_signal_positive)
            Shift_Fold_Signal("output shifting by minus 500.txt", shifted_signal_positive, sample)
            plt.title("Task 2 shifted")
            plt.xlabel('shifted_value_+')
            plt.ylabel('index')
            plt.plot(shifted_signal_positive, sample)
            plt.show()

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()
def Smothing_menu():
    text_label = Label(pro, text="Smothing_menu\n enter window size:")
    text_label.pack()
    text_w = Entry(pro)
    text_w.pack()

    def save_num():
        w = int(text_w.get())
        print("window size: :", w)
        IsPeriodic, SignalType, N1, inx, sample = read_inx_sample()

        result = []

        for i in range(0, len(sample) - w + 1):
            window = sample[i:i + w]
            average = sum(window) / w
            result.append(average)

        print(result)
        if w == 3:
            SignalSamplesAreEqual("MovAvgTest1.txt", inx, result)
        elif w == 5:
            SignalSamplesAreEqual("MovAvgTest2.txt", inx, result)

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                         TASK 7
# ---------------------------------------------------------------------------------------------------

def shift_signal(p_values, shift_amount):
    length = len(p_values)
    shifted_p = [p_values[(i + shift_amount) % length] for i in range(length)]
    return shifted_p
def normalized_cross_Correlation_menu():
    text_label = Label(pro, text="normalized cross correlation of two signals\n")
    text_label.pack()

    IsPeriodic1, SignalType1, N1, inx1, sample1 = read_inx_sample()
    IsPeriodic2, SignalType2, N2, inx2, sample2 = read_inx_sample()

    r12 = []
    shift_amount = 0
    s1_pow2 = [math.pow(s1, 2) for s1 in sample1]
    s2_pow2 = [math.pow(s2, 2) for s2 in sample2]
    for _ in range(len(sample2) + 1):
        shifted_p2 = shift_signal(sample2, shift_amount)
        print(shifted_p2)
        multiplied_signal = [j1 * j2 for j1, j2 in zip(sample1, shifted_p2)]
        shift_amount += 1
        # print(squared_values1)
        # print(squared_values2)
        sum_1 = sum(s1_pow2)
        sum_2 = sum(s2_pow2)
        product_sum = sum(multiplied_signal)
        r12.append(product_sum * (1 / len(inx1)))

    r11_r22_divN = float(f'{(cmath.sqrt(sum_1 * sum_2).real) / N1:.8f}')
    print("r11_r22_divN: ", r11_r22_divN)

    normal_croos_correlation = []
    for i in range(len(sample2) + 1):
        normal_croos_correlation.append(r12[i] / r11_r22_divN)
    normalized_cross_correlation = [float(f'{(r12 / r11_r22_divN):.8f}') for r12 in r12]
    print("normal croos correlation: ", normal_croos_correlation)

    Compare_Signals("CorrOutput.txt", inx1, normalized_cross_correlation)
    return inx1, normalized_cross_correlation
def Time_Analysis_menu():
    text_label = Label(pro, text="Time_Analysis\n"
                                 "perform time delay analysis, \n"
                                 "given two periodic signals and the sampling period,"
                                 "find approximately the delay between them:\n"
                                 "enter sampling freq: ")
    text_label.pack()
    text_Fs = Entry(pro)
    text_Fs.pack()

    def save_num():
        Fs = int(text_Fs.get())
        print("sample freq: ", Fs)

        inx, normalized_cross_correlation = normalized_cross_Correlation_menu()
        max_corr = -1
        for i, ncc in zip(inx, normalized_cross_correlation):
            if ncc >= max_corr:
                max_corr = ncc
                inx_max = i

        print("inx_max: ", inx_max, "max_corr: ", max_corr)
        print("final output", inx_max / Fs)

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        signal = [float(line) for line in lines]
    print(file_path, len(signal), signal)

    total_len = len(signal) * 5
    return signal
def normalized_cross_Correlation_p3(kk:int,signal_test,signal):
    text_label = Label(pro, text="normalized cross correlation of two signals\n")
    text_label.pack()
    if kk==0:
        r12 = []
        shift_amount = 0
        s1_pow2 = [math.pow(s1, 2) for s1 in signal_test]
        s2_pow2 = [math.pow(s2, 2) for s2 in signal]
        for _ in range(len(signal) + 1):
            shifted_p2 = shift_signal(signal, shift_amount)
            # print(shifted_p2)
            multiplied_signal = [j1 * j2 for j1, j2 in zip(signal_test, shifted_p2)]
            shift_amount += 1
            # print(squared_values1)
            # print(squared_values2)
            sum_1 = sum(s1_pow2)
            sum_2 = sum(s2_pow2)
            product_sum = sum(multiplied_signal)
            r12.append(product_sum * (1 / len(signal_test)))

        r11_r22_divN = float(f'{(cmath.sqrt(sum_1 * sum_2).real) / N1:.8f}')
        print("r11_r22_divN: ", r11_r22_divN)

        normal_croos_correlation = []
        for i in range(len(signal) + 1):
            normal_croos_correlation.append(r12[i] / r11_r22_divN)
        normalized_cross_correlation = [float(f'{(r12 / r11_r22_divN):.8f}') for r12 in r12]
        print("normal croos correlation: ", normal_croos_correlation)

        # Compare_Signals("CorrOutput.txt", inx1, normalized_cross_correlation)
        return normalized_cross_correlation









    if kk == 1:
        sample2 = read_file("avg_c1.txt")
        sample1 = read_file("Test Signals/Test1.txt")
        print("in Test1")
    elif kk == 2:
        sample2 = read_file("avg_c2.txt")
        sample1 = read_file("Test Signals/Test1.txt")

    elif kk == 3:
        sample2 = read_file("avg_c1.txt")
        sample1 = read_file("Test Signals/Test2.txt")
        print("in Test2")
    elif kk == 4:
        sample2 = read_file("avg_c2.txt")
        sample1 = read_file("Test Signals/Test2.txt")

    r12 = []
    shift_amount = 0
    s1_pow2 = [math.pow(s1, 2) for s1 in sample1]
    s2_pow2 = [math.pow(s2, 2) for s2 in sample2]
    for _ in range(len(sample2) + 1):
        shifted_p2 = shift_signal(sample2, shift_amount)
        # print(shifted_p2)
        multiplied_signal = [j1 * j2 for j1, j2 in zip(sample1, shifted_p2)]
        shift_amount += 1
        # print(squared_values1)
        # print(squared_values2)
        sum_1 = sum(s1_pow2)
        sum_2 = sum(s2_pow2)
        product_sum = sum(multiplied_signal)
        r12.append(product_sum * (1 / len(sample1)))

    r11_r22_divN = float(f'{(cmath.sqrt(sum_1 * sum_2).real) / N1:.8f}')
    print("r11_r22_divN: ", r11_r22_divN)

    normal_croos_correlation = []
    for i in range(len(sample2) + 1):
        normal_croos_correlation.append(r12[i] / r11_r22_divN)
    normalized_cross_correlation = [float(f'{(r12 / r11_r22_divN):.8f}') for r12 in r12]
    print("normal croos correlation: ", normal_croos_correlation)

    # Compare_Signals("CorrOutput.txt", inx1, normalized_cross_correlation)
    return normalized_cross_correlation
def read_class_file():
    files_class1 = []
    files_class2 = []
    for i in range(1, 6):
        path_file1 = "Class 1/down" + str(i) + ".txt"
        path_file2 = "Class 2/up" + str(i) + ".txt"
        files_class1.append(path_file1)
        files_class2.append(path_file2)

    return files_class1, files_class2
def Template_matching_menu(p,num_of_test,signal_test,signalA,signalB):
    text_label = Label(pro, text="Template_matching\n"
                                 "choose test file:")
    text_label.pack()
    num1=0
    num2=0
    if p==2:
        if num_of_test==1:
            print("in test 1:\n")
            score_class1 = normalized_cross_Correlation_p3(num1,signal_test,signalA)
            score_class2 = normalized_cross_Correlation_p3(num2,signal_test,signalB)
            print(score_class1, score_class2)
            if max(score_class1, default=0) > max(score_class2, default=0):
                l = "class A"
            else:
                l = "class B"
            print(l)

        elif num_of_test==2:
            print("in test 2:\n")
            score_class1 = normalized_cross_Correlation_p3(num1,signal_test,signalA)
            score_class2 = normalized_cross_Correlation_p3(num2,signal_test,signalB)
            print(score_class1,score_class2)
            if max(score_class1, default=0) > max(score_class2, default=0):
                l = "class A"
            else:
                l = "class B"
            print(l)

    text_num_test = Entry(pro)
    text_num_test.pack()

    def save_num():
        num_test = int(text_num_test.get())
        print("nun file test: ", num_test)
        # class1_file = "Class 1"  # down
        # class2_file = "Class 2"  # up
        class1 = []
        class2 = []

        files_class1, files_class2 = read_class_file()
        for i in range(5):
            class1.append(read_file(files_class1[i]))
            class2.append(read_file(files_class2[i]))
        iterate = 250
        k = 0
        avg_c1 = []
        avg_c2 = []
        print(len(class1))
        for k in range(len(class1[0])):
            sum_c1 = class1[0][k] + class1[1][k] + class1[2][k] + class1[3][k] + class1[4][k]
            sum_c2 = class2[0][k] + class2[1][k] + class2[2][k] + class2[3][k] + class2[4][k]
            # print(sum_c)
            avg_c1.append(sum_c1 / 5)
            avg_c2.append(sum_c2 / 5)
        print(avg_c1)
        print(avg_c2)

        with open("avg_c1.txt", "w") as file:
            for ac1 in avg_c1:
                file.write(f"{ac1}\n")

        with open("avg_c2.txt", "w") as file:
            for ac2 in avg_c2:
                file.write(f"{ac2}\n")
        if num_test == 1:
            num1 = 1
            num2 = 2
        elif num_test == 2:
            num1 = 3
            num2 = 4

        score_class1 = normalized_cross_Correlation_p3(num1)
        score_class2 = normalized_cross_Correlation_p3(num2)

        # test_signal = []
        # test_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        # if test_file.endswith('.txt'):
        #     with open(test_file, 'r') as file:
        #         test_signal = [int(line) for line in file]
        # print("test_file",len(test_signal))

        # score_class1=[]
        # score_class2=[]
        # for f in class1:
        #     score_class1 = np.dot(test_signal, f)

        if max(score_class1, default=0) > max(score_class2, default=0):
            l = "up"
            # print(os.path.basename(test_file), " this file matching more to class ", l,
            #       max(score_class1),":",len(test_signal)*total_len2,"down s",max(score_class2))
        else:
            l = "down"
            # print(os.path.basename(test_file), " this file matching more to class ", l,
            #        max(score_class2), ":", len(test_signal)*total_len1,"up s",max(score_class1))

        print(l)

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                         TASK 8
# ---------------------------------------------------------------------------------------------------
def x_k1(signal):
    N1 = len(signal)
    x = np.zeros(N1, dtype=np.complex128)
    for k in range(N1):
        for n in range(N1):
            x[k] += signal[n] * np.exp(-1j * 2 * np.pi * k * n / N1)
    return x
def x_n1(X):
    N1 = len(X)
    x = np.zeros(N1, dtype=np.complex128)
    for n in range(N1):
        for k in range(N1):
            x[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N1)
    x /= N1
    x_n = [round(x.real[i], 2) for i in range(N1)]
    return x_n
def Fast_convolution_menu():
    text_label = Label(pro, text="Fast convolution")
    text_label.pack()
    text_label = Label(pro, text="enter the sampling frequency in HZ:")
    text_label.pack()

    # text_fs = Entry(pro)
    # text_fs.pack()

    def implment_Fast_convolution():
        # fs = int(text_fs.get())
        # print("sampling frequency : ", fs)
        IsPeriodic1, SignalType1, N1, inx1, signal1 = read_inx_sample()
        IsPeriodic2, SignalType2, N2, inx2, signal2 = read_inx_sample()
        start_inx = int(inx1[0] + inx2[0])
        end_inx = int(inx1[-1] + inx2[-1])
        conv_inx = []
        for h in range(start_inx, end_inx + 1):
            conv_inx.append(h)
        print("conv inx: ", conv_inx)
        N1 = len(signal1)
        N2 = len(signal2)
        padded_signal1 = np.pad(signal1, (0, N2 - 1))
        padded_signal2 = np.pad(signal2, (0, N1 - 1))
        print("padded_signal1:", padded_signal1)
        print("padded_signal2:", padded_signal2)

        dft_pad_s1 = x_k1(padded_signal1)
        dft_pad_s2 = x_k1(padded_signal2)
        print("dft_pad_s1:", dft_pad_s1)
        print("dft_pad_s2:", dft_pad_s2)

        mult_signal = dft_pad_s1 * dft_pad_s2
        print("mult_signal:", mult_signal)

        convolution_result = x_n1(mult_signal)

        print("fast Convolution Result:", convolution_result)
        ConvTest(conv_inx, convolution_result)

    save_button = Button(pro, text="Save", command=implment_Fast_convolution)
    save_button.pack()
def Fast_correlation_menu():
    text_label = Label(pro, text="Fast correlation")
    text_label.pack()
    text_label = Label(pro, text="enter the sampling frequency in HZ:")
    text_label.pack()

    # text_fs = Entry(pro)
    # text_fs.pack()

    def implment_Fast_correlation():
        # fs = int(text_fs.get())
        # print("sampling frequency : ", fs)
        sample = [1, 0, 0, 1]
        # sample=[0,1,2,3]
        x_k = get_xofk(4, sample)
        print("x_k: ", x_k)
        x_k_conj = x_k.conjugate()
        print("x_k_conj: ", x_k_conj)
        FD_inverse = []
        for x1, x2 in zip(x_k, x_k_conj):
            FD_inverse.append(x1 * x2)
        print("FD_inverse: ", FD_inverse)

        r12 = []
        shift_amount = 0
        for _ in range(len(x_k_conj)):
            shifted_p2 = shift_signal(x_k_conj, shift_amount)
            # print(shifted_p2)
            multiplied_signal = [j1 * j2 for j1, j2 in zip(x_k, shifted_p2)]
            shift_amount += 1
            product_sum = sum(multiplied_signal)
            r12.append(product_sum.real * (1 / len(x_k)))

        print("r12: ", r12)
        r12_divN = []
        for i in r12:
            r12_divN.append(i.real / len(x_k))
        print("r12_divN: ", r12_divN)

        amp = []
        theta = []
        for k in range(len(x_k)):
            r = np.real(x_k[k])
            imag = np.imag(x_k[k])
            # print(k,"= ",r," ",imag,"\n")
            amp.append(np.sqrt(r ** 2 + imag ** 2))
            theta.append(np.arctan2(imag, r))

        ii, x_n = get_xofn(4, amp, theta)
        print(x_n)

    save_button = Button(pro, text="Save", command=implment_Fast_correlation)
    save_button.pack()


# ---------------------------------------------------------------------------------------------------
#                                        Final TASK 9 (practical)
# ---------------------------------------------------------------------------------------------------
def get_transimition_width(stop_attenuation):
    transition_width = 0
    if stop_attenuation >= 13 and stop_attenuation <= 21:
        transition_width = 0.9
        print("Rectangular")
        window_fun = 1
    if stop_attenuation >= 31 and stop_attenuation <= 44:
        transition_width = 3.1
        print("hanning")
        # window_fun=0.5+0.5*np.cos(2*np.pi*n)/N
    if stop_attenuation >= 41 and stop_attenuation <= 53:
        transition_width = 3.3
        print("hamming")
        # window_fun = 0.54 + 0.46 * np.cos(2 * np.pi * n) / N
    if stop_attenuation >= 57 and stop_attenuation <= 74:
        transition_width = 5.5
        print("blackman")
        # window_fun = 0.42 + 0.5 * (np.cos(2 * np.pi * n) / N-1)+(0.08* (np.cos(4 * np.pi * n) / N-1))
    return transition_width
def get_transimition_width_band_filter(stop_attenuation, pass_band_triple):
    transition_width = 0
    if stop_attenuation >= 13 and stop_attenuation <= 21 and pass_band_triple > 0.7416:
        transition_width = 0.9
        print("Rectangular")
        window_fun = 1
    if stop_attenuation >= 31 and stop_attenuation <= 44 and pass_band_triple > 0.0546:
        transition_width = 3.1
        print("hanning")
        # window_fun=0.5+0.5*np.cos(2*np.pi*n)/N
    if stop_attenuation >= 41 and stop_attenuation <= 53 and pass_band_triple > 0.0194:
        transition_width = 3.3
        print("hamming")
        # window_fun = 0.54 + 0.46 * np.cos(2 * np.pi * n) / N
    if stop_attenuation >= 57 and stop_attenuation <= 74 and pass_band_triple > 0.0017:
        transition_width = 5.5
        print("blackman")
        # window_fun = 0.42 + 0.5 * (np.cos(2 * np.pi * n) / N-1)+(0.08* (np.cos(4 * np.pi * n) / N-1))
    return transition_width
def get_N(delta_f):
    # near greater than odd
    if delta_f % 2 == 0:
        N = int(delta_f) + 1
    elif delta_f % 2 == 1:
        N = int(delta_f)
    elif delta_f % 2 >= 1:
        N = math.ceil(delta_f / 2) * 2 + 1
    else:
        N = math.floor(delta_f / 2) * 2 + 1
    print("N: ", N)
    return N
def read_practical_task(one_or_2):
    signal1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    s1 = open(signal1, 'r')
    l = s1.readlines()
    cnt = 0
    for i in l[:]:
        if cnt == 0:
            FilterType, vFilterType = i.strip().split('=')
            print("FilterType: ", vFilterType)
        elif cnt == 1:
            FS, vFS = i.strip().split('=')
            print("FS: ", vFS)
        elif cnt == 2:
            StopBandAttenuation, vStopBandAttenuation = i.strip().split('=')
            print("StopBandAttenuation: ", vStopBandAttenuation)
        if one_or_2 == 1 and cnt >= 3:
            if cnt == 3:
                FC, vFC = i.strip().split('=')
                print("FC: ", vFC)
            elif cnt == 4:
                TransitionBand, vTransitionBand = i.strip().split('=')
                print("TransitionBand: ", vTransitionBand)
        elif one_or_2 == 2 and cnt >= 3:
            if cnt == 3:
                F1, vF1 = i.strip().split('=')
                print("F1: ", vF1)
            elif cnt == 4:
                F2, vF2 = i.strip().split('=')
                print("F2: ", vF2)
            elif cnt == 5:
                TransitionBand, vTransitionBand = i.strip().split('=')
                print("TransitionBand: ", vTransitionBand)
        cnt += 1
    if cnt == 5 and one_or_2 == 1:
        return vFilterType, int(vFS), int(vStopBandAttenuation), int(vFC), int(vTransitionBand)
    if cnt == 6 and one_or_2 == 2:
        return vFilterType, int(vFS), int(vStopBandAttenuation), int(vF1), int(vF2), int(vTransitionBand)
def test1_lowpass(vFS, vStopBandAttenuation, vFC, vTransitionBand):
    transition_width = get_transimition_width(vStopBandAttenuation)

    delta_f_transition_width = vTransitionBand / vFS
    print("transition_width: ", transition_width)
    print("delta_f_transition_width: ", delta_f_transition_width)
    delta_f = transition_width / delta_f_transition_width
    print("delta_f: ", delta_f)
    N = get_N(delta_f)
    cut_off_frequency_dash = vFC + (vTransitionBand / 2)
    print("cut_off_frequency_dash: ", cut_off_frequency_dash)
    normalize_cut_off_frequency_dash = cut_off_frequency_dash / vFS
    print("normalize_cut_off_frequency_dash: ", normalize_cut_off_frequency_dash)

    ideal_impulse_response_n = []
    window_fun_n = []
    h_n = []
    for n in range(int(N / 2) + 1):
        if n == 0:
            ideal_impulse_response_n.append(2 * normalize_cut_off_frequency_dash)
            window_fun_n.append((0.54 + 0.46) * np.cos(2 * np.pi * n))  # /N
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])
        else:
            omega_c = 2 * np.pi * n
            ideal_impulse_response_n.append(
                ((2 * normalize_cut_off_frequency_dash) / (omega_c * normalize_cut_off_frequency_dash)
                 * (np.sin(normalize_cut_off_frequency_dash * omega_c))))
            window_fun_n.append(0.54 + 0.46 * np.cos((2 * np.pi * n) / N))
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])

    print("ideal_impulse_response_n: ", ideal_impulse_response_n)
    print("window_fun_n", window_fun_n)
    print("h_n:", h_n)
    # index
    inx = []
    for i in range(int(-N / 2), int(N / 2) + 1):
        inx.append(i)
    print(inx)
    n_p_h_n = []
    n_p_h_n = h_n[::-1]
    for i in range(1, len(h_n)):
        n_p_h_n.append(h_n[i])
    print(len(n_p_h_n), n_p_h_n)

    plt.title("Task 9 lowpass test1")
    plt.xlabel('index')
    plt.ylabel('h(n)')
    plt.plot(inx, n_p_h_n)
    plt.show()
    return inx, n_p_h_n
def test3_highpass(vFS, vStopBandAttenuation, vFC, vTransitionBand):
    transition_width = get_transimition_width(vStopBandAttenuation)

    delta_f_transition_width = vTransitionBand / vFS
    print("transition_width: ", transition_width)
    print("delta_f_transition_width: ", delta_f_transition_width)
    delta_f = transition_width / delta_f_transition_width
    print("delta_f: ", delta_f)
    N = get_N(delta_f)
    # -
    cut_off_frequency_dash = vFC - (vTransitionBand / 2)
    print("cut_off_frequency_dash: ", cut_off_frequency_dash)
    normalize_cut_off_frequency_dash = cut_off_frequency_dash / vFS
    print("normalize_cut_off_frequency_dash: ", normalize_cut_off_frequency_dash)

    ideal_impulse_response_n = []
    window_fun_n = []
    h_n = []
    for n in range(int(N / 2) + 1):

        # res = 0.54 + 0.46 * math.cos((2 * math.pi * n) / N)
        if n == 0:
            ideal_impulse_response_n.append(1 - (2 * normalize_cut_off_frequency_dash))
            window_fun_n.append((0.54 + 0.46) * np.cos(2 * np.pi * n))  # /N
            h_n.append(float(format(float(ideal_impulse_response_n[n]) * float(window_fun_n[n]), '.6E')))
        else:
            omega_c = 2 * np.pi * n
            ideal_impulse_response_n.append(
                -2 * normalize_cut_off_frequency_dash * (
                        math.sin(omega_c * normalize_cut_off_frequency_dash) / (
                        omega_c * normalize_cut_off_frequency_dash)))
            #     ((-2 * normalize_cut_off_frequency_dash) / (omega_c * normalize_cut_off_frequency_dash)
            #      * (np.sin(normalize_cut_off_frequency_dash * omega_c))))
            window_fun_n.append(0.54 + 0.46 * np.cos((2 * np.pi * n) / N))
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])

            # ideal_impulse_response_n.append(
            #     ((2 * normalize_cut_off_frequency_dash) / (omega_c * normalize_cut_off_frequency_dash)
            #      * (np.sin(normalize_cut_off_frequency_dash * omega_c))))
            # window_fun_n.append(0.54 + 0.46 * np.cos((2 * np.pi * n) / N))
            # h_n.append(float(format(float(ideal_impulse_response_n[n]) * float(window_fun_n[n]), '.6E')))

    print("ideal_impulse_response_n: ", ideal_impulse_response_n)
    print("window_fun_n", window_fun_n)
    print("h_n:", h_n)
    # index
    inx = []

    for i in range(int(-N / 2), int(N / 2) + 1):
        inx.append(i)
    print(inx)
    n_p_h_n = []
    n_p_h_n = h_n[::-1]
    cnt = int(N / 2)
    #        n_p_h_n[cnt]=h_n[0]

    for i in range(1, len(h_n)):
        n_p_h_n.append(h_n[i])
    print(len(n_p_h_n), n_p_h_n)
    formatted_list = [format(x, '.16E') for x in n_p_h_n]
    print(formatted_list)

    with open("0ut_highpass.txt", "w") as file:
        file.write(f"{0}\n")
        file.write(f"{0}\n")
        file.write(f"{N}\n")
        for i, s in zip(inx, n_p_h_n):
            file.write(f"{int(i)} {float(s)}\n")
    plt.title("Task 9 highpass test3")
    plt.xlabel('index')
    plt.ylabel('h(n)')
    plt.plot(inx, n_p_h_n)
    plt.show()
    return inx, n_p_h_n
def test5_bandpass(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand):
    pass_band_triple = 0.1
    transition_width = get_transimition_width_band_filter(vStopBandAttenuation, pass_band_triple)
    print("transition_width: ", transition_width)

    delta_f_transition_width = vTransitionBand / vFS
    print("delta_f_transition_width: ", delta_f_transition_width)
    delta_f = transition_width / delta_f_transition_width
    print("delta_f: ", delta_f)
    # N
    N = get_N(delta_f)
    # -not+
    cut_off_frequency_dash1 = vF1 - (vTransitionBand / 2)
    cut_off_frequency_dash2 = vF2 + (vTransitionBand / 2)
    print("cut_off_frequency_dash1: ", cut_off_frequency_dash1)
    print("cut_off_frequency_dash2: ", cut_off_frequency_dash2)
    normalize_cut_off_frequency_dash1 = cut_off_frequency_dash1 / vFS
    normalize_cut_off_frequency_dash2 = cut_off_frequency_dash2 / vFS
    print("normalize_cut_off_frequency_dash1: ", normalize_cut_off_frequency_dash1)
    print("normalize_cut_off_frequency_dash2: ", normalize_cut_off_frequency_dash2)

    ideal_impulse_response_n = []
    window_fun_n = []
    h_n = []
    for n in range(int(N / 2) + 1):
        if n == 0:
            ideal_impulse_response_n.append(
                2 * (normalize_cut_off_frequency_dash2 - normalize_cut_off_frequency_dash1))
            window_fun_n.append((round(0.42 + 0.5, 2) * (np.cos(0))) + (0.08 * (np.cos(0))))
            # window_fun_n.append( 0.42 + term1 + term2)
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])
        else:
            first = 2 * normalize_cut_off_frequency_dash2 * (
                    math.sin(n * 2 * math.pi * normalize_cut_off_frequency_dash2) / (
                    n * 2 * math.pi * normalize_cut_off_frequency_dash2))
            second = 2 * normalize_cut_off_frequency_dash1 * (
                    math.sin(n * 2 * math.pi * normalize_cut_off_frequency_dash1) / (
                    n * 2 * math.pi * normalize_cut_off_frequency_dash1))
            # omega_c = 2 * np.pi * n
            ideal_impulse_response_n.append(first - second)
            term1 = 0.5 * math.cos((2 * math.pi * n) / (N - 1))
            term2 = 0.08 * math.cos((4 * math.pi * n) / (N - 1))
            window_fun_n.append(0.42 + term1 + term2)
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])

    print("ideal_impulse_response_n: ", ideal_impulse_response_n)
    print("window_fun_n", window_fun_n)
    print("h_n:", h_n)
    # index
    inx = []
    for i in range(int(-N / 2), int(N / 2) + 1):
        inx.append(i)
    print(inx)
    n_p_h_n = []
    n_p_h_n = h_n[::-1]
    for i in range(1, len(h_n)):
        n_p_h_n.append(h_n[i])
    print(len(n_p_h_n), n_p_h_n)
    return inx, n_p_h_n
def test7_babdstop(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand):
    pass_band_triple = 0.1
    transition_width = get_transimition_width_band_filter(vStopBandAttenuation, pass_band_triple)
    print("transition_width: ", transition_width)

    delta_f_transition_width = vTransitionBand / vFS
    print("delta_f_transition_width: ", delta_f_transition_width)
    delta_f = transition_width / delta_f_transition_width
    print("delta_f: ", delta_f)
    N = get_N(delta_f)
    cut_off_frequency_dash1 = vF1 + (vTransitionBand / 2)
    cut_off_frequency_dash2 = vF2 - (vTransitionBand / 2)
    print("cut_off_frequency_dash1: ", cut_off_frequency_dash1)
    print("cut_off_frequency_dash2: ", cut_off_frequency_dash2)
    normalize_cut_off_frequency_dash1 = cut_off_frequency_dash1 / vFS
    normalize_cut_off_frequency_dash2 = cut_off_frequency_dash2 / vFS
    print("normalize_cut_off_frequency_dash1: ", normalize_cut_off_frequency_dash1)
    print("normalize_cut_off_frequency_dash2: ", normalize_cut_off_frequency_dash2)

    ideal_impulse_response_n = []
    window_fun_n = []
    h_n = []
    for n in range(int(N / 2) + 1):
        omega_c = 2 * np.pi * n
        if n == 0:
            ideal_impulse_response_n.append(
                (1 - (2 * (normalize_cut_off_frequency_dash2 - normalize_cut_off_frequency_dash1))))
            window_fun_n.append((round(0.42 + 0.5, 2) * (np.cos(omega_c))) + (0.08 * (np.cos(omega_c))))
            # window_fun_n.append( 0.42 + term1 + term2)
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])
        else:
            first = 2 * normalize_cut_off_frequency_dash2 * (
                    math.sin(n * 2 * math.pi * normalize_cut_off_frequency_dash2) / (
                    n * 2 * math.pi * normalize_cut_off_frequency_dash2))
            second = 2 * normalize_cut_off_frequency_dash1 * (
                    math.sin(n * 2 * math.pi * normalize_cut_off_frequency_dash1) / (
                    n * 2 * math.pi * normalize_cut_off_frequency_dash1))

            ideal_impulse_response_n.append(second - first)
            term1 = 0.5 * math.cos((2 * math.pi * n) / (N - 1))
            term2 = 0.08 * math.cos((4 * math.pi * n) / (N - 1))
            window_fun_n.append(0.42 + term1 + term2)
            h_n.append(ideal_impulse_response_n[n] * window_fun_n[n])

    h_n = [round(num, 9) for num in h_n]
    print("ideal_impulse_response_n: ", ideal_impulse_response_n)
    print("window_fun_n", window_fun_n)
    print("h_n:", h_n)
    # index
    inx = []
    for i in range(int(-N / 2), int(N / 2) + 1):
        inx.append(i)
    print(inx)
    n_p_h_n = []
    n_p_h_n = h_n[::-1]
    for i in range(1, len(h_n)):
        n_p_h_n.append(h_n[i])
    print(len(n_p_h_n), n_p_h_n)

    return inx, n_p_h_n

#k, vFilterType, vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand, practical
def FIR_filters_menu(k, vFilterType, vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand, practical):
    # save the coefficients to text file.
    # if vFilterType == "Low pass" or vFilterType=="High pass":
    text_label = Label(pro, text="FIR_filters\n"
                                 "enter 1 or 2:\n"
                                 "want Low pass or High pass enter 1\n"
                                 "want Band pass or Band stop enter 2")
    text_label.pack()
    #practical=0
    if practical == 2:
        inx, n_p_h_n = test5_bandpass(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand)
        with open("0ut_pass_band_test6_2.txt", "w") as file:
            file.write(f"{0}\n")
            file.write(f"{0}\n")
            file.write(f"{111}\n")
            for i, s in zip(inx, n_p_h_n):
                file.write(f"{int(i)} {float(s)}\n")

        IsPeriodic1, SignalType1, N1, conv_inx, conv_s = convolve_two_signals_9steps(k)
        rounded_conv_s = [round(x, 8) for x in conv_s]
        with open("0ut_conv_pass_band_2.txt", "w") as file:
            file.write(f"{IsPeriodic1}\n")
            file.write(f"{SignalType1}\n")
            file.write(f"{N1}\n")
            for i, s in zip(conv_inx, rounded_conv_s):
                file.write(f"{int(i)} {s}\n")
        return conv_inx, rounded_conv_s

    text_LowHighpass_or_Bandpassstop = Entry(pro)
    text_LowHighpass_or_Bandpassstop.pack()
    text_label1 = Label(pro, text="enter num_test: ")
    text_label1.pack()
    text_num_test = Entry(pro)
    text_num_test.pack()

    def implement_FIR():
        one_or_2 = int(text_LowHighpass_or_Bandpassstop.get())
        print("LowHighpass or Bandpassstop: ", one_or_2)
        num_test = int(text_num_test.get())
        print("nun file test: ", num_test)

        if one_or_2 == 1:
            vFilterType, vFS, vStopBandAttenuation, vFC, vTransitionBand = read_practical_task(one_or_2)
        elif one_or_2 == 2:
            vFilterType, vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand = read_practical_task(one_or_2)

        if vFilterType == " Low pass":
            # sampling_frequency = 8
            # cut_off_frequency = 1.5
            # stop_attenuation = 51
            # transition_band = 0.5
            if num_test == 1:
                inx, n_p_h_n = test1_lowpass(vFS, vStopBandAttenuation, vFC, vTransitionBand)
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, n_p_h_n)
            elif num_test == 2:
                inx, n_p_h_n = test1_lowpass(vFS, vStopBandAttenuation, vFC, vTransitionBand)
                with open("0ut_lowpass.txt", "w") as file:
                    file.write(f"{0}\n")
                    file.write(f"{0}\n")
                    file.write(f"{53}\n")
                    for i, s in zip(inx, n_p_h_n):
                        file.write(f"{int(i)} {float(s)}\n")
                IsPeriodic1, SignalType1, N2, conv_inx, conv_s = convolve_two_signals_menu()
                rounded_conv_s = [round(x, 8) for x in conv_s]
                with open("0ut_conv_lowpass.txt", "w") as file:
                    file.write(f"{IsPeriodic1}\n")
                    file.write(f"{SignalType1}\n")
                    file.write(f"{N2}\n")
                    for i, s in zip(conv_inx, rounded_conv_s):
                        file.write(f"{int(i)} {s}\n")
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, rounded_conv_s)
        # ----------------------------------------------------------------------------------------------------------------------
        elif vFilterType == " High pass":
            if num_test == 3:
                inx, n_p_h_n = test3_highpass(vFS, vStopBandAttenuation, vFC, vTransitionBand)
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, n_p_h_n)
            elif num_test == 4:
                inx, n_p_h_n = test3_highpass(vFS, vStopBandAttenuation, vFC, vTransitionBand)
                # with open("0ut_highpass_test4.txt", "w") as file:
                #     file.write(f"{0}\n")
                #     file.write(f"{0}\n")
                #     file.write(f"{89}\n")
                #     for i, s in zip(inx, n_p_h_n):
                #         file.write(f"{int(i)} {float(s)}\n")
                IsPeriodic1, SignalType1, N1, conv_inx, conv_s = convolve_two_signals_menu()
                rounded_conv_s = [round(x, 8) for x in conv_s]
                with open("0ut_conv_highpass.txt", "w") as file:
                    file.write(f"{IsPeriodic1}\n")
                    file.write(f"{SignalType1}\n")
                    file.write(f"{N1}\n")
                    for i, s in zip(conv_inx, rounded_conv_s):
                        file.write(f"{int(i)} {s}\n")
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, rounded_conv_s)


        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        elif vFilterType == " Band pass":
            # sampling_frequency = 1000
            # cut_off_frequency1 = 150
            # cut_off_frequency2 = 250
            pass_band_triple = 0.1
            # stop_attenuation = 60
            # transition_band = 50
            if num_test == 5:
                inx, n_p_h_n = test5_bandpass(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand)
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, n_p_h_n)

            elif num_test == 6:
                inx, n_p_h_n = test5_bandpass(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand)
                with open("0ut_pass_band_test6.txt", "w") as file:
                    file.write(f"{0}\n")
                    file.write(f"{0}\n")
                    file.write(f"{111}\n")
                    for i, s in zip(inx, n_p_h_n):
                        file.write(f"{int(i)} {float(s)}\n")

                IsPeriodic1, SignalType1, N1, conv_inx, conv_s = convolve_two_signals_menu()
                rounded_conv_s = [round(x, 8) for x in conv_s]
                with open("0ut_conv_pass_band.txt", "w") as file:
                    file.write(f"{IsPeriodic1}\n")
                    file.write(f"{SignalType1}\n")
                    file.write(f"{N1}\n")
                    for i, s in zip(conv_inx, rounded_conv_s):
                        file.write(f"{int(i)} {s}\n")
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, rounded_conv_s)



        elif vFilterType == " Band stop":
            print("....................")
            pass_band_triple = 0.1
            # stop_attenuation = 60
            # transition_band = 50
            if num_test == 7:
                inx, n_p_h_n = test7_babdstop(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand)
                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, n_p_h_n)
            elif num_test == 8:
                inx, n_p_h_n = test7_babdstop(vFS, vStopBandAttenuation, vF1, vF2, vTransitionBand)
                with open("0ut_pass_stop_test8.txt", "w") as file:
                    file.write(f"{0}\n")
                    file.write(f"{0}\n")
                    file.write(f"{111}\n")
                    for i, s in zip(inx, n_p_h_n):
                        file.write(f"{int(i)} {float(s)}\n")
                IsPeriodic1, SignalType1, N1, conv_inx, conv_s = convolve_two_signals_menu()
                rounded_conv_s = [round(x, 8) for x in conv_s]
                with open("0ut_conv_stop_band.txt", "w") as file:
                    file.write(f"{IsPeriodic1}\n")
                    file.write(f"{SignalType1}\n")
                    file.write(f"{N1}\n")
                    for i, s in zip(conv_inx, rounded_conv_s):
                        file.write(f"{int(i)} {s}\n")

                signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
                Compare_Signals(str((signal2)), inx, rounded_conv_s)

        # signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        # #Compare_Signals(str((signal2)), inx, n_p_h_n)
        # Compare_Signals(str((signal2)), inx, rounded_conv_s)

    save_button = Button(pro, text="Save", command=implement_FIR)
    save_button.pack()

    # ---------------------------------
def sample_up(list, L):
    zero_padded = []
    for num in list:
        zero_padded.append(num)
        zero_padded.extend([0] * (L - 1))
    return zero_padded
def sample_down(lst, m):
    result = []
    result.append(lst[0])
    for i in range(m, len(lst), m):
        result.append(lst[i])
    return result

#conv_inx, rounded_conv_s ,p
def Resampling_menu(conv_inx, rounded_conv_s ,p):
    # testttttt
    text_label = Label(pro, text="Resampling\n"
                                 "enter L:")
    text_label.pack()
    #p=0
    if p == 2:
        # and m==2 and L==3
        one_or_2=1
        vFilterType, vFS, vStopBandAttenuation, vFC, vTransitionBand = read_practical_task(one_or_2)
        inx, n_p_h_n = test1_lowpass(vFS, vStopBandAttenuation, vFC, vTransitionBand)
        with open("0ut_n_p_h_n_Resampling.txt", "w") as file:
            file.write(f"{IsPeriodic}\n")
            file.write(f"{SignalType}\n")
            file.write(f"{53}\n")
            for i, l in zip(inx, n_p_h_n):
                file.write(f"{int(i)} {float(l)}\n")
        # conv_inx, rounded_conv_s
        L=3
        signal = sample_up(rounded_conv_s, L)
        print(len(signal))
        x = 0
        with open("0ut_signal999.txt", "w") as file:
            file.write(f"{IsPeriodic}\n")
            file.write(f"{SignalType}\n")
            file.write(f"{7830}\n")
            for i in signal[:7830]:
                file.write(f"{int(x)} {float(i)}\n")
                x += 1
        # conv_result = np.convolve(signal, n_p_h_n)
        IsPeriodic1, SignalType1, N2, conv_inx, conv_result = convolve_two_signals_menu()
        print("upsampled_result:", conv_result)
        m=2
        signal_down = sample_down(conv_result, m)
        print("up_down_sampled result:", signal_down)
        # signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        # Compare_Signals(str((signal2)), inx, signal_down)
        return inx, signal_down
    text_L = Entry(pro)
    text_L.pack()
    text_label1 = Label(pro, text="enter m:")
    text_label1.pack()
    text_m = Entry(pro)
    text_m.pack()

    def implement_Resampling():
        L = int(text_L.get())
        print("text_L: ", L)
        m = int(text_m.get())
        print("text_m: ", m)

        if m == 0 and L == 0:
            print("m == 0 and L == 0 SO this invalid")
            return 0

        one_or_2 = 1
        vFilterType, vFS, vStopBandAttenuation, vFC, vTransitionBand = read_practical_task(one_or_2)
        inx, n_p_h_n = test1_lowpass(vFS, vStopBandAttenuation, vFC, vTransitionBand)
        with open("0ut_n_p_h_n_Resampling.txt", "w") as file:
            file.write(f"{IsPeriodic}\n")
            file.write(f"{SignalType}\n")
            file.write(f"{53}\n")
            for i, l in zip(inx, n_p_h_n):
                file.write(f"{int(i)} {float(l)}\n")

        IsPeriodic1, SignalType1, N1, inx1, input_file = read_inx_sample()

        if m == 0 and L != 0:  # up
            print(" m == 0 and L != 0:")
            signal1 = sample_up(input_file, L)
            x=0
            with open("0ut_signal1_Resampling.txt", "w") as file:
                file.write(f"{IsPeriodic}\n")
                file.write(f"{SignalType}\n")
                file.write(f"{1198}\n")
                for  i in  signal1[:1198]:
                    file.write(f"{int(x)} {float(i)}\n")
                    x+=1

            IsPeriodic1, SignalType1, N2, conv_inx, conv_result = convolve_two_signals_menu()
            print("upsampled result:", conv_result)
            with open("ccccconnnnnnnnvvvvvv.txt", "w") as file:
                file.write(f"{IsPeriodic}\n")
                file.write(f"{SignalType}\n")
                file.write(f"{1250}\n")
                for i, l in zip(conv_inx, conv_result):
                    file.write(f"{int(i)} {float(l)}\n")
            signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            Compare_Signals(str((signal2)), inx, conv_result)
            return inx,  conv_result

        elif m != 0 and L == 0:  # down
            print("m != 0 and L == 0")
            IsPeriodic1, SignalType1, N2, conv_inx, conv_result = convolve_two_signals_menu()
            signal1 = sample_down(conv_result, m)
            print("Downsampled result:", signal1)
            signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            Compare_Signals(str((signal2)), inx, signal1)
            return inx, signal1

        else:
            signal = sample_up(input_file, L)
            x=0
            with open("0ut_signal3_Resampling.txt", "w") as file:
                file.write(f"{IsPeriodic}\n")
                file.write(f"{SignalType}\n")
                file.write(f"{1198}\n")
                for i in signal[:1198]:
                    file.write(f"{int(x)} {float(i)}\n")
                    x += 1
            #conv_result = np.convolve(signal, n_p_h_n)
            IsPeriodic1, SignalType1, N2, conv_inx, conv_result = convolve_two_signals_menu()
            print("upsampled_result:", conv_result)

            signal_down = sample_down(conv_result, m)
            print("up_down_sampled result:", signal_down)
            signal2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            Compare_Signals(str((signal2)), inx, signal_down)
            return inx, signal_down

    save_button = Button(pro, text="Save", command=implement_Resampling)
    save_button.pack()
def auto_correlation(ii, normalized_signal,p):
    text_label = Label(pro, text=("auto correlation\n"))
    text_label.pack()

    shift_amount = 0
    for _ in range(len(normalized_signal) + 1):
        shifted_p2 = shift_signal(normalized_signal, shift_amount)
        print(shifted_p2)
        multiplied_signal = [j1 * j2 for j1, j2 in zip(normalized_signal, shifted_p2)]
        shift_amount += 1
    r11=[]
    for k in range(0,len(multiplied_signal)):
        r11.append(float((multiplied_signal[k]) / N1))

    print("r11: ", r11)
    print(len(ii),len(r11))
    return ii, r11
def read_class_path1():
    files_classA = []
    files_classB = []
    for i in range(1, 7):
        path_file1 = "A/ASeg" + str(i) + ".txt"
        path_file2 = "B/BSeg" + str(i) + ".txt"  # 2500
        files_classA.append(path_file1)
        files_classB.append(path_file2)

    return files_classA, files_classB
def read_class_file1(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        signal = [float(line) for line in lines]
    print(file_path, len(signal), signal)

    total_len = len(signal) * 6
    return signal
def convolve_two_signals_9steps(path):
    text_label = Label(pro, text="convolve two signals\n")
    text_label.pack()
    IsPeriodic1, SignalType1, N1, inx1, sample1 = read_inx_sample()
    sample2 = read_class_file1(path)

    conv_s = [0] * ((N1 + 2500) - 1)
    print("len(conv_s): ", (N1 + 2500) - 1)
    for n1 in range(len(sample1)):
        for n2 in range(len(sample2)):
            # conv_s[n1 + n2] += int(sample1[n1] * sample2[n2])
            # taskpractical
            conv_s[n1 + n2] += float(sample1[n1] * sample2[n2])
            # print("conv_s",n1 , n2,"=",sample1[n1] ,"*", sample2[n2])

    start_inx = int(inx1[0] + 0)
    end_inx = int(inx1[-1] + 2500)
    conv_inx = []
    for h in range(start_inx, end_inx + 1):
        conv_inx.append(h)
    print("conv inx: ", conv_inx)
    print("conv s: ", conv_s)
    # plt.title("Task 6 conv")
    # plt.xlabel('index')
    # plt.ylabel('samples')
    # plt.plot(conv_inx, conv_s)
    # plt.show()
    # ConvTest(conv_inx, conv_s)

    return (IsPeriodic1, SignalType1, N1, conv_inx, conv_s)


# low = miniF / nyquist
# high = maxF / nyquist
# if Fs<2*Fmax in f1,f2 in band filter:
#     Resampling_menu()
# else:
#     continue
def steps9_test_classification_menu():


    files_classA, files_classB = read_class_path1()

    class_A = []
    class_B = []
    for i in range(6):
        class_A.append(read_class_file1(files_classA[i]))
        class_B.append(read_class_file1(files_classB[i]))

    for k in files_classA[:]:
        InputStopBandAttenuation = 60  # 50
        InputTransitionBand = 50  # 500
        vFilterType = " Band pass"
        vFS = 1000
        vF1 = 150
        vF2 = 250
        practical = 2
        conv_inx, rounded_conv_s = FIR_filters_menu(k, vFilterType, vFS, InputStopBandAttenuation, vF1, vF2,
                                                    InputTransitionBand, practical)  # return fs
        print(vFS)
        #vFS=50
        p = 2
        if vFS > (2*max(vF1,vF2)):
            inx, signal_down = Resampling_menu(conv_inx, rounded_conv_s,p)
            # freq or time
            ii, formatted_s=RemoveDCcomponent_menu(inx, signal_down,p)
            normalize_range="-1 1"
            ii, normalized_signal = normalize_menu(ii, formatted_s,p,normalize_range)
            ii, r11 = auto_correlation(ii, normalized_signal,p)
            theta, amp = DCT_menu(ii, r11,p)
        else:
            print(" new Fs is not valid  ")
            ii, formatted_s = RemoveDCcomponent_menu(conv_inx, rounded_conv_s, p)
            normalize_range = "-1 1"
            ii, normalized_signal = normalize_menu(ii, formatted_s, p, normalize_range)
            ii, r11 = auto_correlation(ii, normalized_signal, p)
            theta, amp = DCT_menu(ii, r11, p)



    avg_c1 = []
    avg_c2 = []
    for k in range(len(class_A[0])):
        sum_c1 = 0
        sum_c2 = 0
        for i in range(0, 6):  # 0-5+1
            sum_c1 += class_A[i][k]
            sum_c2 += class_B[i][k]
            # print(sum_c)
        avg_c1.append(sum_c1 / 6)
        avg_c2.append(sum_c2 / 6)
    print("*********",len(avg_c1),len(avg_c2))
    print(avg_c1)
    print(avg_c2)

    with open("avg_A.txt", "w") as file:
        for ac1 in avg_c1:
            file.write(f"{ac1}\n")

    with open("avg_B.txt", "w") as file:
        for ac2 in avg_c2:
            file.write(f"{ac2}\n")

    p=2
    num_of_test=1
    if num_of_test==1:
        signal_test=read_class_file1("Test Folder/ATest1.txt")
        signalA=read_class_file1("avg_A.txt")
        signalB=read_class_file1("avg_B.txt")
    num_of_test = 1
    if num_of_test==2:
        signal_test=read_class_file1("Test Folder/BTest1.txt")
        signalA = read_class_file1("avg_A.txt")
        signalB = read_class_file1("avg_B.txt")

    Template_matching_menu(p,num_of_test,signal_test,signalA,signalB)

    return 0


menubar = Menu(pro)
f = Menu(menubar, tearoff=0)
f.add_command(label='Sin', command=sin_menu)
f.add_command(label='Cos', command=cos_menu)
#f.add_separator()

ff = Menu(menubar, tearoff=0)
ff.add_command(label='Add', command=add_more2_menu)
ff.add_command(label='Sub', command=sub_menu)
ff.add_command(label='Multi', command=multi_menu)
ff.add_command(label='Squar', command=squar_menu)
ff.add_command(label='Shift', command=shift_menu)
ff.add_command(label='Normalize', command=normalize_menu)
ff.add_command(label='Accumulate', command=accumulate_menu)
#ff.add_separator()

fff = Menu(menubar, tearoff=0)
fff.add_command(label='Number of bits ', command=Number_of_bits_menu)
fff.add_command(label='Number of levels ', command=Number_of_levels_menu)
#fff.add_separator()

ffff = Menu(menubar, tearoff=0)
ffff.add_command(label='DFT', command=DFT_menu)
ffff.add_command(label='IDFT', command=IDFT_menu)
# f5
ffff.add_command(label='DCT', command=DCT_menu)
ffff.add_command(label='Remove DC Component', command=RemoveDCcomponent_menu)
ffff.add_command(label='Fast convolution', command=Fast_convolution_menu)
ffff.add_command(label='Fast correlation', command=Fast_correlation_menu)
#ffff.add_separator()

fffff = Menu(menubar, tearoff=0)
fffff.add_command(label='Smoothing', command=Smothing_menu)
fffff.add_command(label='Sharpening', command=Sharpening_menu)
fffff.add_command(label='Delaying or advancing ', command=Delaying_or_advancing_menu)
fffff.add_command(label='Folding ', command=Fold_menu)
fffff.add_command(label='Delaying or advancing a folded  ', command=RemoveDCcomponent_menu)
fffff.add_command(label='Remove the DC component in frequency ', command=RemoveDCcomponentFrequencyD_menu)
fffff.add_command(label='convolve two signals ', command=convolve_two_signals_menu)
fffff.add_command(label='practical task..')

# practical
fffff.add_command(label='FIR filters ', command=FIR_filters_menu)
fffff.add_command(label='Resampling ', command=Resampling_menu)
fffff.add_command(label='9 steps test classification ', command=steps9_test_classification_menu)
#fffff.add_separator()
ffffff = Menu(menubar, tearoff=0)
ffffff.add_command(label='Normalized Cross Correlation', command=normalized_cross_Correlation_menu)
ffffff.add_command(label='Time Analysis', command=Time_Analysis_menu)
ffffff.add_command(label='Template matching ', command=Template_matching_menu)
#ffffff.add_separator()


menubar.add_cascade(label='Signal Generation', menu=f)
menubar.add_cascade(label='Arithmetic Operations ', menu=ff)
menubar.add_cascade(label='Quantization', menu=fff)
menubar.add_cascade(label='Frequency Domain', menu=ffff)
menubar.add_cascade(label='Time Domain', menu=fffff)
menubar.add_cascade(label='Correlation', menu=ffffff)


pro.config(menu=menubar)
pro.mainloop()

try:
    pro.mainloop()
except KeyboardInterrupt:
    print("Program interrupted by the user")
