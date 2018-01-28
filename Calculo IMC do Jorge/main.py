#coding: utf-8
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import  FloatLayout
Window.clearcolor = get_color_from_hex('#AFEEEE')
class Imc(FloatLayout):
    def limp(self):
        self.ids.peso.text=''
        self.ids.altura.text=''
        self.ids.resultado.text = '[size=40px][color=#293945][b]Resultado [/size][/color][/b]'
    def Cal(self):
        try:
            p = float(self.ids.peso.text)
            a =float(self.ids.altura.text)
            resp=p/a**2
            r=str("IMC: %.2f "%resp)
            if resp < 18.5:
                self.ids.resultado.text = '[size=40px][color=#FF0000][b]'+r+'abaixo do peso'+'[/size][/color][/b]'
            elif resp > 18.6 and resp < 24.9:
                self.ids.resultado.text = '[size=40px][color=#006400][b]' + r + 'peso ideal' + '[/size][/color][/b]'
            elif resp > 25.0 and resp < 29.9:
                self.ids.resultado.text = '[size=40px][color=#293945][b]' + r + 'levemente acima do peso' + '[/size][/color][/b]'
            elif resp > 30.0 and resp < 34.9:
                self.ids.resultado.text = '[size=40px][color=#FF0000][b]' + r + 'obesidade grau 1' + '[/size][/color][/b]'
            elif resp > 35.0 and resp < 39.9:
                self.ids.resultado.text = '[size=40px][color=#FF0000][b]' + r + 'obesidade severa' + '[/size][/color][/b]'
            elif resp > 40:
                self.ids.resultado.text = '[size=40px][color=#FF0000][b]' + r + 'obesidade morbida' + '[/size][/color][/b]'
            print(p,a)
        except:
            self.ids.resultado.text = '[size=30px][color=#FF0000][b]Digite apenas números e não utilize virgulas [/size][/color][/b]'
class HelloApp(App):
    def build(self):
        return Imc()
HelloApp().run()
