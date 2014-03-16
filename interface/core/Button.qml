import QtQuick 1.0

Rectangle {
    id: button
    width: 191
    height: 50
    color: "#178b08"
    radius: 10
    property string btnText
    property string callId
    
    MouseArea {
           
       anchors.fill: parent
       onPressed: parent.color = "#645fa9"
       onReleased: parent.color = "#d1d7f5"
       onClicked: {
           context.onClicked(button.callId)
        }
    }
    border.color: "#645fa9"
    border.width: 2
   
    
    Text {
        id: textBtn
        width: 191
        height: 50
        text: parent.btnText
        font.pixelSize: 34
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }
}	

