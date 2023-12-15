/********************************************************************************
** Form generated from reading UI file 'tinterface.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TINTERFACE_H
#define UI_TINTERFACE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Tinterface
{
public:

    void setupUi(QWidget *Tinterface)
    {
        if (Tinterface->objectName().isEmpty())
            Tinterface->setObjectName(QString::fromUtf8("Tinterface"));
        Tinterface->resize(800, 600);

        retranslateUi(Tinterface);

        QMetaObject::connectSlotsByName(Tinterface);
    } // setupUi

    void retranslateUi(QWidget *Tinterface)
    {
        Tinterface->setWindowTitle(QCoreApplication::translate("Tinterface", "Tinterface", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Tinterface: public Ui_Tinterface {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TINTERFACE_H
