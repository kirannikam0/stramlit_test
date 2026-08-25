import streamlit as st
import facade
import datetime
import time
import pandas as pd

st.set_page_config(
    page_title="streamlit-facade demo",
    page_icon="🎨",
    layout="wide",
)
# ── Session state ──────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

NAV_KEYS = {
    "Home":       "nav_home",
    "Components": "nav_components",
    "Theme":      "nav_theme",
}

# ── Theme ──────────────────────────────────────────────────
if st.session_state.dark_mode:
    facade.theme.apply(
        preset="carbon-sage-dark",
        base="dark",
        font_sans="DM Sans",
        font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",
        radius="md",
    )
else:
    facade.theme.apply(
        preset="carbon-sage",
        base="light",
        font_sans="DM Sans",
        font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",
        radius="md",
    )


# ── Sidebar ────────────────────────────────────────────────
with facade.Sidebar(
    logo="examples/logo.png",
    logo_width=250,
    #title="Streamlit Facade",
    footer="streamlit-facade v0.1.1",
    active=st.session_state.page,
    nav_keys=NAV_KEYS,
):
    if st.button("Home", key="nav_home"):
        st.session_state.page = "Home"
        st.rerun()
    if st.button("Components", key="nav_components"):
        st.session_state.page = "Components"
        st.rerun()
    if st.button("Theme", key="nav_theme"):
        st.session_state.page = "Theme"
        st.rerun()

    st.markdown("---")
    dark = st.toggle(
        "Dark mode",
        value=st.session_state.dark_mode,
        key="dark_toggle",
    )
    if dark != st.session_state.dark_mode:
        st.session_state.dark_mode = dark
        st.rerun()
# ── Pages ──────────────────────────────────────────────────
if st.session_state.page == "Home":
    st.title("streamlit-facade")
    st.markdown("A shadcn-inspired, themeable UI component library for Streamlit.")

    facade.Card(
        title="What is facade?",
        description="facade brings a design token system to Streamlit. Define your theme once and every component inherits it automatically.",
    )
    facade.Card(
        title="No build pipeline",
        description="Pure Python. No Node, no npm, no React. Just pip install and go.",
    )
    facade.Card(
        title="shadcn-inspired",
        description="Clean, minimal components modeled after shadcn/ui — the best design system in the React ecosystem.",
    )

