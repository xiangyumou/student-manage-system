# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 363)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_ban_enable = QtWidgets.QComboBox(Dialog)
        self.comboBox_ban_enable.setObjectName("comboBox_ban_enable")
        self.horizontalLayout.addWidget(self.comboBox_ban_enable)
        self.lineEdit_ban_enable_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ban_enable_id.setObjectName("lineEdit_ban_enable_id")
        self.horizontalLayout.addWidget(self.lineEdit_ban_enable_id)
        self.pushButton_ban_enable = QtWidgets.QPushButton(Dialog)
        self.pushButton_ban_enable.setObjectName("pushButton_ban_enable")
        self.horizontalLayout.addWidget(self.pushButton_ban_enable)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_identity = QtWidgets.QComboBox(Dialog)
        self.comboBox_identity.setObjectName("comboBox_identity")
        self.horizontalLayout_2.addWidget(self.comboBox_identity)
        self.lineEdit_add_account_identifier = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_add_account_identifier.setObjectName("lineEdit_add_account_identifier")
        self.horizontalLayout_2.addWidget(self.lineEdit_add_account_identifier)
        self.pushButton_add_account = QtWidgets.QPushButton(Dialog)
        self.pushButton_add_account.setObjectName("pushButton_add_account")
        self.horizontalLayout_2.addWidget(self.pushButton_add_account)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEdit_student_major = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_student_major.setObjectName("lineEdit_student_major")
        self.horizontalLayout_8.addWidget(self.lineEdit_student_major)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_student_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_student_name.setObjectName("lineEdit_student_name")
        self.horizontalLayout_8.addWidget(self.lineEdit_student_name)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_student_class = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_student_class.setObjectName("lineEdit_student_class")
        self.horizontalLayout_8.addWidget(self.lineEdit_student_class)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_student_enrollment_time = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_student_enrollment_time.setObjectName("lineEdit_student_enrollment_time")
        self.horizontalLayout_8.addWidget(self.lineEdit_student_enrollment_time)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_student_identifier = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_student_identifier.setObjectName("lineEdit_student_identifier")
        self.horizontalLayout_8.addWidget(self.lineEdit_student_identifier)
        self.pushButton_add_student = QtWidgets.QPushButton(Dialog)
        self.pushButton_add_student.setObjectName("pushButton_add_student")
        self.horizontalLayout_8.addWidget(self.pushButton_add_student)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_init_identifier = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_init_identifier.setObjectName("lineEdit_init_identifier")
        self.horizontalLayout_3.addWidget(self.lineEdit_init_identifier)
        self.pushButton_init_account = QtWidgets.QPushButton(Dialog)
        self.pushButton_init_account.setObjectName("pushButton_init_account")
        self.horizontalLayout_3.addWidget(self.pushButton_init_account)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_teacher_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_teacher_id.setObjectName("lineEdit_teacher_id")
        self.horizontalLayout_4.addWidget(self.lineEdit_teacher_id)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_class_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_class_id.setObjectName("lineEdit_class_id")
        self.horizontalLayout_4.addWidget(self.lineEdit_class_id)
        self.pushButton_teacher_manage_class = QtWidgets.QPushButton(Dialog)
        self.pushButton_teacher_manage_class.setObjectName("pushButton_teacher_manage_class")
        self.horizontalLayout_4.addWidget(self.pushButton_teacher_manage_class)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_counselor_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_counselor_id.setObjectName("lineEdit_counselor_id")
        self.horizontalLayout_5.addWidget(self.lineEdit_counselor_id)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_major_id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_major_id.setObjectName("lineEdit_major_id")
        self.horizontalLayout_5.addWidget(self.lineEdit_major_id)
        self.pushButton_add_counselor_manage_major = QtWidgets.QPushButton(Dialog)
        self.pushButton_add_counselor_manage_major.setObjectName("pushButton_add_counselor_manage_major")
        self.horizontalLayout_5.addWidget(self.pushButton_add_counselor_manage_major)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_get_request_list = QtWidgets.QPushButton(Dialog)
        self.pushButton_get_request_list.setObjectName("pushButton_get_request_list")
        self.horizontalLayout_6.addWidget(self.pushButton_get_request_list)
        self.pushButton_get_student_list = QtWidgets.QPushButton(Dialog)
        self.pushButton_get_student_list.setObjectName("pushButton_get_student_list")
        self.horizontalLayout_6.addWidget(self.pushButton_get_student_list)
        self.pushButton_get_login_log = QtWidgets.QPushButton(Dialog)
        self.pushButton_get_login_log.setObjectName("pushButton_get_login_log")
        self.horizontalLayout_6.addWidget(self.pushButton_get_login_log)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_modify_account = QtWidgets.QPushButton(Dialog)
        self.pushButton_modify_account.setObjectName("pushButton_modify_account")
        self.horizontalLayout_7.addWidget(self.pushButton_modify_account)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_ban_enable.setText(_translate("Dialog", "解封/封禁"))
        self.pushButton_add_account.setText(_translate("Dialog", "添加身份账号"))
        self.label_5.setText(_translate("Dialog", "专业"))
        self.label_6.setText(_translate("Dialog", "姓名"))
        self.label_7.setText(_translate("Dialog", "班级"))
        self.label_8.setText(_translate("Dialog", "入学时间"))
        self.label_9.setText(_translate("Dialog", "学号"))
        self.pushButton_add_student.setText(_translate("Dialog", "添加"))
        self.pushButton_init_account.setText(_translate("Dialog", "初始化账号"))
        self.label.setText(_translate("Dialog", "老师id："))
        self.label_2.setText(_translate("Dialog", "班级id:"))
        self.pushButton_teacher_manage_class.setText(_translate("Dialog", "添加"))
        self.label_3.setText(_translate("Dialog", "辅导员id："))
        self.label_4.setText(_translate("Dialog", "专业id:"))
        self.pushButton_add_counselor_manage_major.setText(_translate("Dialog", "添加"))
        self.pushButton_get_request_list.setText(_translate("Dialog", "查看全部请假请求"))
        self.pushButton_get_student_list.setText(_translate("Dialog", "查看学生列表"))
        self.pushButton_get_login_log.setText(_translate("Dialog", "查看登陆日志"))
        self.pushButton_modify_account.setText(_translate("Dialog", "修改账号"))