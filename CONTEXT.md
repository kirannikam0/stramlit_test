# streamlit-facade — LLM Context File

> Drop this file into Claude Projects, attach it to a ChatGPT conversation, or add it to `.cursor/rules`.
> This gives your LLM the full facade API so you can build Streamlit apps with facade immediately.

---

## What is facade?

`streamlit-facade` is a shadcn-inspired, themeable UI component library for Streamlit.
Define your colors, fonts, and radius once — every component picks them up automatically.

- **Pure Python** — no Node, no npm, no React, no build pipeline
- **Design token system** — one `theme.apply()` call, entire app is themed
- **20+ components** — Button, Card, Alert, Badge, Input, Select, Tabs, Accordion, Sidebar and more
- **76 named icons** — unified registry, same name works everywhere
- **11 built-in presets** — light and dark variants included

```bash
pip install streamlit-facade
```

---

## Quick Start

```python
import streamlit as st
import facade

st.set_page_config(layout="wide")

facade.theme.apply(
    preset="carbon-sage",
    font_sans="DM Sans",
    font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",
    radius="lg",
)

facade.Alert("Welcome to facade!", variant="success", title="Hello")
facade.Button("Get started", icon="arrow-right", icon_position="right")
facade.Card(title="facade", description="streamlit but different")
```

---

## Theme System

### `facade.theme.apply()`

```python
facade.theme.apply(
    # Preset (overridden by any explicit param)
    preset="carbon-sage",         # see preset list below
    base="light",                 # "light" | "dark"

    # Color tokens
    primary="#8FAF3D",
    primary_foreground="#FFFFFF",
    background="#F7F7F5",
    foreground="#1C1917",
    muted="#EFEFEB",
    muted_foreground="#78716C",
    border="#D9D9C8",
    destructive="#EF4444",

    # Chrome tokens — sidebar + topbar
    chrome_background="#2C2C2C",
    chrome_foreground="#F5F5F0",
    chrome_border="#3A3A36",

    # Typography
    font_sans="DM Sans",
    font_mono="JetBrains Mono",
    font_link="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap",

    # Radius: xxs | sm | md | lg | xl
    radius="lg",
)
```

### Built-in Presets

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
| `burgundy` | Deep burgundy, warm neutral |

### Radius Scale

| Name | Value |
|---|---|
| `xxs` | 0.125rem |
| `sm` | 0.25rem |
| `md` | 0.5rem |
| `lg` | 0.75rem |
| `xl` | 1rem |

---

## Component API Reference

### Button

```python
facade.Button(
    label: str,
    variant: str = "default",     # "default" | "outline" | "ghost" | "destructive"
    size: str = "md",             # "sm" | "md" | "lg"
    disabled: bool = False,
    icon: str = None,             # facade icon name e.g. "save", "arrow-right"
    icon_position: str = "left",  # "left" | "right"
    key: str = None,
) -> bool
```

```python
# Examples
if facade.Button("Save", icon="save", key="btn1"):
    st.write("Saved!")

facade.Button("Delete", variant="destructive", icon="trash", key="btn2")
facade.Button("Next",   variant="outline",     icon="arrow-right", icon_position="right", key="btn3")
facade.Button("Small",  size="sm", key="btn4")
facade.Button("Large",  size="lg", key="btn5")
```

---

### LinkButton

Same as Button but navigates to an external URL on click. Does not return bool.

```python
facade.LinkButton(
    label: str,
    url: str,
    variant: str = "default",     # "default" | "outline" | "ghost" | "destructive"
    size: str = "md",             # "sm" | "md" | "lg"
    disabled: bool = False,
    icon: str = None,
    icon_position: str = "left",
    key: str = None,
) -> None
```

```python
# Examples
facade.LinkButton("GitHub", url="https://github.com/itsdaniyalm/streamlit-facade", variant="outline", icon="external-link", key="lb1")
facade.LinkButton("PyPI",   url="https://pypi.org/project/streamlit-facade",       variant="ghost",   icon="link",          key="lb2")
```

---

### Input

