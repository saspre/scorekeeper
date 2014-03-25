


import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: page
    width: 480
    height: 272


    function updateSerial(msg) {
        serialtxt.text = msg 
    }

    Core.ScoreText {
        id: serialtxt
        x: page.getCenterX(serialtxt)
        y: 10
        text: qsTr("Place Tag")

    }

    

    Core.Button {
        id: okay
        x: page.getCenterX(okay)
        y: 218
       
       
        callId: "okay"
        btnText: "Okay"
    }

    

  
}
