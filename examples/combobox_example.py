import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ComboBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ComboBox Example")

        name_store = Gtk.ListStore(int, str)
        name_store.append([1, "Billy Bob"])
        name_store.append([11, "Billy Bob Junior"])
        name_store.append([12, "Sue Bob"])
        name_store.append([2, "Joey Jojo"])
        name_store.append([3, "Rob McRoberts"])
        name_store.append([31, "Xavier McRoberts"])

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6,
                       margin_start=10, margin_end=10, margin_top=10, margin_bottom=10)

        name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
        name_combo.connect("changed", self.on_name_combo_changed)
        name_combo.set_entry_text_column(1)
        vbox.append(name_combo)

        country_store = Gtk.ListStore(str)
        countries = [
            "Austria",
            "Brazil",
            "Belgium",
            "France",
            "Germany",
            "Switzerland",
            "United Kingdom",
            "United States of America",
            "Uruguay",
        ]
        for country in countries:
            country_store.append([country])

        country_combo = Gtk.ComboBox.new_with_model(country_store)
        country_combo.connect("changed", self.on_country_combo_changed)
        renderer_text = Gtk.CellRendererText()
        country_combo.pack_start(renderer_text, True)
        country_combo.add_attribute(renderer_text, "text", 0)
        vbox.append(country_combo)

        currencies = [
            "Euro",
            "US Dollars",
            "British Pound",
            "Japanese Yen",
            "Russian Ruble",
            "Mexican peso",
            "Swiss franc",
        ]
        currency_combo = Gtk.ComboBoxText()
        currency_combo.set_entry_text_column(0)
        currency_combo.connect("changed", self.on_currency_combo_changed)
        for currency in currencies:
            currency_combo.append_text(currency)

        currency_combo.set_active(0)
        vbox.append(currency_combo)

        self.set_child(vbox)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            country = model[tree_iter][0]
            print("Selected: country=%s" % country)

    def on_currency_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            print("Selected: currency=%s" % text)


def on_activate(app):
    win = ComboBoxWindow()
    win.connect("destroy", lambda b: app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
