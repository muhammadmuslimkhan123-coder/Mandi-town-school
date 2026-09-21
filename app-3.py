import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(
    page_title="Muslim Airport Bakhar | AirportHub",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# THEME: GREEN + ORANGE
# =========================
st.markdown("""
<style>
:root {
    --green:#138a4b;
    --green2:#0b6b3a;
    --orange:#f28c28;
    --light:#f4faf6;
    --dark:#123524;
}
.stApp { background: linear-gradient(135deg,#f4faf6 0%,#fff8ef 100%); }
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0b6b3a,#138a4b);
}
section[data-testid="stSidebar"] * { color:white !important; }
h1,h2,h3 { color:var(--green2); }
.hero {
    padding:32px; border-radius:22px; color:white;
    background:linear-gradient(135deg,#0b6b3a,#138a4b 65%,#f28c28);
    box-shadow:0 8px 28px rgba(0,0,0,.12);
}
.hero h1 { color:white; font-size:42px; margin-bottom:5px; }
.hero p { color:white; font-size:18px; }
.card {
    background:white; border-radius:18px; padding:20px;
    border:1px solid #e7eee9; box-shadow:0 4px 16px rgba(0,0,0,.06);
    margin-bottom:14px;
}
.metric {
    background:white; padding:18px; border-radius:16px;
    border-left:6px solid var(--orange); box-shadow:0 3px 12px rgba(0,0,0,.06);
}
.badge { padding:6px 12px; border-radius:20px; background:#e9f7ef; color:#0b6b3a; font-weight:700; }
.orange { color:#d96e00; font-weight:700; }
button[kind="primary"] { background:#138a4b !important; }
[data-testid="stMetricValue"] { color:#0b6b3a; }
.footer { text-align:center; padding:25px; color:#567; }
</style>
""", unsafe_allow_html=True)

# =========================
# DATA LAYER (dummy JSON-ready)
# =========================
FLIGHTS = [
    {"Flight":"MB-101","Airline":"Muslim Air","From":"Karachi","To":"Bakhar","Time":"08:30","Gate":"A1","Terminal":"T1","Status":"On Time","Belt":"B2","Aircraft":"A320"},
    {"Flight":"MB-205","Airline":"Pakistan Airways","From":"Lahore","To":"Bakhar","Time":"10:15","Gate":"A3","Terminal":"T1","Status":"Boarding","Belt":"B1","Aircraft":"A321"},
    {"Flight":"MB-310","Airline":"Indus Airlines","From":"Islamabad","To":"Bakhar","Time":"12:40","Gate":"B2","Terminal":"T2","Status":"Delayed","Belt":"B4","Aircraft":"B737"},
    {"Flight":"MB-411","Airline":"Muslim Air","From":"Bakhar","To":"Dubai","Time":"15:20","Gate":"A4","Terminal":"T1","Status":"On Time","Belt":"—","Aircraft":"A330"},
    {"Flight":"MB-512","Airline":"Pakistan Airways","From":"Bakhar","To":"Doha","Time":"18:05","Gate":"B1","Terminal":"T2","Status":"On Time","Belt":"—","Aircraft":"A320"},
]

SHOPS = [
    ["Green Café","Food & Dining","T1","06:00–23:00"],
    ["Bakhar Bites","Food & Dining","T2","07:00–22:00"],
    ["Airport Duty Free","Shopping","T1","24 Hours"],
    ["Travel Essentials","Shopping","T2","08:00–22:00"],
]
PARKING = [
    ["P1 Short Stay","250 spaces","Rs. 150/hour","Available"],
    ["P2 Long Stay","500 spaces","Rs. 800/day","Available"],
    ["VIP Parking","80 spaces","Rs. 1,500/day","Limited"],
]
LOST = []
USERS = [{"email":"admin@muslimairport.pk","role":"Admin"}]

# =========================
# HELPERS
# =========================
def status_badge(status):
    return f'<span class="badge">{status}</span>'

def show_flights(rows):
    if not rows:
        st.info("No flights found.")
        return
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown("# ✈️")
    st.markdown("## Muslim Airport")
    st.markdown("### Bakhar")
    st.caption("AirportHub")
    st.divider()

    page = st.radio("Navigation", [
        "🏠 Home",
        "✈️ Flight Status",
        "📋 Flight Details",
        "🗺️ Terminal Maps",
        "🅿️ Parking",
        "🚕 Transport",
        "🍽️ Shops & Dining",
        "🛋️ Lounges",
        "🕌 Services",
        "🧳 Lost & Found",
        "☎️ Contact & FAQs",
        "👤 User Account",
        "🔔 Notifications",
        "🌐 Language",
        "👨‍💼 Admin Dashboard",
        "👷 Staff Dashboard",
    ])

    st.divider()
    dark = st.toggle("🌙 Dark mode")
    st.caption("MVP • Python-only architecture")
    st.caption("Green + Orange Edition")

# =========================
# HEADER / HERO
# =========================
if page == "🏠 Home":
    st.markdown("""
    <div class="hero">
      <h1>✈️ Muslim Airport Bakhar</h1>
      <p>Welcome to AirportHub — your smart gateway for arrivals, departures, travel and airport services.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    c1,c2,c3,c4 = st.columns(4)
    c1.markdown('<div class="metric"><b>🛫 Departures</b><h2>12</h2></div>',unsafe_allow_html=True)
    c2.markdown('<div class="metric"><b>🛬 Arrivals</b><h2>18</h2></div>',unsafe_allow_html=True)
    c3.markdown('<div class="metric"><b>🟢 Airport Status</b><h2>Normal</h2></div>',unsafe_allow_html=True)
    c4.markdown('<div class="metric"><b>🌤️ Weather</b><h2>28°C</h2></div>',unsafe_allow_html=True)

    st.subheader("🔎 Live Flight Search")
    q = st.text_input("Flight number, airline or city", placeholder="e.g. MB-101 / Karachi")
    if q:
        results = [x for x in FLIGHTS if q.lower() in str(x).lower()]
        show_flights(results)

    a,b = st.columns(2)
    with a:
        st.markdown("### 🛬 Latest Arrivals")
        show_flights([x for x in FLIGHTS if x["To"]=="Bakhar"][:4])
    with b:
        st.markdown("### 🛫 Latest Departures")
        show_flights([x for x in FLIGHTS if x["From"]=="Bakhar"][:4])

    st.subheader("⚡ Quick Links")
    q1,q2,q3,q4 = st.columns(4)
    q1.info("✈️ Flight Status")
    q2.info("🅿️ Parking")
    q3.info("🚕 Transport")
    q4.info("🕌 Airport Services")

# =========================
# FLIGHT STATUS
# =========================
elif page == "✈️ Flight Status":
    st.title("✈️ Flight Status")
    tab1,tab2 = st.tabs(["🛬 Arrivals","🛫 Departures"])
    search = st.text_input("Search flight / airline / city")
    status = st.selectbox("Status",["All","On Time","Boarding","Delayed"])

    data = FLIGHTS
    if search:
        data = [x for x in data if search.lower() in str(x).lower()]
    if status != "All":
        data = [x for x in data if x["Status"] == status]

    with tab1:
        show_flights([x for x in data if x["To"]=="Bakhar"])
    with tab2:
        show_flights([x for x in data if x["From"]=="Bakhar"])
    st.caption("Auto-refresh/API integration can be connected later to Aviationstack, Amadeus or OpenSky.")

# =========================
# FLIGHT DETAILS
# =========================
elif page == "📋 Flight Details":
    st.title("📋 Flight Details")
    flight_no = st.selectbox("Select flight", [x["Flight"] for x in FLIGHTS])
    f = next(x for x in FLIGHTS if x["Flight"] == flight_no)
    st.markdown(f'<div class="card"><h2>{f["Flight"]} • {f["Airline"]}</h2>{status_badge(f["Status"])}</div>',unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    c1.metric("Route",f'{f["From"]} → {f["To"]}')
    c2.metric("Gate",f["Gate"])
    c3.metric("Terminal",f["Terminal"])
    c1,c2,c3 = st.columns(3)
    c1.metric("Schedule",f["Time"])
    c2.metric("Baggage Belt",f["Belt"])
    c3.metric("Aircraft",f["Aircraft"])
    st.info("Delay reason: Operational update / dummy data")
    st.info("🌤️ Weather: 28°C • Clear • Wind 12 km/h")

# =========================
# TERMINAL MAP
# =========================
elif page == "🗺️ Terminal Maps":
    st.title("🗺️ Terminal Maps")
    st.info("Interactive map-ready module. Connect Leaflet/Mapbox API later if required.")
    st.markdown("""
    <div class="card">
    <h3>Terminal 1</h3>
    🛂 Security → 🛫 Gates A1–A4 → 🧳 Baggage → 🚻 Facilities → 🕌 Prayer Room
    </div>
    <div class="card">
    <h3>Terminal 2</h3>
    🛂 Security → 🛫 Gates B1–B4 → 🛍️ Shops → 🍽️ Dining → 🧳 Baggage
    </div>
    """,unsafe_allow_html=True)
    st.subheader("⏱️ Security Wait Times")
    st.progress(.30, "Terminal 1 — 9 minutes")
    st.progress(.50, "Terminal 2 — 15 minutes")
    st.caption("Walking directions and live POIs can be connected to a map provider.")

# =========================
# PARKING
# =========================
elif page == "🅿️ Parking":
    st.title("🅿️ Parking")
    show_flights([]) if False else None
    for p in PARKING:
        st.markdown(f'<div class="card"><h3>🚗 {p[0]}</h3><b>{p[1]}</b> • {p[2]}<br>Availability: {p[3]}</div>',unsafe_allow_html=True)
    st.subheader("🎟️ Parking Booking")
    with st.form("parking"):
        name=st.text_input("Name")
        vehicle=st.text_input("Vehicle number")
        lot=st.selectbox("Parking", [p[0] for p in PARKING])
        submitted=st.form_submit_button("Generate QR Ticket")
        if submitted:
            st.success(f"Parking booked for {name or 'Guest'} — {lot}")
            st.code(f"PARK-BKH-{datetime.now().strftime('%Y%m%d%H%M')}")

# =========================
# TRANSPORT
# =========================
elif page == "🚕 Transport":
    st.title("🚕 Transport")
    for title,desc in [
        ("🚕 Taxi","Airport taxi counters and pickup zones."),
        ("🚌 Bus","City and intercity bus information."),
        ("🚆 Train","Rail connection information."),
        ("🚗 Ride-share","Pickup/drop-off zone information."),
    ]:
        st.markdown(f'<div class="card"><h3>{title}</h3>{desc}</div>',unsafe_allow_html=True)

# =========================
# SHOPS
# =========================
elif page == "🍽️ Shops & Dining":
    st.title("🍽️ Shops & Dining")
    cat=st.selectbox("Category",["All","Food & Dining","Shopping"])
    for s in SHOPS:
        if cat=="All" or s[1]==cat:
            st.markdown(f'<div class="card"><h3>🏪 {s[0]}</h3>{s[1]} • {s[2]} • {s[3]}<br><span class="orange">Special offers available</span></div>',unsafe_allow_html=True)

# =========================
# LOUNGES
# =========================
elif page == "🛋️ Lounges":
    st.title("🛋️ Airport Lounges")
    for name,loc,features in [
        ("Muslim Executive Lounge","Terminal 1","WiFi • Snacks • Prayer Area • Quiet Zone"),
        ("Bakhar Premium Lounge","Terminal 2","WiFi • Meals • Charging • Business Area"),
    ]:
        st.markdown(f'<div class="card"><h3>✨ {name}</h3>{loc}<br>{features}</div>',unsafe_allow_html=True)
    if st.button("Book Lounge Access"):
        st.success("Lounge booking request created.")

# =========================
# SERVICES
# =========================
elif page == "🕌 Services":
    st.title("🕌 Airport Services")
    services=["📶 Free WiFi","🧑‍🦽 Special Assistance","🏥 Medical Centre","🕌 Prayer Room","🧳 Luggage Storage","👶 Family/Child Care","💱 Currency Exchange","ℹ️ Information Desk"]
    cols=st.columns(4)
    for i,s in enumerate(services):
        cols[i%4].markdown(f'<div class="card"><h4>{s}</h4>Available</div>',unsafe_allow_html=True)

# =========================
# LOST & FOUND
# =========================
elif page == "🧳 Lost & Found":
    st.title("🧳 Lost & Found")
    tab1,tab2=st.tabs(["Report Item","Search Report"])
    with tab1:
        with st.form("lost"):
            item=st.text_input("Item")
            location=st.text_input("Last known location")
            contact=st.text_input("Contact")
            details=st.text_area("Description")
            if st.form_submit_button("Submit Report"):
                LOST.append({"Item":item,"Location":location,"Contact":contact,"Description":details})
                st.success("Lost item report submitted.")
    with tab2:
        key=st.text_input("Search item")
        found=[x for x in LOST if key.lower() in str(x).lower()] if key else LOST
        if found: st.dataframe(pd.DataFrame(found),use_container_width=True,hide_index=True)
        else: st.info("No matching reports.")

# =========================
# CONTACT / FAQ
# =========================
elif page == "☎️ Contact & FAQs":
    st.title("☎️ Contact & FAQs")
    st.info("Airport Emergency: 1122 • Information Desk: +92-XXX-XXXXXXX")
    for q,a in [
        ("How can I check my flight?","Use Flight Status and search your flight number."),
        ("Where is parking?","Parking areas P1, P2 and VIP are available."),
        ("Is WiFi available?","Yes, free airport WiFi is available."),
        ("Where is the prayer room?","Prayer facilities are available in both terminals."),
    ]:
        with st.expander(q): st.write(a)
    st.subheader("Contact Form")
    with st.form("contact"):
        st.text_input("Name"); st.text_input("Email"); st.text_area("Message")
        if st.form_submit_button("Send"):
            st.success("Your message has been received.")

# =========================
# ACCOUNT
# =========================
elif page == "👤 User Account":
    st.title("👤 User Account")
    tab1,tab2=st.tabs(["Login","Sign Up"])
    with tab1:
        email=st.text_input("Email",key="loginemail")
        password=st.text_input("Password",type="password",key="loginpass")
        if st.button("Login"):
            st.success("Demo login successful.")
    with tab2:
        email2=st.text_input("Email",key="signupemail")
        password2=st.text_input("Password",type="password",key="signuppass")
        if st.button("Create Account"):
            USERS.append({"email":email2,"role":"Passenger"})
            st.success("Account created.")
    st.subheader("Saved Flights & Trip Alerts")
    st.checkbox("Notify me about flight status changes")
    st.checkbox("Notify me about gate changes")
    st.checkbox("Enable email notifications")

# =========================
# NOTIFICATIONS
# =========================
elif page == "🔔 Notifications":
    st.title("🔔 Notifications")
    alerts=[
        ("MB-205","Boarding started","Gate A3"),
        ("MB-310","Flight delayed","Operational update"),
        ("MB-411","Gate confirmed","Gate A4"),
    ]
    for x in alerts:
        st.markdown(f'<div class="card"><b>🔔 {x[0]}</b><br>{x[1]} — {x[2]}</div>',unsafe_allow_html=True)
    st.subheader("Notification Preferences")
    st.toggle("Email")
    st.toggle("SMS")
    st.toggle("Push")

# =========================
# LANGUAGE
# =========================
elif page == "🌐 Language":
    st.title("🌐 Language / زبان")
    lang=st.selectbox("Select language",["English","اردو (Urdu)","العربية (Arabic)"])
    if lang.startswith("اردو"):
        st.markdown("### مسلم ایئرپورٹ بکھر میں خوش آمدید")
        st.write("پروازوں، آمد و روانگی اور ہوائی اڈے کی خدمات کی معلومات حاصل کریں۔")
    elif lang.startswith("العربية"):
        st.markdown("### مرحباً بكم في مطار مسلم بکھر")
        st.write("معلومات الرحلات والخدمات متاحة هنا.")
    else:
        st.markdown("### Welcome to Muslim Airport Bakhar")
    st.info("RTL-ready interface architecture included for Urdu/Arabic.")

# =========================
# ADMIN
# =========================
elif page == "👨‍💼 Admin Dashboard":
    st.title("👨‍💼 Admin Dashboard")
    st.caption("Demo RBAC • Admin CRUD")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Flights",len(FLIGHTS))
    c2.metric("Users",len(USERS))
    c3.metric("Shops",len(SHOPS))
    c4.metric("Parking Lots",len(PARKING))

    tabs=st.tabs(["Flights CRUD","Airlines","Gates & Terminals","Shops","Parking","Users","Alerts","Analytics"])
    with tabs[0]:
        st.dataframe(pd.DataFrame(FLIGHTS),use_container_width=True,hide_index=True)
        with st.form("addflight"):
            st.write("Add Flight")
            a,b,c=st.columns(3)
            nf=a.text_input("Flight")
            na=b.text_input("Airline")
            route=c.text_input("Route (From → To)")
            if st.form_submit_button("Add"):
                st.success(f"{nf} added to the flight system.")
    with tabs[1]:
        st.dataframe(pd.DataFrame({"Airlines":["Muslim Air","Pakistan Airways","Indus Airlines"]}),use_container_width=True,hide_index=True)
    with tabs[2]:
        st.dataframe(pd.DataFrame({"Terminal":["T1","T1","T2","T2"],"Gate":["A1","A3","B1","B2"]}),use_container_width=True,hide_index=True)
    with tabs[3]:
        st.dataframe(pd.DataFrame(SHOPS,columns=["Name","Category","Terminal","Hours"]),use_container_width=True,hide_index=True)
    with tabs[4]:
        st.dataframe(pd.DataFrame(PARKING,columns=["Lot","Capacity","Rate","Status"]),use_container_width=True,hide_index=True)
    with tabs[5]:
        st.dataframe(pd.DataFrame(USERS),use_container_width=True,hide_index=True)
    with tabs[6]:
        st.text_area("Create Airport Alert")
        st.button("Publish Alert")
    with tabs[7]:
        chart=pd.DataFrame({"Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"Passengers":[1200,1500,1320,1780,1900,2100,1850]})
        st.bar_chart(chart.set_index("Day"))

# =========================
# STAFF
# =========================
elif page == "👷 Staff Dashboard":
    st.title("👷 Staff Dashboard")
    st.info("Role-based operational view")
    c1,c2,c3=st.columns(3)
    c1.metric("Gate Changes",3)
    c2.metric("Security Wait",9)
    c3.metric("Baggage Alerts",2)
    st.subheader("Gate Changes")
    st.dataframe(pd.DataFrame([
        ["MB-205","A3","A4","Updated"],
        ["MB-310","B2","B3","Updated"],
    ],columns=["Flight","Old Gate","New Gate","Status"]),use_container_width=True,hide_index=True)
    st.subheader("Baggage")
    st.warning("Belt B4 requires staff inspection.")

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
<hr>
✈️ <b>Muslim Airport Bakhar — AirportHub</b><br>
Green + Orange Airport Management Web App • Python Edition<br>
MVP data is dummy/demo data. External aviation APIs, database, SMS/email and live maps can be connected in the production layer.
</div>
""",unsafe_allow_html=True)
