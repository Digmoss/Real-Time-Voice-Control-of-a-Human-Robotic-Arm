#! /usr/bin/python3
import time
import tkinter as tk
import sounddevice as sd
import speech_recognition as sr
from threading import Thread
from PIL import Image, ImageTk
from commands_class_V2 import commands

listeningText = "אמור פקודה לביצוע"

class SpeechRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Speech Recognition App")
        self.master.geometry("350x350")

        self.start_button = tk.Button(master, text="Start", command=self.start_listening)
        self.start_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.stop_listening, state=tk.DISABLED)
        self.exit_button.pack()

        self.output_label = tk.Label(master, text="")
        self.output_label.pack()

        self.ear_image = ImageTk.PhotoImage(Image.open("listening.png"))
        self.gear_image = ImageTk.PhotoImage(Image.open("proccessing.png"))

        self.image_lable =tk.Label(master, image=None)
        self.image_lable.pack()

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.myCommand = commands()

        self.is_listening = False

    def start_listening(self):
        self.start_button.pack_forget()
        self.exit_button["state"] = tk.NORMAL
        self.is_listening = True

        self.myCommand.close_all()

        listening_thread = Thread(target=self.my_listen)
        listening_thread.start()

    def makemove(self, val):
        text = "פקודה לא חוקית, נסה שוב"
        match val:
            case "אגודל":
                text = self.myCommand.thumb()
            case "אצבע":
                text = self.myCommand.index()
            case "אמה":
                text = self.myCommand.middle()
            case "קמיצה":
                text = self.myCommand.ring()
            case "זרת":
                text = self.myCommand.pinky()
            case "פתח":
                text = self.myCommand.open_all()
            case "אגרוף":
                text = self.myCommand.close_all()
            case default:
                pass
        return text

    def my_listen(self):
        while self.is_listening:
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=3)
                    self.image_lable.config(image=self.ear_image)
                    self.master.after(0, lambda: self.output_label.config(text=f"{listeningText[::-1]}", font=("Helvetica", 20), fg="green"))
                    self.master.update()
                    audio_data = self.recognizer.listen(source, phrase_time_limit=3)

                    self.image_lable.config(image=self.gear_image)
                    self.master.update()

                    text = self.recognizer.recognize_google(audio_data, language="iw-IL")
                    text2 = self.makemove(text)
                    if(text2=="פקודה לא חוקית, נסה שוב"):
                        self.master.after(0, lambda: self.update_output_label(text2, "red"))
                    else:
                        self.master.after(0, lambda: self.update_output_label(text2, "black"))
                    time.sleep(1)

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")
        time.sleep(1)
        self.master.after(100, self.my_listen)


    def update_output_label(self, text, color):
        if text is not None:
            self.output_label.config(text=text[::-1], font=("Helvetica", 20), fg=color)


    def stop_listening(self):
        self.is_listening = False
        self.start_button.pack()
        self.exit_button["state"] = tk.DISABLED
        self.master.after(100, self.stop_listening_task)


    def stop_listening_task(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechRecognitionApp(root)
    root.mainloop()