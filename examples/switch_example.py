import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class SwitcherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Switch Demo")

        hbox = Gtk.Box(spacing=6, margin_start=10, margin_end=10,
                       margin_top=10, margin_bottom=10)
        self.set_child(hbox)

        switch = Gtk.Switch(hexpand=True)
        switch.connect("notify::active", self.on_switch_activated)
        switch.set_active(False)
        hbox.append(switch)

        switch = Gtk.Switch(hexpand=True)
        switch.connect("notify::active", self.on_switch_activated)
        switch.set_active(True)
        hbox.append(switch)

    def on_switch_activated(self, switch, gparam):
        if switch.get_active():
            state = "on"
        else:
            state = "off"
        print("Switch was turned", state)


def on_activate(app):
    win = SwitcherWindow()
    win.connect("destroy", app.quit)
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
