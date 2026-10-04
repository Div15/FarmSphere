import streamlit as st
from datetime import date, timedelta

st.set_page_config(
    page_title="FarmSphere | Food Transparency",
    page_icon="🌱",
    layout="wide",
)

st.markdown("""
<style>
    .stApp { background: #f7faf7; }
    .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1180px; }
    .hero {
        padding: 2rem 2.2rem;
        border-radius: 20px;
        background: linear-gradient(120deg, #e3f4e5 0%, #f7fff7 100%);
        border: 1px solid #d8ead9;
        margin-bottom: 1.5rem;
    }
    .hero h1 { color: #245c35; font-size: 2.7rem; margin: 0; }
    .hero p { color: #3f5945; font-size: 1.1rem; margin-top: .5rem; }
    .muted { color: #657367; font-size: .9rem; }
    div[data-testid="stMetric"] {
        background: white; border: 1px solid #e1e8e1;
        padding: 1rem; border-radius: 12px;
    }
    .trust-note {
        background: #fff8e8; border: 1px solid #f0dfb2;
        border-radius: 10px; padding: 12px 14px; color: #66501b;
    }
</style>
""", unsafe_allow_html=True)

# Demonstration listings only. Replace with verified seller data before public launch.
# Reset demo data once when the listing structure changes between app versions.
# Streamlit can retain session_state across code updates in an existing browser session.
if st.session_state.get("farmsphere_data_version") != 2:
    for key in ("listings", "orders", "seller_interest"):
        st.session_state.pop(key, None)
    st.session_state["farmsphere_data_version"] = 2

if "listings" not in st.session_state:
    st.session_state.listings = [
        {
            "id": 1, "crop": "Spinach", "emoji": "🥬", "seller": "Priya Kulkarni",
            "seller_type": "Terrace Garden", "location": "Kamothe, Navi Mumbai",
            "price": 35, "unit": "bunch", "quantity": 12,
            "harvest": "2026-10-05", "method": "Home-grown",
            "treatments": "Seller reports no synthetic pesticide use",
            "last_treatment": "No treatment date supplied",
            "notes": "Grown in containers; more details can be requested from the seller",
            "verification": "Seller-reported · not independently verified",
            "progress": 90,
        },
        {
            "id": 2, "crop": "Tomatoes", "emoji": "🍅", "seller": "Sunita Jadhav",
            "seller_type": "Partner Farm", "location": "Pune, Maharashtra",
            "price": 60, "unit": "kg", "quantity": 40,
            "harvest": "2026-10-08", "method": "Organic farming (seller-reported)",
            "treatments": "Treatment details not provided",
            "last_treatment": "Not provided",
            "notes": "Contact seller for crop-care details",
            "verification": "Seller-reported · not independently verified",
            "progress": 70,
        },
        {
            "id": 3, "crop": "Carrots", "emoji": "🥕", "seller": "Ramesh Patil",
            "seller_type": "Partner Farm", "location": "Nashik, Maharashtra",
            "price": 80, "unit": "kg", "quantity": 60,
            "harvest": "2026-10-10", "method": "Natural farming (seller-reported)",
            "treatments": "Treatment details not provided",
            "last_treatment": "Not provided",
            "notes": "Contact seller for crop-care details",
            "verification": "Seller-reported · not independently verified",
            "progress": 65,
        },
        {
            "id": 4, "crop": "Coriander", "emoji": "🌿", "seller": "Anita Deshmukh",
            "seller_type": "Terrace Garden", "location": "Kharghar, Navi Mumbai",
            "price": 25, "unit": "bunch", "quantity": 8,
            "harvest": "2026-10-05", "method": "Home-grown",
            "treatments": "Seller has not provided treatment details",
            "last_treatment": "Not provided",
            "notes": "Small-batch neighborhood produce",
            "verification": "Seller-reported · not independently verified",
            "progress": 95,
        },
    ]

if "orders" not in st.session_state:
    st.session_state.orders = []

if "seller_interest" not in st.session_state:
    st.session_state.seller_interest = []

