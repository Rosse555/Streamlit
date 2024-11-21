import streamlit as st
import pandas as pd

table1=pd.DataFrame({"column1":[1,2,3],"column2":[4,5,6]})

st.title("Bienvenidos muchachos")
st.subheader("Curso de Python")
st.text("En este curso de bienvenida a Python vamos a mirar algunas consideraciones")
st.markdown("---")

st.latex(r"\ln x_{3}^{i d}=-\frac{\Delta_{m}H}{R}\left(\frac{T_{m}-T}{T_{m}T}\right)+\frac{\Delta C_{p}}{R}\left(\frac{T_{m}-T}{T}\right)-\frac{\Delta C p}{R}\ln\left(\frac{T_{m}}{T}\right)")

code="""
print("Hola Mundo")
def funct():
    return 0;"""
st.code(code,language="python")
st.write("## Pandas")
st.table(table1)
st.dataframe(table1)
st.image("1.png",caption="Paraboloide eliptico")
st.video("HUMAN.mp4")
state=st.checkbox("checkbox",value=True)
if state:
    st.write("Hi")
else:
    pass
radio_bnt = st.radio("Donde vive?",options=("Cali","Neiva"))
select = st.selectbox("Cúal es su carro favorito?",options=("Mazda","BMW"))
multi_select = st.multiselect("Cuál es su color favorito",options=("rojo","amarillo","azul"))
st.write(multi_select)
st.title("Suibir archivos")
st.markdown("___")
imagenes=st.file_uploader("suba una imagen",type=["png","jgj"],accept_multiple_files=True)
if imagenes is not None:
    for image in imagenes:
        st.imagen(image)


st.slider("Esto es un slider",min_value=5,max_value=200)

st.text_input("Entre su nombre")

st.text_area("resuma")

st.date_input("Entre su fecha de cumpleaños:")