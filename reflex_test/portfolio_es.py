import reflex as rx
from reflex_test import style

def about_me_text_es() -> rx.Component:
    return rx.vstack(
        rx.text("""Graduado en física con un máster en Big Data Analytics.
                 Actualmente trabajando como Científico de Datos, participando
                 en una variedad de proyectos, incluyendo iniciativas energéticas europeas.""",
                style=style.message_style,
                ),
        rx.text("""Interesado en Inteligencia Artificial, el análisis y la visualización de datos.
                 Este portfolio muestra proyectos que destacan mi compromiso con el aprovechamiento
                 de los datos para obtener resultados significativos. Te invito a explorar y conectar.""",
                style=style.message_style,
                ),
        rx.link(
            rx.button(
                rx.text("Descargar CV", style=style.message_style),
                rx.image(src="/icons/cv.png", width="100%", height="100%"),
                style=style.button_style
                ),
            href="https://drive.google.com/uc?id=1tPkTR6Eh_f-7JZ9qgK6GU5GslPO8N2Jf&export=download",
            ),
        )
def about_me_image_es() -> rx.Component:
    return rx.center(
        rx.image(
            src="/me/me.jpg",
            border_radius="25% 25%",
            ),
    )

def about_me_tab_es() -> rx.Component:
    return rx.tab(
        rx.heading("Sobre mí", style=style.heading_style),
        height="10em"
    )
def about_me_panel_es() -> rx.Component:
    return rx.tab_panel(
        rx.hstack(
            rx.container(
                about_me_text_es(),
                width="60%",
            ),
            rx.container(
                about_me_image_es(),
                width="40%",
            ),
        ),
    )

def technologies_tab_es() -> rx.Component:
    return rx.tab(
        rx.heading("Tecnologías", style=style.heading_style),
        height="10em"
    )
def technologies_panel_es() -> rx.Component:
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
                rx.vstack(rx.heading("Paquetes Python", style=style.subheading_style), width="20%"),
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
                rx.vstack(rx.heading("Bases de datos", style=style.subheading_style), width="20%"),
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
                rx.vstack(rx.heading("Puesta en producción", style=style.subheading_style), width="20%"),
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

def personal_projects_tab_es() -> rx.Component:
    return rx.tab(
        rx.heading("Proyectos personales", style=style.heading_style),
        height="10em"
    )
def personal_projects_panel_es() -> rx.Component:
    return rx.tab_panel(
        rx.vstack(
            rx.hstack(
                rx.vstack(rx.heading("Calculadora", style=style.subheading_style), width="33%"),
                rx.vstack(rx.text("Un ejemplo simple de calculadora que muestra cómo suelo trabajar en Python.", style=style.message_style), width="33%"),
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
                rx.vstack(rx.heading("Póker", style=style.subheading_style), width="33%"),
                rx.vstack(rx.text("Proyecto personal sobre probabilidades en el póker (Texas Hold'em).", style=style.message_style), width="33%"),
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
                rx.vstack(rx.heading("Mantenimiento predictivo de turbinas eólicas", style=style.subheading_style), width="33%"),
                rx.vstack(rx.text("Proyecto personal que mejora la metodología y los modelos del Trabajo Fin de Máster para el mantenimiento predictivo de turbinas.", style=style.message_style), width="33%"),
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

def contact_me_es() -> rx.Component:
    return rx.container(
        rx.text("No dudes en contactar conmigo:", style=style.message_style),
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
                    rx.text("ES", style=style.message_style),
                    rx.icon(tag="arrow_forward"),
                    rx.text("EN", style=style.message_style),
                    style=style.button_style
                ),
                href="/",
            ),
            
        ),
        center_content=True,
    )

def index_es() -> rx.Component:
    return rx.vstack(
    rx.heading("Pablo Bort", style=style.heading_style, height="2em"),
    rx.tabs(
        rx.tab_list(
            about_me_tab_es(),
            technologies_tab_es(),
            personal_projects_tab_es(),
        ),
        rx.tab_panels(
            about_me_panel_es(),
            technologies_panel_es(),
            personal_projects_panel_es(),
        ),
        width="90%",
        variant= "soft-rounded",
        orientation="vertical",
    ),
    contact_me_es(),
)
