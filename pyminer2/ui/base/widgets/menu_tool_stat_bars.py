import os
import sys

from PyQt5.QtCore import QRect, QCoreApplication, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QMenuBar, QMenu, QMainWindow, QAction, QToolBar, QStatusBar, QWidget, QApplication, \
    QGridLayout, QPushButton, QSizePolicy, QTabWidget, QSpacerItem, QHBoxLayout, QVBoxLayout, QToolButton, QLabel

from pyminer2.ui.generalwidgets import PMToolButton


def init_actions(app):
    from .resources import icon_lc_draw_chart, icon_lc_statisiticsmenu, icon_lc_dbreportedit, icon_lc_save, \
        icon_mergedocuments, icon_lc_dataarearefresh, icon_dbviewtables, icon_lc_autosum, icon_New, icon_folder, \
        icon_input, icon_Save, icon_wb_setting_normal, icon_Delete, icon_Cut, icon_Copy, icon_Paste, \
        icon_lc_formfilternavigator, icon_lc_mergecells, icon_hlinettp, icon_dbqueryedit, icon_infobox, \
        icon_lc_dbqueryrename, icon_lc_dia, icon_lc_dbsortingandgrouping, icon_lc_insertplugin, icon_jupyter, \
        icon_python, icon_lc_arrowshapes_right_arrow_callout, icon_ext, icon_ext_install

    app.action_data = QAction(app)

    app.action_data.setIcon(icon_dbviewtables)
    app.action_data.setObjectName("action_data")
    app.action_stats = QAction(app)

    app.action_stats.setIcon(icon_lc_autosum)
    app.action_stats.setObjectName("action_stats")
    app.action_plot = QAction(app)
    app.action_plot.setIcon(icon_lc_draw_chart)
    app.action_plot.setObjectName("action_plot")
    app.action_ext = QAction(app)
    app.action_ext.setIcon(icon_ext)
    app.action_ext.setObjectName('action_ext')
    app.action_model = QAction(app)
    app.action_model.setIcon(icon_lc_statisiticsmenu)
    app.action_model.setObjectName("action_model")
    app.action_menu_new = QAction(app)

    app.action_menu_new.setIcon(icon_New)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_new.setFont(font)
    app.action_menu_new.setObjectName("action_menu_new")
    app.action_menu_open = QAction(app)

    app.action_menu_open.setIcon(icon_folder)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_open.setFont(font)
    app.action_menu_open.setObjectName("action_menu_open")
    app.action_menu_import_file = QAction(app)

    app.action_menu_import_file.setIcon(icon_input)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_import_file.setFont(font)
    app.action_menu_import_file.setObjectName("action_menu_import_file")
    app.action_menu_save = QAction(app)

    app.action_menu_save.setIcon(icon_Save)
    app.action_menu_save.setObjectName("action_menu_save")
    app.action_menu_save_as = QAction(app)
    app.action_menu_save_as.setObjectName("action_menu_save_as")
    app.action_menu_option = QAction(app)

    app.action_menu_option.setIcon(icon_wb_setting_normal)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_option.setFont(font)
    app.action_menu_option.setObjectName("action_menu_option")
    app.action_quit = QAction(app)

    app.action_quit.setIcon(icon_Delete)
    app.action_quit.setObjectName("action_quit")

    app.action_install_ext = QAction(app)
    app.action_install_ext.setIcon(icon_ext_install)
    app.action_install_ext.setObjectName('action_install_ext')

    app.action_menu_cut = QAction(app)

    app.action_menu_cut.setIcon(icon_Cut)
    app.action_menu_cut.setObjectName("action_menu_cut")
    app.action_menu_copy = QAction(app)

    app.action_menu_copy.setIcon(icon_Copy)
    app.action_menu_copy.setObjectName("action_menu_copy")
    app.action_menu_paste = QAction(app)

    app.action_menu_paste.setIcon(icon_Paste)
    app.action_menu_paste.setObjectName("action_menu_paste")
    app.action_menu_toolbar = QAction(app)
    app.action_menu_toolbar.setCheckable(True)
    app.action_menu_toolbar.setChecked(True)
    app.action_menu_toolbar.setObjectName("action_menu_toolbar")
    app.action_menu_statusbar = QAction(app)
    app.action_menu_statusbar.setCheckable(True)
    app.action_menu_statusbar.setChecked(True)
    app.action_menu_statusbar.setObjectName("action_menu_statusbar")
    app.action_transposition = QAction(app)
    app.action_transposition.setObjectName("action_transposition")
    app.action_menu_data_filter = QAction(app)

    app.action_menu_data_filter.setIcon(icon_lc_formfilternavigator)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_data_filter.setFont(font)
    app.action_menu_data_filter.setObjectName("action_menu_data_filter")
    app.action_menu_data_merge_v = QAction(app)
    app.action_menu_data_merge_v.setIcon(icon_mergedocuments)
    app.action_menu_data_merge_v.setObjectName("action_menu_data_merge_v")
    app.action_menu_data_merge_h = QAction(app)

    app.action_menu_data_merge_h.setIcon(icon_lc_mergecells)
    app.action_menu_data_merge_h.setObjectName("action_menu_data_merge_h")
    app.action_menu_stat_describe = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_stat_describe.setFont(font)
    app.action_menu_stat_describe.setObjectName("action_menu_stat_describe")
    app.action_distribution = QAction(app)
    app.action_distribution.setObjectName("action_distribution")
    app.action_missvalue = QAction(app)
    app.action_missvalue.setObjectName("action_missvalue")
    app.action_outlier = QAction(app)
    app.action_outlier.setObjectName("action_outlier")
    app.action_corr = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_corr.setFont(font)
    app.action_corr.setObjectName("action_corr")
    app.action_regression = QAction(app)
    app.action_regression.setObjectName("action_regression")
    app.action_classify = QAction(app)
    app.action_classify.setObjectName("action_classify")
    app.action_dimension_reduction = QAction(app)
    app.action_dimension_reduction.setObjectName("action_dimension_reduction")
    app.action_non_parametric_test = QAction(app)
    app.action_non_parametric_test.setObjectName("action_non_parametric_test ")
    app.action_time_series_prediction = QAction(app)
    app.action_time_series_prediction.setObjectName(
        "action_time_series_prediction")
    app.action_survival_analysis = QAction(app)
    app.action_survival_analysis.setObjectName("action_survival_analysis")
    app.action_line = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_line.setFont(font)
    app.action_line.setObjectName("action_line")
    app.action_histogram = QAction(app)
    app.action_histogram.setObjectName("action_histogram")
    app.action_scatter = QAction(app)
    app.action_scatter.setObjectName("action_scatter")
    app.action_boxplot = QAction(app)
    app.action_boxplot.setObjectName("action_boxplot")
    app.action_bar = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_bar.setFont(font)
    app.action_bar.setObjectName("action_bar")
    app.action_menu_tree = QAction(app)
    app.action_menu_tree.setObjectName("action_menu_tree")
    app.action_roc = QAction(app)
    app.action_roc.setObjectName("action_roc")
    app.action_menu_woe_iv = QAction(app)
    app.action_menu_woe_iv.setObjectName("action_menu_woe_iv")
    app.action_scorecard = QAction(app)
    app.action_scorecard.setObjectName("action_scorecard")
    app.action_ks = QAction(app)
    app.action_ks.setObjectName("action_ks")
    app.action_officesite = QAction(app)

    app.action_officesite.setIcon(icon_hlinettp)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_officesite.setFont(font)
    app.action_officesite.setObjectName("action_officesite")
    app.action_update = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_update.setFont(font)
    app.action_update.setObjectName("action_update")
    app.action_help = QAction(app)
    app.action_help.setIcon(icon_hlinettp)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_help.setFont(font)
    app.action_help.setObjectName("action_help")
    app.action_about = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_about.setFont(font)
    app.action_about.setObjectName("action_about")
    app.action = QAction(app)
    app.action.setObjectName("action")
    app.action_2 = QAction(app)
    app.action_2.setObjectName("action_2")
    app.action_3 = QAction(app)
    app.action_3.setObjectName("action_3")
    app.action_4 = QAction(app)
    app.action_4.setObjectName("action_4")
    app.action_5 = QAction(app)
    app.action_5.setObjectName("action_5")
    app.action_6 = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_6.setFont(font)
    app.action_6.setObjectName("action_6")
    app.action_menu_database = QAction(app)

    app.action_menu_database.setIcon(icon_dbqueryedit)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_menu_database.setFont(font)
    app.action_menu_database.setObjectName("action_menu_database")
    app.action_menu_quick_exit = QAction(app)

    app.action_menu_quick_exit.setIcon(icon_infobox)
    app.action_menu_quick_exit.setObjectName("action_menu_quick_exit")
    app.action_assess = QAction(app)
    app.action_assess.setIcon(icon_lc_dbreportedit)
    app.action_assess.setObjectName("action_assess")

    app.action_menu_dataset = QAction(app)
    app.action_menu_dataset.setIcon(icon_lc_dataarearefresh)
    app.action_menu_dataset.setObjectName("action_menu_dataset")
    app.action_dataset_export = QAction(app)
    app.action_dataset_export.setIcon(icon_lc_save)
    app.action_dataset_export.setObjectName("action_dataset_export")
    app.action_dataset_rename = QAction(app)

    app.action_dataset_rename.setIcon(icon_lc_dbqueryrename)
    app.action_dataset_rename.setObjectName("action_dataset_rename")
    app.action_menu_data_row_filter = QAction(app)
    app.action_menu_data_row_filter.setObjectName(
        "action_menu_data_row_filter")

    app.action_menu_result = QAction(app)
    app.action_menu_result.setIcon(icon_lc_dia)
    app.action_menu_result.setObjectName("action_menu_result")

    app.action_menu_sort = QAction(app)

    app.action_menu_sort.setIcon(icon_lc_dbsortingandgrouping)
    app.action_menu_sort.setObjectName("action_menu_sort")

    app.action_package_manager = QAction(app)
    app.action_package_manager.setIcon(icon_lc_insertplugin)
    app.action_package_manager.setObjectName("action_package_manager")
    app.action_jupyter_notebook = QAction(app)

    app.action_jupyter_notebook.setIcon(icon_jupyter)
    app.action_jupyter_notebook.setObjectName("action_jupyter_notebook")
    app.actionWindows = QAction(app)
    app.actionWindows.setObjectName("actionWindows")
    app.actionFusion = QAction(app)
    app.actionFusion.setObjectName("actionFusion")
    app.actionQdarkstyle = QAction(app)
    app.actionQdarkstyle.setObjectName("actionQdarkstyle")
    app.action_ipython = QAction(app)

    app.action_ipython.setIcon(icon_python)
    app.action_ipython.setObjectName("action_ipython")
    app.action_7 = QAction(app)
    font = QFont()
    font.setFamily("Microsoft YaHei UI")
    app.action_7.setFont(font)
    app.action_7.setObjectName("action_7")
    app.actionWindowsVista = QAction(app)
    app.actionWindowsVista.setObjectName("actionWindowsVista")
    app.action_hide_right = QAction(app)

    app.action_hide_right.setIcon(icon_lc_arrowshapes_right_arrow_callout)
    app.action_hide_right.setObjectName("action_hide_right")
    app.action_menu_workdir = QAction(app)
    app.action_menu_workdir.setCheckable(True)
    app.action_menu_workdir.setChecked(True)
    app.action_menu_workdir.setObjectName("action_menu_workdir")
    app.action_menu_todolist = QAction(app)
    app.action_menu_todolist.setCheckable(True)
    app.action_menu_todolist.setChecked(True)
    app.action_menu_todolist.setObjectName("action_menu_todolist")
    app.action_menu_toolbox = QAction(app)
    app.action_menu_toolbox.setCheckable(True)
    app.action_menu_toolbox.setChecked(True)
    app.action_menu_toolbox.setObjectName("action_menu_toolbox")
    app.action_minitray = QAction(app)
    app.action_minitray.setObjectName("action_minitray")
    app.action_info = QAction(app)
    app.action_info.setObjectName("action_info")
    app.action_success = QAction(app)
    app.action_success.setObjectName("action_success")
    app.action_warning = QAction(app)
    app.action_warning.setObjectName("action_warning")
    app.action_error = QAction(app)
    app.action_error.setObjectName("action_error")


