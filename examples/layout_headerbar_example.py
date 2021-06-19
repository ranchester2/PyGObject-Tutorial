import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio


class HeaderBarWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HeaderBar Demo")
        self.set_default_size(400, 200)

        hb = Gtk.HeaderBar()
        hb.set_show_title_buttons(True)
        self.props.title = "HeaderBar example"
        self.set_titlebar(hb)

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon)
        button.set_child(image)
        hb.pack_end(button)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.add_css_class("linked")

        button = Gtk.Button()
        button.set_child(
            Gtk.Image.new_from_icon_name("pan-start-symbolic")
        )
        box.append(button)

        button = Gtk.Button()
        button = Gtk.Button.new_from_icon_name("pan-end-symbolic")
        box.append(button)

        hb.pack_start(box)

        self.set_child(Gtk.TextView(margin_start=10, margin_end=10,
                              margin_top=10, margin_bottom=10))


def on_activate(app):
    win = HeaderBarWindow()
    win.connect("destroy", lambda b : app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)
app.run(None)
