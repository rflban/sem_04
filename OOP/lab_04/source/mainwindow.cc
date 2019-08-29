#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QTreeWidget>
#include "Canvas.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connectAll();

/*    for (int i = 0; i < 30; i++)*/
        /*ui->treeWidget->addTopLevelItem(new QTreeWidgetItem);*/


/*    for (int i = 0; i < 30; i++)*/
    //{
    //auto page = new QWidget();
    //page->setStyleSheet("background-color: #ff0000;");
    //ui->tabWidget->addTab(page, "Sanya");
    /*}*/

    canvas = new Canvas(this);
    ui->tabWidget->addTab(canvas, "Canvas");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::connectAll()
{
    connect(ui->actionImport, SIGNAL(triggered()), this, SLOT(importData()));
}

void MainWindow::importData()
{
    importDataTriggered();
    canvas->drawLine({500, 500}, {1000, 1000});
}