class PMModernToolbar(QTabWidget):
    def __init__(self):
        super().__init__()
        tab1 = PMToolbarTabHome('主页')
        self.addTab(tab1, tab1.tab_name)
        tab = PMModernToolbarTab('绘图')
        self.addTab(tab, tab.tab_name)
        tab = PMModernToolbarTab('APP')
        self.addTab(tab, tab.tab_name)
        self.setContentsMargins(0, 0, 0, 0)
        # self.setFixedHeight(105)
        # self.setMaximumHeight(120)
        self.setStyleSheet("QTabWidget::pane{border-width: 0px;background-color:#ffffff}"
                           "QTabBar::tab{border-width: 0px;width:60px;font-size:14px;background-color:#618Bd5;height"
                           ":30px;}")
        # "QTabBar::tab:selected{background-color:#618Bd5;font-size:14px;border-bottom:2px solid #618BE5;}"
        # "QTabBar::tab:hover{color:#918Bf5;font-size:14px;border-bottom:2px solid #618BE5;}")


class PMModernToolbarTab(QWidget):
    def __init__(self, tab_name: str):
        super().__init__()
        self.tab_name = tab_name

        self.grid_layout = QGridLayout()
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignBottom)
        self.grid_layout.setSpacing(0)
        layout = QHBoxLayout()
        layout.addLayout(self.grid_layout)
        layout.addItem(
            QSpacerItem(
                20,
                20,
                QSizePolicy.Expanding,
                QSizePolicy.Minimum))
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)

    def add_action(self, from_row: int, from_column: int,
                   row_span: int, column_span: int, icon_path: str = ''):
        if os.path.isfile(icon_path):
            b = PMToolButton()
            b.setText('hahaha')
            b.setIcon(QIcon(icon_path))
        else:
            b = PMToolButton()
            b.setText('hahaha')
        b.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        b.setFixedHeight(30 * row_span)
        b.setFixedWidth(30 * column_span)
        self.grid_layout.addWidget(b, from_row, from_column, row_span, column_span,
                                   alignment=Qt.AlignTop | Qt.AlignBottom)


