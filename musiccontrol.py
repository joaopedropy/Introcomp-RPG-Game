from pygame import mixer

mixer.init()

class Radio:
    def __init__(self, music, volume = 0.2, repeat = False):
        
        self.music = music
        self.volume = volume
        self.repeat = repeat
        
    def play(self):
        
        mixer.music.load(self.music)
        mixer.music.set_volume(self.volume)
        mixer.music.play(-1)
        
    def stop(self):
        
        mixer.music.stop()
        
radio = Radio("musicas/Menu.wav")