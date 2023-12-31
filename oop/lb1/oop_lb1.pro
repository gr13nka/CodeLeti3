QT -= gui

CONFIG += c++11 console
CONFIG -= app_bundle
LIBS += -L/usr/include -lncurses
QMAKE_CXXFLAGS += -lncurses
QMAKE_CXXFLAGS_DEBUG += -lncurses
# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
        application.cpp \
        main.cpp \
        matrix.cpp

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    oop_lb1.pro.user

HEADERS += \
    application.h \
    matrix.h \
    number.h