elif st.session_state.page == "Components":
    st.title("Components")

    # ── Alert ──────────────────────────────────────────────
    st.subheader("Alert")
    facade.Alert("Your changes have been saved.", variant="success", title="Saved!")
    facade.Alert("This action cannot be undone.", variant="warning")
    facade.Alert("Failed to connect to database.", variant="error", title="Error")
    facade.Alert("Your trial ends in 3 days.", variant="info")

    facade.Separator()

    # ── Button ─────────────────────────────────────────────
    st.subheader("Button")
    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        if facade.Button("Default", variant="default", key="btn_default"):
            facade.Toast("Default clicked!", icon="check")
    with col2:
        if facade.Button("Outline", variant="outline", key="btn_outline"):
            facade.Toast("Outline clicked!", icon="info")
    with col3:
        if facade.Button("Ghost", variant="ghost", key="btn_ghost"):
            facade.Toast("Ghost clicked!", icon="sparkle")
    with col4:
        if facade.Button("Danger", variant="destructive", key="btn_danger"):
            facade.Toast("Danger clicked!", icon="error")

    st.subheader("Button with icons")
    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        facade.Button("Save",   variant="default",     icon="save",         key="btn_save")
    with col2:
        facade.Button("Delete", variant="destructive", icon="trash",        key="btn_delete")
    with col3:
        facade.Button("Search", variant="outline",     icon="search",       key="btn_search")
    with col4:
        facade.Button("Next",   variant="ghost",       icon="arrow-right",  icon_position="right", key="btn_next")

    st.subheader("Button sizes")
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        facade.Button("Small",  size="sm", key="btn_sm")
    with col2:
        facade.Button("Medium", size="md", key="btn_md")
    with col3:
        facade.Button("Large",  size="lg", key="btn_lg")

    facade.Separator()

    # ── Badge ──────────────────────────────────────────────
    st.subheader("Badge")
    col1, col2, col3, col4, col5, col6 = st.columns(6, gap="small")
    with col1:
        facade.Badge("Default")
    with col2:
        facade.Badge("Success", variant="success")
    with col3:
        facade.Badge("Warning", variant="warning")
    with col4:
        facade.Badge("Error", variant="error")
    with col5:
        facade.Badge("Outline", variant="outline")
    with col6:
        facade.Badge("Muted", variant="muted")

    st.subheader("Badge custom colors")
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        facade.Badge("Premium", bg_color="#7C3AED", text_color="#FFFFFF")
    with col2:
        facade.Badge("Beta", bg_color="#FFF7ED", text_color="#C2410C", border_color="#FDBA74")
    with col3:
        facade.Badge("New", bg_color="var(--destructive)", text_color="#fff")

    facade.Separator()

    # ── Card ───────────────────────────────────────────────
    st.subheader("Card")
    col1, col2 = st.columns(2, gap="small")
    with col1:
        facade.Card(title="Card Title", description="Supporting description text goes here.")
    with col2:
        facade.Card(title="Another Card", description="Cards are great for grouping related content.")

    facade.Separator()

    # ── Input ──────────────────────────────────────────────
    st.subheader("Input")
    val = facade.Input(placeholder="Type something...", label="Your name", key="inp1")
    if val:
        facade.Alert(f"Hello, {val}!", variant="success")

    facade.Separator()

    # ── Select ─────────────────────────────────────────────
    st.subheader("Select")
    choice = facade.Select(
        options=["Option A", "Option B", "Option C"],
        placeholder="Pick an option...",
        key="sel1",
    )
    if choice:
        facade.Alert(f"You selected: {choice}", variant="info")

    facade.Separator()

    # ── Textarea ───────────────────────────────────────────
    st.subheader("Textarea")
    facade.Textarea(placeholder="Write something...", key="ta1")
    facade.Textarea(label="Description", placeholder="Enter description...", height=200, key="ta2")
    facade.Textarea(label="Bio", max_chars=280, key="ta3")

    facade.Separator()

    # ── Checkbox ───────────────────────────────────────────
    st.subheader("Checkbox")
    c1 = facade.Checkbox("Accept terms and conditions", key="chk1")
    c2 = facade.Checkbox("Subscribe to newsletter", value=True, key="chk2")
    c3 = facade.Checkbox("Disabled option", disabled=True, key="chk3")
    if c1:
        facade.Alert("Terms accepted!", variant="success")

    facade.Separator()

    # ── Radio ──────────────────────────────────────────────
    st.subheader("Radio")
    plan = facade.Radio(
        options=["Free", "Pro", "Enterprise"],
        label="Select plan",
        key="radio1",
    )
    if plan == "Free":
        facade.Alert("You are on the Free plan. Upgrade for more features.", variant="info")
    elif plan == "Pro":
        facade.Alert("You are on the Pro plan. Enjoy your benefits!", variant="success")
    elif plan == "Enterprise":
        facade.Alert("You are on the Enterprise plan. Contact us for onboarding.", variant="warning")

    size = facade.Radio(
        options=["Small", "Medium", "Large"],
        label="Size",
        horizontal=True,
        key="radio2",
    )

    facade.Radio(
        options=["Disabled A", "Disabled B"],
        label="Disabled group",
        disabled=True,
        key="radio3",
    )

    facade.Separator()

    # ── Toggle ─────────────────────────────────────────────
    st.subheader("Toggle")
    notifications = facade.Toggle("Enable notifications", key="tog1")
    dark_mode     = facade.Toggle("Dark mode", value=True, key="tog2")
    analytics     = facade.Toggle("Analytics (disabled)", disabled=True, key="tog3")
    if notifications:
        facade.Alert("Notifications are enabled.", variant="success")
    if dark_mode:
        facade.Alert("Dark mode is on.", variant="info")

    facade.Separator()

    # ── Slider ─────────────────────────────────────────────
    st.subheader("Slider")
    volume = facade.Slider("Volume", min_value=0, max_value=100, value=50, key="sl1")
    st.text(f"Volume: {volume}")
    price_range = facade.Slider(
        "Price range",
        min_value=0,
        max_value=1000,
        value=(100, 500),
        step=50,
        key="sl2",
    )
    st.text(f"Price: ${price_range[0]} to ${price_range[1]}")
    facade.Slider("Disabled", min_value=0, max_value=10, value=3, disabled=True, key="sl3")

    facade.Separator()

    # ── DatePicker ─────────────────────────────────────────
    st.subheader("DatePicker")
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        date = facade.DatePicker(label="Select date", key="dp1")
        st.text(f"Selected: {date}")
    with col2:
        facade.DatePicker(
            label="With range",
            min_value=datetime.date(2024, 1, 1),
            max_value=datetime.date(2026, 12, 31),
            key="dp2",
        )
    with col3:
        facade.DatePicker(label="Disabled", disabled=True, key="dp3")

    facade.Separator()

    # ── Metric ─────────────────────────────────────────────
    st.subheader("Metric")
    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        facade.Metric(label="Revenue", value="$24,500", delta="12%")
    with col2:
        facade.Metric(label="Users", value="1,284", delta="8%")
    with col3:
        facade.Metric(label="Churn", value="3.2%", delta="-0.5%")
    with col4:
        facade.Metric(label="Uptime", value="99.9%", delta_color="off")

    facade.Separator()

    # ── Spinner ────────────────────────────────────────────
    st.subheader("Spinner")
    if facade.Button("Trigger spinner", icon="refresh", key="btn_spinner"):
        with facade.Spinner("Loading data..."):
            time.sleep(2)
        facade.Alert("Done loading!", variant="success")

    facade.Separator()

    # ── Tabs ───────────────────────────────────────────────
    st.subheader("Tabs")
    tab1, tab2, tab3 = facade.Tabs(["Overview", "Analytics", "Settings"])
    with tab1:
        facade.Card(title="Overview", description="This is the overview tab content.")
        facade.Alert("Everything is running smoothly.", variant="success")
    with tab2:
        col1, col2 = st.columns(2, gap="small")
        with col1:
            facade.Metric(label="Sessions", value="12,400", delta="4%")
        with col2:
            facade.Metric(label="Bounce rate", value="38%", delta="-2%")
    with tab3:
        facade.Input(label="App name", placeholder="My App", key="tab_inp1")
        facade.Toggle("Enable notifications", key="tab_tog1")
        facade.Button("Save settings", icon="save", key="tab_btn1")

    facade.Separator()

    # ── Accordion ──────────────────────────────────────────
    st.subheader("Accordion")
    with facade.Accordion("Account details", expanded=True):
        facade.Input(label="Full name", placeholder="John Doe", key="acc_inp1")
        facade.Input(label="Email", placeholder="john@example.com", key="acc_inp2")
    with facade.Accordion("Notification preferences", icon="bell"):
        facade.Toggle("Email notifications", key="acc_tog1")
        facade.Toggle("SMS notifications", key="acc_tog2")
    with facade.Accordion("Danger zone", icon="error"):
        facade.Alert("These actions are irreversible.", variant="warning")
        facade.Button("Delete account", variant="destructive", icon="trash", key="acc_btn1")

    facade.Separator()

    # ── Progress ───────────────────────────────────────────
    st.subheader("Progress")
    facade.Progress(value=75, label="Uploading...")
    facade.Progress(value=45, label="Processing...")
    facade.Progress(value=100, label="Complete")
    facade.Progress(value=10, label="Starting...")

    facade.Separator()

    # ── DataFrame ──────────────────────────────────────────
    st.subheader("DataFrame")
    df = pd.DataFrame({
        "Name":   ["Alice", "Bob", "Charlie", "Diana"],
        "Role":   ["Engineer", "Designer", "Manager", "Analyst"],
        "Status": ["Active", "Active", "Away", "Active"],
        "Score":  [94, 87, 76, 91],
    })
    st.dataframe(df, width='stretch', hide_index=True)

elif st.session_state.page == "Theme":
    st.title("Theme")
    st.markdown("The active theme tokens for this demo.")

    col1, col2 = st.columns(2, gap="small")
    with col1:
        facade.Card(title="Preset",      description="minimal")
        facade.Card(title="Primary",     description="#18181B")
        facade.Card(title="Background",  description="#FFFFFF")
        facade.Card(title="Foreground",  description="#09090B")
        facade.Card(title="Destructive", description="#EF4444")
    with col2:
        facade.Card(title="Muted",              description="#F4F4F5")
        facade.Card(title="Border",             description="#E4E4E7")
        facade.Card(title="Sidebar background", description="#18181B")
        facade.Card(title="Font",               description="DM Sans")
        facade.Card(title="Radius",             description="md (0.5rem)")
