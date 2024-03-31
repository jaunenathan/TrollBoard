import sys
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget, QVBoxLayout, QSlider, QLabel, QProgressBar, QMenuBar, QMenu, QAction, QSizePolicy, QTabWidget, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QTimer, QSize
import yt_dlp
from PyQt5.QtGui import QCursor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl, Qt, QEvent
from datetime import datetime, timedelta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        icon = QIcon('iconnn.ico')
        self.setWindowIcon(icon)
        self.setWindowTitle('TrollBoard by jaunenathan')
        self.load_styles()
        menu_bar = QMenuBar(self)
        file_menu = QMenu('File', self)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        menu_bar.addMenu(file_menu)
        self.setMenuBar(menu_bar)
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.sounds_tab = QWidget()
        self.tab_widget.addTab(self.sounds_tab, 'Sounds')
        self.sounds_layout = QVBoxLayout(self.sounds_tab)
        self.sounds_list = QListWidget(self.sounds_tab)
        self.sounds_list.setSelectionMode(QListWidget.ExtendedSelection)
        self.sounds_list.itemDoubleClicked.connect(self.play_sound)
        self.sounds_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sounds_list.setMaximumSize(QSize(16777215, 300))
        self.search_bar = QLineEdit(self.sounds_tab)
        self.search_bar.setPlaceholderText('Search sounds...')
        self.search_bar.textChanged.connect(self.search_sounds)
        self.slider = QSlider(Qt.Horizontal, self.sounds_tab)
        self.slider.setRange(0, 100)
        self.slider.setValue(0)
        self.slider.sliderMoved.connect(self.set_position)
        self.label = QLabel('Position: 0%', self.sounds_tab)
        self.stop_button = QPushButton('Stop', self.sounds_tab)
        self.stop_button.clicked.connect(self.stop_sound)
        self.sounds_layout.addWidget(self.search_bar)
        self.sounds_layout.addWidget(self.sounds_list)
        self.sounds_layout.addWidget(self.slider)
        self.sounds_layout.addWidget(self.label)
        self.sounds_layout.addWidget(self.stop_button)
        self.sounds_layout.addSpacing(50)
        self.download_tab = QWidget()
        self.tab_widget.addTab(self.download_tab, 'Download')
        self.download_layout = QVBoxLayout(self.download_tab)
        self.url_input = QLineEdit(self.download_tab)
        self.url_input.setPlaceholderText('Enter YouTube URL here')
        self.download_button = QPushButton('Download', self.download_tab)
        self.download_button.clicked.connect(self.download_sound)
        self.progress_bar = QProgressBar(self.download_tab)
        self.download_layout.addWidget(self.url_input)
        self.download_layout.addWidget(self.download_button)
        self.download_layout.addWidget(self.progress_bar)
        self.sound = None
        self.player = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider)
        self.load_sounds()
        self.setFixedSize(800, 600)

    def load_styles(self):
        self.setStyleSheet("""
/* Base */
* {
    color: #e0e0e0;
    font-family: "Segoe UI", sans-serif;
}

QMainWindow, QWidget {
    background-color: #2c2c2c;
}

/* Buttons */
QPushButton {
    background-color: #4a4a4a;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    outline: none;
}

QPushButton:hover {
    background-color: #5f5f5f;
}

QPushButton:pressed {
    background-color: #3d3d3d;
}

/* LineEdit */
QLineEdit {
    background-color: #4a4a4a;
    border: none;
    padding: 10px;
    border-radius: 5px;
}

/* ListWidget */
QListWidget {
    background-color: #4a4a4a;
    border: none;
    padding: 10px;
    border-radius: 5px;
    outline: none;
}

QListWidget::item:hover {
    background-color: #5f5f5f;
}

QListWidget::item:selected {
    background-color: #3d3d3d;
}

/* Slider */
QSlider {
    background-color: #4a4a4a;
    border: none;
    outline: none;
}

QSlider::groove:horizontal {
    border: none;
    height: 10px;
    background: #5f5f5f;
    border-radius: 5px;
}

QSlider::handle:horizontal {
    background: #7f7f7f;
    width: 20px;
    margin: -5px 0;
    border-radius: 5px;
}

/* ProgressBar */
QProgressBar {
    background-color: #4a4a4a;
    border: none;
    text-align: center;
    border-radius: 5px;
}

QProgressBar::chunk {
    background-color: #7f7f7f;
    border-radius: 5px;
}

/* MenuBar */
QMenuBar {
    background-color: #3d3d3d;
    border: none;
    padding: 5px;
    border-radius: 5px;
}

QMenuBar::item {
    background-color: transparent;
    padding: 10px;
    border-radius: 5px;
}

QMenuBar::item:selected {
    background-color: #4a4a4a;
}

/* Menu */
QMenu {
    background-color: #3d3d3d;
    border: none;
    padding: 10px;
    border-radius: 5px;
}

QMenu::item {
    background-color: transparent;
    padding: 10px;
    border-radius: 5px;
}

QMenu::item:selected {
    background-color: #4a4a4a;
}

/* TabWidget */
QTabWidget::pane {
    background-color: #3d3d3d;
    border: none;
    padding: 10px;
    border-radius: 5px;
}

QTabBar::tab {
    background-color: #4a4a4a;
    border: none;
    padding: 10px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:selected {
    background-color: #3d3d3d;
}

/* ScrollBar */
QScrollBar:vertical {
    background-color: #4a4a4a;
    width: 8px;
    border-radius: 4px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background-color: #7f7f7f;
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
    background-color: transparent;
    height: 0px;
}

QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical {
    background-color: #5f5f5f;
    border-radius: 4px;
}

        """)

    def download_sound(self):
        url = self.url_input.text()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'sounds/%(title)s.%(ext)s',
            'progress_hooks': [self.update_progress],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        title = info['title']
        self.sounds_list.addItem(title)
        self.save_sounds()

    def play_sound(self, item=None):
        if item is None:
            item = self.sounds_list.currentItem()
        if isinstance(item, bool):
            item = self.sounds_list.itemAt(self.sounds_list.mapFromGlobal(QCursor.pos()))
        if item is not None:
            title = item.text()
            self.player = QMediaPlayer()
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f'sounds/{title}.mp3')))
            self.player.play()
            self.slider.setRange(0, self.player.duration())
            self.timer.start(1000)

    def stop_sound(self):
        if self.player is not None:
            self.player.stop()
        self.timer.stop()
        self.slider.setValue(0)

    def set_position(self, position):
        if self.player is not None and self.player.is_playing():
            self.player.setPosition(position)

    def update_slider(self):
        if self.player is not None and self.player.state() == QMediaPlayer.PlayingState:
            current_time = self.player.position() / 1000
            self.slider.setValue(int(current_time))
            remaining_time = self.player.duration() - self.player.position()
            current_time_str = str(timedelta(seconds=int(current_time)))
            remaining_time_str = str(timedelta(seconds=int(remaining_time / 1000)))
            self.label.setText(f'Départ: {current_time_str} / Fin: {remaining_time_str}')
        else:
            self.slider.setValue(0)
            self.label.setText('Départ: 0:00:00 / Fin: 0:00:00')

    def update_progress(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes', 0)
            downloaded_bytes = d.get('downloaded_bytes', 0)
            progress = int(downloaded_bytes / total_bytes * 100)
            self.progress_bar.setValue(progress)

    def load_sounds(self):
        sounds_dir = 'sounds'
        if not os.path.exists(sounds_dir):
            os.mkdir(sounds_dir)
        for filename in os.listdir(sounds_dir):
            if filename.endswith('.mp3'):
                title = os.path.splitext(filename)[0]
                self.sounds_list.addItem(title)

    def save_sounds(self):
        sounds_dir = 'sounds'
        if not os.path.exists(sounds_dir):
            os.mkdir(sounds_dir)
        with open('sounds.txt', 'w', encoding='utf-8') as f:
            for i in range(self.sounds_list.count()):
                title = self.sounds_list.item(i).text()
                f.write(f'{title}.mp3\n')

    def search_sounds(self, text):
        for i in range(self.sounds_list.count()):
            item = self.sounds_list.item(i)
            if text.lower() in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
