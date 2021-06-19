import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


@Gtk.Template(filename="template_example.ui")
class Window1(Gtk.Window):
    __gtype_name__ = "window1"

    @Gtk.Template.Callback()
    def onDestroy(self, *args):
        self.get_application().quit()

    @Gtk.Template.Callback()
    def onButtonClicked(self, button):
        print("Hello World!")


def on_activate(app):
    window = Window1()
    app.add_window(window)
    window.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)
app.run(None)
