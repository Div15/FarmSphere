# 🌱 FarmSphere

**Know your grower. Understand your food. Eat with confidence.**

FarmSphere is a Streamlit prototype for a food-transparency marketplace. It helps customers explore produce from partner farms and terrace gardeners and learn more about how their food is grown, what crop treatments are reported, when produce is harvested, and who is responsible for growing it.

## Core idea

The primary purpose of FarmSphere is **food transparency and informed choice**. Customers should not have to rely only on a product label or a seller's broad claim. They should be able to view useful details about the crop and its growing journey.

The platform is designed to surface:

- Seller identity and growing location.
- Growing method and crop-care notes.
- Seller-reported pesticide, fertilizer, and other crop-treatment information.
- The date of the most recent treatment, where supplied.
- Expected harvest or availability date.
- Crop progress and available quantity.
- Whether information is seller-reported or independently verified.

FarmSphere can include both **partner farms** and **terrace gardeners**. Local gardeners provide a way to discover small batches of nearby produce, while scheduled farm deliveries and consolidated pickups can help reduce avoidable transport costs. Logistics supports the transparency mission; it is not the main purpose of the platform.

## Problem statement

Customers often have limited visibility into how fresh produce was grown and handled. Broad labels such as “natural,” “chemical-free,” or “organic” can be difficult to assess without clear definitions, documentation, and verification. At the same time, smaller growers may have difficulty reaching customers directly.

FarmSphere explores a marketplace where sellers disclose their growing practices and crop treatments, and customers can compare listings and ask informed questions before reserving produce.

## Features in this prototype

- Home page introducing food transparency and the seller model.
- Browse produce from partner farms and terrace gardeners.
- Filter listings by seller type, search by crop/seller/location, and filter fulfillment method.
- View seller, location, growing method, treatment disclosure, last treatment date, growing notes, harvest date, price, stock, and fulfillment method.
- Reserve produce and calculate order totals.
- Session-based inventory reduction when an order is reserved.
- My Orders page and a basic crop/order tracking flow.
- Seller dashboard for viewing listings and adding produce.
- Become a Seller form for farm sellers and terrace gardeners, including a growing-practice disclosure.
- Clear distinction between seller-reported information and independently verified claims.

## Tech stack

- Python 3.8+
- Streamlit
- Python `datetime`
- Streamlit Session State for prototype data

No external database or API is required for the demo.

## Project structure

```text
farmsphere/
├── app.py
└── README.md
```

## Setup and run

1. Install Python 3.8 or newer.
2. Save the application code as `app.py`.
3. (Recommended) Create and activate a virtual environment.

   **Windows**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install Streamlit:

   ```bash
   pip install streamlit
   ```

5. Start the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL printed in the terminal, usually `http://localhost:8501`.

## How to demo

1. Open **Explore Produce** and compare a farm listing with a terrace-garden listing.
2. Review each listing's growing method, treatment disclosure, last treatment date, and verification status.
3. Reserve produce and verify that it appears in **My Orders** and that the available quantity decreases.
4. Open **Seller Dashboard** and add a listing with crop-care and treatment details.
5. Open **Become a Seller** and submit a sample seller profile with a growing-practice disclosure.

## Transparency and trust: important distinction

A seller disclosure is **not proof** that produce is pesticide-free, chemical-free, organic, safe, or independently tested. “Chemical-free” is also not a scientifically precise description, since all food consists of chemicals. A responsible production version should use clear, specific descriptions of growing practices and distinguish among:

- Seller-reported information.
- Documents reviewed by the platform.
- Independent certification, where applicable.
- Laboratory residue testing, where applicable, including its scope and date.

The app must not label a seller or crop as “verified pesticide-free” unless a clearly defined, credible verification process supports that claim. Treatment information should be accurate, updated, and displayed with appropriate context.

## Logistics approach

Logistics should enable access to produce, not replace the transparency mission:

1. Sellers declare available quantities and harvest dates.
2. Customers choose pickup, neighborhood drop-off, or scheduled delivery where offered.
3. Nearby terrace-garden orders may be collected locally.
4. Farm orders can be grouped by delivery zone and scheduled day.
5. Collection points or community coordinators can consolidate orders where practical.

These are proposed workflows, not logistics services implemented by this prototype.

## Prototype limitations

- Listings, registrations, and orders use `st.session_state`; they are not persisted to a database and may reset when the session ends or the app restarts.
- Seller registration is a demo flow, not a verified onboarding process.
- Prices, sellers, locations, inventory, and harvest dates are illustrative sample data.
- Treatment and growing-practice information is seller-reported sample data, not independently verified.
- No payment gateway, user authentication, notifications, laboratory testing integration, certification verification, or real-time crop monitoring is implemented.
- Crop progress and order statuses are simulated.

## Future enhancements

### Food transparency
- Maintain a dated crop log from sowing through harvest.
- Record pesticide, fertilizer, and crop-treatment details with dates and product names where appropriate.
- Upload supporting documents, certification details, or test reports, with validity dates and clear scope.
- Add seller identity checks and a transparent verification workflow.
- Provide batch IDs or QR codes so customers can open the crop's history.
- Keep a change history so edits to crop records are traceable.
- Add customer questions and seller responses about growing practices.
- Display clear explanations of what each verification label does and does not mean.

### Marketplace and logistics
- Add SQLite or PostgreSQL for persistent users, listings, inventory, and orders.
- Add buyer, farmer, and terrace-gardener roles with authentication.
- Add neighborhood-based discovery and delivery-radius settings.
- Add order cut-off times, delivery slots, and minimum order values.
- Add group ordering and community collection-point management.
- Add payment integration, notifications, and cancellation workflows.

## License

This is an educational/demo project. Add a license before distributing it as an open-source project.
