
from __future__ import annotations
# Minimal Kivy-UI; wird nur genutzt, wenn Kivy verfügbar ist.
def run_ui():
    try:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        from kivy.uix.label import Label
    except Exception as e:
        raise RuntimeError("Kivy nicht installiert – UI nicht verfügbar") from e

    from .thought_stream import ThoughtStream

    class AureliaApp(App):
        def build(self):
            self.stream = ThoughtStream()
            root = BoxLayout(orientation='vertical', padding=8, spacing=8)
            self.info = Label(text="Aurelia² – Gedanken teilen", size_hint_y=None, height=40)
            self.input = TextInput(hint_text="Schreibe einen Gedanken…", multiline=False)
            btn = Button(text="Speichern")
            btn.bind(on_press=self._save)
            root.add_widget(self.info)
            root.add_widget(self.input)
            root.add_widget(btn)
            return root

        def _save(self, *_):
            txt = (self.input.text or "").strip()
            if not txt:
                self.info.text = "Leerer Gedanke ignoriert."
                return
            self.stream.add(txt)
            self.info.text = "Gespeichert."
            self.input.text = ""

    AureliaApp().run()
