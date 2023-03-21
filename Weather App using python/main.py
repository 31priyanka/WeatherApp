import tkinter as tk
import requests
from PIL import Image, ImageTk

root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")

#Key=f22b0bba326e8e1eeb05a675f7f00eb3
#api url=https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#API URL=api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City: %s\nCondition: %s\nTemperature: %s'%(city,condition,temp)
    except:
        final_str='There was a problem retriving that information'
    return final_str


def get_weather(city):
    weather_key='f22b0bba326e8e1eeb05a675f7f00eb3'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    #sending req to server to get the data from server
    response=requests.get(url,params)
    #print(response.json())
    weather=response.json()
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

    result['text']=format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon_name):
    size=int


img=Image.open('download.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text='Earth including over 200000 cities!',fg='red',font=('times new roman',19,'bold'))
heading_title.place(x=80,y=15)


frame_one=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=460,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=15)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='Get weather',fg='green',font=('times new roman',15,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=8)

frame_two=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=120,width=460,height=350)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)






root.mainloop()
