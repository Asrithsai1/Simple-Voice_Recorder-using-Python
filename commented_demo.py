
from tkinter import *
from tkinter import messagebox
import sounddevice as psound  # For recording audio
from scipy.io.wavfile import write  # For saving the audio file
import time  # For handling timing functions

# Create the main window
window = Tk()
window.geometry("600x700+410+90")  # Set window size and position
window.title("My own voice recorder")  # Set window title
window.configure(background="light blue")  # Set background color

# Function to start recording
def fun_rec():
    freq = 44100  # Sample rate in Hz
    dur = int(time_dur.get())  # Get the duration from the user input
    
    # Start recording with the specified duration and sample rate
    recording = psound.rec(int(dur * freq), samplerate=freq, channels=2)
    
    try:
        my_temp = int(time_dur.get())  # Get the duration for countdown
    except ValueError:
        print("Please enter a valid time duration")  # Error message for invalid input
        return

    # Countdown timer while recording
    while my_temp > 0:
        window.update()  # Update the window
        time.sleep(1)  # Wait for 1 second
        my_temp -= 1  # Decrease the timer by 1
        
        if my_temp == 0:
            messagebox.showinfo("Time countdown", "Time is up")  # Show message when time is up
        
        # Update the countdown display on the screen
        Label(text=f"{str(my_temp)}", font="Arial, 40", width=4, background="light blue").place(x=250, y=600)
    
    psound.wait()  # Wait until the recording is finished
    write("record.wav", freq, recording)  # Save the recording as a WAV file

# Load and set the window icon
icon_img = PhotoImage(file="record.png")
window.iconphoto(False, icon_img)

# Display an image in the window (e.g., a microphone icon)
img = PhotoImage(file="record.png")
my_image = Label(image=img, background="light blue")
my_image.pack(padx=5, pady=5)

# Add a title label to the window
Label(text="Voice Recorder", font=("Arial", 32, "bold"), background="light blue", fg="black").pack()

# Input field for the user to enter recording duration
time_dur = StringVar()
time_entry = Entry(window, textvariable=time_dur, font=("Arial", 32, "bold"), width=15).pack(pady=10)
Label(text="Enter the time in seconds", font=("Arial", 17, "bold"), background="light blue", fg="black").pack()

# Button to start recording
record_bt = Button(window, font=("Arial", 22, "bold"), text="Record", bg="light blue", fg="black", borderwidth=0, command=fun_rec).pack()

# Run the main loop of the Tkinter window
window.mainloop()
