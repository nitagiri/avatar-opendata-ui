import sys
import os
import subprocess
import threading
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QFileDialog, QApplication

class AvatarBackend(QObject):
    logUpdated = Signal(str)
    statusChanged = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def openFileDialog(self):
        folder = QFileDialog.getExistingDirectory(None, "Select processed folder")
        if folder:
            self.runOpenData(folder)

    def runOpenData(self, folderPath):
        if not folderPath:
            self.statusChanged.emit("Error: No folder selected")
            return

        thread = threading.Thread(target=self._run_process, args=(folderPath,), daemon=True)
        thread.start()

    def _run_process(self, folderPath):
        self.statusChanged.emit("Running")

        script = os.path.join("file-opendata", "opendata.py")
        if not os.path.exists(script):
            self.statusChanged.emit("Error: opendata.py not found")
            self.logUpdated.emit(f"Expected script at: {script}")
            return

        cmd = [sys.executable, "-u", script, folderPath]

        try:
            self.logUpdated.emit(f"Starting: {' '.join(cmd)}")
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True
            )
            for line in proc.stdout:
                self.logUpdated.emit(line.rstrip("\n"))

            proc.wait()
            if proc.returncode == 0:
                self.statusChanged.emit("Success")
                self.logUpdated.emit("Open Data finished successfully.")
            else:
                self.statusChanged.emit(f"Error: Return code {proc.returncode}")
                self.logUpdated.emit(f"Process exited with code {proc.returncode}")

        except Exception as e:
            self.statusChanged.emit(f"Error: {str(e)}")
            self.logUpdated.emit(f"Exception: {str(e)}")
