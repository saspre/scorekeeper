import QtQuick 1.0

Rectangle {
    id: button
    width: 150
    height: 50
    color: startColor
    radius: 10
    property string btnText
    property string callId
    property string startColor:"#178b08" 
    border.color: "#645fa9"
    border.width: 2
    
    MouseArea {
           
       anchors.fill: parent
       onPressed: parent.color = "#645fa9"
       onReleased: parent.color = button.startColor
       onClicked: {
           context.onClicked(button.callId)
        }
    }
   
   
    
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

