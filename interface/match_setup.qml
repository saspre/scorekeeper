import QtQuick 1.0

import "core" as Core 

Rectangle {
    width: 480
    height: 272
    color: "black"
    border.color: "black"
    
    function updateTeamA(playerIds){
        teamaplayers.text = playerIds
    }
    
    function updateTeamB(playerIds){
        teambplayers.text = playerIds
    }

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

    Core.Button {
        id: start_match
        callId: "start_match"
        btnText: "Start match"
        x: 145
        y: 214
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