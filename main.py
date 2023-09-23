from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.logger import Logger
from fomular import *


class FunctionScreen(Screen):
    def __init__(self, **kwargs):
        super(FunctionScreen, self).__init__(**kwargs)

        label_1 = Label(text = "Choose yourfomular to calculate:")

        self.btn_1 = Button(text='Ax^2 + Bx - C')
        self.btn_1.on_press = self.first_fomular

        self.btn_2 = Button(text='x^2 + 2Ax + A^2 = 0')
        self.btn_2.on_press = self.second_fomular

        self.btn_3 = Button(text='x^2 - 2Ax + A^2 = 0')
        self.btn_3.on_press = self.third_fomular

        self.btn_4 = Button(text='(Ax + B)^2 * (Ax - B)^2 = 0')
        self.btn_4.on_press = self.fourth_fomular

        self.btn_5 = Button(text='(Ax + B)^3 = 0')
        self.btn_5.on_press = self.fifth_fomular

        self.btn_6 = Button(text='(Ax - B)^3 = 0')
        self.btn_6.on_press = self.sixth_fomular

        self.btn_7 = Button(text='Ax^3 - B^3 = 0')
        self.btn_7.on_press = self.seventh_fomular



        layout_1 = BoxLayout(orientation='vertical', padding = 8, spacing =8)

        layout_1.add_widget(label_1)
        layout_1.add_widget(self.btn_1)
        layout_1.add_widget(self.btn_2)
        layout_1.add_widget(self.btn_3)
        layout_1.add_widget(self.btn_4)
        layout_1.add_widget(self.btn_5)
        layout_1.add_widget(self.btn_6)
        layout_1.add_widget(self.btn_7)


        self.add_widget(layout_1)

    def first_fomular(self):    

        self.fomular = "first"
        self.manager.current = "inputscreen"

    
    def second_fomular(self):
        self.fomular = "second"
        self.manager.current = "inputscreen"
        App.get_running_app().selected_formula = self.fomular


    def third_fomular(self):
        self.fomular = "third"
        App.get_running_app().selected_formula = self.fomular
        self.manager.current = "inputscreen"

    def fourth_fomular(self):

        self.fomular = "fourth"
        App.get_running_app().selected_formula = self.fomular
        self.manager.current = "inputscreen"

    def fifth_fomular(self):
        self.fomular = "fifth"
        App.get_running_app().selected_formula = self.fomular
        self.manager.current = "inputscreen"


    def sixth_fomular(self):
        self.fomular = "sixth"
        App.get_running_app().selected_formula = self.fomular
        self.manager.current = "inputscreen"

    def seventh_fomular(self):
       
        self.formula = "seventh"
        App.get_running_app().selected_formula = self.fomular
        self.manager.current = "inputscreen"







class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        
        self.calulate_btn = Button(text="Calculate")
        self.calulate_btn.on_press = self.calculate

        layout_1 = BoxLayout(orientation="vertical", padding = 8 , spacing = 8)

        self.a_label = Label(text ="Enter the number for A:")
        self.a_inp = TextInput(multiline=False)

        self.b_label = Label(text ="Enter the number for B:")
        self.b_inp = TextInput(multiline=False)

        self.c_label = Label(text ="Enter the number for C:")
        self.c_inp = TextInput(multiline=False)

        layout_1.add_widget(self.a_label)
        layout_1.add_widget(self.a_inp)

        layout_1.add_widget(self.b_label)
        layout_1.add_widget(self.b_inp)

        layout_1.add_widget(self.c_label)
        layout_1.add_widget(self.c_inp)


        layout_1.add_widget(self.calulate_btn)
        self.add_widget(layout_1)

    def calculate(self):
        a = float(self.a_inp.text)
        b = float(self.b_inp.text)
        c = float(self.c_inp.text)

        selected_formula = App.get_running_app().selected_formula
        Logger.info(f"fomular {selected_formula}")

        self.ans = ""

        if selected_formula == "first":
            self.ans = solution1(a, b, c)
        elif selected_formula == "second":
            self.ans = solution2(a)
        elif selected_formula == "third":
            self.ans = solution3(a)
        elif selected_formula == "fourth":
            self.ans = solution4(a, b)
        elif selected_formula == "fifth":
            self.ans = solution5(a, b)
        elif selected_formula == "sixth":
            self.ans = solution6(a, b)
        elif selected_formula == "seventh":
            self.ans = solution7(a, b)
        
        App.get_running_app().ans = self.ans
        self.manager.get_screen("calculate")
        self.manager.current = "calculate"

class CalculateScreen(Screen):

    def __init__(self, **kwargs):
        super(CalculateScreen, self).__init__(**kwargs)

        label_ans = Label(text = "The result for the question is:")
        
        self.label_result = Label(text = App.get_running_app().ans)

        self.again_btn = Button(text = "Another calculation")
        self.again_btn.on_press = self.choose_formula

        outer = BoxLayout(orientation="vertical", padding= 8, spacing = 8)
        outer.add_widget(label_ans)
        outer.add_widget(self.label_result)

        self.add_widget(outer)
        
    
        

    def choose_formula(self):
        self.manager.current = "function"

 
 


class Application(App):
    selected_formula = ""
    ans = ""
    def build(self):
        self.root = ScreenManager()
        self.function_screen = FunctionScreen()
        self.input_screen = InputScreen()
        self.calculate_results = CalculateScreen()
        self.root.add_widget(FunctionScreen(name = "function"))
        self.root.add_widget(InputScreen(name = "inputscreen"))
        self.root.add_widget(CalculateScreen(name = "calculate"))
        return self.root
    
app = Application()
app.run()