#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent): QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    tmr = new QTimer(this); // Создание объекта класса QTimer и передаем адресс переменной
    tmr->setInterval(1000); // Задаем интервал таймера
    connect(tmr, SIGNAL(timeout()), this, SLOT(updateTime())); // Подключаем сигнал таймера к нашему слоту
    tmr->start(); // Запускаем таймер
    ui->TrackingButton->setEnabled(false);

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


}


void MainWindow::on_CheckFileButton_clicked()
{
    ui->TrackingButton->setEnabled(false);
    fileparser.FileContent(ui->CheckFileLine->text().toStdString());

    if (fileparser.Check() == 1)
    {
        QMessageBox msgBox;
        msgBox.setIcon(QMessageBox::Warning);
        msgBox.setWindowTitle("Ошибка");
        msgBox.setText("Не удалось открыть файл!");
        msgBox.exec();
    }
    if (fileparser.Check() == 0)
    {
        ui->TrackingButton->setEnabled(true);
    }
}

