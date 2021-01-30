#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QString>
#include <QChar>
#include <QStringList>
#include <QFileDialog>
#include <QFile>
#include <QTextStream>
#include <QList>
#include <QRegExp>
#include <QDebug>

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


void MainWindow::on_inputFile_Button_clicked()
{
    QString fileName = QFileDialog::getOpenFileName(this, tr("Open File"), "C:/Users/Paul Nesbitt/Desktop", tr("Text files (*.txt)"));
    QFile file(fileName);

    if(!file.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        return;
    }

    int isValid = 0;
    QString passport;
    QTextStream in(&file);
    while(!in.atEnd())
    {
        QString line = in.readLine().trimmed();
        if(!line.isEmpty())
        {
            passport.append(" " + line);
            continue;
        }

        qDebug() << "----------------------------------------------------------";
        qDebug() << passport;

        bool birth_year = false;
        bool issue_year = false;
        bool expiration_year = false;
        bool height = false;
        bool hair_color = false;
        bool eye_color = false;
        bool passport_id = false;
        QStringList fields = passport.split(" ", Qt::SkipEmptyParts);
        foreach(QString part, fields)
        {
            QString field = part.split(":").at(0).trimmed();
            QString value = part.split(":").at(1).trimmed();

            if(field.compare("byr") == 0)
            {
                qDebug() << "Birth Year: " << value;
                birth_year = ((value.length() == 4) && (value.toInt() >= 1920) && (value.toInt() <= 2002));
                qDebug() << "Birth Year? " << birth_year;
            }
            else if(field.compare("iyr") == 0)
            {
                qDebug() << "Issue Year: " << value;
                issue_year = ((value.length() == 4) && (value.toInt() >= 2010) && (value.toInt() <= 2020));
                qDebug() << "Issue Year? " << issue_year;
            }
            else if(field.compare("eyr") == 0)
            {
                qDebug() << "Expiration Year: " << value;
                expiration_year = ((value.length() == 4) && (value.toInt() >= 2020) && (value.toInt() <= 2030));
                qDebug() << "Expiration Year? " << expiration_year;
            }
            else if(field.compare("hgt") == 0)
            {
                QString unit = value.right(2).trimmed();
                if(unit.compare("cm") == 0)
                {
                    int heightVal = value.left(value.indexOf('c')).toInt();
                    qDebug() << "Height: " << heightVal << ", Unit: " << unit;

                    height = ((heightVal >= 150) && (heightVal <= 193));
                    qDebug() << "Height? " << height;
                }
                else if(unit.compare("in") == 0)
                {
                    int heightVal = value.left(value.indexOf('i')).toInt();
                    qDebug() << "Height: " << heightVal << ", Unit: " << unit;

                    height = ((heightVal >= 59) && (heightVal <= 76));
                    qDebug() << "Height? " << height;
                }
                else
                {
                    height = false;
                    qDebug() << "Height? " << height;
                    continue;
                }
            }
            else if(field.compare("hcl") == 0)
            {
                if(value.at(0) != '#')
                {
                    hair_color = false;
                    qDebug() << "Hair Color? " << hair_color;
                    continue;
                }

                QString color = value.split("#", Qt::SkipEmptyParts).at(0).trimmed();
                qDebug() << "Color: " << color;
                if(color.length() != 6)
                {
                    hair_color = false;
                    qDebug() << "Hair Color? " << hair_color;
                    continue;
                }

                hair_color = color.contains(QRegExp("^[a-f0-9]{6}$"));
                qDebug() << "Hair Color? " << hair_color;
            }
            else if(field.compare("ecl") == 0)
            {
                eye_color = ((value.compare("amb") == 0) ||
                             (value.compare("blu") == 0) ||
                             (value.compare("brn") == 0) ||
                             (value.compare("gry") == 0) ||
                             (value.compare("grn") == 0) ||
                             (value.compare("hzl") == 0) ||
                             (value.compare("oth") == 0));
                qDebug() << "Eye Color? " << eye_color;
            }
            else if(field.compare("pid") == 0)
            {
                passport_id = value.contains(QRegExp("^[0-9]{9}$"));
                qDebug() << "PID? " << passport_id;
            }
            else
            {
                continue;
            }
        }

        if(birth_year && issue_year && expiration_year && height && hair_color && eye_color && passport_id)
        {
            isValid++;
        }

        qDebug() << "Is Valid? " << isValid;
        passport.clear();
    }

    qDebug() << "Is Valid (total)? " << isValid;
}