```python
facade.Input(
    placeholder: str = "",
    label: str = None,
    value: str = "",
    disabled: bool = False,
    key: str = None,
) -> str
```

```python
val = facade.Input(label="Email", placeholder="you@example.com", key="inp1")
if val:
    st.write(f"Entered: {val}")
```

---

### Select

```python
facade.Select(
    options: list,
    placeholder: str = "Select...",
    label: str = None,
    disabled: bool = False,
    key: str = None,
) -> str
```

```python
choice = facade.Select(
    options=["Option A", "Option B", "Option C"],
    placeholder="Pick one...",
    key="sel1",
)
```

---

### Textarea

```python
facade.Textarea(
    placeholder: str = "",
    label: str = None,
    value: str = "",
    height: int = 120,
    max_chars: int = None,
    disabled: bool = False,
    key: str = None,
) -> str
```

```python
facade.Textarea(label="Message", placeholder="Write something...", key="ta1")
facade.Textarea(label="Bio",     max_chars=280,                    key="ta2")
facade.Textarea(label="Notes",   height=200,                       key="ta3")
```

---

### Checkbox

```python
facade.Checkbox(
    label: str,
    value: bool = False,
    disabled: bool = False,
    key: str = None,
) -> bool
```

```python
accepted = facade.Checkbox("Accept terms and conditions", key="chk1")
facade.Checkbox("Subscribe to newsletter", value=True,    key="chk2")
facade.Checkbox("Disabled option",         disabled=True, key="chk3")
```

---

### Radio

```python
facade.Radio(
    options: list,
    label: str = None,
    index: int = 0,
    horizontal: bool = False,
    disabled: bool = False,
    key: str = None,
) -> str
```

```python
plan = facade.Radio(options=["Free", "Pro", "Enterprise"], label="Plan", key="rad1")
size = facade.Radio(options=["S", "M", "L"], label="Size", horizontal=True, key="rad2")
```

---

### Toggle

```python
facade.Toggle(
    label: str,
    value: bool = False,
    disabled: bool = False,
    key: str = None,
) -> bool
```

```python
notifications = facade.Toggle("Enable notifications", key="tog1")
facade.Toggle("Dark mode",  value=True,    key="tog2")
facade.Toggle("Disabled",   disabled=True, key="tog3")
```

---

### Slider

```python
facade.Slider(
    label: str,
    min_value: float = 0,
    max_value: float = 100,
    value = 50,              # int, float, or tuple for range slider
    step: float = 1,
    disabled: bool = False,
    key: str = None,
) -> float | tuple
```

```python
vol   = facade.Slider("Volume", min_value=0, max_value=100, value=50, key="sl1")
price = facade.Slider("Price range", min_value=0, max_value=1000, value=(100, 500), step=50, key="sl2")
```

---

### DatePicker

```python
facade.DatePicker(
    label: str = None,
    value = None,
    min_value = None,
    max_value = None,
    disabled: bool = False,
    key: str = None,
) -> datetime.date
```

```python
import datetime
date = facade.DatePicker(label="Select date", key="dp1")
facade.DatePicker(
    label="With range",
    min_value=datetime.date(2024, 1, 1),
    max_value=datetime.date(2026, 12, 31),
    key="dp2",
)
```

---

### Card

```python
facade.Card(
    title: str = None,
    description: str = None,
    key: str = None,
) -> None
```

```python
facade.Card(title="Card Title", description="Supporting description text.")
facade.Card(title="Title only")
```

---

### IconCard

Card with a leading Lucide icon above the title.

```python
facade.IconCard(
    title: str = None,
    description: str = None,
    icon: str = None,        # facade icon name
    icon_size: int = 24,
    key: str = None,
) -> None
```

```python
facade.IconCard(
    title="No build pipeline",
    description="Pure Python. No Node, no npm, no React.",
    icon="terminal",
)
facade.IconCard(title="Token system", description="Define once, inherit everywhere.", icon="settings")
```

---

### StyledContainer

A styled `st.container()` wrapper with configurable borders, background, and radius.
Use it to group any Streamlit components inside a visually distinct card.
`key` is required — it is the CSS scoping anchor via `.st-key-{key}`.

