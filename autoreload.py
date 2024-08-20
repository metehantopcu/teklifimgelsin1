import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start()

    def start(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        self.start()

def main():
    command = 'gunicorn --reload app:app'  # 'myapp:app' kısmını uygulamanızın giriş noktası ile değiştirin
    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    print("Watching for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
