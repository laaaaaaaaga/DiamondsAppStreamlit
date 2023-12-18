import numpy as np
import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()
# import znanych nam bibliotek

filename = "x"
# model = pickle.load(open(filename, 'rb'))
# otwieramy wcześniej wytrenowany model

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
        carat_slider = st.slider("Karaty", value=100, min_value=0, max_value=200)
        cut_slider = st.slider("Cięcie", min_value=0, max_value=17)
        color_slider = st.slider("Kolor", min_value=0, max_value=6)
        clarity_slider = st.slider("Przejrzystość", min_value=0, max_value=10, step=10, value=0)

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