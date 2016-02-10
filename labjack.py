# coding=utf-8
# Copyright 2016 VBS Inc. All rights reserved.
# Ауторска права 2016 ВБШ. Сва права заджана.

import u6
import time
from PyQt4 import QtGui

d = u6.U6()
d.configIO(NumberTimersEnabled=2)
d.getFeedback(u6.Timer0Config(8), u6.Timer1Config(8))
merenje_bool = True

QtGui.QMessageBox.information(None, "Empty Field",
                              "Please enter a name and address.")
while merenje_bool:
    print(d.getFeedback(u6.QuadratureInputTimer()))
    time.sleep(0.015)
