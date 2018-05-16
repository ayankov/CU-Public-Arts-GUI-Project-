from kivy.config import Config
Config.set('graphics','fullscreen','auto')

from kivy.garden.mapview import MapView, MapMarker#, MapLayer
from kivy.app import App
from kivy.properties     import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter    import Scatter
from kivy.uix.image      import Image
from kivy.uix.bubble import Bubble
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lib.osc         import oscAPI
from kivy.garden.tei_knob import  Knob
from kivy.uix.popup     import Popup

#Alexei :
class MyKnob(Knob):
    # Object property that receives the image
    obj = ObjectProperty()

    # on_knob is called if value, token_id or token_placed change
    def on_knob(self, value, pattern_id):
        angle = value
        zoomVal = int(angle)/10
        if zoomVal > 8:
            if zoomVal < 30:
                self.obj.zoom = zoomVal
            else:
                pass
        else:
            pass
        
    def on_token_placed(self, instance, value):
        print "token Placed: " + str(value)
        print str(self.obj.zoom)


class MapViewApp(App):
 #Li   
    ip = '127.0.0.1'   # Receiver ip
    port = 5000        # Receiver port
    def build(self):
        oscAPI.init()
        layout = FloatLayout(orientation='vertical')
        self.mapview = MapView(zoom=15, lat=34.676087, lon = -82.836105)
        a=Label(text='a',font_size='20sp')

        self.m1 = MapMarker(zoom=1,lat=34.675195,lon=-82.83246, source = 'Genus.png')
        self.m1.bind(on_press=self.pressBtn1)
        self.m1.bind(on_release=self.releaseBtn1)
        self.m2 = MapMarker(zoom=1,lat=34.675370,lon=-82.839192, source = 'Flyer_Icon.png')
        self.m2.bind(on_press=self.pressBtn2)
        self.m2.bind(on_release=self.releaseBtn1)        
        self.m3 = MapMarker(zoom=1,lat=34.675838,lon=-82.823200, source = 'Ontogeny.png')                        
        self.m3.bind(on_press=self.pressBtn3)
        self.m3.bind(on_release=self.releaseBtn1)
        self.m4 = MapMarker(zoom=1,lat=34.675704,lon=-82.836138, source = 'P211.png')
        self.m4.bind(on_press=self.pressBtn4)
        self.m4.bind(on_release=self.releaseBtn1)
        self.m5 = MapMarker(zoom=1,lat=34.672836,lon=-82.840756, source = 'Shift.png')
        self.m5.bind(on_press=self.pressBtn5)
        self.m5.bind(on_release=self.releaseBtn1)
        self.m6 = MapMarker(zoom=1,lat=34.678795,lon=-82.843013, source = 'Six.png')
        self.m6.bind(on_press=self.pressBtn6)
        self.m6.bind(on_release=self.releaseBtn1)
        self.m7 = MapMarker(zoom=1,lat=34.676791,lon=-82.840032, source = 'Spiral.png')
        self.m7.bind(on_press=self.pressBtn7)
        self.m7.bind(on_release=self.releaseBtn1)
        self.m8 = MapMarker(zoom=1,lat=34.679532,lon=-82.843674, source = 'Performing.png')
        self.m8.bind(on_press=self.pressBtn8)
        self.m8.bind(on_release=self.releaseBtn1)
        self.m9 = MapMarker(zoom=1,lat=34.678322,lon=-82.8235475, source = 'Three.png')
        self.m9.bind(on_press=self.pressBtn9)
        self.m9.bind(on_release=self.releaseBtn1)
    
        self.orange = (3.5, 1.53, 0, 0.75)
        self.purple = (1.28, 0, 1.28, 0.75)
        self.mapview.add_marker(self.m1)
        self.mapview.add_marker(self.m2)
        self.mapview.add_marker(self.m3)
        self.mapview.add_marker(self.m4)
        self.mapview.add_marker(self.m5)
        self.mapview.add_marker(self.m6)
        self.mapview.add_marker(self.m7)
        self.mapview.add_marker(self.m8)
        self.mapview.add_marker(self.m9)
#Alexei

        
        btn1 =  Button(text='Exterior'
                       ,background_color = self.orange
                       ,pos_hint = {'left': 0.55}
                       ,size_hint = (.1, .07)
                       , font_size=20)
        btn2 =  Button(text='Interior'
                       ,background_color = self.purple
                       ,pos = (200, 0)
                       ,size_hint = (.1, .07)
                       , font_size=20)
        btn3 =  Button(text='All'
                       ,background_color = self.orange
                       ,pos = (400, 0),
                     	size_hint = (.1, .07)
                       , font_size=20)
        btn4 =  Button(text='Center'
                       ,background_color = self.purple
                       ,pos = (600, 0),
                     	size_hint = (.1, .07)
                       , font_size=20)
        


        btn1.bind(on_press=self.pressBtn1a)
        btn1.bind(on_release=self.releaseBtn1a)

        btn2.bind(on_press=self.pressBtn2a)
        btn2.bind(on_release=self.releaseBtn2a)

        btn3.bind(on_press=self.pressBtn3a)
        btn3.bind(on_release=self.releaseBtn3a)

        btn4.bind(on_press=self.pressBtn4a)
        btn4.bind(on_release=self.releaseBtn4a)
        
        knob = MyKnob(pos_hint = {'right': 1},
                         size = (200, 200),
                         min = 0, max = 250,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob_metal.png",
                         marker_img = "bline3.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = self.mapview
                      )
        
        layout.add_widget(self.mapview)
        layout.add_widget(knob)
	layout.add_widget(btn3)
	layout.add_widget(btn1)
	layout.add_widget(btn2)
	layout.add_widget(btn4)


        return layout
    
