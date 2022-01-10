from os import error
import pytest
import gridDisplay

def test_boundaryLine(capfd):
    gridDisplay.boundaryLine()
    out, _ = capfd.readouterr()
    assert\
    ("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")\
    in out

def test_alphabetLine(capfd):
    gridDisplay.alphabetLine()
    out, _ = capfd.readouterr()
    assert\
    ("     A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W     X     Y     Z")\
    in out

#def test_gameGrid(capfd):
