import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("🚀 Projectile Motion Simulator")

st.write("A simple physics simulator for projectile motion.")

# Inputs
velocity = st.number_input("Enter velocity (u)", min_value=0.0, value=20.0)
angle = st.number_input("Enter angle (degrees)", min_value=0.0, max_value=90.0, value=45.0)

g = 9.8

if st.button("Simulate"):

    theta = math.radians(angle)

    # Physics calculations
    time_of_flight = (2 * velocity * math.sin(theta)) / g
    max_height = (velocity**2 * math.sin(theta)**2) / (2 * g)
    horizontal_range = (velocity**2 * math.sin(2 * theta)) / g

    # Results
    st.subheader("📊 Results")
    st.write(f"⏱ Time of Flight: {time_of_flight:.2f} s")
    st.write(f"📈 Maximum Height: {max_height:.2f} m")
    st.write(f"📏 Horizontal Range: {horizontal_range:.2f} m")

    # Time points
    t = np.linspace(0, time_of_flight, 200)

    x = velocity * math.cos(theta) * t
    y = velocity * math.sin(theta) * t - 0.5 * g * t**2

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Trajectory")

    ax.set_xlabel("Distance (x)")
    ax.set_ylabel("Height (y)")
    ax.set_title("Projectile Motion Path")
    ax.legend()

    st.pyplot(fig)

    # Simple animation (slider-based, stable for deployment)
    st.subheader("🎯 Motion View")

    step = st.slider("Move projectile", 0, len(t)-1, 0)

    fig2, ax2 = plt.subplots()
    ax2.plot(x, y, alpha=0.3)
    ax2.scatter(x[step], y[step], color="red", s=80)

    ax2.set_xlabel("Distance (x)")
    ax2.set_ylabel("Height (y)")
    ax2.set_title("Projectile Position")

    st.pyplot(fig2)


        # python -m streamlit run app.py