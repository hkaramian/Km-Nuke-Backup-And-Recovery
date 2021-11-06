


#
#
# Km Backup And Recovery Toolkit v1.0
#
# Developed By Hossein Karamian
# 
# www.kmworks.ir
#
# 10/6/2020
#    _  __  __  __ 
#   | |/ / |  \/  |
#   | ' /  | \  / |
#   |  <   | |\/| |
#   |_|\_\ |_|  |_|
#

"""
Change Log :
v1.0 | first version | October 6 , 2020 
"""

# Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer

try:
    import nuke
    import nukescripts
    if int(nuke.env ["NukeVersionMajor"]) < 11:
        from PySide.QtCore import *
        from PySide.QtGui import *
        print "Km Backup And Recovery ToolKit : www.kmworks.ir"
    else:
        from PySide2.QtCore import *
        from PySide2.QtGui import *
        from PySide2.QtWidgets import *
        print "Km Backup And Recovery ToolKit : www.kmworks.ir"
except ImportError:
    print "not in nuke" # pycharm
    try:
        from PySide.QtCore import *
        from PySide.QtGui import *
        print "using pyside"
    except ImportError:
        from PyQt4.QtCore import *
        from PyQt4.QtGui import *
        Signal = pyqtSignal
        print "using pyqt4"
    pass





