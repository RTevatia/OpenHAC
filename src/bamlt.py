# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bamlt.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1649, 882)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistView = QtWidgets.QListView(self.centralWidget)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout.addWidget(self.playlistView)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horizontalLayout_4.addWidget(self.currentTimeLabel)
        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_4.addWidget(self.timeSlider)
        self.totalTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.horizontalLayout_4.addWidget(self.totalTimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        self.previousButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/control-skip-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_5.addWidget(self.previousButton)
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_5.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/control-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/control-stop-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_5.addWidget(self.stopButton)
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/control-skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)
        self.viewButton = QtWidgets.QPushButton(self.centralWidget)
        self.viewButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/application-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setCheckable(True)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_5.addWidget(self.viewButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/speaker-volume.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1649, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuClassify = QtWidgets.QMenu(self.menuTools)
        self.menuClassify.setObjectName("menuClassify")
        self.menuCreate = QtWidgets.QMenu(self.menuClassify)
        self.menuCreate.setObjectName("menuCreate")
        self.menuAutomate = QtWidgets.QMenu(self.menuClassify)
        self.menuAutomate.setObjectName("menuAutomate")
      #  self.menuAnnotate = QtWidgets.QMenu(self.menuTools)
       # self.menuAnnotate.setObjectName("menuAnnotate")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuPlot = QtWidgets.QMenu(self.menuAnalysis)
        self.menuPlot.setObjectName("menuPlot")
        self.menuPerformance = QtWidgets.QMenu(self.menuPlot)
        self.menuPerformance.setObjectName("menuPerformance")
        self.menuInterpretation = QtWidgets.QMenu(self.menuPlot)
        self.menuInterpretation.setObjectName("menuInterpretation")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_2)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-new-copy-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Project.setIcon(icon1)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-download-resume-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Project.setIcon(icon2)
        self.actionSave_Project.setObjectName("actionSave_Project")
        #self.actionLoad_Project = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-unload-cargo-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.actionLoad_Project.setIcon(icon3)
        #self.actionLoad_Project.setObjectName("actionLoad_Project")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons8-help-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDataframeview = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons8-data-sheet-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataframeview.setIcon(icon5)
        self.actionDataframeview.setObjectName("actionDataframeview")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons8-high-importance-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon6)
        self.actionHelp.setObjectName("actionHelp")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons8-upload-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon7)
        self.actionLoad.setObjectName("actionLoad")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons8-development-skill-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTrain.setIcon(icon8)
        self.actionTrain.setObjectName("actionTrain")
       # self.actionLoad_class = QtWidgets.QAction(MainWindow)
        #self.actionLoad_class.setIcon(icon7)
       # self.actionLoad_class.setObjectName("actionLoad_class")
        self.actionDeploy = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons8-launch-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeploy.setIcon(icon9)
        self.actionDeploy.setObjectName("actionDeploy")
        self.actionFace_and_head = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons8-face-id-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       # self.actionHead_motion = QtWidgets.QAction(MainWindow)
        self.actionFace_and_head.setIcon(icon10)
        self.actionFace_and_head.setObjectName("actionFace_and_head")
        self.actionPose_analysis = QtWidgets.QAction(MainWindow)
        #icon20 = QtGui.QIcon()
        #icon20.addPixmap(QtGui.QPixmap("icons8-confusion-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.actionHead_motion.setIcon(icon20)
        #self.actionHead_motion.setObjectName("actionHead_motion")
        self.actionPose_analysis = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons8-exercise-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPose_analysis.setIcon(icon11)
        self.actionPose_analysis.setObjectName("actionPose_analysis")
        self.actionBinary = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons8-tree-structure-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBinary.setIcon(icon12)
        self.actionBinary.setObjectName("actionBinary")
        self.actionHeartrate = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons8-heart-with-pulse-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHeartrate.setIcon(icon13)
        self.actionHeartrate.setObjectName("actionHeartrate")
        self.actionAdd_video = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons8-video-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_video.setIcon(icon14)
        self.actionAdd_video.setObjectName("actionAdd_video")
        self.actionPrecision_Recall_Curve = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons8-scatter-plot-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrecision_Recall_Curve.setIcon(icon15)
        self.actionPrecision_Recall_Curve.setObjectName("actionPrecision_Recall_Curve")
        self.actionConfusion_Matrix = QtWidgets.QAction(MainWindow)
        self.actionConfusion_Matrix.setIcon(icon15)
        self.actionConfusion_Matrix.setObjectName("actionConfusion_Matrix")
        self.actionAUC = QtWidgets.QAction(MainWindow)
        self.actionAUC.setIcon(icon15)
        self.actionAUC.setObjectName("actionAUC")
        self.actionPrecision_Recall_Curve_2 = QtWidgets.QAction(MainWindow)
        self.actionPrecision_Recall_Curve_2.setIcon(icon15)
        self.actionPrecision_Recall_Curve_2.setObjectName("actionPrecision_Recall_Curve_2")
        #self.actionConfusion_Matrix_2 = QtWidgets.QAction(MainWindow)
       # self.actionConfusion_Matrix_2.setIcon(icon15)
       # self.actionConfusion_Matrix_2.setObjectName("actionConfusion_Matrix_2")
        #self.actionClassification_Report = QtWidgets.QAction(MainWindow)
        #self.actionClassification_Report.setIcon(icon15)
        #self.actionClassification_Report.setObjectName("actionClassification_Report")
        self.actionFeature_Importance = QtWidgets.QAction(MainWindow)
        self.actionFeature_Importance.setIcon(icon15)
        self.actionFeature_Importance.setObjectName("actionFeature_Importance")
        #self.actionClass_Prediciton_Error = QtWidgets.QAction(MainWindow)
        #self.actionClass_Prediciton_Error.setIcon(icon15)
        #self.actionClass_Prediciton_Error.setObjectName("actionClass_Prediciton_Error")
        self.actionSummary = QtWidgets.QAction(MainWindow)
        self.actionSummary.setIcon(icon15)
        self.actionSummary.setObjectName("actionSummary")
        self.actionCorrelation = QtWidgets.QAction(MainWindow)
        self.actionCorrelation.setIcon(icon15)
        self.actionCorrelation.setObjectName("actionCorrelation")
        self.actionReason = QtWidgets.QAction(MainWindow)
        self.actionReason.setIcon(icon15)
        self.actionReason.setObjectName("actionReason")
        self.menuMenu.addAction(self.actionNew_Project)
        self.menuMenu.addAction(self.actionSave_Project)
       # self.menuMenu.addAction(self.actionLoad_Project)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuCreate.addAction(self.actionTrain)
        #self.menuCreate.addAction(self.actionLoad_class)
        self.menuCreate.addAction(self.actionDeploy)
        self.menuAutomate.addAction(self.actionFace_and_head)
        #self.menuAutomate.addAction(self.actionHead_motion)
        self.menuAutomate.addAction(self.actionPose_analysis)
        self.menuAutomate.addAction(self.actionHeartrate)
        self.menuClassify.addAction(self.menuCreate.menuAction())
        self.menuClassify.addAction(self.menuAutomate.menuAction())
       # self.menuAnnotate.addAction(self.actionBinary)
        self.menuTools.addAction(self.menuClassify.menuAction())
       # self.menuTools.addAction(self.menuAnnotate.menuAction())
        self.menuPerformance.addAction(self.actionAUC)
        self.menuPerformance.addAction(self.actionPrecision_Recall_Curve_2)
        #self.menuPerformance.addAction(self.actionConfusion_Matrix_2)
       # self.menuPerformance.addAction(self.actionClassification_Report)
        self.menuPerformance.addAction(self.actionFeature_Importance)
       # self.menuPerformance.addAction(self.actionClass_Prediciton_Error)
        self.menuInterpretation.addAction(self.actionSummary)
        self.menuInterpretation.addAction(self.actionCorrelation)
        self.menuInterpretation.addAction(self.actionReason)
        self.menuPlot.addAction(self.menuPerformance.menuAction())
        self.menuPlot.addAction(self.menuInterpretation.menuAction())
        self.menuAnalysis.addAction(self.actionDataframeview)
        self.menuAnalysis.addAction(self.menuPlot.menuAction())
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionFace_and_head)
       # self.toolBar.addAction(self.actionHead_motion)
        self.toolBar.addAction(self.actionPose_analysis)
        self.toolBar.addAction(self.actionHeartrate)
        self.toolBar.addAction(self.actionTrain)
       # self.toolBar.addAction(self.actionLoad_class)
        self.toolBar.addAction(self.actionDeploy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_video)
        self.toolBar_2.addAction(self.actionNew_Project)
        self.toolBar_2.addAction(self.actionSave_Project)
       # self.toolBar_2.addAction(self.actionLoad_Project)
        self.toolBar_2.addAction(self.actionAbout)
        
      

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "D-BAMLT"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuClassify.setTitle(_translate("MainWindow", "Classify"))
        self.menuCreate.setTitle(_translate("MainWindow", "Create"))
        self.menuAutomate.setTitle(_translate("MainWindow", "Automate"))
       # self.menuAnnotate.setTitle(_translate("MainWindow", "Annotate"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.menuPerformance.setTitle(_translate("MainWindow", "Performance"))
        self.menuInterpretation.setTitle(_translate("MainWindow", "Interpretation"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionNew_Project.setText(_translate("MainWindow", "Add notes"))
        self.actionSave_Project.setText(_translate("MainWindow", "Create logging report from note file"))
       # self.actionLoad_Project.setText(_translate("MainWindow", "Begin logging"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDataframeview.setText(_translate("MainWindow", "Dataframe"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionTrain.setText(_translate("MainWindow", "Train"))
       # self.actionLoad_class.setText(_translate("MainWindow", "Load"))
        self.actionDeploy.setText(_translate("MainWindow", "Deploy"))
        self.actionFace_and_head.setText(_translate("MainWindow", "Face and head behavior"))
       # self.actionHead_motion.setText(_translate("MainWindow", "Head motor and oculomotor"))
        self.actionPose_analysis.setText(_translate("MainWindow", "Body keypoints"))
        self.actionBinary.setText(_translate("MainWindow", "Binary"))
        self.actionHeartrate.setText(_translate("MainWindow", "Heart rate"))
        self.actionAdd_video.setText(_translate("MainWindow", "Add video"))
        self.actionPrecision_Recall_Curve.setText(_translate("MainWindow", "Precision Recall Curve"))
        self.actionConfusion_Matrix.setText(_translate("MainWindow", "Confusion Matrix"))
        self.actionAUC.setText(_translate("MainWindow", "Area Under the Curve"))
        self.actionPrecision_Recall_Curve_2.setText(_translate("MainWindow", "Precision Recall Curve"))
       # self.actionConfusion_Matrix_2.setText(_translate("MainWindow", "Confusion Matrix"))
        #self.actionClassification_Report.setText(_translate("MainWindow", "Classification Report"))
        self.actionFeature_Importance.setText(_translate("MainWindow", "Feature Importance"))
       # self.actionClass_Prediciton_Error.setText(_translate("MainWindow", "Class Prediciton Error"))
        self.actionSummary.setText(_translate("MainWindow", "Summary"))
        self.actionCorrelation.setText(_translate("MainWindow", "Correlation"))
        self.actionReason.setText(_translate("MainWindow", "Reason"))

        self.currentTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.totalTimeLabel.setText(_translate("MainWindow", "0:00"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
