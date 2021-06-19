import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class DialogExample(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, title="My Dialog", transient_for=parent, modal=True)
        self.add_buttons(
            "_Cancel", Gtk.ResponseType.CANCEL, "_OK", Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)

        label = Gtk.Label(label="This is a dialog to display additional information")

        box = self.get_content_area()
        box.append(label)


class DialogWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dialog Example")

        button = Gtk.Button(label="Open dialog", margin_start=6,
                            margin_end=6, margin_top=6, margin_bottom=6)
        button.connect("clicked", self.on_button_clicked)

        self.set_child(button)

    def on_button_clicked(self, widget):
        dialog = DialogExample(self)

        dialog.connect("response", self.on_dialog_response)
        dialog.show()

    def on_dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            print("The OK button was clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("The Cancel button was clicked")

        dialog.destroy()


def on_activate(app):
    win = DialogWindow()
    win.connect("destroy", lambda b: app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
