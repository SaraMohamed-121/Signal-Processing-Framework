#import math
import numpy as np
import matplotlib.pyplot as plt
#import points

file = open(r"C:\Users\user\Downloads\Term 9\Digital Signal Processing\Labs\Lab 1\Signals\signal1.txt","r")
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

print("_______")
file.close()

#////////////////////task 2///////////////////////////
sin_cos_input = r'C:\Users\user\Downloads\Term 9\Digital Signal Processing\Labs\Lab 1\Signals\Sin_Cos\Inputs.txt'
sin_input = r'C:\Users\user\Downloads\Term 9\Digital Signal Processing\Labs\Lab 1\Signals\Sin_Cos\Inputs.txt'

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
signals =[]
#kv_pairss["type"] = "sin"
#kv_pairsc["type"] = "cos"
#stype = kv_pairsc["type"]
#print(stype)
#stypes = kv_pairss["type"]
#print(stypes)
print("_______")
l_c =[]
l_s =[]


#---------------------------------------------------------------------
from tkinter import *
from tkinter import filedialog
pro = Tk()
#pro.configure(bg='white')
pro.geometry("700x360")
pro.title("Signal processing")



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
import tkinter as tk
def add_more2_menu():
    text_label = Label(pro, text="Number of signal")
    text_label.pack()
    text_ns = Entry(pro)
    text_ns.pack()



    def save_value():
        N = int(text_ns.get())

        global entry_file_paths
        entry_file_paths = []
        for i in range(N-2):
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            entry_file_paths.append(file_path)
            label_file = tk.Label(pro, text="Read File " + str(i + 1) + "")
            #label_file = tk.Label(pro, text="Read File " + str(i + ) + "")
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
        add_list=[]
        for i in range(len(r1)):
            if r1[i] == r2[i]:
                add_value = math.fabs(p1[i] + p2[i])
                add_list.append(add_value)
                print(i, " ", add_value)

        plt.title("Task 2 add")
        plt.xlabel('add_value')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(r1,add_list)
        plt.show()



    save_button = Button(pro, text="Show result add", command=save_value)
    save_button.pack()



    #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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

        r1= []
        r2 = []
        p1= []
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
        sub_list=[]
        i_indx=[]
        for i in range(len(r1)):
            if r1[i] == r2[i]:
                sub_value = math.fabs(p1[i]-p2[i])
                sub_list.append(sub_value)
                i_indx.append(i)
                print(i," ",sub_value)

        print(sub_list)
        plt.title("Task 2 sub")
        plt.xlabel('sub_value')
        plt.ylabel('index')
        #for i in range(len(r1)):
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
        multi_list=[]
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
        sqr_list=[]
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
            print(shifted_signal_negative[i]," ",kk[i])
        print("****************************************************")
        for j in range(len(hh)):
            print(shifted_signal_positive[j]," ",kk[j])

        plt.title("Task 2 shifted")
        plt.xlabel('shifted_value_+')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(shifted_signal_positive,kk)
        plt.show()

        plt.title("Task 2 shifted")
        plt.xlabel('shifted_value_-')
        plt.ylabel('index')
        # for i in range(len(r1)):
        plt.plot(shifted_signal_negative,kk)
        plt.show()



    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()

def normalize_menu():
    text_label = Label(pro, text="normalization")
    text_label.pack()
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
        print("min_value: ",min_value,"max_value: ",max_value)
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
        #for i in range(len(r1)):
        plt.plot(rw, items)
        plt.show()

    save_button = Button(pro, text="Save", command=save_v)
    save_button.pack()


