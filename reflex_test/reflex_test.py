import reflex as rx
from reflex_test import style
from reflex_test.portfolio_es import index_es
from reflex_test.state import State

def about_me_text() -> rx.Component:
    return rx.vstack(
        rx.text("""Graduated in physics with a master's degree in Big Data Analytics. 
                Currently working as a Data Scientist, engaging with a variety of projects, 
                including European energy initiatives.""",
                style=style.message_style,
                ),
        rx.text("""Interested in Artificial Intelligence, data analysis, and visualization.
                 This portfolio showcases projects that highlight my commitment to leveraging data for meaningful outcomes.
                 I invite you to explore and connect.""",
                style=style.message_style,
                ),
        rx.link(
            rx.button(
                rx.text("Download CV", style=style.message_style),
                rx.image(src="/icons/cv.png", width="100%", height="100%"),
                style=style.button_style
                ),
            href="https://drive.google.com/uc?id=1NRtDqXdPOhDFerh0NApQIdvkTrrPJCTh&export=download",
            ),
        )
def about_me_image() -> rx.Component:
    return rx.center(
        rx.image(
            src="/me/me.jpg",
            border_radius="25% 25%",
            ),
    )

def about_me_tab() -> rx.Component:
    return rx.tab(
        rx.heading("About me", style=style.heading_style),
        height="10em"
    )
def about_me_panel() -> rx.Component:
    return rx.tab_panel(
        rx.hstack(
            rx.container(
                about_me_text(),
                width="60%",
            ),
            rx.container(
                about_me_image(),
                width="40%",
            ),
        ),
    )

def technologies_tab() -> rx.Component:
    return rx.tab(
        rx.heading("Technologies", style=style.heading_style),
        height="10em"
    )
