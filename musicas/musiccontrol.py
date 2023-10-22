from pygame import mixer

mixer.init()

class Radio:
    def __init__(self):
        
        self.volume = 0.2
        
    def play(self, music):
        
        mixer.music.load(music)
        mixer.music.set_volume(self.volume)
        mixer.music.play(-1)
        
    def stop(self):
        
        mixer.music.stop()
        
radio = Radio()