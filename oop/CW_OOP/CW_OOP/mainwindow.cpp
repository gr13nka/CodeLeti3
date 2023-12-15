#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent): QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    tmr = new QTimer(this); // Создание объекта класса QTimer и передаем адресс переменной
    tmr->setInterval(1000); // Задаем интервал таймера
    connect(tmr, SIGNAL(timeout()), this, SLOT(updateTime())); // Подключаем сигнал таймера к нашему слоту
    tmr->start(); // Запускаем таймер

}

MainWindow::~MainWindow()
{
    delete ui;
    delete tmr;
}

void MainWindow::updateTime()
{
    ui->label->setText(QTime::currentTime().toString());
}

void MainWindow::on_TrackingButton_clicked()
{
    QTime sperma = QTime::currentTime();
    std::cout << (QTime::currentTime().toString().toStdString()) << "\n";

}

