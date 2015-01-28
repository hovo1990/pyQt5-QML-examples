import QtQuick 2.2
import mymodule 1.0

Rectangle {
    color: "black"
    width: 500
    height: 500


    PaintedItem {
        //property string myColor: "green"
        x: 100
        y: 100
        //anchors.centerIn: parent
        width: 100
        height: 100
        color: "blue"

        MouseArea {
            anchors.fill: parent
            onClicked: {
//                Qt.quit();
                parent.color = 'red';
            }
        }
    }

}
