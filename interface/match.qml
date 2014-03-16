import QtQuick 1.1

import "core" as Core 

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

    function updateScoreA(string ) {
        score_a.text = string
    }

    function updateScoreB(string ) {
        score_b.text = string
    }

    Text {
        id: score_a
        x: 45
        y: 8
        width: 131
        height: 48
        text: qsTr("0")
        verticalAlignment: Text.AlignVCenter
        font.pixelSize: 42
    }

    Text {
        id: score_b
        x: 303
        y: 8
        width: 131
        height: 48
        text: qsTr("0")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignRight
        font.pixelSize: 42


        
      
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
            id: team_a_score
            x: 0
            y: 0
            width: 126
            height: 46
            onClicked: {
                context.onClicked("team_a_score")
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
            id: team_b_txt
            x: 24
            y: 13
            width: 80
            height: 20
            text: qsTr("B")
            horizontalAlignment: TextInput.AlignHCenter
            font.pixelSize: 12
        }

        MouseArea {
            id: team_b_score
            x: 0
            y: 0
            width: 126
            height: 46
            onClicked: {
                context.onClicked("team_b_score")
            }
        }
    }

    Rectangle {
        id: startstopgame
        x: 177
        y: 113
        width: 127
        height: 46
        color: "#4e3a3a"
        radius: 10
        TextInput {
            id: startstopgame_txt
            x: 24
            y: 13
            width: 80
            height: 20
            text: qsTr("Start Game")
            horizontalAlignment: TextInput.AlignHCenter
            font.pixelSize: 12
        }

        MouseArea {
            id: startstopgame_ma
            x: 1
            y: 0
            width: 126
            height: 46
            onClicked: {
                qScoreInterface.startMatch()
            }
        }
    }

}