#Li:     
    def pressBtn1(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['1'], 
                     ipAddr= self.ip, port= self.port)
        

    def releaseBtn1(self, event):
        print("Osc message sent")  
        print("button 1 released") 

    def pressBtn2(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['2'], 
                     ipAddr= self.ip, port= self.port)
                       
    def releaseBtn2(self, event):
        print("Osc message sent")  
        print("button 2 released")
                       
    def pressBtn3(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['3'], 
                     ipAddr= self.ip, port= self.port)
                       
    def releaseBtn3(self, event):
        print("Osc message sent")  
        print("button 3 released") 
    
    def pressBtn4(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['4'], 
                     ipAddr= self.ip, port= self.port)
                       
    def releaseBtn4(self, event):
        print("Osc message sent")  
        print("button 4 released") 
    
    def pressBtn5(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['5'], 
                     ipAddr= self.ip, port= self.port)
                           
    def releaseBtn5(self, event):
        print("Osc message sent")  
        print("button 5 released") 
    
    def pressBtn6(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['6'], 
                     ipAddr= self.ip, port= self.port)

                           
    def releaseBtn6(self, event):
        print("Osc message sent")  
        print("button 6 released") 
    
    def pressBtn7(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['7'], 
                     ipAddr= self.ip, port= self.port)
        
    def releaseBtn7(self, event):
        print("Osc message sent")  
        print("button 7 released") 
    
    def pressBtn8(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['8'], 
                     ipAddr= self.ip, port= self.port)
            
    def releaseBtn8(self, event):
        print("Osc message sent")  
        print("button 8 released")    
        
    def pressBtn9(self, event):
        print("button touched")   
        # Send OSC message
        oscAPI.sendMsg('/1/tok', ['9'], 
                     ipAddr= self.ip, port= self.port)
#Li and Alexei:          
    def releaseBtn9(self, event):
        print("Osc message sent")  
        print("button 9 released")

        # return the layout object
        return layout
    def pressBtn1a(self, event):
        # Print to console for debug purposes
        #self.purple = (1.28, 0, 1.28, 1)


        self.mapview.remove_marker(self.m1)
        self.mapview.remove_marker(self.m2)
        self.mapview.remove_marker(self.m3)
        self.mapview.remove_marker(self.m4)
        self.mapview.remove_marker(self.m5)
        self.mapview.remove_marker(self.m6)
        self.mapview.remove_marker(self.m7)
        self.mapview.remove_marker(self.m8)
        self.mapview.remove_marker(self.m9)   
        self.mapview.add_marker(self.m1)
        self.mapview.add_marker(self.m2)
        self.mapview.add_marker(self.m3)

        
        print("show internal markers")
   
    def releaseBtn1a(self, event):
        # Print to console for debug purposes
        print("button release")
        # Change button color
     
    def pressBtn2a(self, event):
        # Print to console for debug purposes
        print("show painting markers")
        # Change button color
        self.mapview.remove_marker(self.m1)
        self.mapview.remove_marker(self.m2)
        self.mapview.remove_marker(self.m3)
        self.mapview.remove_marker(self.m4)
        self.mapview.remove_marker(self.m5)
        self.mapview.remove_marker(self.m6)
        self.mapview.remove_marker(self.m7)
        self.mapview.remove_marker(self.m8)
        self.mapview.remove_marker(self.m9)
        self.mapview.add_marker(self.m4)
        self.mapview.add_marker(self.m5)
        self.mapview.add_marker(self.m7)
        self.mapview.add_marker(self.m8)
        self.mapview.add_marker(self.m9)
      
    def releaseBtn2a(self, event):
        # Print to console for debug purposes
        print("button release")
        # Change button color
    def pressBtn3a(self, event):
        # Print to console for debug purposes
        print("show external markers")
        self.mapview.remove_marker(self.m1)
        self.mapview.remove_marker(self.m2)
        self.mapview.remove_marker(self.m3)
        self.mapview.remove_marker(self.m4)
        self.mapview.remove_marker(self.m5)
        self.mapview.remove_marker(self.m6)
        self.mapview.remove_marker(self.m7)
        self.mapview.remove_marker(self.m8)
        self.mapview.remove_marker(self.m9)   
        self.mapview.add_marker(self.m1)
        self.mapview.add_marker(self.m2)
        self.mapview.add_marker(self.m3)
        self.mapview.add_marker(self.m4)
        self.mapview.add_marker(self.m5)
        self.mapview.add_marker(self.m6)
        self.mapview.add_marker(self.m7)
        self.mapview.add_marker(self.m8)
        self.mapview.add_marker(self.m9)
        # Change button color
        
    def releaseBtn3a(self, event):
        # Print to console for debug purposes
        print("button release")
        # Change button color

#Alexei:
        
    def pressBtn4a(self, event):
        # Print to console for debug purposes
        print("center")
        self.mapview.center_on(34.676087, -82.836105)
        # Change button color
        
    def releaseBtn4a(self, event):
        # Print to console for debug purposes
        print("button release")
        # Change button color


        
    
MapViewApp().run()
