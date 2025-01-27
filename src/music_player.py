import pygame.mixer
from pathlib import Path

THEME_SONG = "media/theme.mp3"


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_track = None
        self.is_paused = False
        self.load_track(THEME_SONG)
        self.play()

    def load_track(self, file_path: str | Path) -> bool:
        """
        Load a music track from the specified path.
        Returns True if successful, False otherwise.
        """
        try:
            pygame.mixer.music.load(file_path)
            self.current_track = file_path
            return True
        except pygame.error:
            print(f"Error loading music file: {file_path}")
            return False

    def play(self, loops: int = -1) -> None:
        """
        Start playing the currently loaded track.
        loops: Number of times to loop (-1 for infinite)
        """
        if self.current_track:
            pygame.mixer.music.play(loops)
            self.is_paused = False

    def pause(self) -> None:
        """Pause the currently playing track"""
        if not self.is_paused and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_paused = True

    def unpause(self) -> None:
        """Resume playing the paused track"""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self) -> None:
        """Stop the currently playing track"""
        pygame.mixer.music.stop()
        self.is_paused = False

    def set_volume(self, volume: float) -> None:
        """
        Set the volume of the music player
        volume: Float between 0.0 and 1.0
        """
        pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))

    def get_volume(self) -> float:
        """Get the current volume"""
        return pygame.mixer.music.get_volume()

    def is_playing(self) -> bool:
        """Check if music is currently playing"""
        return pygame.mixer.music.get_busy() and not self.is_paused
