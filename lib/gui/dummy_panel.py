import wx
import wx.adv

from ..i18n import _


class DummyPanelFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, None, wx.ID_ANY, _("Dummy Panel"), *args, **kwargs)

        self.SetWindowStyle(wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)

        main_panel = wx.Panel(self, wx.ID_ANY)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(main_panel, label=_("Dummy Panel"))
        title_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(title_font)
        main_sizer.Add(title, 0, wx.ALL | wx.ALIGN_CENTER, 20)

        description = wx.StaticText(
            main_panel,
            label=_("This is a dummy panel for testing purposes.")
        )
        description.Wrap(400)
        main_sizer.Add(description, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        self.dummy_button = wx.Button(main_panel, label=_("Click Me!"))
        self.dummy_button.Bind(wx.EVT_BUTTON, self.on_dummy_button_click)
        main_sizer.Add(self.dummy_button, 0, wx.ALL | wx.ALIGN_CENTER, 20)

        close_button = wx.Button(main_panel, wx.ID_CLOSE, _("Close"))
        close_button.Bind(wx.EVT_BUTTON, self.on_close)
        main_sizer.Add(close_button, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        main_panel.SetSizer(main_sizer)

        self.SetSizeHints(main_sizer.CalcMin())
        self.Layout()

    def on_dummy_button_click(self, event):
        """Show a dialog when the dummy button is clicked"""
        wx.MessageBox(
            _("Here could be something."),
            _("Dummy Panel"),
            wx.OK | wx.ICON_INFORMATION
        )

    def on_close(self, event):
        """Close the frame"""
        self.Close()
