import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="A Rehman Projects Hub",
    page_icon="🚀",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

#MainMenu, header, footer {
    visibility: hidden;
    
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%);
    color: #1e293b;
    border: 1px solid #c7d2fe;
}

.block-container {
    padding: 2rem 3rem;
    max-width: none;
    color:#000000;
}

h1, h2, h3 {
    color:#000000;
    font-family: 'Inter', sans-serif;
}

.card {
    color:#000000;
    background: white;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}

.stButton > button {
    width: 100%;
    padding: 14px 18px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    color: white;
    font-weight: 600;
}
/* Metric label */
[data-testid="stMetricLabel"] {
    font-weight: 700 !important;
    font-size: 16px !important;
}

/* Metric value */
[data-testid="stMetricValue"] {
    font-weight: 800 !important;
    font-size: 22px !important;
}

/* Delta text */
[data-testid="stMetricDelta"] {
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page):
    st.session_state.page = page
    st.rerun()

# =====================================================
# DATA SOURCES
# =====================================================

CSV_FILES = {
    "Dental clinic": "https://docs.google.com/spreadsheets/d/1ktUxErd0fS5bdjT4lAkIa6v4tOmRmm9hysTXSpp_mK4/export?format=csv",
    "Hospital": "https://docs.google.com/spreadsheets/d/1xZ2pqjm8RHBWlVIimvBuXPq6UFe4-bL8C4CLfjJHIYA/export?format=csv",
    "Law firm or Advocate firm": "https://docs.google.com/spreadsheets/d/12I5HbsV3d3bDmzM_jUSBlGe1awYfRmW37juPWK0bjhg/export?format=csv",
    "Real Estate": "https://docs.google.com/spreadsheets/d/1j3wnQ25wog9QB_wUoXyXYRAWUUESzHfeRelvwYVahOM/export?format=csv",
    "Coaching Classes/Tutions": "https://docs.google.com/spreadsheets/d/10_Y-GEXHApcWO7Y9ddbTiUvOZv3aWQ_XIjk-ydJFC0s/export?format=csv",
    "CA Firms": "https://docs.google.com/spreadsheets/d/1dxhtJ47-3sh1ab4vvHhrxF904rCvxf63n-UpV2ZO85I/export?format=csv"
}

@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        df.columns = df.columns.str.strip()
        return df
    except:
        return pd.DataFrame()

def get_sheet_url(csv_url):
    return csv_url.replace("/export?format=csv", "/edit")

def interns():
        df0 = pd.read_csv("https://docs.google.com/spreadsheets/d/1qLmeLGtUVxjhJScYqY35vzNZEngsisQfTte6zYfxmoQ/export?format=csv",header=4)
        df0 = df0.iloc[:, 2:]
        st.dataframe(df0)

