from tkinter import *
import pygame
import sounddevice as sd
from scipy.io.wavfile import write

# from playsound import playsound
# from winsound import *

# website for beats = https://freewavesamples.com/bass-drum-2


class View:

    def __init__(self):
        """Starts up the gui."""
        self.window = Tk()
        pygame.init()
        self.audio_num = 0
        self.guitar_on = 0
        self.drum_on = 1
        self.piano_on = 0
        self.kick_drum_1 = pygame.mixer.Sound('Kick-drum.wav')
        self.snare_1 = pygame.mixer.Sound('Snare.wav')
        self.hihat_1 = pygame.mixer.Sound('Hi-Hat.wav')

        self.e_note = pygame.mixer.Sound('open-E-guitar (1).wav')
        self.a_note = pygame.mixer.Sound('open-a-guitar.wav')
        self.d_note = pygame.mixer.Sound('open-d-guitar (1).wav')
        self.g_note = pygame.mixer.Sound('open-g-guitar (1).wav')
        self.b_note = pygame.mixer.Sound('open-b-guitar (1).wav')
        self.little_e_note = pygame.mixer.Sound('open-high-e-guitar.wav')

        self.ep_note = pygame.mixer.Sound('pE.wav')
        self.ap_note = pygame.mixer.Sound('pianoA.wav')
        self.bp_note = pygame.mixer.Sound('pB.wav')
        self.cp_note = pygame.mixer.Sound('pianoC.wav')
        self.dp_note = pygame.mixer.Sound('pD.wav')
        self.fp_note = pygame.mixer.Sound('pF.wav')
        self.gp_note = pygame.mixer.Sound('pianoG.wav')

        self.window.title("Beat Maker")
        self.window.configure(background="black")
        ins = "BEAT MAKER"
        self.instructions = Label(self.window, text=ins, font='Helvetica 20 bold',
                                  bg='yellow').grid(row=0, column=2)
        space = ' '
        self.version = Label(self.window, text=space*20 + 'v.1' + space*20,
                             font='Helvetica 10 bold', bg='yellow').grid(row=1, column=2)

        self.label_drums = Label(self.window, text="DRUM", font="Helvetica 18 bold",
                                 bg="black", fg="red")
        self.label_kick = Label(self.window, text="KICK DRUMS",
                                font='Helvetica 14 bold', bg="black", fg='white')
        self.label_snare = Label(self.window, text="SNARES",
                                 font='Helvetica 14 bold', bg="black", fg='white')
        self.label_hihat = Label(self.window, text="HIHATS",
                                 font='Helvetica 14 bold', bg="black", fg='white')
        self.bottom = Label(self.window, text=space*30, bg="black").grid(row=9, column=2)
        self.label_drums.grid(row=2, column=2)
        self.label_kick.grid(row=3, column=2)
        self.label_snare.grid(row=5, column=2)
        self.label_hihat.grid(row=7, column=2)

        self.button_kick = Button(self.window, text="KICK DRUM 1", command=self.kick_drum_1_play)

        self.button_snare = Button(self.window, text="SNARE 1", command=self.snare_1_play)

        self.button_hihat = Button(self.window, text="HIHAT 1", command=self.hihat_1_play)

        self.button_kick.grid(row=4, column=2)
        self.button_snare.grid(row=6, column=2)
        self.button_hihat.grid(row=8, column=2)

        self.add_guitar_button = Button(
            self.window, text="CLICK TO ADD GUITAR", command=self.lay_out_guitar)
        self.add_guitar_button.grid(row=11, column=2)
        self.add_piano_button = Button(
            self.window, text="CLICK TO ADD PIANO", command=self.lay_out_piano)
        self.add_piano_button.grid(row=13, column=2)
        self.record_button = Button(
            self.window, text="RECORD for 15 seconds(FOR VOICE ONLY, USER CANNOT PLAY BEATS WHILE RECORDING VOICE)", command=self.record_audio)
        self.record_button.grid(row=14, column=2)
