#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "matrix.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_Display_clicked();

    void on_Transpose_clicked();

    void on_Det_clicked();

    void on_Rang_clicked();

    void on_lineEdit_5_editingFinished();

    void on_lineEdit_6_cursorPositionChanged(int arg1, int arg2);

private:
    Ui::MainWindow *ui;
    Matrix m;
};
#endif // MAINWINDOW_H
