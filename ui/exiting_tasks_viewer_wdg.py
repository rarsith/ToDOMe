import sys
from PySide2 import QtWidgets, QtCore

class ExitingTasksViewerWDG(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerWDG, self).__init__(parent)

        self.widget_width = 690
        self.widget_columns_names = ["Priority", "Task", "User", "Status"]
        self.widget_build()

    def widget_build(self):
        self.setDisabled(False)
        self.setMinimumWidth(self.widget_width)
        self.setColumnCount(len(self.widget_columns_names))
        self.setHorizontalHeaderLabels(self.widget_columns_names)
        self.setShowGrid(False)
        self.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.setAlternatingRowColors(True)
        header = self.verticalHeader()
        header.hide()
        self.setColumnWidth(0, round(self.widget_width*0.10))
        self.setColumnWidth(1, round(self.widget_width*0.70))
        self.setColumnWidth(2, round(self.widget_width*0.10))
        self.setColumnWidth(3, round(self.widget_width*0.09))

        self.resizeRowsToContents()


class InputTaskWDG(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super(InputTaskWDG, self).__init__(parent)

        self.widget_width = 690
        self.widget_height = 345
        self.widget_build()

    def widget_build(self):
        self.setMinimumWidth(self.widget_width)
        self.setMinimumHeight(self.widget_height)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = InputTaskWDG()
    test_dialog.show()
    sys.exit(app.exec_())