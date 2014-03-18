import QtQuick 1

Rectangle {
    signal messageRequired;
    id: one

    Rectangle {
        signal something;
        id: inner
        width: 480
        height: 272
        opacity: 0

    }

    function updateMessage(text) {
        messageText.text = text
        inner.opacity = 0

    }

    anchors.fill: parent; color: "black"

    Text {

        id: messageText
        anchors.centerIn: parent; color: "white"
    }

    MouseArea {
        anchors.fill: parent
        onClicked: messageRequired()
    }
}

