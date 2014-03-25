import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: page
    width: 480
    height: 272


    function updateMatchResult(result) {
        match_result.text = result 
    }

    Core.ScoreText {
        id: match_result_header
        x: page.getCenterX(match_result_header)
        y: page.margin
        text: qsTr("Match ended: ")

    }

    Core.ScoreText {
        id: match_result
        x: page.getCenterX(match_result)
        y: 90
        text: qsTr("0 - 0")

    }
   
    

    Core.Button {
        id: cancel
        x: 45
        y: 218
       
       
        callId: "cancel"
        btnText: "Cancel"
    }

     Core.Button {
        id: confirm
        x: 307
        y: 218
       
       
        callId: "confirm"
        btnText: "Confirm"
    }

  
}