class PMToolbarTabHome(PMModernToolbarTab):
    def __init__(self, tab_name: str):
        from pyminer2.ui.base.widgets.resources import icon_New
        super().__init__(tab_name)

        icon_open = QIcon()
        icon_open.addPixmap(
            QPixmap(":/pyqt/source/images/folder.png").scaled(60, 60,
                                                              Qt.IgnoreAspectRatio, Qt.SmoothTransformation),
            QIcon.Normal, QIcon.Off)

        icon_load_data = QIcon(
            '/media/hzy/程序/novalide/forgitcommit/pyminer2/pyminer2/pyminer2/ui' + '/source/images/dbqueryedit.png')
        self.current_col = 0

        self.add_default_sized_action(2, icon=icon_New, text='新建\n脚本')
        self.add_default_sized_action(2, icon=icon_New, text='新建\n数据')
        self.add_splitter(self.current_col)
        self.add_default_sized_action(1, text='打开')
        self.add_default_sized_action(2, text='导入\n数据', icon=icon_load_data)
        self.add_default_sized_action(2, text='保存\n工作区')
        self.add_default_sized_action(2, text='插件')
        self.add_default_sized_action(2, text='帮助')
        self.add_three_stacked_actions(
            3, text=[
                '分析代码', '运行并计时', '清除命令'], icons=[
                icon_load_data, icon_open, icon_New])

    def add_action(self, from_row: int, from_column: int, row_span: int = 3, column_span: int = 2, text: str = '',
                   icon: QIcon = None, text_under_icon=True):
        if text_under_icon:
            b = QToolButton()
            b.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            b.setStyleSheet('QToolButton{background-color:white;border:1px;padding:2px 2px} '
                            'QToolButton:hover{background-color:#ededed}'
                            )
        else:
            b = QPushButton()
            b.setStyleSheet('QPushButton{background-color:white;border:1px;padding:2px 2px;text-align:left;} '
                            'QPushButton:hover{background-color:#ededed}'
                            )
        if icon is not None:
            b.setIcon(icon)
        b.setText(text)

        b.setFixedHeight(25 * row_span)
        b.setFixedWidth(30 * column_span)
        self.grid_layout.addWidget(b, from_row, from_column, row_span, column_span,
                                   alignment=Qt.AlignTop | Qt.AlignBottom)
        # d = min(row_span, column_span)

        # b.setIconSize(QSize(30 * d, 30 * d))
        # spacer = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        # self.grid_layout.addWidget(spacer,2,2)

    def add_default_sized_action(
            self, col_span, text: str = '', icon: QIcon = None):
        self.add_action(
            0,
            self.current_col,
            row_span=3,
            column_span=col_span,
            text=text,
            icon=icon)
        self.current_col += col_span

    def add_three_stacked_actions(self, col_span, text=None, icons=None):
        if text is None:
            text = ['', '', '']
        if icons is None:
            icons = [None, None, None]
        for i in range(3):
            self.add_action(i, self.current_col, row_span=1, column_span=col_span, text=text[i], icon=icons[i],
                            text_under_icon=False)
        # self.add_action(0, self.current_col, row_span=1, column_span=col_span,text=text,icon_path=icon_path)
        # self.add_action(0, self.current_col, row_span=1, column_span=col_span,text=text,icon_path=icon_path)

    def add_splitter(self, xpos):
        qsplitter_label = QLabel()
        qsplitter_label.setFixedWidth(1)
        qsplitter_label.setFixedHeight(75)
        # l.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)
        qsplitter_label.setStyleSheet(
            'QLabel{margin:3px;background-color:#cccccc;border-radius:0px;border:0px}')
        self.grid_layout.addWidget(qsplitter_label, 0, xpos, 3, 1)
        self.current_col += 1


