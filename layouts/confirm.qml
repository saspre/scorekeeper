import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: match
    width: 480
    height: 272


    function updateMatchResult(result) {
        match_result.text = result 
    }

    Core.BaseText {
        id: match_result
        width: parent.width
        x: match.getCenterX(match_result)
        y: 30

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
