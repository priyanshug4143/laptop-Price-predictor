import streamlit  as st
import pickle
import numpy as np
pipe=pickle.load(open("pipe.pkl","rb"))
df=pickle.load(open("df.pkl","rb"))


st.title("Laptop Price Predictor")

#brand
company=st.selectbox("Brand", df["Company"].unique())

#type of laptop
type=st.selectbox("Type of laptop",df["TypeName"].unique())

#Ram
ram=st.selectbox("Ram",[2,4,6,8,12,16,24,32,64])

#Weight
weight=st.number_input("Weight of the laptop")

#Touchsecreen
touchscreen=st.selectbox("TouchScreen",["Yes","NO"])

#ips'
ips=st.selectbox("IPS",["YES","No"])

screen_size=st.number_input("Screen Size")

#Resoltution
resolution=st.selectbox("ScreenResolution",["1920*1080","1366*768","1600*900","3840*2160","3200*1800","2880*1800"
                                                                                           "2560*1600"])

cpu=st.selectbox("CPU",df["CPU Brand"].unique())

hdd=st.selectbox("HDD in(GB",[0,128,256,512,1024,2048])

ssd=st.selectbox("SSD in(GB",[0,8,128,256,512,1024,1024])

Gpu=st.selectbox("GPU",df["GPU Brand"].unique())

os=st.selectbox("OS",df["OS"].unique())

if st.button("Predict Price"):
    ppi=None
    if touchscreen== "Yes":
        touchscreen=1
    else :
        touchscreen=0

    if ips=="Yes":
        ips=1
    else:
        ips=0

    x_res=int(resolution.split("*")[0])
    y_res=int(resolution.split("*")[1])
    ppi=((x_res**2)+(y_res**2))**0.5/screen_size

    quary=np.array([company,type,ram,weight,touchscreen,ips,ppi,hdd,ssd,Gpu,os,cpu])

    quary=quary.reshape(1,12)
    st.title("The Predicted Price For this Configuration is "+str(int(np.exp(pipe.predict(quary)[0]))))