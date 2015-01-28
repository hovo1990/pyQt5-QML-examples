import QtQuick 2.2
import shapes 1.0
//import QtQuick.Window 2.1

Rectangle {
    visible: true
    width: 360
    height: 360

    Ellipse {
        height:100
        width: 100
        anchors.fill: parent
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            Qt.quit();
        }
    }

    Text {
        text: qsTr("Hello World")
        font.pixelSize: 20
        anchors.centerIn: parent
    }
}
