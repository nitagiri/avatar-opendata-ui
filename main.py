import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from avatar_backend import AvatarBackend

def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = AvatarBackend()
    engine.rootContext().setContextProperty("avatarBackend", backend)

    engine.load("CloudComputingTab.qml")

    if not engine.rootObjects():
        print("Failed to load QML")
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
