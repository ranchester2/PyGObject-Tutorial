import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ToggleButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ToggleButton Demo")

        hbox = Gtk.Box(spacing=6, margin_start=10, margin_end=10,
                       margin_top=10, margin_bottom=10)
        self.set_child(hbox)

        button = Gtk.ToggleButton(label="Button 1", hexpand=True)
        button.connect("toggled", self.on_button_toggled, "1")
        hbox.append(button)

        button = Gtk.ToggleButton(
            label="B_utton 2", use_underline=True, hexpand=True
        )
        button.set_active(True)
        button.connect("toggled", self.on_button_toggled, "2")
        hbox.append(button)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)


def on_activate(app):
    win = ToggleButtonWindow()
    win.connect("destroy", lambda b: app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