```python
with facade.StyledContainer(
    border: str = "all",                        # "top" | "bottom" | "left" | "right" | "all" | "none"
    border_color: str = "var(--border)",        # accent border color (hex, rgba, or CSS var)
    border_width: str = "2px",                  # accent border thickness
    border_surround_color: str = "var(--border)", # color for the other 3 sides when border != "all"
    background: str = "var(--background)",
    radius: str = "var(--radius)",
    padding: str = "1.25rem 1.5rem",
    key: str = None,                            # REQUIRED
):
    # any Streamlit content here
```

```python
# Top accent border (e.g. status card)
with facade.StyledContainer(
    border="top",
    border_color="#e05252",
    border_width="3px",
    key="card_critical",
):
    facade.Badge("Critical", variant="error")
    st.markdown("### $43.8M")
    st.caption("493 patients")

# Left accent border
with facade.StyledContainer(
    border="left",
    border_color="var(--primary)",
    border_width="4px",
    key="card_info",
):
    st.markdown("**Left accent border**")

# Full border with custom background
with facade.StyledContainer(
    border="all",
    background="var(--muted)",
    key="card_muted",
):
    st.markdown("Muted background card")

# No border, custom background only
with facade.StyledContainer(
    border="none",
    background="#FFF7ED",
    key="card_warm",
):
    st.markdown("Borderless styled section")
```

---

### Alert

```python
facade.Alert(
    message: str,
    title: str = None,
    variant: str = "info",   # "info" | "success" | "warning" | "error"
    icon: bool = True,
    key: str = None,
) -> None
```

```python
facade.Alert("Changes saved.",         variant="success", title="Saved!")
facade.Alert("Cannot be undone.",      variant="warning")
facade.Alert("Connection failed.",     variant="error",   title="Error")
facade.Alert("Trial ends in 3 days.",  variant="info")
```

---

### Badge

```python
facade.Badge(
    text: str,
    variant: str = "default",   # "default" | "success" | "warning" | "error" | "outline" | "muted"
    bg_color: str = None,       # overrides variant
    text_color: str = None,
    border_color: str = None,
    key: str = None,
) -> None
```

```python
facade.Badge("Default")
facade.Badge("Success", variant="success")
facade.Badge("Warning", variant="warning")
facade.Badge("Error",   variant="error")
facade.Badge("Outline", variant="outline")
facade.Badge("Muted",   variant="muted")

# Custom colors
facade.Badge("Premium", bg_color="#7C3AED", text_color="#fff")
facade.Badge("Beta", bg_color="#FFF7ED", text_color="#C2410C", border_color="#FDBA74")
```

---

### Metric

```python
facade.Metric(
    label: str,
    value,                       # str | int | float
    delta = None,                # str | int | float
    delta_color: str = "normal", # "normal" | "inverse" | "off"
    key: str = None,
) -> None
```

```python
facade.Metric(label="Revenue", value="$24,500", delta="12%")
facade.Metric(label="Churn",   value="3.2%",    delta="-0.5%")
facade.Metric(label="Uptime",  value="99.9%",   delta_color="off")
```

---

### Separator

```python
facade.Separator(
    label: str = None,
    key: str = None,
) -> None
```

```python
facade.Separator()
facade.Separator(label="or")
facade.Separator(label="section title")
```

---

### Progress

```python
facade.Progress(
    value: int,        # 0–100
    label: str = None,
    key: str = None,
) -> None
```

```python
facade.Progress(value=75,  label="Uploading...")
facade.Progress(value=100, label="Complete")
```

---

### Spinner

Context manager — content inside runs while spinner is shown.

```python
with facade.Spinner(text: str = "Loading..."):
    # do work here
    time.sleep(2)
```

```python
import time
if facade.Button("Load data", icon="refresh", key="btn_load"):
    with facade.Spinner("Loading data..."):
        time.sleep(2)
    facade.Alert("Done!", variant="success")
```

---

### Toast

```python
facade.Toast(
    message: str,
    icon: str = None,   # facade icon name
) -> None
```

