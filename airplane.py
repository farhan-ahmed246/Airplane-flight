import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Airplane Ticket Registration",
    page_icon="✈",
    layout="centered"
)

st.title("✈ Airplane Ticket Registration")
st.markdown("---")

st.header("👤 Passenger Registration")

# Number of travelers
num_travelers = st.number_input(
    "How many people are traveling?",
    min_value=1,
    max_value=100,
    step=1
)

st.markdown("---")

all_passengers = []

for i in range(1, int(num_travelers) + 1):
    st.subheader(f"Traveler {i}")

    name = st.text_input(
        f"Name",
        key=f"name_{i}"
    )

    father = st.text_input(
        f"Father Name",
        key=f"father_{i}"
    )

    fullname = st.text_input(
        f"Full Name",
        key=f"fullname_{i}"
    )

    age_input = st.text_input(
        f"Age",
        key=f"age_{i}"
    )

    valid_age = False
    age = None

    if age_input:
        if age_input.isdigit():
            age = int(age_input)
            if age < 5:
                st.warning("⚠️ 5+ years required to enter the plane")
            else:
                valid_age = True
                st.success("✅ Age accepted")
        else:
            st.error("❌ Please enter a NUMBER")

    if name and father and fullname and valid_age:
        st.success("✅ Traveler Selected")
        all_passengers.append({
            "Name": name,
            "Father Name": father,
            "Full Name": fullname,
            "Age": age
        })

    st.markdown("---")

# =========================
# FLIGHT DETAILS (AT BOTTOM)
# =========================

if all_passengers:
    st.header("✈ Flight Details")

    flight_date = st.date_input(
        "Select Flight Date",
        value=None
    )

    if flight_date:
        flight_day = flight_date.strftime("%A")
        st.info(f"📅 Flight Day: **{flight_day}**")

        st.markdown("---")
        st.header("🎫 Final Ticket Summary")

        for p in all_passengers:
            p["Flight Date"] = flight_date
            p["Flight Day"] = flight_day

        st.table(all_passengers)
    else:
        st.warning("⚠️ Please select flight date to continue")
