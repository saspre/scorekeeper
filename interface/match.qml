import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: match
    width: 480
    height: 272




    function updateScoreA(string ) {
        score_a.text = string
    }

    function updateScoreB(string ) {
        score_b.text = string
    }

    Core.ScoreText {
        id: score_a
        x: 45
        y: 8
        text: qsTr("0")
    }

    Core.ScoreText {
        id: score_b
        x: 303
        y: 8
        text: qsTr("0")
  
    }

    Core.ScoreText {
        id: dash
        x: 232
        y: 8
        text: qsTr("-")
    }

    

    Core.Button {
        id: team_a_score
        x: 45
        y: 218
       
       
        callId: "team_a_score"
        btnText: "Score A"
    }

     Core.Button {
        id: team_b_score
        x: 307
        y: 218
       
       
        callId: "team_b_score"
        btnText: "Score B"
    }

    Core.Button {
        id: start_game
        x: 177
        y: 113
        callId: "start_game"
        btnText: "Start Game"
    }

}
