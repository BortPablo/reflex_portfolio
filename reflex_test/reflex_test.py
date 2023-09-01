import reflex as rx
from reflex_test import style

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
        rx.button_group(
            rx.link(
                rx.button(
                    rx.image(src="/icons/icons8-linkedin.svg", width="100%", height="100%"),
                    style=style.button_style
                    ),
                href="https://www.linkedin.com/in/pablo-bort-gomez/",
                is_external=True,
                width="33%",
                ),
            rx.link(
                rx.button(
                    rx.image(src="/icons/github-mark.svg", width="100%", height="100%"),
                    style=style.button_style
                    ),
                href="https://github.com/BortPablo",
                is_external=True,
                width="33%",
                ),
            rx.link(
                rx.button(
                    rx.image(src="/icons/cv.png", width="100%", height="100%"),
                    style=style.button_style
                    ),
                href="https://drive.google.com/uc?id=1NRtDqXdPOhDFerh0NApQIdvkTrrPJCTh&export=download",
                width="33%",
                ),
        ),
    )

def about_me_image() -> rx.Component:
    return rx.center(
        rx.image(
            src="me.jpg",
            border_radius="25% 25%",
            ),
    )

def about_me() -> rx.Component:
    return rx.accordion_item(
            rx.accordion_button(
                rx.heading("About me", style=style.heading_style),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.hstack(
                    rx.container(
                        about_me_text(),
                        width="50%",
                    ),
                    rx.container(
                        about_me_image(),
                        width="50%",
                    ),
                ),
                open=True,
            ),
        )

def technologies() -> rx.Component:
    return rx.accordion_item(
            rx.accordion_button(
                rx.heading("Technologies", style=style.heading_style),
                rx.accordion_icon(),

            ),
            rx.accordion_panel(
                rx.hstack(
                    rx.container(
                        rx.vstack(rx.heading("ETL/ML frameworks", style=style.subheading_style), height="20%"),
                        rx.hstack(
                            rx.vstack(
                                rx.image(src="/icons/mlflow-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/qlik-logo.png", width="100%", height="100%"),
                                width="50%",
                            ),
                            rx.vstack(
                                rx.image(src="/icons/tableau-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/grafana-logo.png", width="100%", height="100%"),
                                width="50%",
                            ),
                            height="80%",
                        ),
                        width="25%",
                        height="20em",
                        center_content=True,
                    ),
                    rx.container(
                        rx.vstack(rx.heading("Python packages", style=style.subheading_style), height="20%"),
                        rx.hstack(
                            rx.vstack(
                                rx.image(src="/icons/pandas-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/scipy-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/numpy-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/matplotlib-logo.png", width="100%", height="100%"),
                                width="50%",
                            ),
                            rx.vstack(
                                rx.image(src="/icons/tensorflow-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/sklearn-logo.png", width="100%", height="100%"),
                                rx.image(src="/icons/xgboost-logo.png", width="100%", height="100%"),
                                width="50%",
                            ),
                            height="80%",
                        ),
                        width="25%",
                        height="20em",
                        center_content=True,
                    ),
                    rx.container(
                        rx.vstack(rx.heading("Databases", style=style.subheading_style), height="20%"),
                        rx.vstack(
                            rx.image(src="/icons/influxdb-logo.png"),
                            rx.image(src="/icons/mongodb-logo.png"),
                            rx.image(src="/icons/mysql-logo.png"),
                            height="80%",
                        ),
                        width="25%",
                        height="20em",
                        center_content=True,
                    ),
                    rx.container(
                        rx.vstack(rx.heading("Containers", style=style.subheading_style), height="20%"),
                        rx.vstack(
                            rx.image(src="/icons/portainer-logo.png"),
                            rx.image(src="/icons/docker-logo.png"),
                            rx.image(src="/icons/kubernetes-logo.png"),
                            height="80%",

                        ),
                        width="25%",
                        height="20em",
                        center_content=True,
                    ),
                ),
            ),
        )

def personal_projects() -> rx.Component:
    return rx.accordion_item(
            rx.accordion_button(
                rx.heading("Personal projects", style=style.heading_style),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
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
                    ),            
            ),
        )
    )

def contact_me() -> rx.Component:
    return rx.accordion_item(
            rx.accordion_button(
                rx.heading("Contact me", style=style.heading_style),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.text("Feel free to get in touch with me"),
                rx.button_group(
                    rx.link(
                        rx.button(
                            rx.image(src="/icons/email.png", width="100%", height="100%"),
                            style=style.button_style
                            ),
                        href="mailto:pablobort98@gmail.com",
                        width="33%",
                        ),
                    rx.link(
                        rx.button(
                            rx.image(src="/icons/icons8-linkedin.svg", width="100%", height="100%"),
                            style=style.button_style
                            ),
                        href="https://www.linkedin.com/in/pablo-bort-gomez/",
                        width="33%",
                        ),
                    rx.link(
                        rx.button(
                            rx.image(src="/icons/github-mark.svg", width="100%", height="100%"),
                            style=style.button_style
                            ),
                        href="https://github.com/BortPablo",
                        width="33%",
                        ),
                ),
            ),
        )

def index() -> rx.Component:
    return rx.vstack(
    rx.heading("Pablo Bort", style=style.heading_style),
    rx.accordion(
        about_me(),
        technologies(),
        personal_projects(),
        contact_me(),
        allow_toggle=True,
        width="50%",
    ),
)


app = rx.App()
app.add_page(index)
app.compile()
