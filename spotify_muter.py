import time
import win32gui
import win32process
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

class SpotifyMuter:
    def __init__(self):
        self.muted = False
        self.previous_volume = 1.0  # Default to max volume if unknown

    def get_spotify_session(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == "Spotify.exe":
                return session
        return None

    def get_window_title_by_pid(self, pid):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    hwnds.append(hwnd)
            return True
        
        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        
        for hwnd in hwnds:
            title = win32gui.GetWindowText(hwnd)
            if title and title != "Default IME" and title != "MSCTFIME UI": # Filter common invisible/overlay windows
                 # Spotify main window usually has a title. Sometimes there are multiple windows.
                 # The main player window title changes with the song.
                 return title
        return None

    def is_ad(self, title):
        # Strategy: Allowlist approach.
        # 1. "Artist - Song" format is considered content.
        # 2. Specific static titles are considered idle/safe.
        # 3. Everything else is treated as an ad.
        
        # Check for standard music format "Artist - Song"
        if " - " in title:
            return False
            
        # Allow specific static titles (Idle states)
        allowed_titles = ["Spotify", "Spotify Free", "Spotify Premium"]
        if title in allowed_titles:
            return False
            
        # If it doesn't look like a song and isn't a known safe title, mute it.
        return True

    def run(self):
        print("Spotify Ad Muter started... Press Ctrl+C to exit.")
        try:
            while True:
                session = self.get_spotify_session()
                if session:
                    volume = session.SimpleAudioVolume
                    pid = session.ProcessId
                    title = self.get_window_title_by_pid(pid)
                    
                    if title:
                        # print(f"Current Title: {title}") # Debugging
                        if self.is_ad(title):
                            if not self.muted:
                                print(f"Ad detected: '{title}'. Muting...")
                                self.previous_volume = volume.GetMasterVolume()
                                volume.SetMasterVolume(0.0, None)
                                self.muted = True
                        else:
                            if self.muted:
                                print(f"Ad finished: '{title}'. Restoring volume...")
                                volume.SetMasterVolume(self.previous_volume, None)
                                self.muted = False
                    else:
                        # Could not find window title, maybe minimized to tray or no visible window
                        pass
                else:
                    # Spotify not running
                    pass

                time.sleep(1) 
        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    muter = SpotifyMuter()
    muter.run()
