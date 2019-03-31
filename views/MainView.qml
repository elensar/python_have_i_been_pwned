import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    title: qsTr('Have I Been Pwned - password check')
    width: 640
    height: 480
    visible: true

    GridLayout {
        id: grid
        width: 480
        columns: 1
        rows: 6
        anchors.margins: 5

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1

            Label {
                text: qsTr('Password:')
            }
            TextField{
                text: appVM.password
                onTextChanged: appVM.password = text
            }
        }

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1

            Label {
                text: qsTr('Password Hash:')
            }
            Label {
                text: appVM.password_hash
            }
        }

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1

            Label {
                text: qsTr('Show all results:')
            }
            CheckBox{
                text: appVM.show_results
                checked: appVM.show_results
            }
        }

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1

            Label {
                text: qsTr('Result:')
            }
            Label{
                text: appVM.result
            }
        }

        ColumnLayout {
            spacing: 2
            Layout.columnSpan: 1

            Button {
                text: qsTr('&Apply')
                onClicked: appVM.apply('test')
            }
        }
    }
}
