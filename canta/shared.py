# -*- coding: utf-8 -*-
# .

__project_name__ = 'Defter'
__author__ = 'argekod'
__date__ = '3/28/16'

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsItem

renk_degismis_nesne_yazi_rengi = QColor(232, 50, 120)
# renk_degismis_nesne_yazi_rengi = QColor(0,0,255)
renk_kirmizi = QColor(Qt.red)
renk_siyah = QColor(Qt.black)
renk_mavi = QColor(Qt.blue)
activeItemLineColor = QColor(Qt.red)

# bunlarin degerleri degismesin, cunku nesneler kaydedilirken bu degerler de kaydediliyor.
# sonra eski dosyalar acilmaz, degisiklik yapilirsa
userType = QGraphicsItem.UserType
BASE_ITEM_TYPE = userType + 1
RECT_ITEM_TYPE = userType + 2
ELLIPSE_ITEM_TYPE = userType + 3
IMAGE_ITEM_TYPE = userType + 4
PATH_ITEM_TYPE = userType + 5
TEXT_ITEM_TYPE = userType + 6
WEB_ITEM_TYPE = userType + 7
VIDEO_ITEM_TYPE = userType + 8
GROUP_ITEM_TYPE = userType + 9
MIRRORLINE_TYPE = userType + 10
TEMP_TEXT_ITEM_TYPE = userType + 11
KUTUPHANE_NESNESI = userType + 12
LINE_ITEM_TYPE = userType + 13
DOSYA_ITEM_TYPE = userType + 14
YUVARLAK_FIRCA_BOYUTU_ITEM_TYPE = userType + 15


# ---------------------------------------------------------------------
def unicode_to_bool(what):
    if what == "false" or what is False:
        return 0
    elif what == "true" or what is True:
        return 1


# ---------------------------------------------------------------------
def calculate_alpha(delta, col):
    alpha = col.alpha()

    if delta > 0:
        if alpha + 10 < 256:
            col.setAlpha(alpha + 10)
        else:
            col.setAlpha(255)
    else:
        if alpha - 10 > 0:
            col.setAlpha(alpha - 10)
        else:
            col.setAlpha(0)

    return col
    # return QColor().fromRgb(col.red(), col.green(),col.blue(),col.alpha())
