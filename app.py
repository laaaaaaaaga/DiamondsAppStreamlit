import numpy as np
import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()
# import

#filename = "model.pkl"
#model=pickle.load(open(filename, 'rb'))

#encoderfile = "ordinal_encoder.pkl"
#encoder=pickle.load(open(encoderfile,'rb'))

#scalerfile = "scaler.pkl"
#scaler=pickle.load(open(scalerfile,'rb'))

color_d = {0: "D", 1: "E",2: "F", 3: "G",4: "H", 5: "I"}
cut_d = {0: "Ideal", 1: "Premium",2: "Very_Good", 3: "Good",4: "Fair"}
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
        cut_radio = st.radio("Cięcie", list(cut_d.keys()), index=0, format_func=lambda x:cut_d[x],horizontal=True)
        color_radio = st.radio("Kolor", list(color_d.keys()), index=1, format_func=lambda x:color_d[x], horizontal=True)
        clarity_radio = st.radio("Przejrzystość", list(clarity_d.keys()), index=2, format_func=lambda x:clarity_d[x])
        carat_slider = st.slider("Karaty", value=1.00, min_value=0.50, max_value=3.00)
    with right:
        depth_slider = st.slider("Głębia", min_value=55.00, max_value=65.00, value=60.00, step = 0.01)
        table_slider = st.slider("Tabela", min_value=43.00, max_value=95.00, value =64.00 )
        x_slider = st.slider("x", min_value=1.00, max_value=10.00, value=5.00)
        y_slider = st.slider("y", min_value=1.00, max_value=10.00, value=5.00)
        z_slider = st.slider("z", min_value=1.00, max_value=6.00, value=3.00)

    data = np.array([carat_slider,cut_radio,color_radio,clarity_radio,depth_slider,table_slider,x_slider,y_slider,z_slider])
    data = data.reshape(1,-1)
    #    data = np.array([])
    #    data = data.reshape(-1,1)
#    survival = model.predict(data)
#   s_confidence = model.predict_proba(data)

#    with prediction:
#        st.header("sugerowany koszt diamentu to: {0}".format("Tak" if survival[0] == 1 else "Nie"))
#        st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))


if __name__ == "__main__":
    main()