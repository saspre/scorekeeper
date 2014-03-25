

import QtQuick 1.1

import "core" as Core 

Core.Interface {
    id: page
    width: 480
    height: 272
    property int btndist: 65


     Core.BaseText {
        id: menuhead
        font.pixelSize: 42
        text: qsTr("GameLink")
        y: page.margin 
        x: page.getCenterX(menuhead)
    }

    Core.MenuButton {
        id: startmatch_btn
        callId: "new_match"
        btnText: qsTr("Start Match")
        y: page.margin + btndist
        x: page.getCenterX(startmatch_btn)
    }

    Core.MenuButton {
        id: recentmatch_btn
        callId: "recent_matches"
        x: page.getCenterX(startmatch_btn)
        y: page.margin + btndist * 2
        
        btnText: qsTr("Recent Matches")
    }

    Core.MenuButton {
        id: get_serial_btn
        callId: "get_serial"
        x: page.getCenterX(get_serial_btn)
        y: page.margin + btndist * 3
        
        btnText: qsTr("Check Serial")
    }


}
