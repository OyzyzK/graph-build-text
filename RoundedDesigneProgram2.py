# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphModel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import traceback

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1074, 828)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#FFFFFF")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 0, 771, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_count = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_count.setGeometry(QtCore.QRect(110, 90, 71, 21))
        self.textEdit_count.setStyleSheet("background-color: #f4f4f4")
        self.textEdit_count.setObjectName("textEdit_count")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 90, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_size = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_size.setGeometry(QtCore.QRect(320, 90, 71, 21))
        self.textEdit_size.setStyleSheet("background-color: #f4f4f4")
        self.textEdit_size.setObjectName("textEdit_size")
        self.cbx_color = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_color.setGeometry(QtCore.QRect(440, 90, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setBold(True)
        font.setWeight(75)
        self.cbx_color.setFont(font)
        self.cbx_color.setStyleSheet("background-color: #f4f4f4")
        self.cbx_color.setObjectName("cbx_color")
        self.cbx_color.addItem("")
        self.cbx_color.addItem("")
        self.cbx_color.addItem("")
        self.cbx_color.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_graph_build = QtWidgets.QPushButton(self.centralwidget)
        self.btn_graph_build.setGeometry(QtCore.QRect(10, 130, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.btn_graph_build.setFont(font)
        self.btn_graph_build.setStyleSheet("background-color:#F0F0F0F0;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_graph_build.setObjectName("btn_graph_build")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(380, 790, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setWeight(50)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("background-color: #f0f0f0;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_save.setObjectName("btn_save")
        self.textEdit_report = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_report.setGeometry(QtCore.QRect(10, 390, 521, 391))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.textEdit_report.setFont(font)
        self.textEdit_report.setStyleSheet("background-color: #f0f0f0")
        self.textEdit_report.setObjectName("textEdit_report")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_fullText = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_fullText.setGeometry(QtCore.QRect(560, 80, 501, 701))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.textEdit_fullText.setFont(font)
        self.textEdit_fullText.setWhatsThis("")
        self.textEdit_fullText.setStyleSheet("background-color: #B2BABB")
        self.textEdit_fullText.setPlaceholderText("")
        self.textEdit_fullText.setObjectName("textEdit_fullText")
        self.btn_cloud_build = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cloud_build.setGeometry(QtCore.QRect(10, 280, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cloud_build.setFont(font)
        self.btn_cloud_build.setStyleSheet("background-color:#F0F0F0F0;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_cloud_build.setObjectName("btn_cloud_build")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(560, 790, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_open.setFont(font)
        self.btn_open.setStyleSheet("background-color:#F4F4F4F4;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_open.setObjectName("btn_open")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(940, 790, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setWeight(50)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color:#F0F0F0F0;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_clear.setObjectName("btn_clear")
        self.textEdit_size_context = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_size_context.setGeometry(QtCore.QRect(960, 50, 101, 21))
        self.textEdit_size_context.setStyleSheet("background-color: #f4f4f4")
        self.textEdit_size_context.setObjectName("textEdit_size_context")
        self.btn_find_word = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find_word.setGeometry(QtCore.QRect(780, 50, 171, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_find_word.setFont(font)
        self.btn_find_word.setStyleSheet("background-color:#F4F4F4F4;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_find_word.setObjectName("btn_find_word")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 240, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit_size_cloud = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_size_cloud.setGeometry(QtCore.QRect(320, 240, 71, 21))
        self.textEdit_size_cloud.setStyleSheet("background-color: #f4f4f4")
        self.textEdit_size_cloud.setObjectName("textEdit_size_cloud")
        self.textEdit_count_cloud = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_count_cloud.setGeometry(QtCore.QRect(110, 240, 71, 21))
        self.textEdit_count_cloud.setStyleSheet("background-color: #f4f4f4")
        self.textEdit_count_cloud.setObjectName("textEdit_count_cloud")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 200, 401, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 240, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.cbx_color_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_color_2.setGeometry(QtCore.QRect(440, 240, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setBold(True)
        font.setWeight(75)
        self.cbx_color_2.setFont(font)
        self.cbx_color_2.setStyleSheet("background-color: #f4f4f4")
        self.cbx_color_2.setObjectName("cbx_color_2")
        self.cbx_color_2.addItem("")
        self.cbx_color_2.addItem("")
        self.cbx_color_2.addItem("")
        self.cbx_color_2.addItem("")
        self.cbx_color_2.addItem("")
        self.cbx_color_2.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 320, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 350, 521, 21))
        self.textEdit.setStyleSheet("background-color: #f4f4f4")
        self.textEdit.setObjectName("textEdit")
        self.btn_open_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_2.setGeometry(QtCore.QRect(400, 320, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_open_2.setFont(font)
        self.btn_open_2.setStyleSheet("background-color:#F4F4F4F4;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.btn_open_2.setObjectName("btn_open_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText(f"Ошибка:\n, {traceback.format_exc()}")
        self.textEdit_count.clear()
        self.textEdit_size.clear()
        x = msg.exec_()


    def save_as(self):
        S__File = QtWidgets.QFileDialog.getSaveFileName(None, 'SaveTextFile', '/', "Text Files (*.txt)")
        Text = self.textEdit_report.toPlainText()
        if S__File[0]:
            with open(S__File[0], 'w') as file:
                file.write(Text)


    def add_edge(self, f_item, s_item, graph=None):
        graph.add_edge(f_item, s_item)
        graph.add_edge(s_item, f_item)



    def count_words_fast(self):
        from collections import Counter
        text = self.textEdit_fullText.toPlainText().lower().split(" ")
        shortskips = [sh_ch for sh_ch in text if len(sh_ch)<4]
        skips = self.textEdit.toPlainText().split(" ") + shortskips
        text.remove(ch for ch in skips if ch in text)
        word_counts = Counter(text)
        return word_counts


    def graph_view(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        counter = self.count_words_fast()
        if self.textEdit_count.toPlainText().isalpha() or self.textEdit_count.toPlainText() == "" or self.textEdit_fullText.toPlainText() == "" or self.textEdit_size.toPlainText() == "":
            return self.error()
        iterations = int(self.textEdit_count.toPlainText())
        most = [i for i in counter.most_common(iterations)]
        graph = nx.Graph()
        print(most[1])
        graph.nodes()
        for i in range(iterations):
            while i >= 0:
                self.add_edge(f'{(most[i])}', f'{(most[i - 1])}', graph=graph)
                self.add_edge(f'{(most[i-2])}', f'{(most[i - 3])}', graph=graph)
                i -= 1
        nx.draw(graph, with_labels=True, node_size=int(self.textEdit_size.toPlainText()), arrows=False,
                pos=nx.random_layout(graph), node_color=self.choose_color())
        plt.show()
        self.report()
        #self.sentiment_analysis()


    def sentence(self):
        context = self.textEdit_size_context.toPlainText()
        if not self.textEdit_fullText.find(context):
            cursor = self.textEdit_fullText.textCursor()
            cursor.setPosition(0)
            self.textEdit_fullText.setTextCursor(cursor)
            self.textEdit_fullText.find(context)


    def sentiment_analysis(self):
        from dostoevsky.tokenization import RegexTokenizer
        from dostoevsky.models import FastTextSocialNetworkModel
        tokenizer = RegexTokenizer()
        model = FastTextSocialNetworkModel(tokenizer=tokenizer)
        messages = [
            'Сегодня хорошая погода',
            'Я счастлив проводить с тобою время',
            'Мне нравится эта музыкальная композиция',
            'В больнице была ужасная очередь',
            'Сосед с верхнего этажа мешает спать',
            'Маленькая девочка потерялась в торговом центре',
        ]
        results = model.predict(messages, k=2)
        for message, sentiment in zip(messages, results):
         self.textEdit_report.setPlainText(f"{message}, '-&gt;', {sentiment}")


    def report(self):
        counter = self.count_words_fast()
        iterations = int(self.textEdit_count.toPlainText())
        num_unique = len(self.count_words_fast())
        most = []
        for i in counter.most_common(iterations): most.append(i)
        print(*[x[0] for x in most], sep=",")
        print(*[x[1] for x in most], sep=",")
        self.textEdit_report.setText("Отчет данных по произвдению: \n"
                                     f"Всего слов: {len(self.textEdit_fullText.toPlainText().split())}, Уникальных слов: {num_unique}\n"
                                     f"Топ {iterations} слов:")
        for i in most: self.textEdit_report.append(f"{i[0]}, — {i[1]}")


    def cloud(self):
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
        if self.textEdit_fullText.toPlainText() == "" or self.textEdit_count_cloud.toPlainText() == "" or self.textEdit_size_cloud.toPlainText() == "":
            return self.error()
        text_raw = " ".join(self.count_words_fast())
        maxwords = int(self.textEdit_count_cloud.toPlainText())
        maxsize = int(self.textEdit_size_cloud.toPlainText())
        if self.textEdit.toPlainText()=="": stop_words = ""
        stop_words=set(self.textEdit.toPlainText().split())
        wordcloud = WordCloud(max_words=maxwords, max_font_size=maxsize, colormap=self.choose_color_cloud(),stopwords=stop_words).generate(
            text_raw)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


    def book_clear(self):
        self.textEdit_fullText.clear()


    def choose_color(self):
        clr = self.cbx_color.currentText()
        colors = {
            "Зеленый": "green",
            "Красный": "red",
            "Синий": "blue",
            "Желтый": "yellow"
        }
        for k in colors.keys():
            if clr == k:
                return colors[k]


    def choose_color_cloud(self):
        clr = self.cbx_color_2.currentText()
        colors = {
            "Зеленый": "Greens",
            "Красный": "Reds",
            "Синий": "Blues",
            "Оранжевый": "Oranges",
            "Фиолетовый": "Purples",
            "Серый": "Greys"
        }
        for k in colors.keys():
            if clr == k:
                return colors[k]


    def open_dialog_box(self):
        try:
            filename = QFileDialog.getOpenFileName()
            self.path = filename[0]
            self.textEdit_fullText.setText(self.path)
            with open(self.path, 'r', encoding="utf-8") as file:
                self.textEdit_fullText.setPlainText(file.read())
        except:
            pass


    def open_skips(self):
        try:
            filename = QFileDialog.getOpenFileName()
            self.path = filename[0]
            self.textEdit.setText(self.path)
            with open(self.path, 'r',encoding="utf-8") as file:
                self.textEdit.setPlainText(file.read())
        except:
            pass


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Построение модели данных художественных произведений"))
        self.label_2.setText(_translate("MainWindow", "Построение моделей данных художественных произведений"))
        self.label.setText(_translate("MainWindow", "Свойства для построения  графовой модели данных:"))
        self.label_6.setText(_translate("MainWindow", "Цвет "))
        self.cbx_color.setItemText(0, _translate("MainWindow", "Зеленый"))
        self.cbx_color.setItemText(1, _translate("MainWindow", "Красный"))
        self.cbx_color.setItemText(2, _translate("MainWindow", "Синий"))
        self.cbx_color.setItemText(3, _translate("MainWindow", "Желтый"))
        self.label_4.setText(_translate("MainWindow", "Размер узлов"))
        self.btn_graph_build.setText(_translate("MainWindow", " Построить графовую модель "))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.label_3.setText(_translate("MainWindow", "Текст произведения"))
        self.textEdit_fullText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic UI Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.btn_cloud_build.setText(_translate("MainWindow", "Построить модель Облако слов"))
        self.btn_open.setText(_translate("MainWindow", "Открыть файл"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))
        self.btn_find_word.setText(_translate("MainWindow", "Найти слово в контексте:"))
        self.label_5.setText(_translate("MainWindow", "Количество "))
        self.label_7.setText(_translate("MainWindow", "Количество "))
        self.label_8.setText(_translate("MainWindow", "Размер шрифта "))
        self.label_9.setText(_translate("MainWindow", "Свойства для построения модели  данных Облако слов:"))
        self.label_11.setText(_translate("MainWindow", "Цвет "))
        self.cbx_color_2.setItemText(0, _translate("MainWindow", "Зеленый"))
        self.cbx_color_2.setItemText(1, _translate("MainWindow", "Красный"))
        self.cbx_color_2.setItemText(2, _translate("MainWindow", "Синий"))
        self.cbx_color_2.setItemText(3, _translate("MainWindow", "Оранжевый"))
        self.cbx_color_2.setItemText(4, _translate("MainWindow", "Фиолетовый"))
        self.cbx_color_2.setItemText(5, _translate("MainWindow", "Серый"))
        self.label_10.setText(_translate("MainWindow", "Необрабатываемые слова при построении:"))
        self.btn_open_2.setText(_translate("MainWindow", "Открыть файл"))
        self.btn_open.clicked.connect(self.open_dialog_box)
        self.btn_clear.clicked.connect(self.book_clear)
        self.btn_save.clicked.connect(self.save_as)
        self.btn_graph_build.clicked.connect(self.graph_view)
        self.btn_find_word.clicked.connect(self.sentence)
        self.btn_cloud_build.clicked.connect(self.cloud)
        self.btn_open_2.clicked.connect(self.open_skips)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
