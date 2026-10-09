import streamlit as st
from datetime import date

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="FarmSphere",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f7faf7;
    }

    .hero {
        padding: 35px;
        border-radius: 20px;
        background: linear-gradient(135deg, #dff3df, #f5fff5);
        margin-bottom: 25px;
    }

    .hero h1 {
        color: #245c35;
        font-size: 48px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 20px;
        color: #48604d;
    }

    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        border: 1px solid #e1e8e1;
        margin-bottom: 15px;
    }

    .farmer {
        font-size: 17px;
        color: #555;
    }

    .price {
        font-size: 25px;
        font-weight: bold;
        color: #287a3d;
    }

    .status {
        padding: 10px;
        border-radius: 10px;
        background-color: #eaf7ea;
        color: #286638;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# DATA
# -----------------------------
farms = {
    "🥕 Carrots": {
        "farmer": "Ramesh Patil",
        "location": "Nashik, Maharashtra",
        "price": 80,
        "harvest": "15 September 2026",
        "stage": "Growing",
        "progress": 65,
        "method": "Natural farming"
    },
    "🍅 Tomatoes": {
        "farmer": "Sunita Jadhav",
        "location": "Pune, Maharashtra",
        "price": 60,
        "harvest": "5 September 2026",
        "stage": "Flowering",
        "progress": 50,
        "method": "Organic farming"
    },
    "🥬 Spinach": {
        "farmer": "Mahesh Shinde",
        "location": "Satara, Maharashtra",
        "price": 40,
        "harvest": "28 August 2026",
        "stage": "Almost ready",
        "progress": 85,
        "method": "Organic farming"
    },
    "🌾 Rice": {
        "farmer": "Vijay More",
        "location": "Kolhapur, Maharashtra",
        "price": 95,
        "harvest": "20 October 2026",
        "stage": "Growing",
        "progress": 45,
        "method": "Sustainable farming"
    }
}


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🌱 FarmSphere")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🛒 Explore Farms",
        "📍 Track My Crop",
        "📦 My Orders",
        "👨‍🌾 Farmer Dashboard"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "FarmSphere connects consumers directly with farmers "
    "and makes the journey from farm to fork transparent."
)


# =====================================================
# HOME
# =====================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🌱 FarmSphere</h1>
        <p>Know your farmer. Trust your food.</p>
        <p>
        Connect directly with farmers, track your crops,
        and receive fresh produce from the farm.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Why FarmSphere?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👨‍🌾 Partner Farmers", "250+")

    with col2:
        st.metric("🌾 Farms", "120+")

    with col3:
        st.metric("🥬 Produce", "35+")

    with col4:
        st.metric("📦 Orders Delivered", "8,500+")

    st.markdown("---")

    st.subheader("The FarmSphere Promise")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        ### 🔍 Transparency
        Know who grows your food and where it comes from.
        """)

    with c2:
        st.markdown("""
        ### 🌱 Track Your Crop
        Follow your crop from planting to harvest.
        """)

    with c3:
        st.markdown("""
        ### 🤝 Direct Connection
        Farmers get direct access to customers.
        """)

    st.markdown("---")

    st.subheader("How it works")

    steps = [
        ("1️⃣", "Choose", "Select the produce you want."),
        ("2️⃣", "Connect", "Choose a partner farm."),
        ("3️⃣", "Track", "Follow your crop's progress."),
        ("4️⃣", "Harvest", "Receive fresh produce.")
    ]

    cols = st.columns(4)

    for col, (number, title, description) in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div class="card">
                <h2>{number}</h2>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)


# =====================================================
# EXPLORE FARMS
# =====================================================

elif page == "🛒 Explore Farms":

    st.title("🛒 Explore Partner Farms")

    st.write(
        "Choose fresh produce directly from our partner farmers."
    )

    selected_crop = st.selectbox(
        "What would you like to buy?",
        list(farms.keys())
    )

    farm = farms[selected_crop]

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown(f"""
        <div class="card">
            <h2>{selected_crop}</h2>
            <p class="farmer">👨‍🌾 Farmer: <b>{farm['farmer']}</b></p>
            <p>📍 {farm['location']}</p>
            <p>🌱 Method: {farm['method']}</p>
            <p>📅 Expected harvest: {farm['harvest']}</p>
            <p class="price">₹{farm['price']} / kg</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.subheader("Crop Progress")

        st.progress(farm["progress"] / 100)

        st.write(f"{farm['progress']}% grown")

        st.success(f"Status: {farm['stage']}")

    quantity = st.number_input(
        "Quantity (kg)",
        min_value=1,
        max_value=20,
        value=2
    )

    total = quantity * farm["price"]

    st.info(f"Total price: ₹{total}")

    if st.button("🌱 Reserve My Harvest", type="primary"):

        st.success(
            f"Your {selected_crop} harvest has been reserved!"
        )

        st.balloons()


