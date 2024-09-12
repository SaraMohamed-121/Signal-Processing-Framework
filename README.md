# Signal Processing Framework Development 📊🧮
This project is a framework for signal processing using Python, designed to help visualize and manipulate signals with various features.

# 🔲 Task 1 - Signal Processing Framework
## Features

### 1. Reading and Displaying Signals
- **Read Samples from a Text File**: The framework allows the user to load signal samples from a `.txt` file.
- **Continuous and Discrete Representation**: The signal can be displayed in both continuous and discrete-time forms for better visualization and analysis.

### 2. Signal Generation
- **Sinusoidal and Cosinusoidal Signals**: Users can generate sinusoidal or cosinusoidal signals with customizable parameters, including:
  - **Amplitude (A)**: Control the height of the wave.
  - **Phase Shift (θ)**: Adjust the phase of the wave.
  - **Analog Frequency (f)**: Set the frequency of the analog signal.
  - **Sampling Frequency (fs)**: Define the sampling rate (must satisfy the sampling theorem).
  
- The framework includes a **Signal Generation** menu with two options:
  1. **Sine Wave**
  2. **Cosine Wave**

### 3. Multiple Signal Display
- The framework supports displaying two signals at the same time for comparison and analysis.

## 🎯Usage
1. **Reading Signal Samples from a File**: Place your signal samples in a `.txt` file and load it into the framework to visualize the signal.
2. **Generating a Signal**:
   - From the menu, choose to generate a sine or cosine wave.
   - Input the required parameters like amplitude, phase shift, and frequency.
3. **Simultaneous Signal Display**: The framework allows two signals to be displayed at once for a side-by-side comparison.


---

# 🔲 Task 2 - Signal Processing Framework with Arithmetic Operations
## Features

### 1. Arithmetic Operations Menu
- **Addition**: Add multiple input signals and display the resulting signal.
- **Subtraction**: Subtract input signals and display the resulting signal.
- **Multiplication**: Multiply a signal by a constant to either amplify or reduce the signal’s amplitude (invert if the constant equals -1).
- **Squaring**: Square the signal and display the resulting signal.


---


# 🔲 Task 3 - Signal Quantization

### Features

- **Quantization of Input Signals**: The framework allows the user to quantize a signal by specifying either:
  - **Number of Levels**: Directly input the levels needed.
  - **Number of Bits**: The application will compute the appropriate number of levels based on the number of bits.

- **Signal Display**: The application will display:
  - **Quantized Signal**: The quantized version of the input signal.
  - **Quantization Error**: The error between the original and quantized signal.
  - **Encoded Signal**: The encoded representation of the quantized signal.
    
## 🎯 Usage
1. ** Quantize Signals**: Quantize an input signal by selecting the number of levels or bits and visualize the quantization error and encoded signal.


---

# 🔲 Task 4 - Frequency Domain

### Features

- **Fourier Transform**: Apply Fourier transform to any input signal and display frequency versus amplitude and frequency versus phase relations. The user will be prompted to enter the sampling frequency in Hz.
  
- **Modify Signal Components**: Allow modification of the amplitude and phase of the signal’s frequency components.

- **Signal Reconstruction (IDFT)**: Reconstruct the signal using Inverse Discrete Fourier Transform (IDFT).

- **Save Frequency Components**: Save the frequency components of the signal in a `.txt` file in polar form (amplitude and phase).

- **Read Frequency Components**: Read a `.txt` file containing frequency components in polar form and reconstruct the signal using IDFT.

**Hint**: Due to the similarity between DFT and IDFT, the code should be designed smartly to handle both transformations efficiently.

## 🎯 Usage
1. **Fourier Transform**: Input a signal, apply the Fourier transform, and view the frequency domain components (amplitude and phase).
2. **Modify Components**: Adjust the frequency components and view the updated signal in both time and frequency domains.
3. **Reconstruction**: Use IDFT to reconstruct the signal from its frequency components, either by computing them or loading from a file.
4. **Save & Load**: Save the frequency components of the signal in polar form and reload them to reconstruct the signal.
   

---

# 🔲 Task 5 - Frequency Domain Enhancements

### Features

- **Discrete Cosine Transform (DCT)**: Compute the DCT for a given input signal. Display the result and allow the user to choose the first `m` coefficients to be saved in a `.txt` file.

- **Remove DC Component**: Provide the functionality to remove the DC component from the signal.

## 🎯 Usage
1. **Compute DCT**: Apply DCT to an input signal, view the result, and save the first `m` coefficients if desired.
2. **Remove DC Component**: Process the signal to remove the DC component.


---


# 🔲 Task 6 - Time Domain

## Features

### 1. Smoothing
- **Moving Average**: Compute the moving average \( y(n) \) for a signal \( x(n) \). The user can specify the number of points to include in the averaging process.

### 2. Sharpening
- **First Derivative**: Compute and display the first derivative of the input signal \( Y(n) = x(n) - x(n-1) \).
- **Second Derivative**: Compute and display the second derivative of the input signal \( Y(n) = x(n+1) - 2x(n) + x(n-1) \).

### 3. Delaying or Advancing
- **Delay or Advance**: Shift the signal by \( k \) steps either forward (advancing) or backward (delaying).

### 4. Folding
- **Signal Folding**: Fold the signal to visualize its symmetric properties.

### 5. Delaying or Advancing a Folded Signal
- **Delay or Advance Folded Signal**: Shift the folded signal by \( k \) steps.

### 6. Remove DC Component
- **DC Component Removal**: Remove the DC component of the signal in the frequency domain.

### 7. Convolution
- **Signal Convolution**: Convolve two signals to analyze their interaction and combined effect.

## 🎯 Usage
1. **Smoothing**: Enter the number of points for averaging to smooth the signal.
2. **Sharpening**: Compute and display the first and second derivatives of the input signal.
3. **Delaying or Advancing**: Shift the signal by a specified number of steps.
4. **Folding**: Fold the signal to view its symmetrical properties.
5. **Delaying or Advancing Folded Signal**: Adjust the position of the folded signal.
6. **Remove DC Component**: Eliminate the DC component from the signal in the frequency domain.
7. **Convolution**: Convolve two signals and view the result.
   

---

Here’s the `README.md` section for Task 7:

---

# 🔲 Task 7 - Correlation

## Features

### 1. Correlation
- **Normalized Cross-Correlation**: Compute the normalized cross-correlation of two signals to measure their similarity and detect any shifts or alignments between them.

### 2. Time Analysis
- **Time Delay Analysis**: Perform time delay analysis on two periodic signals. Given the sampling period, approximate the delay between the two signals to understand their temporal relationship.

### 3. Template Matching
- **Template Matching**: Allow users to provide paths for two folders of signal classes and a test folder. Using template matching, the application will label all signals in the test folder based on their similarity to the templates provided in the class folders.

## 🎯 Usage
1. **Correlation**: Compute the normalized cross-correlation between two signals to analyze their similarity.
2. **Time Analysis**: Input two periodic signals and the sampling period to estimate the time delay between them.
3. **Template Matching**: Provide paths for class folders and a test folder, then use template matching to label signals in the test folder.


---
