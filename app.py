import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="FarmSphere", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.hero{padding:35px;border-radius:20px;background:linear-gradient(135deg,#dff3df,#f5fff5);margin-bottom:25px}
.hero h1{color:#245c35;font-size:46px;margin-bottom:5px}
.hero p{font-size:19px;color:#48604d;margin:2px 0}
.price{font-size:24px;font-weight:bold;color:#287a3d}
.badge{display:inline-block;padding:3px 10px;border-radius:12px;font-size:13px;margin-right:6px;background:#eaf7ea;color:#286638;font-weight:600}
.badge.terrace{background:#fff3d6;color:#8a5a00}
.badge.lab{background:#e1ecff;color:#1d4f9c}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------- CONSTANTS
HUBS = ["Andheri West", "Bandra", "Powai", "Thane"]
PRACTICES = [
    "No synthetic pesticides", "No chemical fertilizers", "Compost / vermicompost only",
    "Neem / bio-pesticide only", "Native / open-pollinated seeds", "Rainwater harvesting",
]
VERIF = {"Self-declared": 45, "Community-verified": 70, "Lab-tested": 88}
STAGES = [("🌱", "Seed planted", 0), ("🌿", "Growing", 30), ("🌼", "Flowering", 50),
          ("🧺", "Ready to harvest", 85), ("📦", "At your hub", 100)]


def next_day(weekday):
    d = date.today() + timedelta(days=1)
    while d.weekday() != weekday:
        d += timedelta(days=1)
    return d


SLOTS = [f"Tue {next_day(1):%d %b}", f"Sat {next_day(5):%d %b}"]


def L(id, emoji, crop, seller, stype, loc, price, stock, harvest_days, progress,
      method, verif, practices, log):
    return dict(id=id, emoji=emoji, crop=crop, seller=seller, type=stype, loc=loc,
                price=price, stock=stock, reserved=0, harvest=date.today() + timedelta(days=harvest_days),
                progress=progress, method=method, verif=verif, practices=practices, log=log)


def init():
    if "listings" in st.session_state:
        return
    t = date.today()
    d = lambda n: (t - timedelta(days=n)).strftime("%d %b")
    st.session_state.listings = [
        L(1, "🥕", "Carrots", "Ramesh Patil", "Farm", "Nashik", 80, 120, 6, 65, "Natural farming",
          "Lab-tested", PRACTICES[:5], [(d(20), "Vermicompost applied"), (d(9), "Neem spray (bio)")]),
        L(2, "🍅", "Tomatoes", "Sunita Jadhav", "Farm", "Pune", 60, 150, 4, 50, "Organic farming",
          "Community-verified", PRACTICES[:4], [(d(14), "Cow-dung slurry"), (d(5), "Neem spray (bio)")]),
        L(3, "🥬", "Spinach", "Mahesh Shinde", "Farm", "Satara", 40, 80, 3, 85, "Organic farming",
          "Lab-tested", PRACTICES[:3], [(d(10), "Compost top-dressing")]),
        L(4, "🌾", "Rice", "Vijay More", "Farm", "Kolhapur", 95, 300, 11, 45, "Sustainable farming",
          "Community-verified", [PRACTICES[0], PRACTICES[1], PRACTICES[5]], [(d(30), "Green manure")]),
        L(5, "🌿", "Coriander & Mint", "Meera Kulkarni", "Terrace Garden", "Powai", 30, 4, 2, 90, "Container organic",
          "Community-verified", PRACTICES[:3], [(d(7), "Vermicompost"), (d(3), "Soap-nut spray")]),
        L(6, "🌶️", "Green Chillies", "Anil D'Souza", "Terrace Garden", "Bandra", 70, 3, 3, 80, "Grow-bags, compost",
          "Self-declared", PRACTICES[:2], [(d(12), "Kitchen-compost mix")]),
        L(7, "🍆", "Brinjal", "Farah Sheikh", "Terrace Garden", "Andheri West", 55, 6, 5, 70, "Container organic",
          "Self-declared", PRACTICES[:4], [(d(6), "Neem oil spray")]),
    ]
    st.session_state.cart = []
    st.session_state.orders = []
    st.session_state.route_fill = {(h, s): n for (h, s), n in zip(
        [(h, s) for h in HUBS for s in SLOTS], [6, 3, 8, 4, 2, 9, 5, 1])}


init()
S = st.session_state


def trust(l):
    return min(100, VERIF[l["verif"]] + 2 * len(l["practices"]))


def avail(l):
    return l["stock"] - l["reserved"]


def badges(l):
    cls = "terrace" if l["type"] == "Terrace Garden" else ""
    icon = "🏡" if cls else "🚜"
    out = f'<span class="badge {cls}">{icon} {l["type"]}</span>'
    out += f'<span class="badge {"lab" if l["verif"] == "Lab-tested" else ""}">✔ {l["verif"]}</span>'
    return out


def delivery_fee(subtotal, hub, slot):
    fill = S.route_fill[(hub, slot)]
    if subtotal >= 500 or fill >= 10:
        return 0
    return 20 if fill >= 5 else 40


# ---------------------------------------------------------------- SIDEBAR
st.sidebar.title("🌱 FarmSphere")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", "🛒 Explore Produce", f"🧺 Cart ({len(S.cart)})", "📍 Track My Crop",
    "📦 My Orders", "🏡 Become a Seller", "👨‍🌾 Seller Dashboard", "🚚 How We Keep Logistics Lean"])
st.sidebar.markdown("---")
st.sidebar.info("Chemical-free food you can verify. Know the grower, see the grow log, "
                "and get it from a hub near you.")

# ---------------------------------------------------------------- HOME
if page == "🏠 Home":
    st.markdown("""<div class="hero"><h1>🌱 FarmSphere</h1>
    <p>Know your grower. Trust your food.</p>
    <p>Pesticide-free produce from farms and neighbourhood terrace gardens, with a full "Food Passport" for every crop.</p></div>""",
                unsafe_allow_html=True)
    ls = S.listings
    c = st.columns(4)
    c[0].metric("Growers", len({l["seller"] for l in ls}))
    c[1].metric("🚜 Farms", sum(l["type"] == "Farm" for l in ls))
    c[2].metric("🏡 Terrace gardens", sum(l["type"] == "Terrace Garden" for l in ls))
    c[3].metric("Pickup hubs", len(HUBS))
    st.markdown("---")
    st.subheader("The FarmSphere Promise")
    a, b, c = st.columns(3)
    a.markdown("### 🔍 Food Passport\nSee practices, input log and verification level for every listing.")
    b.markdown("### 🧪 Verified, not just claimed\nSelf-declared → community-verified → lab-tested residue reports.")
    c.markdown("### 🏡 Hyperlocal + 🚜 Farm\nTerrace gardeners supply your neighbourhood; farms supply volume.")
    st.markdown("---")
    st.subheader("How it works")
    cols = st.columns(4)
    for col, (n, t, dsc) in zip(cols, [
        ("1️⃣", "Pre-order", "Pick produce and a delivery day (Tue / Sat)."),
        ("2️⃣", "Harvest to order", "Growers harvest only what's ordered. Less waste."),
        ("3️⃣", "Pool at hub", "Farm trucks and terrace drop-offs meet at a neighbourhood hub."),
        ("4️⃣", "Collect or deliver", "Pick up at the hub or get one pooled, low-cost delivery.")]):
        with col.container(border=True):
            st.markdown(f"## {n}\n**{t}**\n\n{dsc}")

# ---------------------------------------------------------------- EXPLORE
elif page == "🛒 Explore Produce":
    st.title("🛒 Explore Produce")
    f1, f2, f3 = st.columns(3)
    types = f1.multiselect("Grower type", ["Farm", "Terrace Garden"], default=["Farm", "Terrace Garden"])
    min_v = f2.selectbox("Minimum verification", list(VERIF.keys()))
    near = f3.selectbox("Prefer my area", ["Any"] + HUBS)

    items = [l for l in S.listings if l["type"] in types and VERIF[l["verif"]] >= VERIF[min_v]]
    if near != "Any":
        items.sort(key=lambda l: l["loc"] != near)
    if not items:
        st.warning("No produce matches these filters.")

    for l in items:
        with st.container(border=True):
            left, mid, right = st.columns([3, 2, 2])
            with left:
                st.markdown(f"### {l['emoji']} {l['crop']}")
                st.markdown(badges(l), unsafe_allow_html=True)
                st.write(f"👤 **{l['seller']}** · 📍 {l['loc']} · 🌱 {l['method']}")
                st.markdown(f"<span class='price'>₹{l['price']} / kg</span>", unsafe_allow_html=True)
            with mid:
                st.write(f"🛡️ Trust score: **{trust(l)}/100**")
                st.progress(trust(l) / 100)
                st.write(f"Growth {l['progress']}% · harvest ~{l['harvest']:%d %b}")
                st.progress(l["progress"] / 100)
            with right:
                a = avail(l)
                if a <= 0:
                    st.error("Fully booked for this cycle")
                else:
                    st.caption(f"{a} kg still available this cycle")
                    q = st.number_input("kg", 1, min(a, 20), min(2, a), key=f"q{l['id']}")
                    if st.button("Add to cart", key=f"add{l['id']}", type="primary"):
                        S.cart.append((l["id"], q))
                        st.toast(f"Added {q} kg {l['crop']}")
            with st.expander("📘 Food Passport"):
                st.write("**Growing practices**")
                for p in l["practices"]:
                    st.write(f"✅ {p}")
                st.write("**Input / spray log**")
                for dt, note in l["log"]:
                    st.write(f"🗓️ {dt}: {note}")
                if l["verif"] == "Lab-tested":
                    st.success("Latest pesticide-residue report: none detected")
                elif l["verif"] == "Community-verified":
                    st.info("Visited and verified by a FarmSphere community volunteer")
                else:
                    st.warning("Grower's own declaration. Verification pending.")

# ---------------------------------------------------------------- CART
elif page.startswith("🧺"):
    st.title("🧺 Your Cart")
    if not S.cart:
        st.info("Your cart is empty. Explore produce to add items.")
    else:
        by_id = {l["id"]: l for l in S.listings}
        subtotal = 0
        for i, (lid, q) in enumerate(S.cart):
            l = by_id[lid]
            subtotal += l["price"] * q
            c1, c2 = st.columns([5, 1])
            c1.write(f"{l['emoji']} **{l['crop']}** from {l['seller']} · {q} kg · ₹{l['price'] * q}")
            if c2.button("Remove", key=f"rm{i}"):
                S.cart.pop(i)
                st.rerun()
        st.markdown("---")
        c1, c2 = st.columns(2)
        hub = c1.selectbox("Pickup / delivery hub", HUBS)
        slot = c2.selectbox("Delivery day", SLOTS)
        fill = S.route_fill[(hub, slot)]
        fee = delivery_fee(subtotal, hub, slot)
        st.progress(min(fill, 10) / 10)
        st.caption(f"{fill}/10 orders on this route. Delivery fee drops as more neighbours join "
                   f"(free at 10 orders or ₹500+).")
        mode = st.radio("How do you get it?", ["Collect from hub (free)", "Pooled home delivery"], horizontal=True)
        fee = 0 if mode.startswith("Collect") else fee
        st.info(f"Subtotal ₹{subtotal} + delivery ₹{fee} = **₹{subtotal + fee}**")
        if st.button("✅ Place Order", type="primary"):
            for lid, q in S.cart:
                by_id[lid]["reserved"] += q
            S.orders.append(dict(items=[(by_id[lid]["crop"], by_id[lid]["emoji"], by_id[lid]["seller"], q,
                                          by_id[lid]["id"]) for lid, q in S.cart],
                                 hub=hub, slot=slot, mode=mode, total=subtotal + fee))
            S.route_fill[(hub, slot)] += 1
            S.cart = []
            st.success("Order placed. Growers will harvest to order for your slot.")
            st.balloons()

# ---------------------------------------------------------------- TRACK
elif page == "📍 Track My Crop":
    st.title("📍 Track My Crop")
    names = {f"{l['emoji']} {l['crop']} · {l['seller']}": l for l in S.listings}
    l = names[st.selectbox("Select crop", list(names))]
    st.markdown(badges(l), unsafe_allow_html=True)
    st.write(f"**{l['seller']}** · {l['loc']} · {l['method']}")
    st.progress(l["progress"] / 100)
    st.write(f"Growth: **{l['progress']}%** · Expected harvest **{l['harvest']:%d %b %Y}**")
    st.subheader("Crop journey")
    for icon, name, threshold in STAGES:
        (st.success if l["progress"] >= threshold and threshold < 100 else st.info)(
            f"{icon} {name}{' ✓' if l['progress'] >= threshold and threshold < 100 else ''}")
    st.subheader("🧾 What went into this crop")
    for dt, note in l["log"]:
        st.write(f"🗓️ {dt}: {note}")
    st.caption("Growers post updates from the field. Customers with an order get notified.")

# ---------------------------------------------------------------- ORDERS
elif page == "📦 My Orders":
    st.title("📦 My Orders")
    if not S.orders:
        st.info("No orders yet.")
    for o in reversed(S.orders):
        with st.container(border=True):
            st.markdown(f"**{o['slot']}** · {o['hub']} · {o['mode']} · **₹{o['total']}**")
            for crop, emoji, seller, q, _ in o["items"]:
                st.write(f"{emoji} {crop} · {q} kg · {seller}")
            st.success("✓ Order confirmed")
            st.info("⏳ Harvest-to-order pending")
            st.info("⏳ Arrival at hub pending")

# ---------------------------------------------------------------- BECOME A SELLER
elif page == "🏡 Become a Seller":
    st.title("🏡 Become a Seller")
    st.write("Grow on a terrace, balcony or small plot? Sell your surplus to neighbours. "
             "No trucks, just drop it at your nearest hub on delivery day.")
    with st.form("seller"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Your name")
        stype = c2.selectbox("I grow on a", ["Terrace Garden", "Farm"])
        crop = c1.text_input("Crop (e.g. Methi)")
        emoji = c2.text_input("Emoji", "🥬", max_chars=2)
        hub = c1.selectbox("Nearest hub", HUBS)
        price = c2.number_input("Price per kg (₹)", 10, 500, 50)
        stock = c1.number_input("Expected harvest (kg)", 1, 500, 5)
        days = c2.number_input("Ready in (days)", 1, 120, 7)
        practices = st.multiselect("Practices you follow", PRACTICES)
        note = st.text_input("Last input applied (e.g. 'Vermicompost, 3 days ago')")
        pledge = st.checkbox("I confirm I use no synthetic pesticides or chemical fertilizers, "
                             "and I agree to a photo check or a community visit.")
        if st.form_submit_button("List my produce", type="primary"):
            if not (name and crop and practices and pledge):
                st.error("Please add your name, crop, at least one practice, and accept the pledge.")
            else:
                S.listings.append(L(max(l["id"] for l in S.listings) + 1, emoji, crop, name, stype, hub,
                                    price, stock, days, 10, "Chemical-free", "Self-declared", practices,
                                    [(date.today().strftime("%d %b"), note or "Listing created")]))
                st.success("Listed! You start as Self-declared. Get a volunteer visit or a lab test "
                           "to earn a higher trust score and more visibility.")
    st.subheader("Trust ladder")
    for k, v in VERIF.items():
        st.write(f"**{k}**: base trust {v}/100")

# ---------------------------------------------------------------- SELLER DASHBOARD
elif page == "👨‍🌾 Seller Dashboard":
    st.title("👨‍🌾 Seller Dashboard")
    sellers = sorted({l["seller"] for l in S.listings})
    me = st.selectbox("Viewing as", sellers)
    mine = [l for l in S.listings if l["seller"] == me]
    c = st.columns(3)
    c[0].metric("Reserved (kg)", sum(l["reserved"] for l in mine))
    c[1].metric("Expected revenue", f"₹{sum(l['reserved'] * l['price'] for l in mine)}")
    c[2].metric("Avg trust score", round(sum(trust(l) for l in mine) / len(mine)))
    st.subheader("🧺 Harvest-to-order list")
    st.dataframe([{"Crop": l["crop"], "Pre-ordered kg": l["reserved"], "Listed kg": l["stock"],
                   "Harvest by": f"{l['harvest']:%d %b}", "Drop-off": "Farm truck" if l["type"] == "Farm" else l["loc"] + " hub"}
                  for l in mine], use_container_width=True)
    st.caption("Harvest only the pre-ordered quantity. Anything extra is listed for the next cycle.")
    st.subheader("🤖 Demand insight")
    for l in mine:
        ratio = l["reserved"] / l["stock"]
        if ratio > 0.7:
            st.warning(f"{l['crop']}: {int(ratio * 100)}% booked. Consider listing more next cycle.")
        elif ratio < 0.2:
            st.info(f"{l['crop']}: low bookings so far. Lower the price slightly or share an update with followers.")

# ---------------------------------------------------------------- LOGISTICS
elif page == "🚚 How We Keep Logistics Lean":
    st.title("🚚 How We Keep Logistics Lean")
    st.markdown("""
- **Fixed delivery days (Tue / Sat), not daily.** Growers harvest once per cycle.
- **Harvest to order.** Orders close before harvest, so there is no stock guessing and little waste.
- **Neighbourhood hubs.** One consolidated farm truck per hub. Terrace gardeners walk their produce over.
- **Route pooling.** Delivery fees fall as more neighbours join the same route.
- **Terrace gardens fill the gaps.** Leafy greens, herbs and chillies come from within a few km, cutting long-haul trips.
""")
    st.subheader("Route fill by hub and day")
    rows = [{"Hub": h, "Day": s, "Orders": S.route_fill[(h, s)],
             "Fee for ₹300 order": f"₹{delivery_fee(300, h, s)}"} for h in HUBS for s in SLOTS]
    st.dataframe(rows, use_container_width=True)
    st.subheader("Illustrative cost per kg")
    c1, c2 = st.columns(2)
    c1.metric("Daily direct delivery", "₹18 / kg")
    c2.metric("Pooled twice-weekly", "₹6 / kg", "-67%")
    st.caption("Example figures to show the effect of pooling. Replace with your real trip costs.")
