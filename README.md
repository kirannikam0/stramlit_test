# facade

**streamlit but different**

facade is a shadcn-inspired, themeable UI component library for Streamlit. Define your colors, fonts, and radius once every component picks it up automatically.

```python
pip install streamlit-facade
```

---

## Quick start

```python
import streamlit as st
import facade

facade.theme.apply(
    preset="carbon-sage",
    font_sans="DM Sans",
    font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",
    radius="md",
)

facade.Alert("Welcome to facade!", variant="success", title="Hello")
facade.Button("Get started", icon="arrow-right", icon_position="right")
facade.Card(title="facade", description="streamlit but different")
```

---

## Why facade?

Streamlit is powerful but opinionated about looks. facade gives you a proper design token system one `theme.apply()` call and your entire app gets a consistent, professional look without touching CSS.

- **No build pipeline** — pure Python, no Node, no npm, no React
- **shadcn-inspired** — clean, minimal components modeled after the best design system in the React ecosystem
- **Token system** — define colors once, every component inherits automatically
- **Dark mode** — every preset ships with a light and dark variant
- **Lucide icons** — 1500+ icons available via `facade.Icon()`

---

## Theme system

```python
facade.theme.apply(
    preset="carbon-sage",      # built-in preset
    base="light",              # "light" | "dark"
    primary="#8FAF3D",         # override any token
    background="#F7F7F5",
    font_sans="DM Sans",
    font_link="https://fonts.googleapis.com/...",
    radius="md",               # xxs | sm | md | lg | xl
)
```

### Built-in presets

| Preset | Style |
|---|---|
| `default` | Classic blue, professional |
| `default-dark` | Deep navy dark mode |
| `minimal` | Near-black, tight radius |
| `warm` | Amber accent, warm cream |
| `dark` | Blue accent, dark slate |
| `carbon-sage` | Sage green, warm chalk |
| `carbon-sage-dark` | Sage green, warm carbon dark |
| `carbon-light` | Electric lime, warm white |
| `carbon-dark` | Electric lime, pure dark |
| `carbon-amber` | Amber accent, warm carbon |
| `daniyal` | Navy brand theme |

---

## Components

### Form
```python
facade.Button("Click me", variant="default", icon="save")
facade.Input(label="Email", placeholder="you@example.com")
facade.Select(options=["A", "B", "C"], placeholder="Pick one")
facade.Textarea(label="Message", placeholder="Write something...")
facade.Checkbox("Accept terms", key="chk1")
facade.Radio(options=["Free", "Pro"], label="Plan", key="radio1")
facade.Toggle("Dark mode", key="tog1")
facade.Slider("Volume", min_value=0, max_value=100, value=50)
facade.DatePicker(label="Select date")
```

### Display
```python
facade.Card(title="Title", description="Supporting text")
facade.Alert("Something happened", variant="success", title="Done!")
facade.Badge("New", variant="success")
facade.Badge("Pro", bg_color="#7C3AED", text_color="#fff")
facade.Metric(label="Revenue", value="$24,500", delta="12%")
facade.Separator()
facade.Separator(label="or")
with facade.Spinner("Loading..."):
    time.sleep(2)
```

### Layout
```python
tab1, tab2 = facade.Tabs(["Overview", "Settings"])
with tab1:
    st.write("Overview content")

with facade.Accordion("Details", icon="info"):
    st.write("Hidden content")

facade.Toast("Saved!", icon="check")

with facade.Sidebar(logo="logo.png", footer="v0.1.0"):
    if st.button("Home", key="nav_home"):
        st.session_state.page = "Home"
        st.rerun()
```

### Data
```python
facade.Progress(value=75, label="Uploading...")
st.dataframe(df, use_container_width=True)  # themed automatically
```

---

## Icons

facade uses a unified icon system one name works everywhere:

```python
# In components
facade.Button("Save", icon="save")
facade.Alert("Done", variant="success")  # icon auto-selected

# Standalone SVG (for custom HTML)
from facade.lucide import icon_html
svg = icon_html("circle-check", size=16, color="var(--primary)")

# See all available icons
facade.icon_names()
```

Button icons use Material Symbols (native Streamlit). HTML component icons use Lucide SVGs. facade handles the translation you always use the same name.

---

## Sidebar

```python
with facade.Sidebar(
    logo="assets/logo.png",
    logo_width=200,
    title="My App",
    footer="v1.0.0",
    active=st.session_state.page,
    nav_keys={"Home": "nav_home", "Dashboard": "nav_dash"},
):
    if st.button("Home", key="nav_home"):
        st.session_state.page = "Home"
        st.rerun()
    if st.button("Dashboard", key="nav_dash"):
        st.session_state.page = "Dashboard"
        st.rerun()
```

---

## Token reference

```python
facade.theme.apply(
    preset="default",
    base="light",                    # "light" | "dark"
    primary="#1059A0",
    primary_foreground="#FFFFFF",
    background="#FFFFFF",
    foreground="#0F172A",
    muted="#F1F5F9",
    muted_foreground="#64748B",
    border="#E2E8F0",
    destructive="#EF4444",
    chrome_background="#1059A0",     # sidebar + topbar background
    chrome_foreground="#E8EDF2",     # sidebar + topbar text
    chrome_border="#1E6FBE",         # sidebar + topbar border
    font_sans="Inter",
    font_mono="JetBrains Mono",
    font_link="https://fonts.googleapis.com/...",
    radius="md",                     # xxs | sm | md | lg | xl
)
```

---

## Requirements

- Python 3.8+
- Streamlit 1.35.0+

---

## License

MIT © Daniyal M

---

## Links

- [Website](https://facade-docs.streamlit.app/)
- [GitHub](https://github.com/itsdaniyalm/streamlit-facade)
- [PyPI](https://pypi.org/project/streamlit-facade)
- [Report a bug](https://github.com/itsdaniyalm/streamlit-facade/issues)
