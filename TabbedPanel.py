from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):

        tb = TabbedPanel(do_default_tab=True, tab_pos="top_left", default_tab_text="START MENU")

        gl = GridLayout(rows=1)
        gl.add_widget(Button(size_hint=(0.2, 0.1), text="default_tab Button 1"))
        gl.add_widget(Button(size_hint=(0.2, 0.1), text="default_tab Button 2"))
        gl.add_widget(Button(size_hint=(0.2, 0.1), text="default_tab Button 3"))
        tb.default_tab_content = gl

        tbi = TabbedPanelItem(text="1", background_color=[1, 0, 0, 1])
        tbi.add_widget(Label(text="я лэйбл"))
        tbi.add_widget(tbi)

        tbi2 = TabbedPanelItem(text="2", background_color=[0, 1, 0, 1])
        bl = BoxLayout()
        bl.add_widget(Button(text = 'кнопка 1'))
        bl.add_widget(Button(text = 'кнопка 2'))
        tbi2.add_widget(bl)
        tb.add_widget(tbi2)

        tbi3 = TabbedPanelItem(text="3", background_color=[0, 0, 1, 1])
        tbi3.add_widget(Button(size_hint = (0.2, 0.1), text = 'кнопка 3'))
        tb.add_widget(tbi3)

        return tb

if __name__ == '__main__':
    MyApp().run()