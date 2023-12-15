#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_Display_clicked()
{
   m.show_matrix();
}


void MainWindow::on_Transpose_clicked()
{
    m.transpose();
}


void MainWindow::on_Det_clicked()
{
    m.det();
}


void MainWindow::on_Rang_clicked()
{
    m.rang();
}


