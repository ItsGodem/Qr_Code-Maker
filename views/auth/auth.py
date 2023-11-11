
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock, mainthread
from kivy.uix.modalview import ModalView
from app.users import *
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty,ObjectProperty
import shutil as sh
import os as o
Builder.load_file('views/auth/auth.kv')
import qrcode
class Auth(BoxLayout):
    qrpath=StringProperty('api/img/Qr_Code.png')
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    def save(self):
        s=Savefile()
        s.open()
        s.save = self.save2
    def convert(self):
        teqr =self.ids.text_qr.text   
        if len(teqr)>0:
            qr = qrcode.make(teqr)
            with open('api/qrcodename.txt','r') as text:
                a =text.readline()
                qr.save('api/img/'+'Qr_Code'+a+'.png')  
                self.qrpath = 'api/img/'+'Qr_Code'+a+'.png'
                with open('api/qrcodename.txt','w') as text1:
                    text1.write(str(int(a)+1))
        else:
            self.ids.text_qr.text    = 'write a text here'
    def save2(self, tex):
        a = self.qrpath.replace('api/img','')
        sh.copyfile(self.qrpath,tex+a)
class Savefile(ModalView):
    save=ObjectProperty(allownone=True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