# =====================================================
# TRACK CROP
# =====================================================

elif page == "📍 Track My Crop":

    st.title("📍 Track My Crop")

    selected_crop = st.selectbox(
        "Select your crop",
        list(farms.keys())
    )

    farm = farms[selected_crop]

    st.markdown(f"### {selected_crop}")

    st.write(
        f"Farmer: **{farm['farmer']}** | "
        f"Location: **{farm['location']}**"
    )

    st.progress(farm["progress"] / 100)

    st.write(f"Crop growth: **{farm['progress']}%**")

    st.markdown("---")

    st.subheader("🌱 Crop Journey")

    stages = [
        ("🌱", "Seed planted", True),
        ("🌿", "Crop growing", farm["progress"] >= 40),
        ("🌼", "Flowering", farm["progress"] >= 50),
        ("🥕", "Ready for harvest", farm["progress"] >= 85),
        ("📦", "Delivered", False)
    ]

    for icon, stage, completed in stages:

        if completed:
            st.success(f"{icon} {stage} ✓")
        else:
            st.info(f"{icon} {stage}")

    st.markdown("---")

    st.subheader("📅 Expected Harvest")

    st.write(f"**{farm['harvest']}**")

    st.caption(
        "Customers receive regular updates about their crop "
        "from the partner farmer."
    )


# =====================================================
# ORDERS
# =====================================================

elif page == "📦 My Orders":

    st.title("📦 My Orders")

    order = {
        "crop": "🥕 Carrots",
        "farmer": "Ramesh Patil",
        "quantity": "3 kg",
        "status": "Growing",
        "delivery": "18 September 2026"
    }

    st.markdown(f"""
    <div class="card">
        <h2>{order['crop']}</h2>
        <p>👨‍🌾 Farmer: <b>{order['farmer']}</b></p>
        <p>📦 Quantity: {order['quantity']}</p>
        <p>🚚 Expected delivery: {order['delivery']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Order Status")

    st.success("✓ Order confirmed")
    st.success("✓ Farmer assigned")
    st.success("✓ Crop growing")
    st.info("⏳ Harvest pending")
    st.info("⏳ Delivery pending")


# =====================================================
# FARMER DASHBOARD
# =====================================================

elif page == "👨‍🌾 Farmer Dashboard":

    st.title("👨‍🌾 Farmer Dashboard")

    st.write(
        "A simple dashboard for partner farmers."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Active Orders", "24")

    with col2:
        st.metric("Expected Revenue", "₹42,500")

    with col3:
        st.metric("Crop Health", "92%")

    st.markdown("---")

    st.subheader("📊 Current Crops")

    crop_data = {
        "Crop": ["Carrots", "Tomatoes", "Spinach", "Rice"],
        "Area": ["2 acres", "1.5 acres", "1 acre", "3 acres"],
        "Growth": ["65%", "50%", "85%", "45%"],
        "Orders": [15, 20, 12, 30]
    }

    st.dataframe(
        crop_data,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🤖 FarmSphere AI Recommendation")

    st.warning(
        "Demand prediction: Tomato demand is expected to increase "
        "by approximately 20% next month. Consider increasing "
        "tomato cultivation."
)
