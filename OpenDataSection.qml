import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: parent ? parent.width - 40 : 800
    height: 500
    color: "#fafafa"
    radius: 8
    border.width: 1
    border.color: "#cccccc"

    Column {
        anchors.margins: 12
        anchors.fill: parent
        spacing: 12

        Label { 
            text: "Open Data Publishing"
            font.bold: true
            font.pointSize: 16
        }

        Row {
            spacing: 12

            Button {
                text: "Open Data"
                onClicked: {
                    avatarBackend.openFileDialog()
                }
            }

            Label {
                id: statusLabel
                text: "Idle"
                color: "blue"
            }
        }

        TextArea {
            id: consoleLog
            width: parent.width - 24
            height: 350
            wrapMode: TextArea.Wrap
            readOnly: true
        }

       Connections {
    target: avatarBackend

    function onLogUpdated(log) {
        consoleLog.text += log + "\n"
        consoleLog.moveCursorSelection(consoleLog.text.length)
    }

    function onStatusChanged(status) {
        statusLabel.text = status
        if (status === "Success") statusLabel.color = "green"
        else if (status.indexOf("Error") !== -1) statusLabel.color = "red"
        else statusLabel.color = "blue"
    }
}

    }
}
