import QtQuick 1.0

Rectangle {
    width: 480
    height: 272
    color: "black"
    border.color: "black"

    Text {
        id: headline
        x: 9
        y: 8
        width: 463
        height: 80
        color: "#ffffff"
        text: qsTr("Scan Your Tag")
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 67
    }

    Rectangle {
        id: start_match
        x: 145
        y: 214
        width: 191
        height: 50
        color: "#178b08"
        
        MouseArea {
            id: mousearea
            x: -1
            y: 0
            width: 192
            height: 50
            onClicked:{
                context.onClicked("start_match")
            }
        }
        
        Text {
            id: buttontext
            x: 0
            y: 0
            width: 191
            height: 50
            text: qsTr("Start Match")
            font.pixelSize: 34
        }
    }

    Text {
        id: teamatext
        x: 10
        y: 100
        width: 122
        height: 26
        color: "#ffffff"
        text: qsTr("Team A")
        font.pixelSize: 22
    }

    Text {
        id: teambtext
        x: 250
        y: 100
        width: 122
        height: 26
        color: "#ffffff"
        text: qsTr("Team B")
        font.pixelSize: 22
    }

    Text {
        id: teamaplayers
        x: 10
        y: 127
        width: 216
        height: 68
        color: "#ffffff"
        text: qsTr("(no player scanned)")
        font.pixelSize: 18
    }

    Text {
        id: teambplayers
        x: 256
        y: 127
        width: 216
        height: 68
        color: "#ffffff"
        text: qsTr("(no player scanned)")
        font.pixelSize: 18
    }
}