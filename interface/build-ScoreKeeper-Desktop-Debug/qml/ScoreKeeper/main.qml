import QtQuick 1.1

Rectangle {
    width: 360
    height: 360
    Text {
        text: qsTr("Hello World")
        anchors.centerIn: parent
    }
    MouseArea {
        width: 480
        height: 272
        anchors.fill: parent
        onClicked: {
            Qt.quit();
        }
    }
}
