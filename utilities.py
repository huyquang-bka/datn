def QT_pointInRect(qpoint_, qrect):
    x1 = qrect.x()
    y1 = qrect.y()
    w = qrect.width()
    h = qrect.height()
    x2, y2 = x1 + w, y1 + h
    x = qpoint_.x()
    y = qpoint_.y()
    if (x1 < x and x < x2):
        if (y1 < y and y < y2):
            return True
    return False