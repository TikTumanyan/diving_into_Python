import os
import shutil

types = {
    'Pictures New': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos New': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv'],
    'Documents New': ['.pdf', '.docx', '.txt', '.xls', '.ppt', '.md'],
    'All Other': []
}

desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

for folder in types:
    os.makedirs(os.path.join(desktop, folder), exist_ok=True)

def organizing():
    for file in os.listdir(desktop):
        file_path = os.path.join(desktop, file)
        if os.path.isdir(file_path): continue
        ext = os.path.splitext(file)[1].lower()
        moved = False
        for folder, extensions in types.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(desktop, folder, file))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(desktop, 'Other', file)))

if __name__ == "__main__":
    organizing()

