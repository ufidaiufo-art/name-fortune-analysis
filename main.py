from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from name_analysis import analyze_name, predict_fortune

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 背景色
        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        
        layout.bind(size=self.update_rect, pos=self.update_rect)
        
        # 标题
        title = Label(
            text='名字五行分析与运势预测',
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)
        
        # 名字输入
        input_layout = BoxLayout(orientation='horizontal', spacing=10)
        input_label = Label(
            text='输入姓名:',
            font_size=16,
            size_hint_x=0.3
        )
        self.name_input = TextInput(
            hint_text='请输入姓名',
            font_size=16,
            size_hint_x=0.7
        )
        input_layout.add_widget(input_label)
        input_layout.add_widget(self.name_input)
        layout.add_widget(input_layout)
        
        # 分析按钮
        analyze_button = Button(
            text='分析五行',
            font_size=16,
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.8, 1)
        )
        analyze_button.bind(on_press=self.analyze_name)
        layout.add_widget(analyze_button)
        
        # 预测按钮
        predict_button = Button(
            text='预测运势',
            font_size=16,
            size_hint_y=None,
            height=50,
            background_color=(0.4, 0.7, 0.4, 1)
        )
        predict_button.bind(on_press=self.predict_fortune)
        layout.add_widget(predict_button)
        
        # 结果显示
        self.result_label = Label(
            text='分析结果将显示在这里',
            font_size=14,
            halign='left',
            valign='top',
            size_hint_y=None,
            text_size=(self.width - 40, None)
        )
        
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.result_label)
        layout.add_widget(scroll_view)
        
        self.add_widget(layout)
    
    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos
        self.result_label.text_size = (instance.width - 40, None)
    
    def analyze_name(self, instance):
        name = self.name_input.text.strip()
        if not name:
            self.result_label.text = '请输入姓名'
            return
        
        result = analyze_name(name)
        self.result_label.text = result
    
    def predict_fortune(self, instance):
        name = self.name_input.text.strip()
        if not name:
            self.result_label.text = '请输入姓名'
            return
        
        result = predict_fortune(name)
        self.result_label.text = result

class NameFortuneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    NameFortuneApp().run()