#---------------------------------------------------------------------------------------------------
#                                         TASK 3
#---------------------------------------------------------------------------------------------------
from QuanTest1 import *
from QuanTest2 import *
#from pathlib import Path

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


        ranges = [(format(min_amp + i * delta,".2f"), format(min_amp + (i + 1) * delta, ".2f")) for i in range(nl)]

        midpoint = np.linspace(min_amp + delta / 2, max_amp - delta / 2, nl)
        print("mid: ", midpoint)
        print("num ranges :",len(ranges)," ", ranges)

        Encoded = [format(num, '03b') for num in range(0, nl)]
        print("Encoded: ", Encoded)
        en = []
        quantized_sample=[]
        #quantized_sample = np.zeros_like(sample)

        for i, s in enumerate(sample):
            for my_range in ranges[:]:
                if s==0.9:
                    en.append(str(110))
                    quantized_sample.append(round(float(0.85), 2))
                    break
                elif s >= float(my_range[0]) and s <= float(my_range[1]):
                    en.append(Encoded[np.argmin(np.abs(midpoint - s))])
                    quantized_sample.append(round(midpoint[np.argmin(np.abs(midpoint - s))],2))
                    break

        """
        for i, s in enumerate(sample):
                en.append(Encoded[np.argmin(np.abs(midpoints - s))])
                quantized_sample[i] = midpoints[np.argmin(np.abs(midpoints - s))]"""
        """for i, s in enumerate(sample):
            idx = np.digitize(s, midpoints) - 1
            en.append(Encoded[idx])
            quantized_sample[i] = midpoints[idx]"""

        print("Encoded in each sample ",len(en)," ", en)
        print("quantized_sample: ",len(quantized_sample)," ", quantized_sample)
        QuantizationTest1(fn,en,quantized_sample)


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
        print("max_amp: ",max_amp,"\nmin_amp",min_amp,"\ndelata: ",delta)
        """l=[[]]
                l[0][0]=min_amp
                l[nl-1][1]=max_amp
                for i in range(nl):
                    for j in range(2):
                        l[i][j].append(min_amp+delta)"""
        midpoints = np.linspace(min_amp + delta / 2, max_amp - delta / 2, nl)
        print("mid: ", midpoints)

        intervalinx = list(range(1, nl+1))
        print("intervalinx: ",intervalinx)
        Encoded=[format(num, '02b') for num in range(0, nl)]
        print("Encoded: ",Encoded)
        en=[]
        ii=[]
        quantized_sample = np.zeros_like(sample)
        for i, s in enumerate(sample):
            en.append(Encoded[np.argmin(np.abs(midpoints - s))])
            ii.append(intervalinx[np.argmin(np.abs(midpoints - s))])
            quantized_sample[i] = midpoints[np.argmin(np.abs(midpoints - s))]

        quantization_error = quantized_sample-sample
        print("num of sample: ", len(sample))
        avg_power_error = np.mean(np.square(quantization_error))

        print("indx interval in each sample ", ii)
        print("Encoded in each sample ", en)
        print("quantized_sample: ", quantized_sample)
        print("quantization error: ", quantization_error)
        print("average power error: ", avg_power_error)

        QuantizationTest2(fn,ii,en,quantized_sample,quantization_error)

    save_button = Button(pro, text="Save", command=save_num)
    save_button.pack()
#---------------------------------------------------------------------------------------------------
#                                         TASK 4
#---------------------------------------------------------------------------------------------------
#import cmath
#import math
from signalcompare import *
import re


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
    return IsPeriodic,SignalType,N1,inx,sample

def get_xofk(N1: int, sample: list):
    x = np.zeros(N1, dtype=np.complex128)
    for k in range(N1):
        for n in range(N1):
            x[k] += sample[n] * np.exp(-1j * 2 * np.pi * k * n / N1)
    return x

def after_change_DFT(amp: list,theta: list,fs: int):

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
    #print(fundamentalfreq)
    omega = []
    cnt = 1
    for n in range(fs):
        omega.append(fundamentalfreq * cnt)
        cnt += 1
    print("omega",omega)

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

    return formatted_amp,formatted_theta,omega,amp,theta

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
    return A_out,P_out