##
        self.window.mainloop()

    def lay_out_guitar(self):
        self.guitar_on = 1
        self.add_guitar_button.grid_forget()
        self.remove_guitar_button = Button(
            self.window, text="CLICK TO REMOVE GUITAR", command=self.delete_guitar)
        self.remove_guitar_button.grid(row=11, column=2)
        self.label_guitar = Label(self.window, text="GUITAR",
                                  font="Helvetica 18 bold", bg="black", fg="red")
        self.label_guitar.grid(row=1, column=0)
        self.e_label = Label(self.window, text="E NOTE",
                             font='Helvetica 14 bold', bg="black", fg='white')
        self.e_label.grid(row=2, column=0)
        self.a_label = Label(self.window, text="A NOTE",
                             font='Helvetica 14 bold', bg="black", fg='white')
        self.a_label.grid(row=4, column=0)
        self.d_label = Label(self.window, text="D NOTE",
                             font='Helvetica 14 bold', bg="black", fg='white')
        self.d_label.grid(row=6, column=0)
        self.g_label = Label(self.window, text="G NOTE",
                             font='Helvetica 14 bold', bg="black", fg='white')
        self.g_label.grid(row=8, column=0)
        self.b_label = Label(self.window, text="B NOTE",
                             font='Helvetica 14 bold', bg="black", fg='white')
        self.b_label.grid(row=10, column=0)
        self.little_e_label = Label(self.window, text="E NOTE",
                                    font='Helvetica 14 bold', bg="black", fg='white')
        self.little_e_label.grid(row=12, column=0)
        self.e_button = Button(self.window, text="E NOTE", command=self. play_g_e
                               )
        self.e_button.grid(row=3, column=0)
        self.a_button = Button(self.window, text="A NOTE", command=self.play_g_a
                               )
        self.a_button.grid(row=5, column=0)
        self.d_button = Button(self.window, text="D NOTE", command=self.play_g_d
                               )
        self.d_button.grid(row=7, column=0)
        self.g_button = Button(self.window, text="G NOTE", command=self.play_g_g
                               )
        self.g_button.grid(row=9, column=0)
        self.b_button = Button(self.window, text="B NOTE", command=self.play_g_b
                               )
        self.b_button.grid(row=11, column=0)
        self.little_e_button = Button(self.window, text="E NOTE", command=self.play_g_little_e
                                      )
        self.little_e_button.grid(row=13, column=0)

    def delete_guitar(self):
        self.guitar_on = 0
        self.label_guitar.grid_forget()
        self.e_label.grid_forget()
        self.a_label.grid_forget()
        self.d_label.grid_forget()
        self.g_label.grid_forget()
        self.b_label.grid_forget()
        self.little_e_label.grid_forget()
        self.e_button.grid_forget()
        self.a_button.grid_forget()
        self.d_button.grid_forget()
        self.g_button.grid_forget()
        self.b_button.grid_forget()
        self.little_e_button.grid_forget()
        self.remove_guitar_button.grid_forget()
        self.add_guitar_button.grid(row=12, column=2)

    def lay_out_piano(self):
        self.piano_on = 1
        self.add_piano_button.grid_forget()
        self.remove_piano_button = Button(
            self.window, text="CLICK TO REMOVE PIANO", command=self.delete_piano)
        self.remove_piano_button.grid(row=13, column=2)
        self.piano_label = Label(self.window, text="PIANO", font="Helvetica 18 bold",
                                 bg="black", fg="red")
        self.piano_label.grid(row=1, column=4)
        self.cp_label = Label(self.window, text="E NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.cp_label.grid(row=2, column=4)
        self.ap_label = Label(self.window, text="A NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.ap_label.grid(row=4, column=4)
        self.ep_label = Label(self.window, text="B NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.ep_label.grid(row=6, column=4)
        self.gp_label = Label(self.window, text="C NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.gp_label.grid(row=8, column=4)
        self.bp_label = Label(self.window, text="B NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.bp_label.grid(row=10, column=4)
        self.fp_label = Label(self.window, text="F NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.fp_label.grid(row=12, column=4)
        self.dp_label = Label(self.window, text="G NOTE",
                              font='Helvetica 14 bold', bg="black", fg='white')
        self.dp_label.grid(row=14, column=4)

        self.ep_button = Button(self.window, text="E NOTE", command=self.play_ep
                                )
        self.ep_button.grid(row=3, column=4)
        self.ap_button = Button(self.window, text="A NOTE", command=self.play_ap
                                )
        self.ap_button.grid(row=5, column=4)
        self.bp_button = Button(self.window, text="B NOTE", command=self.play_bp
                                )
        self.bp_button.grid(row=7, column=4)
        self.cp_button = Button(self.window, text="C NOTE", command=self.play_cp
                                )
        self.cp_button.grid(row=9, column=4)
        self.dp_button = Button(self.window, text="B NOTE", command=self.play_dp
                                )
        self.dp_button.grid(row=11, column=4)
        self.fp_button = Button(self.window, text="F NOTE", command=self.play_fp
                                )
        self.fp_button.grid(row=13, column=4)
        self.gp_button = Button(self.window, text="G NOTE", command=self.play_gp
                                )
        self.gp_button.grid(row=15, column=4)

    def record_audio(self):
        """
        if self.piano_on == 1:
            self.delete_piano()
        if self.guitar_on == 1:
            self.delete_guitar()
        self.delete_mid_screen()
        """
        file_name = 'audio' + str(self.audio_num) + '.wav'

        # This connects to the microphone and is able to record any sound that is picked up
        # I was thinking that since if you play the sound you can also hear the
        # sound picked up by the microphone, we can use this.
        # The only thing is that it works in the program if you just hit record but
        # when you try pressing the other buttons, it crashes and that might just be
        # because im not defining everything well enough.
        fs = 44100
        seconds = 15  # We can change this but for now 15 since we have to test it
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(file_name, fs, recording)  # The audio name needs to be changing every single time
        # or it not it won't work.
        self.audio_num += 1

    def delete_mid_screen(self):
        self.drum_on = 1
        self.label_drums.grid_forget()
        self.label_kick.grid_forget()
        self.label_snare.grid_forget()
        self.label_hihat.grid_forget()

        self.button_kick.grid_forget()
        self.button_snare.grid_forget()
        self.button_hihat.grid_forget()

        self.add_guitar_button.grid_forget()
        self.add_piano_button.grid_forget()
        self.add_piano_button.grid_forget()

    def delete_piano(self):
        self.piano_on = 0
        self.piano_label.grid_forget()
        self.cp_label.grid_forget()
        self.ap_label.grid_forget()
        self.ep_label.grid_forget()
        self.gp_label.grid_forget()
        self.bp_label.grid_forget()
        self.fp_label.grid_forget()
        self.dp_label.grid_forget()
        self.ep_button.grid_forget()
        self.ap_button.grid_forget()
        self.bp_button.grid_forget()
        self.cp_button.grid_forget()
        self.dp_button.grid_forget()
        self.fp_button.grid_forget()
        self.gp_button.grid_forget()
        self.remove_piano_button.grid_forget()
        self.add_piano_button.grid(row=13, column=2)

    def kick_drum_1_play(self):
        self.kick_drum_1.play()

    def snare_1_play(self):
        self.snare_1.play()

    def hihat_1_play(self):
        self.hihat_1.play()

    def play_g_e(self):
        self.e_note.play()

    def play_g_a(self):
        self.a_note.play()

    def play_g_d(self):
        self.d_note.play()

    def play_g_g(self):
        self.g_note.play()

    def play_g_b(self):
        self.b_note.play()

    def play_g_little_e(self):
        self.little_e_note.play()

    def play_cp(self):
        self.cp_note.play()

    def play_ap(self):
        self.ap_note.play()

    def play_ep(self):
        self.ep_note.play()

    def play_gp(self):
        self.gp_note.play()

    def play_bp(self):
        self.bp_note.play()

    def play_fp(self):
        self.fp_note.play()

    def play_dp(self):
        self.dp_note.play()
