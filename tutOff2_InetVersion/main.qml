import QtQuick 2.0
import mymodule 1.0

Rectangle {
    color: "black"
    width: 500
    height: 500

    PaintedItem {
        x: 100
        y: 100
        //anchors.centerIn: parent
        width: 100
        height: 100

        MouseArea {
            anchors.fill: parent
            onClicked: {
                Qt.quit();
            }
        }
    }

    PaintedItem {
        x: 300
        y: 300
//        anchors.centerIn: parent
        width: 100
        height: 100
    }
}