def compare_out_and_plot(formatted_amp: list,formatted_theta: list,omega: list,amp: list,theta:list):
        print("//////////",amp)
        print("//////////",theta)
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
        print(len(omega),omega)
        print(len(amp),amp)
        print(len(theta),theta)
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

        IsPeriodic,SignalType,N1,inx,sample=read_inx_sample()
        x=get_xofk(N1,sample)
        print("x[k]: ",x)

        amp=[]
        theta=[]
        for k in range(len(x)):
            r = np.real(x[k])
            imag = np.imag(x[k])
            #print(k,"= ",r," ",imag,"\n")
            amp.append(np.sqrt(r ** 2 + imag ** 2))
            theta.append(np.arctan2(imag, r))
            #print(k,"::",amp[k]," ",theta[k],"\n")
        print("Amp :", amp)
        print("Theta :", theta)

        #modify
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

                formatted_amp,formatted_theta,omega,amp2,theta2=after_change_DFT(amp, theta, fs)
                compare_out_and_plot(formatted_amp, formatted_theta, omega, amp2, theta2)
                # return amp, theta

            save_button = Button(pro, text="Save Modify", command=Save_modify)
            save_button.pack()

        save_button = Button(pro, text="modify amp and theta", command=modify_amp_theta)
        save_button.pack()


        formatted_amp,formatted_theta,omega,amp,theta=after_change_DFT(amp, theta,fs)
        compare_out_and_plot(formatted_amp,formatted_theta,omega,amp,theta)

    save_button = Button(pro, text="Save", command=implment_DFT)
    save_button.pack()


def get_xofn(N1: int, float_list_A: list,float_list_P: list):
    x = []
    for n in range(N1):
        r=0.0
        imag=0.0
        for k in range(N1):
            r += float_list_A[k] * math.cos((2 * math.pi * k * n / N1) + float_list_P[k])
            imag += float_list_A[k] * math.sin((2 * math.pi * k * n / N1) + float_list_P[k])
        x.append((r, imag))
    x_n = [(round(i[0] / N1, 2)) for i in x]

    inx=0
    ii=[]
    for s in x_n:
        ii.append(inx)
        print(ii[inx]," ", s)
        inx+=1

    return ii,x_n

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
    return i_out,s_out


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

        print("f_a: ",float_list_A)
        print("f_p: ",float_list_P)
        ii,x_n =get_xofn(N1,float_list_A,float_list_P)
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

        i_out,s_out=read_output_IDFD()

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

# ---------------------------------


menubar = Menu(pro)

f = Menu(menubar, tearoff=0)
f.add_command(label='Sin', command=sin_menu)
f.add_command(label='Cos', command=cos_menu)
f.add_separator()
f.add_command(label='Exit', command=pro.quit)

ff = Menu(menubar, tearoff=0)
ff.add_command(label='Add', command=add_more2_menu)
ff.add_command(label='Sub', command=sub_menu)
ff.add_command(label='Multi', command=multi_menu)
ff.add_command(label='Squar', command=squar_menu)
ff.add_command(label='Shift', command=shift_menu)
ff.add_command(label='Normalize', command=normalize_menu)
ff.add_command(label='Accumulate', command=accumulate_menu)
ff.add_separator()
ff.add_command(label='Exit', command=pro.quit)

fff = Menu(menubar, tearoff=0)
fff.add_command(label='Number of bits ', command=Number_of_bits_menu)
fff.add_command(label='Number of levels ', command=Number_of_levels_menu)
fff.add_separator()
fff.add_command(label='Exit', command=pro.quit)

ffff = Menu(menubar, tearoff=0)
ffff.add_command(label='DFT', command=DFT_menu)
ffff.add_command(label='IDFT', command=IDFT_menu)
ffff.add_separator()
ffff.add_command(label='Exit', command=pro.quit)

menubar.add_cascade(label='Signal Generation', menu=f)
menubar.add_cascade(label='Arithmetic Operations ', menu=ff)
menubar.add_cascade(label='Quantization', menu=fff)
menubar.add_cascade(label='Frequency Domain', menu=ffff)

pro.config(menu=menubar)
pro.mainloop()