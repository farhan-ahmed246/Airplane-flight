import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Airplane Ticket Registration",
    page_icon="✈",
    layout="centered"
)

st.title("✈ Airplane Ticket Registration")
st.markdown("---")

st.header("Flight Details")

flight_date = st.date_input(
    "Select Flight Date",
    min_value=date.today()
)

flight_day = flight_date.strftime("%A")

st.info(f"📆 Flight Day: **{flight_day}**")

st.markdown("---")
st.header("Ticket Registration")

num_travelers = st.number_input(
    "How many people are traveling?",
    min_value=1,
    max_value=100,
    step=1
)

st.markdown("---")

all_data = []

for i in range(1, int(num_travelers) + 1):
    st.subheader(f"Traveler {i} Information")

    name = st.text_input(
        f"Traveler {i} Name",
        key=f"name_{i}"
    )

    father = st.text_input(
        f"Traveler {i} Father Name",
        key=f"father_{i}"
    )

    fullname = st.text_input(
        f"Traveler {i} Full Name",
        key=f"fullname_{i}"
    )

    age_input = st.text_input(
        f"Traveler {i} Age",
        key=f"age_{i}"
    )

    valid = False

    if age_input:
        if age_input.isdigit():
            age = int(age_input)
            if age < 5:
                st.warning("⚠️ 5+ Years kids can enter the plane")
            else:
                valid = True
                st.success(f"Age entered: {age}", icon="✅")
        else:
            st.error("❌ Please enter a NUMBER")

    if name and father and fullname and valid:
        st.success("✅ You are selected")
        all_data.append({
            "Name": name,
            "Father Name": father,
            "Full Name": fullname,
            "Age": age,
            "Flight Date": flight_date,
            "Flight Day": flight_day
        })

    st.markdown("---")

if all_data:
    st.header("🎫 Registration Summary")
    st.table(all_data)