class PMMenuBar(QMenuBar):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.main_window = main_window
        self.setGeometry(QRect(0, 0, 1366, 23))
        self.setObjectName("menubar")

        self.menu_file = QMenu(self)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.menu_file.setFont(font)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QMenu(self)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.menu_edit.setFont(font)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_view = QMenu(self)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.menu_view.setFont(font)
        self.menu_view.setObjectName("menu_view")
        self.menu_data = QMenu(self)
        self.menu_data.setObjectName("menu_data")
        self.menu_stat = QMenu(self)
        self.menu_stat.setObjectName("menu_stat")
        self.menu_analyze = QMenu(self)
        self.menu_analyze.setObjectName("menu_analyze")
        self.menu_plot = QMenu(self)
        self.menu_plot.setObjectName("menu_plot")
        self.menu_model = QMenu(self)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.menu_model.setFont(font)
        self.menu_model.setObjectName("menu_model")
        self.menu_help = QMenu(self)
        self.menu_help.setObjectName("menu_help")
        self.menu_assess = QMenu(self)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.menu_assess.setFont(font)
        self.menu_assess.setObjectName("menu_assess")
        init_actions(self.main_window)
        self.translate()

    def bind_events(self, app):
        self.menu_file.addAction(app.action_menu_new)
        self.menu_file.addAction(app.action_menu_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(app.action_menu_import_file)
        self.menu_file.addAction(app.action_menu_database)
        self.menu_file.addSeparator()
        self.menu_file.addAction(app.action_menu_save)
        self.menu_file.addAction(app.action_menu_save_as)
        self.menu_file.addSeparator()
        self.menu_file.addAction(app.action_menu_option)
        self.menu_file.addSeparator()
        self.menu_file.addAction(app.action_quit)
        self.menu_file.addAction(app.action_install_ext)
        self.menu_edit.addAction(app.action_menu_cut)
        self.menu_edit.addAction(app.action_menu_copy)
        self.menu_edit.addAction(app.action_menu_paste)
        self.menu_view.addAction(app.action_menu_toolbar)
        self.menu_view.addAction(app.action_menu_statusbar)
        self.menu_view.addAction(app.action_menu_workdir)
        self.menu_view.addAction(app.action_menu_todolist)
        self.menu_view.addAction(app.action_menu_toolbox)
        self.menu_view.addAction(app.action_menu_result)
        self.menu_view.addAction(app.actionFusion)
        self.menu_view.addAction(app.actionQdarkstyle)
        self.menu_view.addAction(app.actionWindows)
        self.menu_view.addAction(app.actionWindowsVista)
        self.menu_view.addSeparator()
        self.menu_view.addAction(app.action_minitray)
        self.menu_view.addAction(app.action_info)
        self.menu_view.addAction(app.action_success)
        self.menu_view.addAction(app.action_warning)
        self.menu_view.addAction(app.action_error)
        self.menu_data.addAction(app.action_6)
        self.menu_data.addAction(app.action_menu_data_filter)
        self.menu_stat.addAction(app.action_menu_stat_describe)
        self.menu_analyze.addAction(app.action_corr)
        self.menu_plot.addAction(app.action_line)
        self.menu_plot.addAction(app.action_bar)
        self.menu_plot.addAction(app.action_7)
        self.menu_model.addAction(app.action_menu_tree)
        self.menu_help.addAction(app.action_officesite)
        self.menu_help.addAction(app.action_update)
        self.menu_help.addAction(app.action_help)
        self.menu_help.addAction(app.action_about)
        self.menu_assess.addAction(app.action_menu_woe_iv)

        self.addAction(self.menu_file.menuAction())
        self.addAction(self.menu_edit.menuAction())
        self.addAction(self.menu_view.menuAction())
        self.addAction(self.menu_data.menuAction())
        self.addAction(self.menu_stat.menuAction())
        self.addAction(self.menu_analyze.menuAction())
        self.addAction(self.menu_plot.menuAction())
        self.addAction(self.menu_model.menuAction())
        self.addAction(self.menu_assess.menuAction())
        self.addAction(self.menu_help.menuAction())
        self.translate()

    def translate(self):
        app = self.main_window
        _translate = QCoreApplication.translate
        self.menu_file.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_edit.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.menu_view.setTitle(_translate("MainWindow", "视图(&V)"))
        self.menu_data.setTitle(_translate("MainWindow", "数据(&D)"))
        self.menu_stat.setTitle(_translate("MainWindow", "统计(&S)"))
        self.menu_analyze.setTitle(_translate("MainWindow", "分析(A)"))
        self.menu_plot.setTitle(_translate("MainWindow", "可视化(&P)"))
        self.menu_model.setTitle(_translate("MainWindow", "模型(&M)"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.menu_assess.setTitle(_translate("MainWindow", "评估(&Z)"))

        app.action_data.setText(_translate("MainWindow", "数据"))
        app.action_data.setToolTip(_translate("MainWindow", "查看数据窗口"))
        app.action_stats.setText(_translate("MainWindow", "统计"))
        app.action_stats.setToolTip(_translate("MainWindow", "统计"))
        app.action_plot.setText(_translate("MainWindow", "可视化"))
        app.action_plot.setToolTip(_translate("MainWindow", "可视化"))
        app.action_model.setText(_translate("MainWindow", "模型"))
        app.action_model.setToolTip(_translate("MainWindow", "模型"))
        app.action_ext.setText(_translate("MainWindow", "插件"))
        app.action_ext.setToolTip(_translate("MainWindow", "插件"))
        app.action_menu_new.setText(_translate("MainWindow", "新建(&N)"))
        app.action_menu_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        app.action_menu_open.setText(_translate("MainWindow", "打开(&O)"))
        app.action_menu_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        app.action_menu_import_file.setText(_translate("MainWindow", "导入(&I)"))
        app.action_menu_import_file.setShortcut(
            _translate("MainWindow", "Ctrl+I"))
        app.action_menu_save.setText(_translate("MainWindow", "保存(&S)"))
        app.action_menu_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        app.action_menu_save_as.setText(_translate("MainWindow", "另存为"))
        app.action_menu_option.setText(_translate("MainWindow", "设置(&X)"))
        app.action_menu_option.setShortcut(_translate("MainWindow", "Alt+M"))
        app.action_quit.setText(_translate("MainWindow", "退出(&Q)"))
        app.action_quit.setShortcut(_translate("MainWindow", "Alt+Q"))
        app.action_install_ext.setText(_translate("MainWindow", "安装插件"))
        app.action_install_ext.setShortcut(_translate("MainWindow", "安装插件"))
        app.action_menu_cut.setText(_translate("MainWindow", "剪切(&X)"))
        app.action_menu_copy.setText(_translate("MainWindow", "复制(&C)"))
        app.action_menu_paste.setText(_translate("MainWindow", "粘贴(P)"))
        app.action_menu_toolbar.setText(_translate("MainWindow", "工具栏"))
        app.action_menu_statusbar.setText(_translate("MainWindow", "状态栏"))
        app.action_transposition.setText(_translate("MainWindow", "转置"))
        app.action_transposition.setShortcut(
            _translate("MainWindow", "Ctrl+T"))
        app.action_menu_data_filter.setText(_translate("MainWindow", "筛选"))
        app.action_menu_data_filter.setShortcut(
            _translate("MainWindow", "Alt+F"))
        app.action_menu_data_merge_v.setText(_translate("MainWindow", "纵向合并"))
        app.action_menu_data_merge_h.setText(_translate("MainWindow", "横向合并"))
        app.action_menu_stat_describe.setText(_translate("MainWindow", "描述统计"))
        app.action_distribution.setText(_translate("MainWindow", "数据分布"))
        app.action_missvalue.setText(_translate("MainWindow", "缺失值"))
        app.action_outlier.setText(_translate("MainWindow", "异常值"))
        app.action_corr.setText(_translate("MainWindow", "相关"))
        app.action_regression.setText(_translate("MainWindow", "回归"))
        app.action_classify.setText(_translate("MainWindow", "分类"))
        app.action_dimension_reduction.setText(_translate("MainWindow", "降维"))
        app.action_non_parametric_test.setText(
            _translate("MainWindow", "非参数检验"))
        app.action_time_series_prediction.setText(
            _translate("MainWindow", "时间序列预测"))
        app.action_survival_analysis.setText(_translate("MainWindow", "生存分析"))
        app.action_line.setText(_translate("MainWindow", "折线图"))
        app.action_line.setShortcut(_translate("MainWindow", "Alt+L"))
        app.action_histogram.setText(_translate("MainWindow", "直方图"))
        app.action_histogram.setShortcut(_translate("MainWindow", "Alt+H"))
        app.action_scatter.setText(_translate("MainWindow", "散点图"))
        app.action_scatter.setShortcut(_translate("MainWindow", "Alt+S"))
        app.action_boxplot.setText(_translate("MainWindow", "盒型图"))
        app.action_boxplot.setShortcut(_translate("MainWindow", "Alt+B"))
        app.action_bar.setText(_translate("MainWindow", "条形图"))
        app.action_bar.setShortcut(_translate("MainWindow", "Alt+P"))
        app.action_menu_tree.setText(_translate("MainWindow", "决策树"))
        app.action_menu_tree.setShortcut(_translate("MainWindow", "Alt+T"))
        app.action_roc.setText(_translate("MainWindow", "ROC曲线"))
        app.action_roc.setShortcut(_translate("MainWindow", "Alt+R"))
        app.action_menu_woe_iv.setText(_translate("MainWindow", "WOE&&IV"))
        app.action_menu_woe_iv.setShortcut(_translate("MainWindow", "Alt+W"))
        app.action_scorecard.setText(_translate("MainWindow", "评分卡"))
        app.action_scorecard.setShortcut(_translate("MainWindow", "Alt+S"))
        app.action_ks.setText(_translate("MainWindow", "KS值"))
        app.action_ks.setShortcut(_translate("MainWindow", "Alt+K"))
        app.action_officesite.setText(_translate("MainWindow", "官方网站"))
        app.action_update.setText(_translate("MainWindow", "检查更新"))
        app.action_help.setText(_translate("MainWindow", "帮助文档"))
        app.action_about.setText(_translate("MainWindow", "关于"))
        app.action.setText(_translate("MainWindow", "删除行"))
        app.action_2.setText(_translate("MainWindow", "删除列"))
        app.action_3.setText(_translate("MainWindow", "拆分列"))
        app.action_4.setText(_translate("MainWindow", "重新编码"))
        app.action_5.setText(_translate("MainWindow", "唯一值"))
        app.action_6.setText(_translate("MainWindow", "数据角色"))
        app.action_menu_database.setText(_translate("MainWindow", "从数据库导入"))
        app.action_menu_quick_exit.setText(_translate("MainWindow", "快速退出"))
        app.action_menu_quick_exit.setShortcut(
            _translate("MainWindow", "Alt+Shift+Q"))
        app.action_assess.setText(_translate("MainWindow", "评估"))
        app.action_assess.setToolTip(_translate("MainWindow", "评估"))
        app.action_menu_dataset.setText(_translate("MainWindow", "测试"))
        app.action_menu_dataset.setToolTip(_translate("MainWindow", "测试"))
        app.action_dataset_export.setText(_translate("MainWindow", "导出数据集"))
        app.action_dataset_export.setToolTip(_translate("MainWindow", "导出数据集"))
        app.action_dataset_rename.setText(_translate("MainWindow", "重命名"))
        app.action_dataset_rename.setToolTip(
            _translate("MainWindow", "重命名数据集"))
        app.action_menu_data_row_filter.setText(
            _translate("MainWindow", "行筛选"))
        app.action_menu_result.setText(_translate("MainWindow", "结果"))
        app.action_menu_sort.setText(_translate("MainWindow", "排序"))
        app.action_package_manager.setText(
            _translate("MainWindow", "Python包管理工具"))
        app.action_package_manager.setToolTip(
            _translate("MainWindow", "Python包管理工具"))
        app.action_jupyter_notebook.setText(
            _translate("MainWindow", "jupyter_notebook"))
        app.actionWindows.setText(_translate("MainWindow", "Windows"))
        app.actionFusion.setText(_translate("MainWindow", "Fusion"))
        app.actionQdarkstyle.setText(_translate("MainWindow", "QDarkStyle"))
        app.action_ipython.setText(_translate("MainWindow", "ipython"))
        app.action_7.setText(_translate("MainWindow", "直方图"))
        app.actionWindowsVista.setText(
            _translate("MainWindow", "WindowsVista"))
        app.action_hide_right.setText(_translate("MainWindow", "隐藏侧边栏"))
        app.action_hide_right.setToolTip(_translate("MainWindow", "隐藏侧边栏"))
        app.action_menu_workdir.setText(_translate("MainWindow", "工作区间"))
        app.action_menu_todolist.setText(_translate("MainWindow", "任务列表"))
        app.action_menu_toolbox.setText(_translate("MainWindow", "工具窗口"))
        app.action_minitray.setText(_translate("MainWindow", "最小化到托盘"))
        app.action_info.setText(_translate("MainWindow", "信息提示"))
        app.action_success.setText(_translate("MainWindow", "成功消息"))
        app.action_warning.setText(_translate("MainWindow", "警告消息"))
        app.action_error.setText(_translate("MainWindow", "错误消息"))


class PMToolBarTop(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent
        # app = self.main_window
        self.setObjectName("toolBar_left")

    def bind_events(self, app):
        self.addAction(app.action_menu_new)
        self.addAction(app.action_menu_open)
        self.addSeparator()
        self.addAction(app.action_menu_option)
        self.addAction(app.action_menu_import_file)
        self.addAction(app.action_menu_database)
        self.addAction(app.action_menu_sort)
        self.addAction(app.action_menu_data_filter)
        self.addAction(app.action_menu_data_merge_v)
        self.addAction(app.action_menu_data_merge_h)
        self.addAction(app.action_menu_result)
        self.addAction(app.action_menu_dataset)
        self.addAction(app.action_package_manager)
        self.addAction(app.action_ipython)
        self.addAction(app.action_jupyter_notebook)
        self.addAction(app.action_menu_quick_exit)
        self.addSeparator()
        self.addAction(app.action_hide_right)

        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "标准工具栏"))


class PMToolBarRight(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent

    def bind_events(self, app):
        _translate = QCoreApplication.translate
        self.setLayoutDirection(Qt.RightToLeft)
        self.setObjectName("toolBar_right")
        self.addAction(app.action_data)
        self.addAction(app.action_stats)
        self.addAction(app.action_plot)
        self.addAction(app.action_model)
        self.addAction(app.action_assess)
        self.addAction(app.action_ext)
        self.setWindowTitle(_translate("MainWindow", "分析工具栏"))


class PMStatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.setObjectName("statusBar")


if __name__ == '__main__':
    class TestWidget(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout()
            self.setLayout(layout)
            layout.addWidget(PMModernToolbar())
            layout.addWidget(QPushButton())


    app = QApplication(sys.argv)

    fname = None

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    form = TestWidget()
    form.show()
    app.exec_()
