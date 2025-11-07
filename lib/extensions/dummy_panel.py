import wx
from ..gui.dummy_panel import DummyPanelFrame
from ..i18n import _
from .base import InkstitchExtension


class DummyPanel(InkstitchExtension):

    def effect(self) -> None:
        app = wx.App()
        frame = DummyPanelFrame()
        frame.Show()
        app.MainLoop()
