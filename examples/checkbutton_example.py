import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class CheckButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CheckButton Demo")

        hbox = Gtk.Box(spacing=6, margin_start=10, margin_end=10,
                       margin_top=10, margin_bottom=10)
        self.set_child(hbox)

        button = Gtk.CheckButton.new_with_label("Button 1")
        button.connect("toggled", self.on_button_toggled, "1")
        hbox.append(button)

        button = Gtk.CheckButton.new_with_mnemonic("B_utton 2")
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
    win = CheckButtonWindow()
    win.connect("destroy", lambda b: app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
