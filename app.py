import numpy as np
import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()
# import znanych nam bibliotek

filename = "x"
model = ""
# model = pickle.load(open(filename, 'rb'))
# otwieramy wcześniej wytrenowany model

color_d = {0: "D", 1: "E",2: "F", 3: "G",4: "H", 5: "I"}
cut_d = {0: "Ideal", 1: "Premium",2: "Very Good", 3: "Good",4: "Fair"}
clarity_d = {0: "SI1", 1: "SI2",2: "VS1", 3: "VS2",4: "VVS1", 5: "VVS2", 6: "I1", 7: "IF"}
def main():
    st.set_page_config(page_title="Koszt Diamentu?")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image(
        "https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/ab/Diamond_JE3_BE3.png/revision/latest?cb=20230924193138"
    )

    with overview:
        st.title("Ile te diaxy mają kosztować?")

    with left:
        cut_radio = st.radio("Cięcie", list(cut_d.keys()), index=0, format_func=lambda x:cut_d[x])
        color_slider = st.radio("Kolor", list(color_d.keys()), index=1, format_func=lambda x:color_d[x])
        clarity_slider = st.radio("Przejrzystość", list(clarity_d.keys()), index=2, format_func=lambda x:clarity_d[x])
        carat_slider = st.slider("Karaty", value=100, min_value=0, max_value=200)
    with right:
        depth_slider = st.slider("Głębia", min_value=0, max_value=500, step=10)
        table_slider = st.slider("Tabela", min_value=0, max_value=500, step=10)
        x_slider = st.slider("x", min_value=0, max_value=500, step=10)
        y_slider = st.slider("y", min_value=0, max_value=500, step=10)
        z_slider = st.slider("z", min_value=0, max_value=500, step=10)

    data = np.array([])
    data = data.reshape(1,-1)
    #    data = np.array([])
    #    data = data.reshape(-1,1)
    survival = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.header("sugerowany koszt diamentu to: {0}".format("Tak" if survival[0] == 1 else "Nie"))
        st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))


if __name__ == "__main__":
    main()