class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(808, 755)
        icon = QIcon()
        icon.addPixmap(QPixmap(os.path.dirname(__file__)+"/icons/backup_on.png"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_status = QGroupBox(Form)
        self.groupBox_status.setObjectName("groupBox_status")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_status)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_backup_service_status = QLabel(self.groupBox_status)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_backup_service_status.setFont(font)
        self.label_backup_service_status.setObjectName("label_backup_service_status")
        self.horizontalLayout_7.addWidget(self.label_backup_service_status)
        self.comboBox_backup_service_status = QComboBox(self.groupBox_status)
        self.comboBox_backup_service_status.setObjectName("comboBox_backup_service_status")
        self.comboBox_backup_service_status.addItem("")
        self.comboBox_backup_service_status.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_backup_service_status)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_icon = QLabel(self.groupBox_status)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/backup_on.png"))
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_8.addWidget(self.label_icon)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.line_4 = QFrame(self.groupBox_status)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_8.addWidget(self.line_4)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_static_panel = QLabel(self.groupBox_status)
        self.label_static_panel.setObjectName("label_static_panel")
        self.horizontalLayout_6.addWidget(self.label_static_panel)
        self.pushButton_add_to_pane = QPushButton(self.groupBox_status)
        self.pushButton_add_to_pane.setObjectName("pushButton_add_to_pane")
        self.horizontalLayout_6.addWidget(self.pushButton_add_to_pane)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_help = QLabel(self.groupBox_status)
        self.label_help.setObjectName("label_help")
        self.horizontalLayout_11.addWidget(self.label_help)
        self.pushButton_documentation = QPushButton(self.groupBox_status)
        self.pushButton_documentation.setObjectName("pushButton_documentation")
        self.horizontalLayout_11.addWidget(self.pushButton_documentation)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_8.setStretch(0, 8)
        self.horizontalLayout_8.setStretch(1, 10)
        self.horizontalLayout_8.setStretch(2, 3)
        self.horizontalLayout_8.setStretch(3, 11)
        self.horizontalLayout_8.setStretch(4, 2)
        self.horizontalLayout_8.setStretch(5, 12)
        self.horizontalLayout_8.setStretch(6, 10)
        self.horizontalLayout_8.setStretch(7, 10)
        self.horizontalLayout_8.setStretch(8, 10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout_7.addWidget(self.groupBox_status)
        self.groupBox_settings4 = QGroupBox(Form)
        self.groupBox_settings4.setObjectName("groupBox_settings4")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_settings4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QLabel(self.groupBox_settings4)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QLabel(self.groupBox_settings4)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line = QFrame(self.groupBox_settings4)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.checkBox_in_script_folder_service = QCheckBox(self.groupBox_settings4)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_in_script_folder_service.setFont(font)
        self.checkBox_in_script_folder_service.setChecked(True)
        self.checkBox_in_script_folder_service.setObjectName("checkBox_in_script_folder_service")
        self.verticalLayout_3.addWidget(self.checkBox_in_script_folder_service)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_local_backup_scheduling = QLabel(self.groupBox_settings4)
        self.label_local_backup_scheduling.setObjectName("label_local_backup_scheduling")
        self.horizontalLayout_3.addWidget(self.label_local_backup_scheduling)
        self.comboBox_local_backup_scheduling = QComboBox(self.groupBox_settings4)
        self.comboBox_local_backup_scheduling.setObjectName("comboBox_local_backup_scheduling")
        self.comboBox_local_backup_scheduling.addItem("")
        self.comboBox_local_backup_scheduling.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_local_backup_scheduling)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.checkBox_local_big_file_option = QCheckBox(self.groupBox_settings4)
        self.checkBox_local_big_file_option.setObjectName("checkBox_local_big_file_option")
        self.verticalLayout_3.addWidget(self.checkBox_local_big_file_option)
        self.label_empty_space = QLabel(self.groupBox_settings4)
        self.label_empty_space.setText("")
        self.label_empty_space.setObjectName("label_empty_space")
        self.verticalLayout_3.addWidget(self.label_empty_space)
        self.pushButton_2 = QPushButton(self.groupBox_settings4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.line_2 = QFrame(self.groupBox_settings4)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_9.addWidget(self.line_2)
        spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QLabel(self.groupBox_settings4)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_5 = QLabel(self.groupBox_settings4)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.line_3 = QFrame(self.groupBox_settings4)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.checkBox_secondary_backup_service = QCheckBox(self.groupBox_settings4)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_secondary_backup_service.setFont(font)
        self.checkBox_secondary_backup_service.setChecked(False)
        self.checkBox_secondary_backup_service.setObjectName("checkBox_secondary_backup_service")
        self.verticalLayout_4.addWidget(self.checkBox_secondary_backup_service)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_local_backup_scheduling_2 = QLabel(self.groupBox_settings4)
        self.label_local_backup_scheduling_2.setEnabled(False)
        self.label_local_backup_scheduling_2.setObjectName("label_local_backup_scheduling_2")
        self.horizontalLayout_5.addWidget(self.label_local_backup_scheduling_2)
        self.comboBox_secondary_backup_scheduling = QComboBox(self.groupBox_settings4)
        self.comboBox_secondary_backup_scheduling.setEnabled(False)
        self.comboBox_secondary_backup_scheduling.setObjectName("comboBox_secondary_backup_scheduling")
        self.comboBox_secondary_backup_scheduling.addItem("")
        self.comboBox_secondary_backup_scheduling.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_secondary_backup_scheduling)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.checkBox_secondary_big_file_option = QCheckBox(self.groupBox_settings4)
        self.checkBox_secondary_big_file_option.setEnabled(False)
        self.checkBox_secondary_big_file_option.setObjectName("checkBox_secondary_big_file_option")
        self.verticalLayout_4.addWidget(self.checkBox_secondary_big_file_option)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_path = QLabel(self.groupBox_settings4)
        self.label_path.setEnabled(False)
        self.label_path.setObjectName("label_path")
        self.horizontalLayout_4.addWidget(self.label_path)
        self.lineEdit_secondary_backup_path = QLineEdit(self.groupBox_settings4)
        self.lineEdit_secondary_backup_path.setEnabled(False)
        self.lineEdit_secondary_backup_path.setObjectName("lineEdit_secondary_backup_path")
        self.horizontalLayout_4.addWidget(self.lineEdit_secondary_backup_path)
        self.pushButton_select_secondary_backup_directory = QPushButton(self.groupBox_settings4)
        self.pushButton_select_secondary_backup_directory.setEnabled(False)
        self.pushButton_select_secondary_backup_directory.setMaximumSize(QSize(40, 16777215))
        self.pushButton_select_secondary_backup_directory.setObjectName("pushButton_select_secondary_backup_directory")
        self.horizontalLayout_4.addWidget(self.pushButton_select_secondary_backup_directory)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.pushButton_open_secondary_backup_directory = QPushButton(self.groupBox_settings4)
        self.pushButton_open_secondary_backup_directory.setEnabled(False)
        self.pushButton_open_secondary_backup_directory.setObjectName("pushButton_open_secondary_backup_directory")
        self.verticalLayout_4.addWidget(self.pushButton_open_secondary_backup_directory)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 4)
        self.horizontalLayout_9.setStretch(2, 4)
        self.horizontalLayout_9.setStretch(3, 4)
        self.horizontalLayout_9.setStretch(4, 4)
        self.horizontalLayout_9.setStretch(5, 4)
        self.horizontalLayout_9.setStretch(6, 4)
        self.verticalLayout_7.addWidget(self.groupBox_settings4)
        self.groupBox_backups_list = QGroupBox(Form)
        self.groupBox_backups_list.setObjectName("groupBox_backups_list")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_backups_list)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.label = QLabel(self.groupBox_backups_list)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_backups_list_filter_type = QComboBox(self.groupBox_backups_list)
        self.comboBox_backups_list_filter_type.setMaximumSize(QSize(160, 16777215))
        self.comboBox_backups_list_filter_type.setObjectName("comboBox_backups_list_filter_type")
        self.comboBox_backups_list_filter_type.addItem("")
        self.comboBox_backups_list_filter_type.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_backups_list_filter_type)
        spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.pushButton_refresh = QPushButton(self.groupBox_backups_list)
        self.pushButton_refresh.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(os.path.dirname(__file__)+"/icons/refresh.png"), QIcon.Normal, QIcon.Off)
        self.pushButton_refresh.setIcon(icon1)
        self.pushButton_refresh.setIconSize(QSize(30, 30))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        spacerItem11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 11)
        self.horizontalLayout.setStretch(3, 4)
        self.horizontalLayout.setStretch(5, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget_backups_list = QTableWidget(self.groupBox_backups_list)
        self.tableWidget_backups_list.setShowGrid(True)
        self.tableWidget_backups_list.setGridStyle(Qt.DashLine)
        self.tableWidget_backups_list.setWordWrap(True)
        self.tableWidget_backups_list.setObjectName("tableWidget_backups_list")
        self.tableWidget_backups_list.setColumnCount(6)
        self.tableWidget_backups_list.setRowCount(2)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(0, 1, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(0, 2, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(0, 4, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(0, 5, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(1, 1, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(1, 2, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(1, 4, item)
        item = QTableWidgetItem()
        self.tableWidget_backups_list.setItem(1, 5, item)
        self.tableWidget_backups_list.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_backups_list.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_backups_list.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_backups_list.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout_2.addWidget(self.tableWidget_backups_list)
        self.verticalLayout_7.addWidget(self.groupBox_backups_list)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_plugins_version = QLabel(Form)
        self.label_plugins_version.setObjectName("label_plugins_version")
        self.horizontalLayout_2.addWidget(self.label_plugins_version)
        spacerItem12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QLabel(Form)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Km Backup And Recovery"))
        self.groupBox_status.setTitle(_translate("Form", "Status"))
        self.label_backup_service_status.setText(_translate("Form", "Backup Service :"))
        self.comboBox_backup_service_status.setItemText(0, _translate("Form", "Enable"))
        self.comboBox_backup_service_status.setItemText(1, _translate("Form", "Disable"))
        self.label_static_panel.setText(_translate("Form", "Use As Static Panel :"))
        self.pushButton_add_to_pane.setToolTip(_translate("Form", "Add this panel to nuke static panels "))
        self.pushButton_add_to_pane.setText(_translate("Form", "Add Panel To Pane"))
        self.label_help.setText(_translate("Form", "Help :"))
        self.pushButton_documentation.setText(_translate("Form", "Documentation"))
        self.groupBox_settings4.setTitle(_translate("Form", "Settings"))
        self.label_2.setText(_translate("Form", "Local  Backup"))
        self.label_4.setText(_translate("Form", "(Create Backup Folder Beside Project File)"))
        self.checkBox_in_script_folder_service.setText(_translate("Form", "Active"))
        self.label_local_backup_scheduling.setText(_translate("Form", "Scheduling :"))
        self.comboBox_local_backup_scheduling.setItemText(0, _translate("Form", "Keep one version per hour"))
        self.comboBox_local_backup_scheduling.setItemText(1, _translate("Form", "Keep one version per day"))
        self.checkBox_local_big_file_option.setText(_translate("Form", "Big Script File Option (disable save trigger)"))
        self.pushButton_2.setText(_translate("Form", "Open Local Backup Folder"))
        self.label_3.setText(_translate("Form", "Secondary Backup"))
        self.label_5.setText(_translate("Form", "(Same Location For All Projects)"))
        self.checkBox_secondary_backup_service.setText(_translate("Form", "Active"))
        self.label_local_backup_scheduling_2.setText(_translate("Form", "Scheduling :"))
        self.comboBox_secondary_backup_scheduling.setItemText(0, _translate("Form", "Keep one version per hour"))
        self.comboBox_secondary_backup_scheduling.setItemText(1, _translate("Form", "Keep one version per day"))
        self.checkBox_secondary_big_file_option.setText(_translate("Form", "Big Script File Option (disable save trigger)"))
        self.label_path.setText(_translate("Form", "Path :"))
        self.lineEdit_secondary_backup_path.setText(_translate("Form", "C:\\Nuke_Backups\\"))
        self.pushButton_select_secondary_backup_directory.setText(_translate("Form", "..."))
        self.pushButton_open_secondary_backup_directory.setText(_translate("Form", "Open Secondary Backup Folder"))
        self.groupBox_backups_list.setTitle(_translate("Form", "Backups"))
        self.label.setText(_translate("Form", "Source :"))
        self.comboBox_backups_list_filter_type.setItemText(0, _translate("Form", "Local Backups"))
        self.comboBox_backups_list_filter_type.setItemText(1, _translate("Form", "Secondary Backups"))
        self.pushButton_refresh.setToolTip(_translate("Form", "Refresh List"))
        self.tableWidget_backups_list.setSortingEnabled(True)
        item = self.tableWidget_backups_list.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_backups_list.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget_backups_list.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Backup Time"))
        item = self.tableWidget_backups_list.horizontalHeaderItem(1)
        item.setText(_translate("Form", "File url"))
        item.setToolTip(_translate("Form", "Copy url to clipboard"))
        item = self.tableWidget_backups_list.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Replace"))
        item = self.tableWidget_backups_list.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Open"))
        item = self.tableWidget_backups_list.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Delete"))
        item = self.tableWidget_backups_list.horizontalHeaderItem(5)
        item.setText(_translate("Form", "FileName"))
        __sortingEnabled = self.tableWidget_backups_list.isSortingEnabled()
        self.tableWidget_backups_list.setSortingEnabled(False)
        item = self.tableWidget_backups_list.item(0, 1)
        item.setText(_translate("Form", "Do It"))
        item = self.tableWidget_backups_list.item(0, 2)
        item.setText(_translate("Form", "Do It"))
        item = self.tableWidget_backups_list.item(0, 4)
        item.setText(_translate("Form", "Do It"))
        item = self.tableWidget_backups_list.item(0, 5)
        item.setText(_translate("Form", "Dessert_shot_001_7-27-2020_11AM"))
        item = self.tableWidget_backups_list.item(1, 1)
        item.setText(_translate("Form", "Do It"))
        item = self.tableWidget_backups_list.item(1, 2)
        item.setText(_translate("Form", "Do It"))
        item = self.tableWidget_backups_list.item(1, 4)
        item.setText(_translate("Form", "Do It"))
        item = self.tableWidget_backups_list.item(1, 5)
        item.setText(_translate("Form", "Dessert_shot_001_7-27-2020_12PM"))
        self.tableWidget_backups_list.setSortingEnabled(__sortingEnabled)
        self.label_plugins_version.setText(_translate("Form", "Km Backup & Recovery v1.0"))
        self.label_8.setText(_translate("Form", "By Hossein Karamian"))
        self.label_9.setText(_translate("Form", "www.kmworks.ir"))







import os
import platform
import subprocess
import datetime

operatingSystem = platform.system()


import json
import time

from nukescripts import panels


from functools import partial
'''
kmb_settings = {
  "service_status": "Enable",
  "Scheduling": "daily", # daily or hourly
  "in-script-backup" : "Enable",
  "secondary-backup" : "Enable",
  "sub-folder": "Enable",
  "secondary-backup-path" : "C:/Nuke_Backups/"
}
'''






class Km_Backup_Panel(QWidget,Ui_Form):
    """docstring for Km_Backup_Panel"""

    settings = {
      "service_status": "Enable",
      "local_backup_Scheduling": "daily", # daily or hourly
      "secondary_backup_Scheduling": "daily", # daily or hourly
      "in-script-backup" : "Enable",
      "secondary-backup" : "Enable",
      "sub-folder": "Enable",
      "local_backup_big_script_file_option": "Enable",
      "secondary_backup_big_script_file_option": "Enable",
      "secondary-backup-path" : "C:/Nuke_Backups/"
    }

    def __init__(self):
        super(Km_Backup_Panel, self).__init__()
        self.setupUi(self)

        
        self.update_UI()

        if self.settings["service_status"] == "Enable":
            nuke.addOnScriptSave(self.make_backup)
        
        self.tableWidget_backups_list.setRowCount(0)
        #Signals :
        self.comboBox_backup_service_status.currentIndexChanged.connect(self.backup_service_status_change)
        self.comboBox_local_backup_scheduling.currentIndexChanged.connect(self.local_backup_scheduling_change)
        self.comboBox_secondary_backup_scheduling.currentIndexChanged.connect(self.secondary_backup_scheduling_change)
        self.checkBox_in_script_folder_service.stateChanged['int'].connect(self.in_script_folder_backup_change)
        self.pushButton_2.clicked.connect(self.open_in_script_backup_folder)
        self.checkBox_secondary_backup_service.stateChanged['int'].connect(self.secondary_backup_service_change)
        self.checkBox_local_big_file_option.stateChanged['int'].connect(self.local_big_file_option_change)
        self.checkBox_secondary_big_file_option.stateChanged['int'].connect(self.secondary_big_file_option_change)
        self.pushButton_select_secondary_backup_directory.clicked.connect(self.set_seocondary_backup_directory)
        self.pushButton_open_secondary_backup_directory.clicked.connect(self.open_secondary_backup_folder)
        self.pushButton_add_to_pane.clicked.connect(self.add_to_pane)
        self.pushButton_refresh.clicked.connect(self.update_list)
        self.pushButton_documentation.clicked.connect(self.open_documentation)
        self.comboBox_backups_list_filter_type.currentIndexChanged.connect(self.backups_list_filter_type_change)
        self.label_9.setText('''<a href='http://www.kmworks.ir' style='color:#555273;text-decoration: none;'>www.kmworks.ir</a>''')
        self.label_9.setOpenExternalLinks(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


        #self.label_3.setText("salam")

        #self.set_last_backup_time()


    #Define Singnal functions    


    def load_settings(self):
        plugin_path = os.path.dirname(__file__)
        with open(plugin_path+'/settings.json') as json_file:
            self.settings = json.load(json_file)

    def save_settings(self):
        plugin_path = os.path.dirname(__file__)
        with open(plugin_path+'/settings.json', 'w') as outfile:
            json.dump(self.settings, outfile)

    def update_UI(self):

        self.load_settings()

        if self.settings["service_status"] == "Enable" :
            self.label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/backup_on.png"))
            self.comboBox_backup_service_status.setCurrentIndex(0)
        else :
            self.label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/backup_off.png")) 
            self.comboBox_backup_service_status.setCurrentIndex(1)

        if self.settings["local_backup_Scheduling"] == "hourly" :
            self.comboBox_local_backup_scheduling.setCurrentIndex(0)
        else :
            self.comboBox_local_backup_scheduling.setCurrentIndex(1)

        if self.settings["secondary_backup_Scheduling"] == "hourly" :
            self.comboBox_secondary_backup_scheduling.setCurrentIndex(0)
        else :
            self.comboBox_secondary_backup_scheduling.setCurrentIndex(1)

        if self.settings["local_backup_big_script_file_option"] == "Enable" :
            self.checkBox_local_big_file_option.setChecked(True)
        if self.settings["secondary_backup_big_script_file_option"] == "Enable" :
            self.checkBox_secondary_big_file_option.setChecked(True)

        if self.settings["in-script-backup"] == "Enable" :
            self.checkBox_in_script_folder_service.setChecked(True)
            self.pushButton_2.setEnabled(True)
            self.label_local_backup_scheduling.setEnabled(True)
            self.comboBox_local_backup_scheduling.setEnabled(True)
            self.checkBox_local_big_file_option.setEnabled(True)
        else :
            self.checkBox_in_script_folder_service.setChecked(False)
            self.pushButton_2.setEnabled(False)
            self.label_local_backup_scheduling.setEnabled(False)
            self.comboBox_local_backup_scheduling.setEnabled(False)
            self.checkBox_local_big_file_option.setEnabled(False)

        if self.settings["secondary-backup"] == "Enable" :
            self.checkBox_secondary_backup_service.setChecked(True)
            self.lineEdit_secondary_backup_path.setEnabled(True)
            self.label_local_backup_scheduling_2.setEnabled(True)
            self.comboBox_secondary_backup_scheduling.setEnabled(True)
            self.checkBox_secondary_big_file_option.setEnabled(True)
            self.label_path.setEnabled(True)
            self.pushButton_select_secondary_backup_directory.setEnabled(True)
            self.pushButton_open_secondary_backup_directory.setEnabled(True)
        else :
            self.checkBox_secondary_backup_service.setChecked(False)
            self.lineEdit_secondary_backup_path.setEnabled(False)
            self.label_local_backup_scheduling_2.setEnabled(False)
            self.comboBox_secondary_backup_scheduling.setEnabled(False)
            self.checkBox_secondary_big_file_option.setEnabled(False)
            self.label_path.setEnabled(False)
            self.pushButton_select_secondary_backup_directory.setEnabled(False)
            self.pushButton_open_secondary_backup_directory.setEnabled(False)

        self.lineEdit_secondary_backup_path.setText(self.settings["secondary-backup-path"])


        self.update_list()


    def update_list(self) :

        if nuke.Root().name() == 'Root': #check project saved yet or not
            #nuke.message("Km_backup : First save the Project")
            pass
        else :
            local_backup_path = nuke.script_directory()
            secondary_backup_path = self.settings["secondary-backup-path"]
            script_name = self.get_script_name_without_version()
            if self.comboBox_backups_list_filter_type.currentIndex() == 0 :
                backup_folder = local_backup_path
            else :
                backup_folder = secondary_backup_path
            for shot_folder in nuke.getFileNameList(backup_folder):
                #print shot_folder
                if (shot_folder == "backups-"+script_name) :
                    #print "if kok"
                    backup_filesss= nuke.getFileNameList(backup_folder+"/backups-"+script_name)
                    row_number = 0
                    #self.tableWidget_backups_list.setRowCount(len(backup_filesss))
                    #for i in reversed(range(0, self.tableWidget_backups_list.rowCount())) : 
                    #    self.tableWidget_backups_list.removeRow(i)


                    self.tableWidget_backups_list.setParent(None) #destroy older table
                    #create new table (becouse of bugs and problems)
                    self.tableWidget_backups_list = QTableWidget(self.groupBox_backups_list)
                    self.tableWidget_backups_list.setShowGrid(True)
                    self.tableWidget_backups_list.setGridStyle(Qt.DashLine)
                    self.tableWidget_backups_list.setWordWrap(True)
                    self.tableWidget_backups_list.setObjectName("tableWidget_backups_list")
                    self.tableWidget_backups_list.setColumnCount(6)
                    self.tableWidget_backups_list.setRowCount(len(backup_filesss))
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setVerticalHeaderItem(0, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setVerticalHeaderItem(1, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setVerticalHeaderItem(2, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setHorizontalHeaderItem(0, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setHorizontalHeaderItem(1, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setHorizontalHeaderItem(2, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setHorizontalHeaderItem(3, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setHorizontalHeaderItem(4, item)
                    item = QTableWidgetItem()
                    self.tableWidget_backups_list.setHorizontalHeaderItem(5, item)
                    item = self.tableWidget_backups_list.horizontalHeaderItem(0)
                    item.setText("Backup Time")
                    item = self.tableWidget_backups_list.horizontalHeaderItem(1)
                    item.setText("File url")
                    item = self.tableWidget_backups_list.horizontalHeaderItem(2)
                    item.setText("Replace")
                    item.setToolTip("Copy url to clipboard")
                    item = self.tableWidget_backups_list.horizontalHeaderItem(3)
                    item.setText("Open")
                    item = self.tableWidget_backups_list.horizontalHeaderItem(4)
                    item.setText("Delete")
                    item = self.tableWidget_backups_list.horizontalHeaderItem(5)
                    item.setText("FileName")

                    for backup_file in backup_filesss  :
                        #print backup_file
                        file_full_path = backup_folder+"/backups-"+script_name+"/"+backup_file
                        backup_time = os.stat(file_full_path)
                        backup_time = datetime.datetime.fromtimestamp(backup_time.st_mtime).strftime('%Y-%m-%d %H:%M:%S') #convert to standard time
                        #print file_full_path
                        #print file_full_path + " --- > " + backup_time

                        item = QTableWidgetItem()
                        self.tableWidget_backups_list.setVerticalHeaderItem(row_number, item)
                        item = self.tableWidget_backups_list.verticalHeaderItem(row_number)
                        item.setText((str)(row_number+1))

                        item = QTableWidgetItem()
                        item.setText(backup_time)
                        self.tableWidget_backups_list.setItem(row_number, 0, item)

                        item = QTableWidgetItem()
                        item.setText(file_full_path)
                        self.tableWidget_backups_list.setItem(row_number, 1, item)

                        temp_button = QPushButton(self.tableWidget_backups_list)
                        temp_button.setText("")
                        temp_button.setObjectName("temp_button123")
                        temp_button.setIconSize((QSize(20,20)))
                        temp_button.setIcon(QIcon(QPixmap(os.path.dirname(__file__)+"/icons/icon_recover.png")))
                        temp_button.clicked.connect(partial(self.recover_backup_file,file_full_path))
                        self.tableWidget_backups_list.setCellWidget(row_number, 2,temp_button)

                        temp_button = QPushButton(self.tableWidget_backups_list)
                        temp_button.setText("")
                        temp_button.setObjectName("temp_button123")
                        temp_button.setIconSize((QSize(20,20)))
                        temp_button.setIcon(QIcon(QPixmap(os.path.dirname(__file__)+"/icons/nukex.png")))
                        temp_button.clicked.connect(partial(self.open_script_file,file_full_path))
                        self.tableWidget_backups_list.setCellWidget(row_number, 3,temp_button)

                        temp_button = QPushButton(self.tableWidget_backups_list)
                        temp_button.setText("")
                        temp_button.setObjectName("temp_button123")
                        temp_button.setIconSize((QSize(20,20)))
                        temp_button.setIcon(QIcon(QPixmap(os.path.dirname(__file__)+"/icons/icon_delete.png")))
                        temp_button.clicked.connect(partial(self.delete_backup_file,file_full_path))
                        self.tableWidget_backups_list.setCellWidget(row_number, 4,temp_button)

                        item = QTableWidgetItem()
                        item.setText(backup_file)
                        self.tableWidget_backups_list.setItem(row_number, 5, item)

                        row_number = row_number + 1 
                    
                    #self.verticalLayout_2.addWidget(self.tableWidget_backups_list)
                    self.tableWidget_backups_list.horizontalHeader().setDefaultSectionSize(88)
                    self.tableWidget_backups_list.horizontalHeader().setMinimumSectionSize(20)
                    self.tableWidget_backups_list.horizontalHeader().setStretchLastSection(True)
                    self.tableWidget_backups_list.verticalHeader().setDefaultSectionSize(30)
                    self.verticalLayout_2.addWidget(self.tableWidget_backups_list)
                    self.tableWidget_backups_list.setSortingEnabled(False)

                    self.tableWidget_backups_list.sortItems(0, Qt.DescendingOrder)

        
    def sort_backup_table(self):
        self.tableWidget_backups_list.sortItems(0, Qt.DescendingOrder)

    def showSampleMesseage(self,paramteeeeer):
        nuke.message("test")


    def delete_backup_file(self,file_to_delete):
        try:
            print "file to delete : "+file_to_delete
            os.remove(file_to_delete)
            print "file deleted"
            self.update_list()
        except Exception as e:
            print "eror"
        else:
            pass
        #finally:
        #   pass

    def recover_backup_file(self,file_to_recover):
        if nuke.ask("It will delete current nodegraph and replace it with the backup file ,Do you want to continue?"):
            # delete current node graph
            for item in nuke.allNodes():
                nuke.delete(item)

            #insert backup file node graph
            nuke.loadToolset(file_to_recover)



    def open_script_file(self,file_to_open) :
        nuke.scriptOpen(file_to_open)

    def open_documentation(self):
        subprocess.Popen(os.path.dirname(__file__)+"/UserGuide.pdf",shell=True)

    def backup_service_status_change(self):
        if self.comboBox_backup_service_status.currentIndex() == 0 :
            nuke.addOnScriptSave(self.make_backup)
            self.settings["service_status"] = "Enable"
            self.save_settings()
            self.label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/backup_on.png"))
        else :
            nuke.removeOnScriptSave(self.make_backup)
            self.settings["service_status"] = "Disable"
            self.save_settings()
            self.label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/backup_off.png")) 

    def make_backup(self):

        if self.settings["service_status"] != "Enable":
            return

        if nuke.Root().name() == 'Root': #check project saved yet or not
            nuke.message("Km_backup : First save the Project")
            #pass
        else :
            nuke.removeOnScriptSave(self.make_backup)
            script = nuke.root().name()
            script_name = os.path.basename(script)
            script_name = os.path.splitext(script_name)[0]
            local_backup_folder_path = self.get_local_backup_folder_path()
            secondary_backup_folder_path = self.settings["secondary-backup-path"]+"/backups-"+self.get_script_name_without_version()
            current_time = time.strftime("Date_20%y_%m_%d-Hour_%H")

            if self.settings["in-script-backup"] == "Enable" :   
                if self.settings["local_backup_Scheduling"] == "daily" :
                    current_time = time.strftime("Date_20%y_%m_%d")
                in_folder_backup_file_full_path = "{}/bckp_{}_{}.nk".format(local_backup_folder_path, script_name, current_time)  # backup file path with project file name
                if not os.path.exists(local_backup_folder_path):
                    os.makedirs(local_backup_folder_path)

                if os.path.exists(local_backup_folder_path):
                    backup_condition = True
                    if self.settings["local_backup_big_script_file_option"] == "Enable" :
                        backup_condition = self.big_file_option_check(in_folder_backup_file_full_path,self.settings["local_backup_Scheduling"])

                    if backup_condition :
                        if operatingSystem == "Windows":
                            ##nuke.removeOnScriptSave(make_backup)
                            nuke.scriptSave(in_folder_backup_file_full_path)
                            print "local backup successfull"
                            ##nuke.addOnScriptSave(make_backup)
                        else :
                            nuke.message("Km_backup : operatingSystem not supported")
                else:
                    nuke.message("Km_backup : local backup folder does not exists")

            current_time = time.strftime("Date_20%y_%m_%d-Hour_%H")
            if self.settings["secondary-backup"] == "Enable" :   
                if self.settings["secondary_backup_Scheduling"] == "daily" :
                    current_time = time.strftime("Date_20%y_%m_%d")
                secondary_backup_file_full_path = "{}/bckp_{}_{}.nk".format(secondary_backup_folder_path, script_name, current_time)  # backup file path with project file name
                if not os.path.exists(secondary_backup_folder_path):
                    os.makedirs(secondary_backup_folder_path)

                if os.path.exists(secondary_backup_folder_path):
                    backup_condition = True
                    if self.settings["secondary_backup_big_script_file_option"] == "Enable" :
                        backup_condition = self.big_file_option_check(secondary_backup_file_full_path,self.settings["secondary_backup_Scheduling"])
                    if backup_condition :
                        if operatingSystem == "Windows":
                            ##nuke.removeOnScriptSave(make_backup)
                            nuke.scriptSave(secondary_backup_file_full_path)
                            print "secondary backup successfull"
                            ##nuke.addOnScriptSave(make_backup)
                        else :
                            nuke.message("Km_backup : operatingSystem not supported")
                else:
                    nuke.message("Km_backup : local backup folder does not exists")
            #time.sleep(0.5)
            nuke.addOnScriptSave(self.make_backup)
            self.update_list()


    def big_file_option_check(self,file_full_path, backup_type) :

        if not os.path.exists(file_full_path) :
            return True

        t1 = datetime.datetime.fromtimestamp(os.stat(file_full_path).st_mtime)
        t2 = datetime.datetime.now()
        t_dif = t2 - t1
        if backup_type == "hourly":
            if os.path.exists(file_full_path) :
                return False
            else :
                return True
        else: #for daily
            if t_dif.seconds < 10800 : # 10800 seconds = 3 hours
                return False
            else :
                return True




    def local_backup_scheduling_change(self):
        if self.comboBox_local_backup_scheduling.currentIndex() == 0 :
            self.settings["local_backup_Scheduling"] = "hourly"
            self.save_settings()
        else :
            self.settings["local_backup_Scheduling"] = "daily"
            self.save_settings()

    def secondary_backup_scheduling_change(self):
        if self.comboBox_secondary_backup_scheduling.currentIndex() == 0 :
            self.settings["secondary_backup_Scheduling"] = "hourly"
            self.save_settings()
        else :
            self.settings["secondary_backup_Scheduling"] = "daily"
            self.save_settings()

    def backups_list_filter_type_change(self):
        self.update_list()

    def in_script_folder_backup_change(self):
        if self.checkBox_in_script_folder_service.isChecked():
            self.settings["in-script-backup"] = "Enable"
            self.save_settings()
            self.pushButton_2.setEnabled(True)
            self.label_local_backup_scheduling.setEnabled(True)
            self.comboBox_local_backup_scheduling.setEnabled(True)
            self.checkBox_local_big_file_option.setEnabled(True)
        else:
            self.settings["in-script-backup"] = "Disable"
            self.save_settings()
            self.pushButton_2.setEnabled(False)
            self.label_local_backup_scheduling.setEnabled(False)
            self.comboBox_local_backup_scheduling.setEnabled(False)
            self.checkBox_local_big_file_option.setEnabled(False)

    def secondary_backup_service_change(self):
        if self.checkBox_secondary_backup_service.isChecked():
            self.settings["secondary-backup"] = "Enable"
            self.save_settings()
            self.lineEdit_secondary_backup_path.setEnabled(True)
            self.pushButton_select_secondary_backup_directory.setEnabled(True)
            self.pushButton_open_secondary_backup_directory.setEnabled(True)
            self.label_local_backup_scheduling_2.setEnabled(True)
            self.comboBox_secondary_backup_scheduling.setEnabled(True)
            self.checkBox_secondary_big_file_option.setEnabled(True)
            self.label_path.setEnabled(True)
        else:
            self.settings["secondary-backup"] = "Disable"
            self.save_settings()
            self.lineEdit_secondary_backup_path.setEnabled(False)
            self.pushButton_select_secondary_backup_directory.setEnabled(False)
            self.pushButton_open_secondary_backup_directory.setEnabled(False)
            self.label_local_backup_scheduling_2.setEnabled(False)
            self.comboBox_secondary_backup_scheduling.setEnabled(False)
            self.checkBox_secondary_big_file_option.setEnabled(False)
            self.label_path.setEnabled(False)

    def local_big_file_option_change(self):
        if self.checkBox_local_big_file_option.isChecked():
            self.settings["local_backup_big_script_file_option"] = "Enable"
            self.save_settings()
        else:
            self.settings["local_backup_big_script_file_option"] = "Disable"
            self.save_settings()

    def secondary_big_file_option_change(self):
        if self.checkBox_secondary_big_file_option.isChecked():
            self.settings["secondary_backup_big_script_file_option"] = "Enable"
            self.save_settings()
        else:
            self.settings["secondary_backup_big_script_file_option"] = "Disable"
            self.save_settings()


    def combo_change_test(self):
        if self.comboBox.currentIndex() == 0 :
            nuke.message("Km_backup :is enable")
        else :
            nuke.message("Km_backup :is disable")

    def get_script_name_without_version(self) : 
        script = nuke.root().name()
        script_name = os.path.basename(script)
        script_name = os.path.splitext(script_name)[0]
        try:
            ##print script_name
            version_number = nukescripts.version_get(script_name,"v")[1]
            ##print version_number
            script_name_without_version = script_name.replace("_v"+version_number, "")
            script_name_without_version = script_name_without_version.replace("_V"+version_number, "")
            ##print script_name_without_version
            return script_name_without_version
        except Exception as e:
            return script_name

    def get_local_backup_folder_path(self) :
        local_backup_folder_path = nuke.script_directory()+"/backups-"+self.get_script_name_without_version()
        return local_backup_folder_path

    def open_in_script_backup_folder(self):
        if nuke.Root().name() == 'Root': #check project saved yet or not
            nuke.message("Km_backup : First save the Project")
        else : 
            local_backup_folder_path = self.get_local_backup_folder_path()
            if not os.path.exists(local_backup_folder_path):
                os.makedirs(local_backup_folder_path)

            if os.path.exists(local_backup_folder_path):
                if operatingSystem == "Windows":
                    os.startfile(local_backup_folder_path)
                elif operatingSystem == "Darwin":
                    subprocess.Popen(["open", local_backup_folder_path])
                else:
                    subprocess.Popen(["xdg-open", local_backup_folder_path])
            else:
                nuke.message("Km_backup : local backup folder does not exists")

            

    def open_secondary_backup_folder(self):
        path = self.lineEdit_secondary_backup_path.text()

        if not os.path.exists(path):
            os.makedirs(path)

        if os.path.exists(path):
            if operatingSystem == "Windows":
                os.startfile(path)
            elif operatingSystem == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])
        else:
            nuke.message("Km_backup : the path does not exists")

    def set_seocondary_backup_directory(self):
        #filePath = nuke.getFilename('Seocondary Backup Folder', '')
        seocondary_backup_directory = QFileDialog.getExistingDirectory(self, 'Select Seocondary Backup Directory')
        if seocondary_backup_directory:
            self.settings["secondary-backup-path"] = seocondary_backup_directory
            self.save_settings()
            self.lineEdit_secondary_backup_path.setText(self.settings["secondary-backup-path"])

    def add_to_pane(self):
        pane = nuke.getPaneFor('Properties.1')
        panels.registerWidgetAsPanel('km_bakup.Km_Backup_Panel', 'Km Backup And Recovery', 'uk.co.thefoundry.Km_Backup_Panel', True).addToPane(pane)






panels.registerWidgetAsPanel('km_bakup.Km_Backup_Panel', 'Km Backup And Recovery', 'uk.co.thefoundry.Km_Backup_Panel')


Km_Backup_Panel_Instance = Km_Backup_Panel()


def show_panel() :
    #Km_Backup_Panel_Instance = Km_Backup_Panel()
    Km_Backup_Panel_Instance.show()
    Km_Backup_Panel_Instance.update_UI()
    #Km_Backup_Panel_Instance.update_list()

##Km_Backup_Panel.show()










