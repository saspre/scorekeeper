import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: page
    width: 480
    height: 272


    function updateErrorMessage(msg) {
        match_result.text = msg 
    }

    Core.ScoreText {
        id: match_result
        x: page.getCenterX(match_result)
        y: 10
        text: qsTr("An error Occured")

    }
   
    

    Core.Button {
        id: okay
        x: page.getCenterX(okay)
        y: 218
       
       
        callId: "okay"
        btnText: "Okay"
    }

    

  
}
