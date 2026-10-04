import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="FarmSphere", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.main { background-color: #f7faf7; }
.hero { padding: 30px; border-radius: 18px; background: linear-gradient(135deg,#dff3df,#f5fff5); margin-bottom: 20px; }
.hero h1 { color: #245c35; font-size: 44px; margin-bottom: 4px; }
.hero p { color: #48604d; font-size: 18px; }
.card { padding: 18px; border-radius: 14px; background: white; border: 1px solid #e1e8e1; margin-bottom: 12px; }
.price { color: #287a3d; font-size: 23px; font-weight: bold; }
.small-muted { color: #617064; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# Demo data. In a production app, store this in a database.
if "listings" not in st.session_state:
    st.session_state.listings = [
        {"crop":"🥕 Carrots","seller":"Ramesh Patil","seller_type":"Partner Farm","location":"Nashik, Maharashtra","price":80,"unit":"kg","quantity":60,"harvest":"2026-10-10","method":"Natural farming","progress":65,"fulfillment":"Scheduled delivery","min_order":2,"treatments":"Seller-reported: crop treatment details not yet provided","last_treatment":"Not provided","growing_notes":"Ask seller for details","verification":"Not verified"},
        {"crop":"🍅 Tomatoes","seller":"Sunita Jadhav","seller_type":"Partner Farm","location":"Pune, Maharashtra","price":60,"unit":"kg","quantity":100,"harvest":"2026-10-08","method":"Organic farming","progress":50,"fulfillment":"Scheduled delivery","min_order":2,"treatments":"Seller-reported: crop treatment details not yet provided","last_treatment":"Not provided","growing_notes":"Ask seller for details","verification":"Not verified"},
        {"crop":"🥬 Spinach","seller":"Priya Kulkarni","seller_type":"Terrace Garden","location":"Kamothe, Navi Mumbai","price":35,"unit":"bunch","quantity":12,"harvest":"2026-10-05","method":"Home-grown, chemical-conscious","progress":90,"fulfillment":"Pickup / neighborhood drop","min_order":1,"treatments":"Seller-reported: no synthetic pesticide use declared","last_treatment":"No treatment date provided","growing_notes":"Home-grown; practices should be confirmed with seller","verification":"Not verified"},
        {"crop":"🌿 Coriander","seller":"Anita Deshmukh","seller_type":"Terrace Garden","location":"Kharghar, Navi Mumbai","price":25,"unit":"bunch","quantity":8,"harvest":"2026-10-05","method":"Home-grown","progress":95,"fulfillment":"Pickup / neighborhood drop","min_order":1,"treatments":"Seller-reported: no synthetic pesticide use declared","last_treatment":"No treatment date provided","growing_notes":"Home-grown; practices should be confirmed with seller","verification":"Not verified"},
        {"crop":"🌾 Rice","seller":"Vijay More","seller_type":"Partner Farm","location":"Kolhapur, Maharashtra","price":95,"unit":"kg","quantity":200,"harvest":"2026-10-20","method":"Sustainable farming","progress":45,"fulfillment":"Bulk scheduled delivery","min_order":5,"treatments":"Seller-reported: crop treatment details not yet provided","last_treatment":"Not provided","growing_notes":"Ask seller for details","verification":"Not verified"},
        {"crop":"🌶️ Green Chillies","seller":"Sagar Mehta","seller_type":"Terrace Garden","location":"Vashi, Navi Mumbai","price":30,"unit":"100 g","quantity":10,"harvest":"2026-10-06","method":"Home-grown","progress":85,"fulfillment":"Pickup / neighborhood drop","min_order":1,"treatments":"Seller-reported: no synthetic pesticide use declared","last_treatment":"No treatment date provided","growing_notes":"Home-grown; practices should be confirmed with seller","verification":"Not verified"},
    ]

if "orders" not in st.session_state:
    st.session_state.orders = [
        {"crop":"🥕 Carrots","seller":"Ramesh Patil","quantity":3,"unit":"kg","total":240,"status":"Growing","delivery":"2026-10-12","fulfillment":"Scheduled delivery"}
    ]

if "flash_message" not in st.session_state:
    st.session_state.flash_message = ""

farms = st.session_state.listings
pages = [
    "🏠 Home", "🛒 Explore Produce", "📍 Track My Crop", "📦 My Orders",
    "👨‍🌾 Seller Dashboard", "➕ Become a Seller"
]
st.sidebar.title("🌱 FarmSphere")
page = st.sidebar.radio("Navigate", pages)
st.sidebar.markdown("---")
st.sidebar.info("Know your grower. Understand your food. Eat with confidence.")
if st.session_state.flash_message:
    st.sidebar.success(st.session_state.flash_message)
    st.session_state.flash_message = ""

if page == "🏠 Home":
    st.markdown("""
    <div class="hero">
      <h1>🌱 FarmSphere</h1>
      <p><b>Know your grower. Trust your food.</b></p>
      <p>Buy fresh produce from partner farms and neighborhood terrace gardens—without depending on daily farm-to-door trips.</p>
    </div>
    """, unsafe_allow_html=True)
    farm_count = len({x["seller"] for x in farms if x["seller_type"] == "Partner Farm"})
    garden_count = len({x["seller"] for x in farms if x["seller_type"] == "Terrace Garden"})
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("👨‍🌾 Farm sellers", farm_count)
    c2.metric("🪴 Terrace gardeners", garden_count)
    c3.metric("🥬 Produce listings", len(farms))
    c4.metric("📦 Demo orders", len(st.session_state.orders))
    st.markdown("---")
    st.subheader("Food transparency comes first")
    st.write("FarmSphere is designed to make growing practices visible, so customers can make informed choices instead of relying only on labels such as “natural” or “organic.”")
    t1, t2, t3 = st.columns(3)
    t1.markdown("**🌿 Growing practices**\n\nSee the methods a seller reports using.")
    t2.markdown("**🧪 Treatment disclosure**\n\nCheck whether pesticides or other crop treatments were used and when.")
    t3.markdown("**📅 Crop journey**\n\nView harvest dates, seller details, and availability.")
    st.markdown("---")
    st.subheader("Two ways to buy fresh produce")
    a,b = st.columns(2)
    with a:
        st.markdown("""<div class="card"><h3>🚜 Partner Farms</h3>
        <p>Bulk quantities, planned harvests, and scheduled delivery days.</p>
        <p><b>Best for:</b> weekly vegetables, family orders, and larger quantities.</p></div>""", unsafe_allow_html=True)
    with b:
        st.markdown("""<div class="card"><h3>🪴 Terrace Gardeners</h3>
        <p>Small batches of home-grown vegetables, herbs, and seasonal surplus.</p>
        <p><b>Best for:</b> nearby pickup, neighborhood drops, and small quantities.</p></div>""", unsafe_allow_html=True)
    st.subheader("How FarmSphere reduces logistics costs")
    for title, desc in [
        ("1. Choose a delivery window", "Farm sellers offer planned harvest and delivery days instead of daily collection."),
        ("2. Buy from nearby growers", "Terrace gardeners can serve customers in the same neighborhood."),
        ("3. Consolidate orders", "Customers can use collection points or grouped neighborhood drops where available."),
    ]:
        st.markdown(f"**{title}** — {desc}")
    st.caption("Demo note: seller profiles, inventory, orders, and delivery status are stored in Streamlit session state, not a permanent database.")

elif page == "🛒 Explore Produce":
    st.title("🛒 Explore Fresh Produce")
    st.write("Compare farm and terrace-garden listings. Availability and prices below are sample data.")
    st.info("FarmSphere makes growing-practice and treatment information visible. In this prototype, disclosures are seller-reported and are not proof of pesticide-free status, organic certification, or laboratory testing.")
    f1, f2, f3 = st.columns([1,1,1])
    with f1:
        seller_filter = st.selectbox("Seller type", ["All sellers","Partner Farm","Terrace Garden"])
    with f2:
        search_text = st.text_input("Search crop or seller", placeholder="e.g. spinach, Priya")
    with f3:
        location_filter = st.selectbox("Fulfillment", ["All methods","Scheduled delivery","Bulk scheduled delivery","Pickup / neighborhood drop"])
    filtered = farms
    if seller_filter != "All sellers":
        filtered = [x for x in filtered if x["seller_type"] == seller_filter]
    if search_text.strip():
        q = search_text.strip().lower()
        filtered = [x for x in filtered if q in x["crop"].lower() or q in x["seller"].lower() or q in x["location"].lower()]
    if location_filter != "All methods":
        filtered = [x for x in filtered if x["fulfillment"] == location_filter]
    if not filtered:
        st.info("No listings match these filters. Try a different search.")
    for idx, listing in enumerate(filtered):
        with st.container(border=True):
            left, right = st.columns([3,1])
            with left:
                st.subheader(listing["crop"])
                st.caption(f"{listing['seller_type']} • {listing['location']}")
                st.write(f"**Seller:** {listing['seller']}")
                st.write(f"**Growing method (seller-reported):** {listing['method']}")
                st.write(f"**Pesticide / treatment disclosure:** {listing.get('treatments', 'Not provided')}")
                st.write(f"**Last treatment date:** {listing.get('last_treatment', 'Not provided')}")
                st.write(f"**Growing notes:** {listing.get('growing_notes', 'Ask seller for details')}")
                st.caption(f"Transparency status: {listing.get('verification', 'Not verified')} — seller claims are not independently certified in this demo.")
                st.write(f"**Expected harvest / availability:** {listing['harvest']}")
                st.write(f"**Fulfillment:** {listing['fulfillment']}")
                st.progress(min(listing["progress"],100)/100)
                st.caption(f"Crop progress / readiness: {listing['progress']}%")
            with right:
                st.markdown(f'<div class="price">₹{listing["price"]} / {listing["unit"]}</div>', unsafe_allow_html=True)
                st.write(f"Available: **{listing['quantity']} {listing['unit']}**")
                max_qty = max(1, int(listing["quantity"]))
                quantity = st.number_input("Quantity", min_value=1, max_value=max_qty, value=min(listing["min_order"],max_qty), key=f"qty_{farms.index(listing)}")
                st.caption(f"Minimum order: {listing['min_order']} {listing['unit']}")
                st.write(f"**Total: ₹{quantity * listing['price']}**")
                if st.button("Reserve produce", key=f"reserve_{farms.index(listing)}", type="primary"):
                    if quantity > listing["quantity"]:
                        st.error("Not enough stock available.")
                    else:
                        st.session_state.orders.append({
                            "crop":listing["crop"],"seller":listing["seller"],"quantity":quantity,
                            "unit":listing["unit"],"total":quantity*listing["price"],"status":"Reserved",
                            "delivery":listing["harvest"],"fulfillment":listing["fulfillment"]
                        })
                        listing["quantity"] -= quantity
                        st.success("Reservation added to My Orders.")
                        st.rerun()

elif page == "📍 Track My Crop":
    st.title("📍 Track My Crop")
    if not st.session_state.orders:
        st.info("You have no reservations yet. Explore produce to reserve a crop.")
    else:
        choices = [f"{i+1}. {o['crop']} — {o['seller']}" for i,o in enumerate(st.session_state.orders)]
        selected = st.selectbox("Select an order", range(len(choices)), format_func=lambda i: choices[i])
        order = st.session_state.orders[selected]
        listing = next((x for x in farms if x["crop"] == order["crop"] and x["seller"] == order["seller"]), None)
        st.subheader(order["crop"])
        st.write(f"Seller: **{order['seller']}**")
        st.write(f"Quantity: **{order['quantity']} {order['unit']}**")
        st.write(f"Fulfillment: **{order['fulfillment']}**")
        st.write(f"Expected harvest / availability: **{order['delivery']}**")
        if listing:
            st.progress(listing["progress"]/100)
            st.write(f"Crop progress / readiness: **{listing['progress']}%**")
        st.markdown("### 🌱 Order journey")
        status = order["status"]
        stages = ["Reservation placed","Seller preparing produce","Ready for pickup / dispatch","Completed"]
        current = 0 if status == "Reserved" else 1
        for i, stage in enumerate(stages):
            if i <= current:
                st.success(f"✓ {stage}")
            else:
                st.info(f"○ {stage}")
        st.caption("Tracking is a prototype status flow. Live crop logs, treatment history, independent verification, and seller updates require a database and a verification process.")

elif page == "📦 My Orders":
    st.title("📦 My Orders")
    if not st.session_state.orders:
        st.info("No orders yet. Visit Explore Produce to reserve something.")
    for i, order in enumerate(st.session_state.orders, start=1):
        with st.container(border=True):
            st.subheader(f"Order {i}: {order['crop']}")
            c1,c2,c3 = st.columns(3)
            c1.write(f"**Seller:** {order['seller']}")
            c2.write(f"**Quantity:** {order['quantity']} {order['unit']}")
            c3.write(f"**Total:** ₹{order['total']}")
            st.write(f"**Status:** {order['status']} • **Expected availability:** {order['delivery']}")
            st.caption(f"Fulfillment: {order['fulfillment']}")

elif page == "👨‍🌾 Seller Dashboard":
    st.title("👨‍🌾 Seller Dashboard")
    st.write("Demo dashboard for both partner farmers and terrace gardeners.")
    seller_names = sorted({x["seller"] for x in farms})
    selected_seller = st.selectbox("View seller", seller_names)
    seller_items = [x for x in farms if x["seller"] == selected_seller]
    seller_type = seller_items[0]["seller_type"] if seller_items else "Seller"
    seller_orders = [o for o in st.session_state.orders if o["seller"] == selected_seller]
    m1,m2,m3 = st.columns(3)
    m1.metric("Seller type", seller_type)
    m2.metric("Active listings", len(seller_items))
    m3.metric("Reservations", len(seller_orders))
    st.subheader("Your listings")
    if seller_items:
        st.dataframe([{"Crop":x["crop"],"Available quantity":f'{x["quantity"]} {x["unit"]}',"Price":f'₹{x["price"]}/{x["unit"]}',"Harvest / availability":x["harvest"],"Treatment disclosure":x.get("treatments","Not provided"),"Last treatment":x.get("last_treatment","Not provided"),"Fulfillment":x["fulfillment"]} for x in seller_items], use_container_width=True)
    else:
        st.info("No listings yet.")
    st.markdown("---")
    st.subheader("Add a produce listing")
    with st.form("add_listing_form"):
        crop_name = st.text_input("Produce name", placeholder="e.g. Mint leaves")
        emoji = st.selectbox("Icon", ["🥬","🍅","🥕","🌿","🌶️","🍋","🥒","🍆","🌱"])
        quantity_available = st.number_input("Available quantity", min_value=1, value=5)
        unit = st.selectbox("Unit", ["kg","bunch","piece","100 g","250 g"])
        price = st.number_input("Price (₹ per selected unit)", min_value=1, value=30)
        harvest_date = st.date_input("Harvest / available date", value=date.today()+timedelta(days=1))
        fulfillment = st.selectbox("Fulfillment method", ["Pickup / neighborhood drop","Scheduled delivery","Bulk scheduled delivery"])
        method = st.text_input("Growing method", value="Home-grown")
        treatments = st.text_area("Pesticide / fertilizer / crop-treatment disclosure", placeholder="Describe what you use, or state that details are not known.")
        last_treatment = st.text_input("Date of most recent crop treatment (if applicable)", placeholder="YYYY-MM-DD or Not applicable")
        growing_notes = st.text_area("Additional growing notes", placeholder="Water source, composting, pest management, etc.")
        submitted = st.form_submit_button("Add listing")
    if submitted:
        if not crop_name.strip():
            st.error("Please enter a produce name.")
        else:
            st.session_state.listings.append({
                "crop":f"{emoji} {crop_name.strip()}","seller":selected_seller,"seller_type":seller_type,
                "location":seller_items[0]["location"] if seller_items else "Location not set",
                "price":int(price),"unit":unit,"quantity":int(quantity_available),
                "harvest":harvest_date.isoformat(),"method":method.strip() or "Not specified",
                "progress":100,"fulfillment":fulfillment,"min_order":1,
                "treatments":treatments.strip() or "Not provided by seller",
                "last_treatment":last_treatment.strip() or "Not provided",
                "growing_notes":growing_notes.strip() or "No additional notes",
                "verification":"Seller-reported; not independently verified"
            })
            st.success("Listing added for this session.")
            st.rerun()

elif page == "➕ Become a Seller":
    st.title("➕ Become a FarmSphere Seller")
    st.write("Register as a partner farm or a terrace gardener. This demo collects details for the current session only.")
    st.info("Terrace gardeners can list surplus home-grown produce in small quantities and choose pickup or neighborhood delivery.")
    with st.form("seller_registration"):
        seller_name = st.text_input("Your name")
        seller_type = st.radio("Seller type", ["Terrace Garden","Partner Farm"], horizontal=True)
        location = st.text_input("Neighborhood / city", placeholder="e.g. Kamothe, Navi Mumbai")
        produce = st.text_input("What do you grow?", placeholder="e.g. spinach, coriander, tomatoes")
        capacity = st.selectbox("Typical quantity", ["Small batches (1–10 units)","Medium batches (11–50 units)","Bulk supply (50+ units)"])
        fulfillment = st.selectbox("Preferred fulfillment", ["Pickup / neighborhood drop","Scheduled delivery","Bulk scheduled delivery"])
        method = st.text_input("Growing method", placeholder="e.g. compost, natural pest management, home-grown")
        practices = st.text_area("How do you manage pests and crop health?", placeholder="Mention pesticides, organic sprays, compost, or other treatments used.")
        disclosure_agreement = st.checkbox("I will provide honest, up-to-date information about growing practices and crop treatments.")
        register = st.form_submit_button("Register interest", type="primary")
    if register:
        if not seller_name.strip() or not location.strip() or not produce.strip():
            st.error("Please fill in your name, location, and produce.")
        elif not disclosure_agreement:
            st.error("Please confirm that you will disclose growing practices and crop treatments.")
        else:
            st.session_state.listings.append({
                "crop":f"🌱 {produce.strip()}","seller":seller_name.strip(),"seller_type":seller_type,
                "location":location.strip(),"price":30,"unit":"kg","quantity":5,
                "harvest":(date.today()+timedelta(days=1)).isoformat(),
                "method":method.strip() or "Not specified","progress":100,
                "fulfillment":fulfillment,"min_order":1,
                "treatments":practices.strip() or "Not provided by seller",
                "last_treatment":"Not provided",
                "growing_notes":"Seller onboarding disclosure; details may require follow-up",
                "verification":"Seller-reported; not independently verified"
            })
            st.session_state.flash_message = f"Welcome, {seller_name.strip()}! A sample listing was created."
            st.success("Registration saved for this session and a sample listing was created. Add real onboarding, validation, and persistence before launch.")
            st.caption(f"Declared typical quantity: {capacity}")
