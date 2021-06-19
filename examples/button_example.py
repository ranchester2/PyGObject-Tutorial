import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Button Demo")
        hbox = Gtk.Box(spacing=6, margin_start=10, margin_end=10,
                       margin_top=10, margin_bottom=10)
        self.set_child(hbox)

        button = Gtk.Button(label="Click Me", hexpand=True)
        button.connect("clicked", self.on_click_me_clicked)
        hbox.append(button)

        button = Gtk.Button(label="_Open", use_underline=True, hexpand=True)
        button.connect("clicked", self.on_open_clicked)
        hbox.append(button)

        button = Gtk.Button(label="_Close", use_underline=True, hexpand=True)
        button.connect("clicked", self.on_close_clicked)
        hbox.append(button)

    def on_click_me_clicked(self, button):
        print('"Click me" button was clicked')

    def on_open_clicked(self, button):
        print('"Open" button was clicked')

    def on_close_clicked(self, button):
        print("Closing application")
        self.get_application().quit()


def on_activate(app):
    win = ButtonWindow()
    win.connect("destroy", app.quit)
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
