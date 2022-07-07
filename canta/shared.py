# -*- coding: utf-8 -*-
# .

__project_name__ = 'Defter'
__author__ = 'Erdinç Yılmaz'
__date__ = '3/28/16'

import os
from uuid import uuid4

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap, QPainter, QBrush
from PySide6.QtWidgets import QGraphicsItem

DEFTER_KLASOR_ADRES = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEFTER_AYARLAR_DOSYA_ADRES = os.path.join(DEFTER_KLASOR_ADRES, "_ayarlar.ini")
DEFTER_AYARLAR_ARACLAR_DOSYA_ADRES = os.path.join(DEFTER_KLASOR_ADRES, "_ayarlar_araclar.ini")
DEFTER_ORG_NAME = "defter"
DEFTER_ORG_DOMAIN = "defter"
DEFTER_APP_NAME = "Defter"

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
def kim(kac_basamak):
    # veya str(uuid.uuid4())[:5] yerine uuid.uuid4().hex[:5]
    return uuid4().hex[:kac_basamak]


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


# ---------------------------------------------------------------------
def kutulu_arkaplan_olustur(widget, kareBoyutu=10):
    kb = kareBoyutu

    pMap = QPixmap(2 * kb, 2 * kb)
    p = QPainter(pMap)
    p.fillRect(0, 0, kb, kb, QColor(200, 200, 200))
    p.fillRect(kb, kb, kb, kb, QColor(210, 210, 210))
    p.fillRect(0, kb, kb, kb, QColor(190, 190, 190))
    p.fillRect(kb, 0, kb, kb, QColor(200, 200, 200))
    p.end()
    palette = widget.palette()
    palette.setBrush(widget.backgroundRole(), QBrush(pMap))
    widget.setAutoFillBackground(True)
    widget.setPalette(palette)
