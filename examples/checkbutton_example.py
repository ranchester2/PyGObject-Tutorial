import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class CheckButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CheckButton Demo")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, margin_start=10, margin_end=10,
                       margin_top=10, margin_bottom=10)
        self.set_child(vbox)

        ungrouped_hbox = Gtk.Box(spacing=6)

        button = Gtk.CheckButton.new_with_label("Button 1")
        button.connect("toggled", self.on_button_toggled, "1")
        ungrouped_hbox.append(button)

        button = Gtk.CheckButton.new_with_mnemonic("B_utton 2")
        button.set_active(True)
        button.connect("toggled", self.on_button_toggled, "2")
        ungrouped_hbox.append(button)

        vbox.append(ungrouped_hbox)

        grouped_hbox = Gtk.Box(spacing=6)

        grouped_button1 = Gtk.CheckButton.new_with_label("Grouped Button 1")
        grouped_button1.connect("toggled", self.on_button_toggled, "G1")
        grouped_hbox.append(grouped_button1)

        grouped_button2 = Gtk.CheckButton.new_with_label("Grouped Button 2")
        grouped_button2.set_active(True)
        grouped_button2.set_group(grouped_button1)
        grouped_button2.connect("toggled", self.on_button_toggled, "G2")
        grouped_hbox.append(grouped_button2)

        vbox.append(grouped_hbox)

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
