import webview
import os

# Path to your HTML file
html_file = os.path.join(os.path.dirname(__file__), './ui/index.html')

def create_window():
    window = webview.create_window('My Application', html_file)
    webview.start()

if __name__ == '__main__':
    create_window()
