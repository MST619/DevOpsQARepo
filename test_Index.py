from inspect import indentsize
from os import error
import pytest
import Index

gameGridList = []

@pytest.mark.parametrize("xAxis, yAxis, expectedprint",
                        [("4", "4", "    A     B     C     D\n"+
                    " " + "+-----+-----+-----+-----+\n" +
                "1|     |     |     |     |\n" +
                " " + "+-----+-----+-----+-----+\n" +
                "2|     |     |     |     |\n" +
                " " + "+-----+-----+-----+-----+\n" +
                "3|     |     |     |     |\n" +
                " " + "+-----+-----+-----+-----+\n" +
                "4|     |     |     |     |\n" +
                " " + "+-----+-----+-----+-----+\n")])
def test_gameGrid(capfd, xAxis, yAxis, expectedprint):
    Index.gameGrid(xAxis, yAxis)
    out, _ = capfd.readouterr()
    assert expectedprint in out

# def test_newGame(capfd, monkeypatch, gameGridList):
#     monkeypatch.setattr('builtins.input', lambda _: "27")
#     expected = "Invalid Input!\n\
# Please Select Game Ma Size\n\
# Enter in your desired map size width (Max:26)"
#     Index.newGame(gameGridList)
#     out, _ = capfd.readouterr()
#     assert out == expected



@pytest.mark.parametrize("input, expectedprint", 
                        [("27", "Invalid Input!\n\n" +
                        "Please Select Game Map size\n" +
                        "Enter in your desired map size width (Max: 26)")])
def test_newGame(capfd, input, expectedprint):
    Index.newGame(input)
    out, _ = capfd.readouterr()
    assert expectedprint in out