def technologies_panel() -> rx.Component:
    return rx.tab_panel(
        rx.vstack(
            rx.hstack(
                rx.vstack(rx.heading("ETL/ML frameworks", style=style.subheading_style), width="20%"),
                rx.box(
                    rx.hstack(
                        rx.vstack(rx.image(src="/icons/MLflow-Logo.svg"), width="25%"),
                        rx.vstack(rx.image(src="/icons/Qlik_Logo.png", width="70%", height="70%"), width="25%"),
                        rx.vstack(rx.image(src="/icons/tableau-logo.png", width="50%", height="50%"), width="25%"),
                        rx.vstack(rx.image(src="/icons/grafana-logo.png", width="40%", height="40%"), width="25%"),
                    ),
                    width="75%",
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),
            rx.hstack(
                rx.vstack(rx.heading("Python packages", style=style.subheading_style), width="20%"),
                rx.box(
                    rx.hstack(
                        rx.vstack(rx.image(src="/icons/pandas-logo.png"), width="14.2%"),
                        rx.vstack(rx.image(src="/icons/scipy-logo.png"), width="14.2%"),
                        rx.vstack(rx.image(src="/icons/numpy-logo.png"), width="14.2%"),
                        rx.vstack(rx.image(src="/icons/matplotlib-logo.png"), width="14.2%"),
                        rx.vstack(rx.image(src="/icons/tensorflow-logo.png"), width="14.2%"),
                        rx.vstack(rx.image(src="/icons/sklearn-logo.png"), width="14.2%"),
                        rx.vstack(rx.image(src="/icons/xgboost-logo.png"), width="14.2%"),
                    ),
                    width="75%",
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),
            rx.hstack(
                rx.vstack(rx.heading("Databases", style=style.subheading_style), width="20%"),
                rx.box(
                    rx.hstack(
                        rx.vstack(rx.image(src="/icons/influxdb-logo.png"), width="33%"),
                        rx.vstack(rx.image(src="/icons/mongodb-logo.png", width="70%", height="70%"), width="33%"),
                        rx.vstack(rx.image(src="/icons/mysql-logo.png", width="70%", height="70%"), width="33%"),
                    ),
                    width="75%",
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),
            rx.hstack(
                rx.vstack(rx.heading("Deployment", style=style.subheading_style), width="20%"),
                rx.box(
                    rx.hstack(
                        rx.vstack(rx.image(src="/icons/portainer-logo.png", width="70%", height="70%"), width="33%"),
                        rx.vstack(rx.image(src="/icons/docker-logo.png", width="70%", height="70%"), width="33%"),
                        rx.vstack(rx.image(src="/icons/kubernetes-logo.png", width="70%", height="70%"), width="33%"),
                    ),
                    width="75%",
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),
        ),
    )

def personal_projects_tab() -> rx.Component:
    return rx.tab(
        rx.heading("Personal projects", style=style.heading_style),
        height="10em"
    )
def personal_projects_panel() -> rx.Component:
    return rx.tab_panel(
        rx.vstack(
            rx.hstack(
                rx.vstack(rx.heading("Calculator", style=style.subheading_style), width="33%"),
                rx.vstack(rx.text("A simple example of a calculator showing how I usually work in Python.", style=style.message_style), width="33%"),
                rx.vstack(
                    rx.link(
                        rx.button(
                            rx.image(src="/icons/GitHub_Logo.png", width="100%", height="100%"),
                            style=style.button_style
                        ),
                        href="https://github.com/BortPablo/calculator-test",
                        is_external=True,
                    ),
                    width="33%",
                    center_content=True,
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),
            rx.hstack(
                rx.vstack(rx.heading("Poker", style=style.subheading_style), width="33%"),
                rx.vstack(rx.text("Personal project concerning probabilities in poker (Texas Hold'em).", style=style.message_style), width="33%"),
                rx.vstack(
                    rx.link(
                        rx.button(
                            rx.image(src="/icons/GitHub_Logo.png", width="100%", height="100%"),
                            style=style.button_style
                        ),
                        href="https://github.com/BortPablo/poker",
                        is_external=True,
                    ),
                    width="33%",
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),
            rx.hstack(
                rx.vstack(rx.heading("Turbine predictive maintenance", style=style.subheading_style), width="33%"),
                rx.vstack(rx.text("Personal project improving methodology and models of master thesis for turbine predictive maintenance.", style=style.message_style), width="33%"),
                rx.vstack(
                    rx.link(
                        rx.button(
                            rx.image(src="/icons/GitHub_Logo.png", width="100%", height="100%"),
                            style=style.button_style
                        ),
                        href="https://github.com/BortPablo/turbine_predictive_maintenance",
                        is_external=True,
                    ),
                    width="33%",
                ),
                height="10em",
                width="100%",
                border_radius="1em",
                border="1px solid #FF0080",
            ),            
        ),
    )

def contact_me() -> rx.Component:
    return rx.container(
        rx.text("Feel free to get in touch with me:", style=style.message_style),
        rx.button_group(
            rx.link(
                rx.button(
                    rx.image(src="/icons/email.png", width="100%", height="100%"),
                    style=style.button_style
                    ),
                href="mailto:pablobort98@gmail.com",
                ),
            rx.link(
                rx.button(
                    rx.image(src="/icons/icons8-linkedin.svg", width="100%", height="100%"),
                    style=style.button_style
                    ),
                href="https://www.linkedin.com/in/pablo-bort-gomez/",
                ),
            rx.link(
                rx.button(
                    rx.image(src="/icons/github-mark.svg", width="100%", height="100%"),
                    style=style.button_style
                    ),
                href="https://github.com/BortPablo",
                ),
            rx.link(
                rx.button(
                    rx.text("EN", style=style.message_style),
                    rx.icon(tag="arrow_forward"),
                    rx.text("ES", style=style.message_style),
                    style=style.button_style
                ),
                href="/es",
            ),
            
        ),
        center_content=True,
    )

def index() -> rx.Component:
    return rx.vstack(
    rx.heading("Pablo Bort", style=style.heading_style, height="2em"),
    rx.tabs(
        rx.tab_list(
            about_me_tab(),
            technologies_tab(),
            personal_projects_tab(),
        ),
        rx.tab_panels(
            about_me_panel(),
            technologies_panel(),
            personal_projects_panel(),
        ),
        width="90%",
        variant= "soft-rounded",
        orientation="vertical",
    ),
    contact_me(),
)


app = rx.App(state=State)
app.add_page(index)
app.add_page(index_es, route="/es")
app.compile()