PAGES = [
    "Home",
    "Explore Produce",
    "My Orders",
    "Crop Journey",
    "Become a Seller",
]

st.sidebar.title("🌱 FarmSphere")
st.sidebar.caption("Food transparency, from grower to customer")
page = st.sidebar.radio("Menu", PAGES)
st.sidebar.markdown("---")
st.sidebar.caption("Demo application · Sample seller and crop data")

if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>🌱 FarmSphere</h1>
        <p><b>Know your grower. Understand your food. Eat with confidence.</b></p>
        <p>Explore how your produce is grown, what crop treatments sellers report, and when it is harvested.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Food transparency comes first")
    a, b, c = st.columns(3)
    with a:
        st.markdown("### 🌿 Growing practices")
        st.write("See the growing methods and crop-care notes shared by each seller.")
    with b:
        st.markdown("### 🧪 Treatment disclosure")
        st.write("Review reported pesticide, fertilizer, and treatment information, including dates when supplied.")
    with c:
        st.markdown("### 📅 Crop journey")
        st.write("Check who grew the produce, where it was grown, and its expected harvest date.")

    st.markdown("---")
    st.subheader("Explore produce")
    st.write("Compare available produce from partner farms and neighborhood terrace gardeners. Select **Explore Produce** from the menu to browse listings.")

    st.markdown("""
    <div class="trust-note">
        <b>Transparency note:</b> Seller disclosures are not proof of pesticide-free status, organic certification,
        or laboratory testing. FarmSphere should clearly distinguish seller-reported information from independently
        verified evidence.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Who can sell on FarmSphere?")
    left, right = st.columns(2)
    with left:
        st.markdown("#### 🚜 Partner farms")
        st.write("Share produce listings, crop-care details, harvest dates, and available quantities.")
    with right:
        st.markdown("#### 🪴 Terrace gardeners")
        st.write("Offer small batches of home-grown vegetables and herbs to nearby customers.")

elif page == "Explore Produce":
    st.title("Explore Produce")
    st.write("Review the available produce and the information each seller has shared.")
    st.info("Listings below are sample data for demonstration. Growing and treatment details are seller-reported unless explicitly verified.")

    f1, f2 = st.columns([1, 2])
    with f1:
        seller_filter = st.selectbox("Seller type", ["All sellers", "Partner Farm", "Terrace Garden"])
    with f2:
        search = st.text_input("Search by produce, seller, or location", placeholder="e.g. spinach or Kamothe")

    listings = st.session_state.listings
    visible = []
    for item in listings:
        if seller_filter != "All sellers" and item["seller_type"] != seller_filter:
            continue
        if search.strip():
            query = search.strip().lower()
            if not any(query in str(item[k]).lower() for k in ["crop", "seller", "location"]):
                continue
        visible.append(item)

    if not visible:
        st.warning("No matching produce found. Try a different search.")
    for item in visible:
        with st.container(border=True):
            detail, purchase = st.columns([3, 1])
            with detail:
                st.subheader("{} {}".format(item.get("emoji", "🌱"), item.get("crop", "Produce")))
                st.caption(f'{item["seller_type"]} · {item["location"]}')
                st.write(f'**Grown by:** {item["seller"]}')
                st.write(f'**Growing method:** {item["method"]}')
                st.write(f'**Crop treatment disclosure:** {item["treatments"]}')
                st.write(f'**Most recent treatment date:** {item["last_treatment"]}')
                st.write(f'**Growing notes:** {item["notes"]}')
                st.write(f'**Expected harvest / availability:** {item["harvest"]}')
                st.caption(f'Information status: {item["verification"]}')
            with purchase:
                st.metric("Price", f'₹{item["price"]} / {item["unit"]}')
                st.write(f'Available: **{item["quantity"]} {item["unit"]}**')
                quantity = st.number_input(
                    "Quantity", min_value=1, max_value=max(1, int(item["quantity"])),
                    value=1, key=f'qty_{item["id"]}'
                )
                st.write(f'**Total: ₹{quantity * item["price"]}**')
                if st.button("Reserve", key=f'reserve_{item["id"]}', type="primary", disabled=item["quantity"] < 1):
                    if quantity > item["quantity"]:
                        st.error("Not enough stock available.")
                    else:
                        st.session_state.orders.append({
                            "order_id": len(st.session_state.orders) + 1,
                            "listing_id": item["id"], "crop": item["crop"], "emoji": item["emoji"],
                            "seller": item["seller"], "quantity": quantity, "unit": item["unit"],
                            "total": quantity * item["price"], "status": "Reserved",
                            "harvest": item["harvest"], "treatments": item["treatments"],
                            "verification": item["verification"],
                        })
                        item["quantity"] -= quantity
                        st.success("Reservation added to My Orders.")
                        st.rerun()

elif page == "My Orders":
    st.title("My Orders")
    if not st.session_state.orders:
        st.info("You have not reserved any produce yet. Browse produce to get started.")
    else:
        for order in st.session_state.orders:
            with st.container(border=True):
                st.subheader(f'{order["emoji"]} {order["crop"]}')
                col1, col2, col3 = st.columns(3)
                col1.write(f'**Seller:** {order["seller"]}')
                col2.write(f'**Quantity:** {order["quantity"]} {order["unit"]}')
                col3.write(f'**Total:** ₹{order["total"]}')
                st.write(f'**Status:** {order["status"]}')
                st.write(f'**Expected harvest / availability:** {order["harvest"]}')
                st.caption("This is a reservation demo, not a paid or confirmed commercial order.")

elif page == "Crop Journey":
    st.title("Crop Journey")
    if not st.session_state.orders:
        st.info("Reserve produce first to see its crop information here.")
    else:
        labels = [f'{o["order_id"]}. {o["crop"]} — {o["seller"]}' for o in st.session_state.orders]
        selected_index = st.selectbox("Select a reserved crop", range(len(labels)), format_func=lambda i: labels[i])
        order = st.session_state.orders[selected_index]
        st.subheader(f'{order["emoji"]} {order["crop"]}')
        st.write(f'**Seller:** {order["seller"]}')
        st.write(f'**Expected harvest / availability:** {order["harvest"]}')
        st.write(f'**Treatment disclosure:** {order["treatments"]}')
        st.caption(f'Information status: {order["verification"]}')
        st.markdown("#### Order progress")
        st.success("✓ Reservation recorded")
        st.info("○ Harvest or pickup update — not connected in this demo")
        st.info("○ Fulfillment update — not connected in this demo")
        st.caption("Live crop logs and seller updates would require seller accounts and persistent storage.")

elif page == "Become a Seller":
    st.title("Become a Seller")
    st.write("FarmSphere welcomes partner farms and terrace gardeners who are willing to share clear, honest information about their growing practices.")

    with st.form("seller_interest_form"):
        name = st.text_input("Name")
        seller_type = st.radio("Seller type", ["Terrace Garden", "Partner Farm"], horizontal=True)
        location = st.text_input("Location / neighborhood")
        produce = st.text_input("What do you grow?")
        growing_method = st.text_area("Describe your growing method")
        treatment_info = st.text_area("What pesticides, sprays, fertilizers, or crop treatments do you use?")
        consent = st.checkbox("I agree to keep growing-practice and crop-treatment information accurate and up to date.")
        submitted = st.form_submit_button("Submit seller interest", type="primary")

    if submitted:
        if not name.strip() or not location.strip() or not produce.strip():
            st.error("Please enter your name, location, and produce.")
        elif not consent:
            st.error("Please confirm the disclosure statement.")
        else:
            st.session_state.seller_interest.append({
                "name": name.strip(),
                "type": seller_type,
                "location": location.strip(),
                "produce": produce.strip(),
                "growing_method": growing_method.strip(),
                "treatment_info": treatment_info.strip(),
                "submitted_on": date.today().isoformat(),
            })
            st.success("Seller interest recorded for this session.")
            st.caption("This demo does not publish your details or create a public listing. A real version needs secure storage and an onboarding review.")

st.sidebar.markdown("---")
st.sidebar.caption("FarmSphere prototype · No independent crop verification or live delivery tracking")
        