def form():

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <a href="https://docs.google.com/forms/d/e/1FAIpQLScHz7fdRGl0RbMTyh_8N5VH9G0K1LDsszsZRqwHMe9CsXcqlA/viewform" target="_blank">
                <button style="
                    width:100%;
                    padding:14px;
                    border-radius:12px;
                    background:linear-gradient(135deg, #8b5cf6, #ec4899);
                    color:white;
                    border:2px solid #000000;
                    font-weight:600;
                    cursor:pointer;
                ">
                    Attendance Form
                </button>
            </a>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <a href="https://docs.google.com/forms/d/e/1FAIpQLScsuKWWQGPPrSVhQwJGj0r1ADWS0QyAtgrxJ-V_3z8yhV32YQ/viewform?usp=send_form" target="_blank">
                <button style="
                    width:100%;
                    padding:14px;
                    border-radius:12px;
                    background:linear-gradient(135deg, #8b5cf6, #ec4899);
                    color:white;
                    border:2px solid #000000;
                    font-weight:600;
                    cursor:pointer;
                ">
                    Team Leader Attendance Form
                </button>
            </a>
            """, unsafe_allow_html=True)
        
        st.markdown("")
        
        st.markdown("""
            <a href="https://my-app-app-og6fmsc6u66nmh2bn5qodx.streamlit.app/" target="_blank">
                <button style="
                    width:100%;
                    padding:14px;
                    border-radius:12px;
                    background:linear-gradient(135deg, #8b5cf6, #ec4899);
                    color:white;
                    border:2px solid #000000;
                    font-weight:600;
                    cursor:pointer;
                ">
                    Interns Status
                </button>
            </a>
            """, unsafe_allow_html=True)
        
        
    


# =====================================================
# HOME
# =====================================================

if st.session_state.page == "home":
    
    

    

    # st.title("🚀Internship Report")
    st.markdown("""
    <div class="card" style="margin-bottom:20px;">
        <h2 style="margin:0; color:#111827;">Intenship Report</h2>
        <p style="margin-top:8px; color:#6b7280; font-size:15px;">
            A centralized dashboard system to explore business data, game analytics, and club insights.
            Built for fast navigation and clean analytics experience.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Internship Projects")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="margin:0;">🤖 Club Data</h3>
           <p style="margin-top:8px; color:#000; font-size:13px;">
                Analyze school clubs, sponsors, budgets, and participation insights.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Open Club Data", use_container_width=True, on_click=lambda: go("club"))

    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="margin:0;">📊 Business Dashboard</h3>
            <p style="margin-top:8px; color:#6b7280; font-size:13px;">
                Explore business leads, domains, cities, and contact intelligence.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Open Business Dashboard", use_container_width=True, on_click=lambda: go("business"))

    with col3:
        st.markdown("""
        <div class="card">
            <h3 style="margin:0;">🎮 Game Analysis</h3>
            <p style="margin-top:8px; color:#6b7280; font-size:13px;">
                Filter and analyze games by category, title, and quality metrics.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Open Game Analysis", use_container_width=True, on_click=lambda: go("game"))

    

    with st.expander("Login Credentials (CJN)"):

        # st.markdown("### Login Credentials (CJN)")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("#### Admin Credentials")
            st.code("cjn.rehmantade331@gmail.com")

        with col2:
            st.markdown("#### Password")
            st.code("Pass@143")

        with col3:
            st.markdown("#### Website")
            st.code("https://cjnnow.com/admin")  
        
        col1, col2,col3 = st.columns(3)

        with col1:
            st.markdown(" #### College Credientials")
            st.code("admin@nkorchid.com")

        with col2:
            st.markdown("#### Password")
            st.code("Pass@143")
        with col3:
            st.markdown("#### Website")
            st.code("https://cjnnow.com/school-admin-login")         # st.status("copied")



    st.markdown(" ### Interns Attendace")
    interns()
    form()
    st.stop()


# =====================================================
# GAME PAGE (UNCHANGED)
# =====================================================

elif st.session_state.page == "game":

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back"):
            st.session_state.page = "home"
            st.rerun()
        st.title(" Game Analysis Dashboard")
    with col2:
        # st.write("")

        pass

    @st.cache_data
    def load_game_data():
        return pd.read_csv("https://docs.google.com/spreadsheets/d/1KXFlUwUnplUFtbrVZqvmSmZXhnLZZtta1qcY1xcCP0g/export?format=csv")

    df = load_game_data()

    

    st.divider()
    ################################################### 
    game_col1,game_col2=st.columns(2)
    with game_col1:
        search = st.text_input("Search Game Title")
    with game_col2:
        category = st.selectbox("Category", ["All"] + list(df["Category"].dropna().unique()))

    filtered = df.copy()

    if search:
        filtered = filtered[filtered["Game Title"].str.contains(search, case=False)]

    if category != "All":
        filtered = filtered[filtered["Category"] == category]

    
    col1,col2=st.columns(2)
    with col1:
        st.image(
                    "Game Analysis.png",   # replace with your image path
                    use_container_width=True
                )
    with col2:
        st.markdown("")



    st.dataframe(filtered, use_container_width=True)

# =====================================================
# BUSINESS DASHBOARD (REPLACED - FINAL VERSION)
# =====================================================

elif st.session_state.page == "business":


    
    


    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back"):
            st.session_state.page = "home"
            st.rerun()
        st.title(" Business Leads Dashboard")

    with col2:
    # st.write("")
     pass
    st.caption("By A Rehman")

    tabs = st.tabs(list(CSV_FILES.keys()))

    def card(col, title, value, color):
        with col:
            st.markdown(f"""
            <div style="
                background:{color};
                padding:16px;
                border-radius:14px;
                text-align:center;
            ">
                <div style="font-size:13px;color:#374151">{title}</div>
                <div style="font-size:22px;font-weight:700;color:#111827">{value}</div>
            </div>
            """, unsafe_allow_html=True)

        

    for tab, (name, url) in zip(tabs, CSV_FILES.items()):

        with tab:

            df = load_data(url)

            if df.empty:
                st.warning("⚠️ Data not available")

                continue

            # =================================================
            # KPI CARDS
            # =================================================

            c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

            card(c1, "Total", len(df), "#eef2ff")
            card(c2, "Domains", df["Buisness Domain"].nunique() if "Buisness Domain" in df else 0, "#ecfeff")
            card(c3, "Cities", df["City, State"].nunique() if "City, State" in df else 0, "#f0fdf4")
            card(c4, "Emails", df["Email"].notna().sum() if "Email" in df else 0, "#fff7ed")
            card(c5, "Contacts", df["Contact No"].notna().sum() if "Contact No" in df else 0, "#fef2f2")
            card(c6, "Maps", df["Link Of Google Map"].notna().sum() if "Link Of Google Map" in df else 0, "#f5f3ff")
            card(c7, "Web", df["Website / Social"].notna().sum() if "Website / Social" in df else 0, "#f0f9ff")

            st.divider()

            # =================================================
            # IMAGE SECTION
            # =================================================

            col1,col2=st.columns(2)
            with col1:
                st.image(
                    "Business Domain.png",   # replace with your image path
                    use_container_width=True
                )
            with col2:
                st.markdown("")
            

        


        

            # =================================================
            # TABLE
            # =================================================

            st.dataframe(df, use_container_width=True, hide_index=True)

            st.divider()

            # =================================================
            # GOOGLE SHEET LINK
            # =================================================

            st.link_button(
                "🔗 Open Google Sheet",
                get_sheet_url(url),
                use_container_width=True
            )
            
    
        # =====================================================
# CLUB PAGE
# =====================================================

elif st.session_state.page == "club":

    import plotly.express as px

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back"):
            st.session_state.page = "home"
            st.rerun()
        st.title(" Club Data Analysis")

    with col2:
        pass
        # st.title(" Club Data Analysis")

    @st.cache_data
    def load_club_data():
        return pd.read_csv("https://docs.google.com/spreadsheets/d/1xBU0rUJXPmt1ZGupM7kt3Rmp2ViMQQ2tPRaxdD_IRGk/export?format=csv")

    df = load_club_data()

    st.markdown("_____")

    

    # ================= KPI METRICS =================
    cols = st.columns(12)

    def kpi(col_obj, label, column):
        pct = df[column].notna().mean() * 100
        col_obj.metric(label, df[column].count(), f"{pct:.0f}% data")

    kpi(cols[0], "GroupMemberID", "GroupMemberID")
    kpi(cols[1], "SchoolClubID", "SchoolClubID")
    kpi(cols[2], "ClubName", "ClubName")
    kpi(cols[3], "ClubSchoolName", "ClubSchoolName")
    kpi(cols[4], "ClubCategoryID", "ClubCategoryID")
    kpi(cols[5], "ClubStatus", "ClubStatus")
    kpi(cols[6], "ClubContactNumber", "ClubContactNumber")
    kpi(cols[7], "ClubLocation", "ClubLocation")
    kpi(cols[8], "ClubWebsite", "ClubWebsite")
    kpi(cols[9], "ClubEmail", "ClubEmail")
    kpi(cols[10], "SocialLinks", "SocialLinks")
    kpi(cols[11], "ClubImagePath", "ClubImagePath")

    cols2 = st.columns(12)

    kpi(cols2[0], "PrimarySponsorID", "PrimarySponsorID")
    kpi(cols2[1], "PrimarySponsorName", "PrimarySponsorName")
    kpi(cols2[2], "ClubBudget", "ClubBudget")
    kpi(cols2[3], "ClubPresidentID", "ClubPresidentID")
    kpi(cols2[4], "ClubPresidentName", "ClubPresidentName")
    kpi(cols2[5], "ClubPresidentPRN", "ClubPresidentPRN")
    kpi(cols2[6], "ClubMentorID", "ClubMentorID")
    kpi(cols2[7], "ClubMentorName", "ClubMentorName")
    kpi(cols2[8], "ClubWebsite", "ClubWebsite")
    kpi(cols2[9], "DataCollectedByID", "DataCollectedByID")
    kpi(cols2[10], "DataCollectedByName", "DataCollectedByName")
    kpi(cols2[11], "ClubName", "ClubName")

    st.markdown("_____")



    # ================= FULL DATA =================
    st.dataframe(df, use_container_width=True)

    

    st.markdown("_____")

    

    # ================= CLUB ANALYSIS =================
    st.subheader("Club Name Analysis")

    club_counts = df["ClubName"].value_counts().reset_index()
    club_counts.columns = ["ClubName", "Count"]

    c1, c2 = st.columns(2)

    with c1:
        st.dataframe(club_counts)

    with c2:
        fig = px.treemap(
            club_counts.head(100),
            path=["ClubName"],
            values="Count",
            title="Top 100 Clubs"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.metric("Missing Club Names", df["ClubName"].isnull().sum())

    st.markdown("_____")

    # ================= SCHOOL ANALYSIS =================
    st.subheader("School Name Analysis")

    school_counts = df["ClubSchoolName"].value_counts().reset_index()
    school_counts.columns = ["ClubSchoolName", "Count"]

    c3, c4 = st.columns(2)

    with c3:
        st.dataframe(school_counts)

    with c4:
        fig2 = px.treemap(
            school_counts.head(100),
            path=["ClubSchoolName"],
            values="Count",
            title="Top 100 Schools"
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.metric("Missing School Names", df["ClubSchoolName"].isnull().sum())

    st.markdown("_____")

    

    # ================= DATA COLLECTED BY =================
    st.subheader("Data Collected By Analysis")

    collected_counts = df["DataCollectedByName"].value_counts().reset_index()
    collected_counts.columns = ["Name", "Count"]

    c5, c6 = st.columns(2)

    with c5:
        st.dataframe(collected_counts)

    with c6:
        fig3 = px.pie(
            collected_counts,
            names="Name",
            values="Count",
            title="Data Collected By"
        )
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("_____")

    



   

# import streamlit as st
