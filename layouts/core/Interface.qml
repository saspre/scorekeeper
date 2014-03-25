

import QtQuick 1.0

Rectangle {
    

    id: root
    width: 480
    height: 272
    color: "#111111"

    function getCenterX(item) {
        return (root.width / 2) - item.width / 2
    }

    function getCenterY(item) {
        return (root.height / 2) - item.height / 2
    }

    property int margin: 10

}