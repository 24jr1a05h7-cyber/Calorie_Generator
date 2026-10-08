import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SESSION STATE
# ============================================================

if "calculated" not in st.session_state:
    st.session_state.calculated = False

if "bmr" not in st.session_state:
    st.session_state.bmr = 0.0

if "daily_calories" not in st.session_state:
    st.session_state.daily_calories = 0.0

if "activity_factor" not in st.session_state:
    st.session_state.activity_factor = 0.0

if "user_data" not in st.session_state:
    st.session_state.user_data = {}


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN APPLICATION
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(0, 255, 170, 0.12),
                transparent 25%
            ),
            radial-gradient(
                circle at 95% 10%,
                rgba(0, 180, 255, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(255, 193, 7, 0.07),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #06150f 0%,
                #0b2419 50%,
                #06120d 100%
            );

        min-height: 100vh;
    }


    /* ========================================================
       MAIN CONTENT WIDTH
       ======================================================== */

    .block-container {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       GENERAL TEXT VISIBILITY
       ======================================================== */

    body,
    .stApp,
    .stMarkdown,
    .stText,
    p,
    span,
    label {
        color: #f2f7f4;
    }


    /* Markdown text */

    .stMarkdown p {
        color: #e2ebe6 !important;
        line-height: 1.65;
    }


    /* Headings */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #ffffff !important;
    }


    /* Caption */

    .stCaption,
    [data-testid="stCaptionContainer"] {
        color: #c9d7d0 !important;
    }


    /* ========================================================
       MAIN TITLE
       ======================================================== */

    .stApp h1 {
        text-align: center;

        font-size: 48px;

        font-weight: 900;

        margin-bottom: 5px;

        background:
            linear-gradient(
                90deg,
                #00f5a0,
                #00d9f5,
                #ffe259
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }


    /* ========================================================
       TABS
       ======================================================== */

    button[data-baseweb="tab"] {
        color: #dce9e3 !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        padding: 14px 20px !important;

        border-radius: 12px 12px 0 0 !important;
    }


    button[data-baseweb="tab"]:hover {
        color: #ffffff !important;
    }


    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00f5a0 !important;
        font-weight: 800 !important;
    }


    /* ========================================================
       TAB PANEL
       ======================================================== */

    div[data-baseweb="tab-panel"] {
        color: #f2f7f4 !important;
    }


    /* ========================================================
       INPUT LABELS
       ======================================================== */

    div[data-testid="stWidgetLabel"] p {
        color: #f1f7f4 !important;

        font-weight: 600 !important;

        font-size: 15px !important;
    }


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    div[data-baseweb="input"] {
        color: #ffffff !important;
    }


    div[data-baseweb="input"] input {
        color: #ffffff !important;

        background-color: #10281e !important;

        caret-color: #00f5a0 !important;
    }


    div[data-baseweb="input"] input::placeholder {
        color: #aebeb6 !important;
    }


    /* ========================================================
       SELECT BOX
       ======================================================== */

    div[data-baseweb="select"] {
        color: #ffffff !important;
    }


    div[data-baseweb="select"] > div {
        background-color: #10281e !important;

        border:
            1px solid #365548 !important;

        border-radius: 12px !important;

        color: #ffffff !important;
    }


    div[data-baseweb="select"] span {
        color: #ffffff !important;
    }


    /* Dropdown menu */

    ul[role="listbox"] {
        background-color: #10281e !important;
    }


    li[role="option"] {
        color: #ffffff !important;

        background-color: #10281e !important;
    }


    li[role="option"]:hover {
        background-color: #174a35 !important;
    }


    /* ========================================================
       NUMBER INPUT
       ======================================================== */

    div[data-testid="stNumberInput"] button {
        background-color: #17372a !important;

        color: #ffffff !important;

        border-color: #365548 !important;
    }


    div[data-testid="stNumberInput"] button:hover {
        background-color: #20523b !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    div.stButton > button {
        width: 100%;

        min-height: 55px;

        border: none !important;

        border-radius: 16px !important;

        background:
            linear-gradient(
                135deg,
                #00c853,
                #00a884,
                #008fba
            ) !important;

        color: #ffffff !important;

        font-size: 17px !important;

        font-weight: 800 !important;

        letter-spacing: 0.3px;

        box-shadow:
            0 8px 25px rgba(0, 200, 120, 0.25);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    div.stButton > button:hover {
        transform: translateY(-3px);

        box-shadow:
            0 12px 35px rgba(0, 220, 150, 0.40);

        color: #ffffff !important;
    }


    div.stButton > button:active {
        transform: scale(0.98);
    }


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    div[data-testid="stMetric"] {
        background:
            rgba(16, 40, 30, 0.92);

        border:
            1px solid #315545;

        border-radius: 18px;

        padding: 20px;

        box-shadow:
            0 10px 25px rgba(0, 0, 0, 0.25);
    }


    div[data-testid="stMetricLabel"] {
        color: #d0ddd7 !important;
    }


    div[data-testid="stMetricLabel"] p {
        color: #d0ddd7 !important;
    }


    div[data-testid="stMetricValue"] {
        color: #ffe259 !important;

        font-weight: 800 !important;
    }


    div[data-testid="stMetricDelta"] {
        color: #d0ddd7 !important;
    }


    /* ========================================================
       INFO / SUCCESS / WARNING
       ======================================================== */

    div[data-testid="stAlert"] {
        border-radius: 15px;
    }


    div[data-testid="stAlert"] p {
        color: #ffffff !important;

        font-weight: 500;
    }


    /* ========================================================
       CODE BOX
       ======================================================== */

    div[data-testid="stCode"] {
        background-color: #091a12 !important;

        border:
            1px solid #294b3a !important;

        border-radius: 12px;
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    hr {
        border-color:
            rgba(255, 255, 255, 0.15) !important;
    }


    /* ========================================================
       LINKS
       ======================================================== */

    a {
        color: #00f5a0 !important;
    }


    /* ========================================================
       CHECKBOX
       ======================================================== */

    div[data-testid="stCheckbox"] label {
        color: #f2f7f4 !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;

        color: #a8bbb1;

        font-size: 13px;

        margin-top: 40px;

        padding-top: 20px;

        border-top:
            1px solid rgba(255, 255, 255, 0.12);
    }


    /* ========================================================
       MOBILE RESPONSIVE
       ======================================================== */

    @media (max-width: 768px) {

        .stApp h1 {
            font-size: 34px;
        }

        button[data-baseweb="tab"] {
            font-size: 13px !important;

            padding:
                10px 7px !important;
        }

        div[data-testid="stMetric"] {
            padding: 15px;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.title("🥗 Calorie Calculator")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#d5e2dc;
        font-size:17px;
        margin-bottom:25px;
    ">
        Estimate your daily energy requirement using your
        personal and activity information ⚡
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TABS
# ============================================================

calculator_tab, results_tab, guide_tab = st.tabs(
    [
        "🧮 Calculator",
        "📊 Results",
        "💡 Guide"
    ]
)


# ============================================================
# CALCULATOR TAB
# ============================================================

with calculator_tab:

    st.header("👤 Personal Details")

    st.caption(
        "Enter your information to calculate an estimated "
        "daily energy requirement."
    )

    st.divider()


    # --------------------------------------------------------
    # PERSONAL DETAILS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        age = st.number_input(
            "🎂 Age",
            min_value=18,
            max_value=100,
            value=18,
            step=1
        )


        height = st.number_input(
            "📏 Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.5
        )


    with col2:

        gender = st.selectbox(
            "⚧ Sex used for calculation",
            [
                "Male",
                "Female"
            ]
        )


        weight = st.number_input(
            "⚖️ Weight (kg)",
            min_value=25.0,
            max_value=250.0,
            value=65.0,
            step=0.5
        )


    st.divider()


    # --------------------------------------------------------
    # ACTIVITY DETAILS
    # --------------------------------------------------------

    st.header("🏃 Activity Details")

    st.caption(
        "Select the activity level that best represents "
        "your usual routine."
    )


    activity_options = {

        "🪑 Sedentary": {
            "description":
                "Little or no regular exercise",
            "factor":
                1.20
        },

        "🚶 Lightly Active": {
            "description":
                "Light exercise around 1–3 days/week",
            "factor":
                1.375
        },

        "🏃 Moderately Active": {
            "description":
                "Moderate exercise around 3–5 days/week",
            "factor":
                1.55
        },

        "🏋️ Very Active": {
            "description":
                "Hard exercise around 6–7 days/week",
            "factor":
                1.725
        },

        "🔥 Extremely Active": {
            "description":
                "Very demanding physical activity",
            "factor":
                1.90
        }
    }


    activity = st.selectbox(
        "🔥 Activity Level",
        list(activity_options.keys())
    )


    st.info(
        "💡 " + activity_options[activity]["description"]
    )


    st.write("")


    # --------------------------------------------------------
    # CALCULATE BUTTON
    # --------------------------------------------------------

    left_space, button_area, right_space = st.columns(
        [1, 2, 1]
    )


    with button_area:

        calculate_button = st.button(
            "⚡  CALCULATE MY REQUIREMENT",
            use_container_width=True
        )


    # --------------------------------------------------------
    # CALCULATION
    # --------------------------------------------------------

    if calculate_button:

        # Mifflin-St Jeor equation

        if gender == "Male":

            bmr = (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                + 5
            )

        else:

            bmr = (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                - 161
            )


        activity_factor = (
            activity_options[activity]["factor"]
        )


        daily_calories = (
            bmr * activity_factor
        )


        # Save values

        st.session_state.bmr = bmr

        st.session_state.daily_calories = daily_calories

        st.session_state.activity_factor = (
            activity_factor
        )


        st.session_state.user_data = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "activity": activity
        }


        st.session_state.calculated = True


        st.success(
            "✅ Calculation completed successfully! "
            "Open the 📊 Results tab."
        )


# ============================================================
# RESULTS TAB
# ============================================================

with results_tab:

    if not st.session_state.calculated:

        st.header("📊 Your Results")

        st.info(
            "No result has been calculated yet."
        )

        st.write(
            "Go to the 🧮 Calculator tab, enter your details, "
            "and click the calculation button."
        )


    else:

        daily_calories = (
            st.session_state.daily_calories
        )

        bmr = st.session_state.bmr

        activity_factor = (
            st.session_state.activity_factor
        )

        user_data = (
            st.session_state.user_data
        )


        # ----------------------------------------------------
        # MAIN RESULT
        # ----------------------------------------------------

        st.header(
            "⚡ Estimated Daily Energy Requirement"
        )


        st.metric(
            label="Your estimated daily requirement",
            value=f"{daily_calories:,.0f} kcal/day"
        )


        st.success(
            f"🎉 Estimated requirement: "
            f"{daily_calories:,.0f} kcal/day"
        )


        st.divider()


        # ----------------------------------------------------
        # RESULT METRICS
        # ----------------------------------------------------

        metric1, metric2, metric3 = st.columns(3)


        with metric1:

            st.metric(
                label="🔥 Estimated BMR",
                value=f"{bmr:,.0f} kcal"
            )


        with metric2:

            st.metric(
                label="🏃 Activity Factor",
                value=f"{activity_factor}"
            )


        with metric3:

            st.metric(
                label="🎂 Age",
                value=f"{user_data['age']} years"
            )


        st.divider()


        # ----------------------------------------------------
        # USER INFORMATION
        # ----------------------------------------------------

        st.header("📋 Your Entered Information")


        information_col1, information_col2 = (
            st.columns(2)
        )


        with information_col1:

            st.write(
                f"**🎂 Age:** "
                f"{user_data['age']} years"
            )

            st.write(
                f"**⚧ Sex:** "
                f"{user_data['gender']}"
            )

            st.write(
                f"**📏 Height:** "
                f"{user_data['height']} cm"
            )


        with information_col2:

            st.write(
                f"**⚖️ Weight:** "
                f"{user_data['weight']} kg"
            )

            st.write(
                f"**🏃 Activity:** "
                f"{user_data['activity']}"
            )


        st.divider()


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        st.header("💡 Simple Interpretation")


        st.info(
            f"Based on the information entered, your "
            f"estimated daily energy requirement is "
            f"approximately {daily_calories:,.0f} kcal/day."
        )


        st.warning(
            "⚠️ This is an educational estimate. Actual "
            "energy needs can vary between individuals. "
            "It should not be treated as medical or "
            "dietary advice."
        )


        st.write("")


        # ----------------------------------------------------
        # RESET BUTTON
        # ----------------------------------------------------

        reset_left, reset_button, reset_right = (
            st.columns([1, 2, 1])
        )


        with reset_button:

            reset_clicked = st.button(
                "🔄  START NEW CALCULATION",
                use_container_width=True
            )


            if reset_clicked:

                st.session_state.calculated = False

                st.session_state.bmr = 0.0

                st.session_state.daily_calories = 0.0

                st.session_state.activity_factor = 0.0

                st.session_state.user_data = {}

                st.rerun()


# ============================================================
# GUIDE TAB
# ============================================================

with guide_tab:

    st.header("💡 How This Calculator Works")

    st.caption(
        "A simple explanation of the calculation process."
    )

    st.divider()


    # --------------------------------------------------------
    # STEP 1
    # --------------------------------------------------------

    st.subheader("🔥 Step 1 — BMR")

    st.write(
        "BMR means Basal Metabolic Rate. It is an estimate "
        "of the energy required for basic body functions "
        "while at rest."
    )


    st.divider()


    # --------------------------------------------------------
    # STEP 2
    # --------------------------------------------------------

    st.subheader("🏃 Step 2 — Activity Level")

    st.write(
        "An activity factor is selected according to the "
        "activity level entered by the user."
    )


    st.divider()


    # --------------------------------------------------------
    # STEP 3
    # --------------------------------------------------------

    st.subheader("🧮 Step 3 — Estimated Requirement")

    st.write(
        "The application multiplies the estimated BMR by "
        "the selected activity factor."
    )


    st.code(
        """
Estimated Daily Energy Requirement
        =
Estimated BMR × Activity Factor
        """,
        language="text"
    )


    st.divider()


    # --------------------------------------------------------
    # IMPORTANT INFORMATION
    # --------------------------------------------------------

    st.subheader("⚠️ Important Information")

    st.warning(
        "This application provides an educational estimate. "
        "Individual energy needs can vary. It is not medical "
        "advice or a personalized treatment plan."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🥗 Calorie Calculator • Built with Python + Streamlit • "
    "No database used"
)