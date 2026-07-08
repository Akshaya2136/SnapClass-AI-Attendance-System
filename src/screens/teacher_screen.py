import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    # Initialize session state
    if "teacher_login_type" not in st.session_state:
        st.session_state.teacher_login_type = "login"

    # Display appropriate screen
    if st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    else:
        teacher_screen_register()


# ---------------- LOGIN ---------------- #

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control+backspace",
        ):
            st.session_state.login_type = None
            st.rerun()

    st.header("Login using password", text_alignment="center")

    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter username",
        placeholder="akshaya",
    )

    teacher_pass = st.text_input(
        "Enter password",
        type="password",
        placeholder="Enter your password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Login Now",
            icon=":material/passkey:",
            shortcut="control+enter",
            width="stretch",
        ):
            # TODO: Add login logic here
            pass

    with btnc2:
        if st.button(
            "Register Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
        ):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()


# ---------------- REGISTER ---------------- #

def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to home",
            type="secondary",
            key="registerbackbtn",   # Different key
            shortcut="control+backspace",
        ):
            st.session_state.login_type = None
            st.rerun()

    st.header("Register your teacher profile")

    st.space()
    st.space()

    teacher_username = st.text_input(
        "Enter username",
        placeholder="akshaya",
    )

    teacher_name = st.text_input(
        "Enter name",
        placeholder="Akshaya Yammadi",
    )

    teacher_pass = st.text_input(
        "Enter password",
        type="password",
        placeholder="Enter your password",
    )

    teacher_pass_confirm = st.text_input(
        "Confirm password",
        type="password",
        placeholder="Enter your password",
    )

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Register Now",
            icon=":material/passkey:",
            shortcut="control+enter",
            width="stretch",
            type="primary"
        ):
           # TODO: Add registration logic here
           pass

    with btnc2:
        if st.button(
            "Login Instead",
            type="secondary",
            icon=":material/passkey:",
            width="stretch"
        ):
            st.session_state.teacher_login_type = "login"
            st.rerun()

    footer_dashboard()