from kivy.config           import Config
Config.set('graphics', 'left', 0)
Config.set('graphics', 'top', 0)
#Config.set('graphics', 'Borderless', 1)
#Config.set('graphics', 'fullscreen', 1)
import kivy
import os
from kivy.app 					import App
from kivy.lang 					import Builder 
from kivy.uix.image 			import Image
from kivy.uix.label 			import Label
from kivy.core.audio 			import SoundLoader
from kivy.uix.gridlayout  		import GridLayout
from kivy.uix.floatlayout 		import FloatLayout
from kivy.uix.togglebutton 		import ToggleButton
from kivy.uix.button			import Button
from kivy.core.window     		import Window
from kivy.lib.osc				import oscAPI 
from kivy.clock					import Clock
from kivy.animation				import Animation
from kivy.properties			import NumericProperty

sub_current = 1
target = ''
uncover = 1
class TestApp(App):
	ip = '0.0.0.0'
	port = 5000 
	def build(self):
		self.layout = FloatLayout(orientation='vertical')
		self.wimg = Image(source = None)

		self.fw_btn =  Button(pos = (500, 50), size_hint = (.15, .2),
										 background_normal = './general/fw_btn.png',
										 background_down = './general/fw_btn_alt.png')
		self.bk_btn = Button(pos = (100, 50), size_hint = (.15, .2),
										 background_normal = './general/bk_btn.png',
										 background_down = './general/bk_btn_alt.png')
		self.cover = Image(source = './general/cover_default.png')
		self.btn3 =  ToggleButton(pos_hint = {'right': 1}, size_hint = (.2, .25),
										 background_normal = './general/speaker_off.png',
										 background_down = './general/speaker_on.png')

		self.layout.add_widget(self.cover)
		oscAPI.init()  
		oscid = oscAPI.listen(ipAddr=self.ip, port= self.port) 
		Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
		oscAPI.bind(oscid, self.cb_tok, '/1/tok')
		return self.layout
	def cb_tok(self, value, instance): 
		global target
		global uncover
		target = str(value[2])
		global sub_current
		sub_current = 1
		if self.btn3.state == 'down':
			self.sound.stop()
		else:
			pass
		self.sound = SoundLoader.load('./Data/'+target+'/audio.wav')
		self.btn1 =  ToggleButton(pos = (-5, 60),size_hint = (.1, .5),
										 background_normal = './general/tabs1.png',
										 background_down ='./Data/'+target+'/tab1.png',
										 group = 'tabs')
		self.btn2 =  ToggleButton(pos = (-5, 320), size_hint = (.1, .5),
										 background_normal = './general/tabs2.png',
										 background_down='./Data/'+target+'/tab2.png',
										 group = 'tabs')
		self.btn3 =  ToggleButton(pos_hint = {'right': 1}, size_hint = (.2, .25),
										 background_normal = './general/speaker_off.png',
										 background_down = './general/speaker_on.png')
		self.btn4 =  ToggleButton(pos = (0, 0), size = (1, 1),
										 background_normal = './Data/'+target+'/background.png',
										 background_down='./Data/'+target+'/background_alt.png')
		self.exit_btn = Button (pos = (-10, -10), size_hint = (.1, .15),
										 background_normal = './general/exit.png',
										 background_down = './general/exit_alt.png')

		self.btn1.bind(on_press=self.pressBtn)
		self.btn2.bind(on_press=self.pressBtn2)
		self.btn3.bind(on_press=self.pressBtn3)
		self.btn4.bind(on_press=self.pressBtn4)
		self.exit_btn.bind(on_release=self.pressExit)
		self.layout.add_widget(self.btn4)
		self.layout.add_widget(self.btn2)
		self.layout.add_widget(self.btn1)
		self.layout.add_widget(self.btn3)
		self.layout.add_widget(self.exit_btn)
		self.layout.remove_widget(self.fw_btn)
		self.layout.remove_widget(self.bk_btn)
		self.layout.remove_widget(self.wimg)
		if uncover == 1:
			self.layout.remove_widget(self.cover)
			uncover = 0
		else:
			pass
	def pressBtn(self, event):
		if self.btn1.state == 'down':
			self.btn1.size_hint =  (.95, 1.6)
			self.btn1.pos = (20, -250)
			self.btn2.size_hint = (.1, .5)
			self.btn2.pos = (-5, 320)
			self.wimg = Image(source = './Data/'+target+'/extra'+str(sub_current)+'.png',
									allow_stretch = True,
									size_hint_y = 0.5, size_hint_x = 0.5,
									pos = (165, 250))
			self.layout.add_widget(self.wimg)
			self.fw_btn.bind(on_press=self.pressFwBtn)
			self.bk_btn.bind(on_press=self.pressBkBtn)
			self.layout.add_widget(self.fw_btn)
			self.layout.add_widget(self.bk_btn)
		else:
			self.btn1.size_hint = (.1, .5)
			self.btn1.pos = (-5, 60)
			self.fw_btn.unbind(on_press=self.pressFwBtn)
			self.bk_btn.unbind(on_press=self.pressBkBtn)
			self.layout.remove_widget(self.wimg)
			self.layout.remove_widget(self.fw_btn)
			self.layout.remove_widget(self.bk_btn)
	def pressBtn2(self, event):
		if self.btn2.state == 'down':
			self.btn2.size_hint =  (.95, 1.6)
			self.btn2.pos = (20,-250)
			self.btn1.size_hint = (.1, .5)
			self.btn1.pos = (-5, 60)
			self.fw_btn.unbind(on_press=self.pressFwBtn)
			self.bk_btn.unbind(on_press=self.pressBkBtn)
			self.layout.remove_widget(self.wimg)
			self.layout.remove_widget(self.fw_btn)
			self.layout.remove_widget(self.bk_btn)
		else:
			self.btn2.size_hint = (.1, .5)
			self.btn2.pos = (-5, 320)
	def pressBtn3(self, event):
		if self.btn3.state == 'down':
			self.sound.play()
		else:
			self.sound.stop()
	def pressBtn4(self, event):
		pass
	def pressFwBtn(self, event):
		global sub_current
		sub_temp = './Data/'+target+'/extra'+str(sub_current+1)+'.png'
		if os.path.exists(sub_temp):
			self.fw_btn.background_down = './general/fw_btn_alt.png'
			self.wimg.source = sub_temp
			sub_current = sub_current+1
			print(sub_current)
		else:
			self.fw_btn.background_down = './general/fw_btn2.png'
	def pressBkBtn(self, event):
		global sub_current
		if sub_current-1 is not 0:
			self.bk_btn.background_down = './general/bk_btn_alt.png'
			self.wimg.source = './Data/'+target+'/extra'+str(sub_current-1)+'.png'
			sub_current = sub_current-1
			print(sub_current)
		else:
			self.bk_btn.background_down = './general/bk_btn2.png'
	def pressExit(self, event):
		self.cover = Image(source = './general/cover_default.png')
		self.layout.add_widget(self.cover)
		self.sound.stop()
		if self.btn1.state == 'down':
			self.layout.remove_widget(self.wimg)
			self.layout.remove_widget(self.fw_btn)
			self.layout.remove_widget(self.bk_btn)
		self.btn1.state = 'normal'
		self.btn1.size_hint = (.1, .5)
		self.btn1.pos = (-5, 60)
		self.btn2.state = 'normal'
		self.btn2.size_hint = (.1, .5)
		self.btn2.pos = (-5, 320)
		self.btn3.state = 'normal'
		self.btn4.state = 'normal'
		global sub_current
		global uncover
		sub_current = 1
		uncover = 1
TestApp().run()
