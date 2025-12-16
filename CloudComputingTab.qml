import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: root
    visible: true
    width: 900
    height: 700
    title: "Avatar — Cloud Computing"

    ScrollView {
        anchors.fill: parent

        Column {
            width: parent.width
            spacing: 20
            padding: 20

            Label {
                text: "Cloud Computing"
                font.bold: true
                font.pointSize: 20
            }

            // Include the Open Data UI section
            OpenDataSection { }
        }
    }
}
