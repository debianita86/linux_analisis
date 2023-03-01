from kivy.uix.boxlayout import BoxLayout
from librerias.sysinfo import SysInfo
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.app import App
from kivy.clock import Clock

class Linux_Practice(App):
    def build(self):
        self.miLibreria = SysInfo()
        self.bl1 = BoxLayout(orientation="vertical")
        self.bl2 = BoxLayout(orientation="horizontal")
        self.lbl1 = Label(text="My Linux analitics App")
        self.btn1 = Button(text="Sys info")
        self.btn2 = Button(text="Temperatura")
        self.btn3 = Button(text="About me")
        self.lbl2  = Label(text=" ")
        self.bl2.add_widget(self.btn1)
        self.bl2.add_widget(self.btn2)
        self.bl2.add_widget(self.btn3)
        self.bl1.add_widget(self.lbl1)
        self.bl1.add_widget(self.bl2)
        self.bl1.add_widget(self.lbl2)
        self.btn1.bind(on_press=self.acciones_btn1)
        self.btn2.bind(on_press=self.acciones_btn2)
        self.btn3.bind(on_press=self.acciones_btn3)
        return self.bl1
    
    def acciones_btn3(self, *args):
        self.detieneRelojes()
        salida = "Diego Parra \n aparra@institutoi3.edu.co \n 3108673000"
        self.lbl2.text=salida
        
    def acciones_btn1(self, *args):
        self.detieneRelojes()
        Clock.schedule_interval(self.reloj1, 1)
    
    def acciones_btn2(self, *args):
        self.detieneRelojes()
        salida = self.miLibreria.temperatura()
        self.lbl2.text= salida

    
    def reloj1(self, dt):
        textoSalida = self.miLibreria.fecha_hora() +"\n" + self.miLibreria.host_name() + "\n"+ self.miLibreria.Ram()
        self.lbl2.text = textoSalida
    
    def detieneRelojes(self):
        Clock.unschedule(self.reloj1)

if __name__ == "__main__":
    Linux_Practice().run()