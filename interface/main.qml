import QtQuick 1.1

Rectangle {
    id: rectangle1
    width: 480
    height: 272
    gradient: Gradient {
        GradientStop {
            id: gradientStop1
            position: 0
            color: "#ffffff"
        }

        GradientStop {
            position: 1
            color: "#abc09f"
        }
    }

    Text {
        id: score_a
        x: 45
        y: 8
        width: 131
        height: 48
        text: qsTr("Text")
        verticalAlignment: Text.AlignVCenter
        font.pixelSize: 12
    }

    Text {
        id: score_b
        x: 303
        y: 8
        width: 131
        height: 48
        text: qsTr("Text")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 12
    }

    Text {
        id: dash
        x: 232
        y: 5
        text: qsTr("-")
        horizontalAlignment: Text.AlignHCenter
        font.pixelSize: 47
    }

    MouseArea {
        id: a_scored
        x: 303
        y: 200
    }

    Rectangle {
        id: team_a
        x: 45
        y: 218
        width: 127
        height: 46
        color: "#4e3a3a"
        radius: 10

        TextInput {
            id: team_a_txt
            x: 24
            y: 13
            width: 80
            height: 20
            text: qsTr("A")
            horizontalAlignment: TextInput.AlignHCenter
            font.pixelSize: 12
        }

        MouseArea {
            id: team_a_score_ma
            x: 0
            y: 0
            width: 126
            height: 46
            onClicked: {
                qScoreInterface.aScored()
            }
        }
    }

    Rectangle {
        id: team_b
        x: 307
        y: 218
        width: 127
        height: 46
        color: "#4e3a3a"
        radius: 10
        TextInput {
            id: team_b_txt1
            x: 24
            y: 13
            width: 80
            height: 20
            text: qsTr("B")
            horizontalAlignment: TextInput.AlignHCenter
            font.pixelSize: 12
        }

        MouseArea {
            id: team_b_score_ma1
            x: 0
            y: 0
            width: 126
            height: 46
            onClicked: {
                qScoreInterface.bScored()
            }
        }
    }

}