```python
facade.Toast("Saved successfully!", icon="check")
facade.Toast("Something went wrong.", icon="error")
facade.Toast("Here's some info.",    icon="info")
```

---

### Tabs

Returns a tuple of tab context managers.

```python
facade.Tabs(tabs: list[str]) -> tuple
```

```python
tab1, tab2, tab3 = facade.Tabs(["Overview", "Analytics", "Settings"])
with tab1:
    facade.Card(title="Overview", description="Tab content here.")
with tab2:
    facade.Metric(label="Sessions", value="12,400", delta="4%")
with tab3:
    facade.Toggle("Notifications", key="tog1")
    facade.Button("Save", icon="save", key="btn_save")
```

---

### Accordion

```python
with facade.Accordion(
    title: str,
    expanded: bool = False,
    icon: str = None,     # facade icon name
    key: str = None,
):
    # content here
```

```python
with facade.Accordion("Account details", expanded=True):
    facade.Input(label="Full name", key="inp1")
    facade.Input(label="Email",     key="inp2")

with facade.Accordion("Notifications", icon="bell"):
    facade.Toggle("Email notifications", key="tog1")

with facade.Accordion("Danger zone", icon="error"):
    facade.Alert("Irreversible.", variant="warning")
    facade.Button("Delete", variant="destructive", icon="trash", key="btn_del")
```

---

### Sidebar

```python
with facade.Sidebar(
    logo: str = None,          # file path or URL
    logo_width: int = 160,
    logo_height: int = None,
    title: str = None,
    footer: str = None,
    dividers: bool = False,
    active: str = None,        # active page name
    nav_keys: dict = None,     # {"Page": "button_key"}
):
    # nav buttons here
```

```python
if "page" not in st.session_state:
    st.session_state.page = "Home"

NAV_KEYS = {"Home": "nav_home", "Docs": "nav_docs"}

with facade.Sidebar(
    logo="assets/logo.png",
    logo_width=180,
    footer="v0.1.4",
    active=st.session_state.page,
    nav_keys=NAV_KEYS,
):
    if st.button("Home", key="nav_home"):
        st.session_state.page = "Home"
        st.rerun()
    if st.button("Docs", key="nav_docs"):
        st.session_state.page = "Docs"
        st.rerun()
```

---

### TopBar

```python
facade.TopBar(
    title: str = None,
    user: str = None,
    avatar: str = None,   # single letter shown in avatar circle
) -> None
```

```python
facade.TopBar(title="My App", user="Daniyal", avatar="D")
```

---

## Icon System

facade has a registry of **76 named icons**. The same name works in every component:
- In `Button` / `LinkButton` — uses Material Symbols (native Streamlit)
- In `Alert`, `Accordion`, `Toast`, `IconCard`, `StyledContainer` — uses Lucide SVGs

```python
# In components — use facade icon name
facade.Button("Save",   icon="save")
facade.Button("Delete", icon="trash",       variant="destructive")
facade.Button("Next",   icon="arrow-right", icon_position="right")

with facade.Accordion("Notifications", icon="bell"):
    ...

facade.Toast("Saved!", icon="check")

# Standalone Lucide SVG for custom HTML
from facade.lucide import icon_html
svg = icon_html("circle-check", size=16, color="var(--primary)")
st.markdown(svg, unsafe_allow_html=True)

# List all 76 available icon names
facade.icon_names()
```

### Full Icon Registry

```
arrow-down, arrow-left, arrow-right, arrow-up,
bell, bug, calendar, chart, chart-line, chart-pie,
check, check-simple, clock, close, cloud, code,
collapse, copy, dashboard, database, download,
edit, error, expand, external-link, eye, eye-off,
file, filter, flag, folder, fullscreen, grid,
heart, help, home, image, info, link, list,
lock, login, logout, mail, menu, minus,
more, more-vertical, next, notification,
plus, prev, print, refresh, save, search,
send, settings, share, sort, sparkle, star,
tag, terminal, trash, trending-down, trending-up,
unlock, upload, user, users, warning,
zap, zoom-in, zoom-out
```

---

## CSS Variables

All tokens are available as CSS variables throughout the app:

