import QtQuick 2.2
import mymodule 1.0

Rectangle {
//    color: "black"
    width: 500
    height: 500

    Column
    {

        PaintedItem {
            id: myPaintedItem
            //property string myColor: "green"
            x: 100
            y: 100
            //anchors.centerIn: parent
            width: 100
            height: 100
            color: "green"

            onReadySignal: {
                color = "blue"
            }

            onReadyChanged: {
                readyStatus.text = value;
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
    //                Qt.quit();
                    parent.color = 'red';
                }
            }
        }

        Text {
            id: readyStatus
            text: "Hello world"
            font.pixelSize: 32
        }
    }
}
