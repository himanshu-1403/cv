from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        opLabel = Label(size_hint_y = 0.75, font_size=50)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        griddd = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            griddd.add_widget(Button(text=symbol))

        clearOption = Button(text = 'Clear', size_hint_y=None, height=100)
        def print_button_text(instance):
            opLabel.text += instance.text
        for button in griddd.children[1:]:
            button.bind(on_press=print_button_text)
        def resize_label_text(label, new_height):
            label.fontsize = 0.5*label.height
        opLabel.bind(height=resize_label_text)

        def evaluate_result(instance):
            try:
                opLabel.text = str(eval(opLabel.text))
            except SyntaxError:
                opLabel.text = 'Python Syntax error!'
        griddd.children[0].bind(on_press=evaluate_result)

        def clear_label(instance):
            opLabel.text = " "
        clearOption.bind(on_press=clear_label)

        root.add_widget(opLabel)
        root.add_widget(griddd)
        root.add_widget(clearOption)
        return root
myApp().run()