```css
var(--primary)
var(--primary-foreground)
var(--background)
var(--foreground)
var(--muted)
var(--muted-foreground)
var(--border)
var(--destructive)
var(--chrome-background)
var(--chrome-foreground)
var(--chrome-border)
var(--font-sans)
var(--font-mono)
var(--radius)
```

Use them in custom HTML:

```python
st.markdown("""
<div style="
    background: var(--muted);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem;
    color: var(--foreground);
    font-family: var(--font-sans);
">
    Custom themed div
</div>
""", unsafe_allow_html=True)
```

---

## CSS Scoping

Streamlit adds `class="st-key-{key}"` to every widget's parent div when a `key=` is passed.
Use this to scope custom CSS to a specific component:

```python
st.markdown("""
<style>
    .st-key-my_button button {
        background: var(--primary) !important;
        border-radius: var(--radius) !important;
    }
</style>
""", unsafe_allow_html=True)

facade.Button("Custom", key="my_button")
```

This is also how `StyledContainer` works internally — it injects CSS targeting `.st-key-{key}` on the container div.

---

## Multi-page Pattern

```python
import streamlit as st
import facade

st.set_page_config(layout="wide")

facade.theme.apply(preset="carbon-sage", radius="lg")

if "page" not in st.session_state:
    st.session_state.page = "Home"

NAV_KEYS = {"Home": "nav_home", "Dashboard": "nav_dash", "Settings": "nav_settings"}

with facade.Sidebar(
    logo="assets/logo.png",
    logo_width=180,
    footer="My App v1.0",
    active=st.session_state.page,
    nav_keys=NAV_KEYS,
):
    if st.button("Home",      key="nav_home"):
        st.session_state.page = "Home";      st.rerun()
    if st.button("Dashboard", key="nav_dash"):
        st.session_state.page = "Dashboard"; st.rerun()
    if st.button("Settings",  key="nav_settings"):
        st.session_state.page = "Settings";  st.rerun()

if st.session_state.page == "Home":
    st.title("Home")

elif st.session_state.page == "Dashboard":
    st.title("Dashboard")
    col1, col2, col3 = st.columns(3, gap="small")
    with col1: facade.Metric(label="Revenue", value="$24,500", delta="12%")
    with col2: facade.Metric(label="Users",   value="1,284",   delta="8%")
    with col3: facade.Metric(label="Uptime",  value="99.9%",   delta_color="off")

elif st.session_state.page == "Settings":
    st.title("Settings")
    facade.Input(label="App name", placeholder="My App", key="inp_name")
    facade.Toggle("Enable notifications", key="tog_notifs")
    facade.Button("Save", icon="save", key="btn_save")
```

---

## Rules for LLMs

- `--muted` is the component surface color (cards, inputs, containers). `--background` is the page background. Keep them distinct for proper visual hierarchy.
- `StyledContainer` defaults to `var(--muted)` background — override with `background=` param if needed
- Always use `key=` on every interactive component to avoid Streamlit duplicate key errors
- `facade.Button` returns `bool` — use inside `if` for click handling
- `facade.LinkButton` does NOT return bool — never use in `if` statement
- `facade.Tabs` returns a tuple — unpack it then use `with tab:` syntax
- `facade.Accordion` and `facade.Sidebar` are context managers — use `with` syntax
- `facade.Spinner` is a context manager — put work inside the `with` block
- `facade.StyledContainer` is a context manager — `key` is required, put any Streamlit content inside
- Icons use facade registry names, not Lucide names directly
- `facade.icon_names()` returns the full list of 76 valid icon names
- Never set `font-family` on `span` or `*` selectors — breaks Material Icons
- CSS variables (`var(--primary)` etc.) work in any `st.markdown` HTML
- `st.container(key="name")` + `.st-key-name` CSS is the way to style sections
- facade never auto-loads fonts — always pass `font_link` to `theme.apply()`

---

## Package Info

- **PyPI**: `pip install streamlit-facade`
- **Version**: 0.1.6
- **GitHub**: https://github.com/itsdaniyalm/streamlit-facade
- **Requires**: Python 3.8+, Streamlit 1.35.0+
- **License**: MIT