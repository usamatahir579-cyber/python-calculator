# 🚀 Projectile Motion Simulator

A physics-based web app that simulates projectile motion in real time.  
Built with Python and Streamlit — no math degree required to use it.

---

## 🎯 What It Does

Enter a launch velocity and angle, click **Simulate**, and instantly get:

- ⏱ **Time of Flight** — how long the object stays in the air
- 📈 **Maximum Height** — the peak point of the trajectory  
- 📏 **Horizontal Range** — total distance covered

Plus a **live trajectory graph** and an **interactive slider** that moves the 
projectile along its path step by step.

---

## 🛠️ Built With

- Python 3
- Streamlit — for the interactive web UI
- NumPy — for physics calculations
- Matplotlib — for trajectory plotting

---

## ▶️ Run It Locally

```bash
git clone https://github.com/usamatahir579-cyber/python-calculator.git
cd python-calculator
pip install streamlit numpy matplotlib
python -m streamlit run app.py
```

The app opens in your browser automatically at `http://localhost:8501`

---

## 🧠 The Physics Behind It

| Variable | Formula |
|---|---|
| Time of Flight | `T = 2u·sin(θ) / g` |
| Max Height | `H = u²·sin²(θ) / 2g` |
| Horizontal Range | `R = u²·sin(2θ) / g` |

Where `u` = initial velocity, `θ` = launch angle, `g` = 9.8 m/s²

---

## 👨‍💻 Author

**Usama Tahir** — Physics student & Python developer  
📧 Need a custom Python tool or data script? 
**[Hire me on Fiverr →](https://www.fiverr.com/users/renausama)**

---

## ⭐ If you find this useful, give it a star!
Usama Tahir
