import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Hello World")
        vbox.append(self.entry)

        hbox = Gtk.Box(spacing=6, vexpand=True)
        vbox.append(hbox)

        self.check_editable = Gtk.CheckButton(label="Editable", hexpand=True)
        self.check_editable.connect("toggled", self.on_editable_toggled)
        self.check_editable.set_active(True)
        hbox.append(self.check_editable)

        self.check_visible = Gtk.CheckButton(label="Visible", hexpand=True)
        self.check_visible.connect("toggled", self.on_visible_toggled)
        self.check_visible.set_active(True)
        hbox.append(self.check_visible)

        self.pulse = Gtk.CheckButton(label="Pulse", hexpand=True)
        self.pulse.connect("toggled", self.on_pulse_toggled)
        self.pulse.set_active(False)
        hbox.append(self.pulse)

        self.icon = Gtk.CheckButton(label="Icon", hexpand=True)
        self.icon.connect("toggled", self.on_icon_toggled)
        self.icon.set_active(False)
        hbox.append(self.icon)

    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)

    def on_visible_toggled(self, button):
        value = button.get_active()
        self.entry.set_visibility(value)

    def on_pulse_toggled(self, button):
        if button.get_active():
            self.entry.set_progress_pulse_step(0.2)
            # Call self.do_pulse every 100 ms
            self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
        else:
            # Don't call self.do_pulse anymore
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
            self.entry.set_progress_pulse_step(0)

    def do_pulse(self, user_data):
        self.entry.progress_pulse()
        return True

    def on_icon_toggled(self, button):
        if button.get_active():
            icon_name = "system-search-symbolic"
        else:
            icon_name = None
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, icon_name)


def on_activate(app):
    win = EntryWindow()
    win.connect("destroy", lambda b : app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
