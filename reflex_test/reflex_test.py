import reflex as rx

def about_me_text() -> rx.Component:
    return rx.vstack(
        rx.text("""Graduated in physics with a master's degree in Big Data Analytics. 
                Currently working as a Data Scientist, engaging with a variety of projects, 
                including European energy initiatives.""",
                font_size="1.25em",
                ),
        rx.text("""Interested in Artificial Intelligence, data analysis, and visualization.
                 This portfolio showcases projects that highlight my commitment to leveraging data for meaningful outcomes.
                 I invite you to explore and connect.""",
                font_size="1.25em",
                ),
        rx.hstack(
            rx.button(rx.image(src="/icons/linkedin.svg", width="100%", height="100%"), on_click="https://www.linkedin.com/in/pablo-bort-gomez/"),
            rx.button(rx.image(src="/icons/github.svg", width="100%", height="100%")),
            rx.button(rx.image(src="/icons/cv.png", width="100%", height="100%")),
        ),
        width="50%",
        padding="1em",
    )
        

def about_me_image() -> rx.Component:
    return rx.center(
        rx.image(
            src="me.jpg",
            width="50%", 
            height="50%",
            border_radius="25% 25%",
            ),
        width="50%",
    )


def about_me() -> rx.Component:
    return rx.accordion_item(
            rx.accordion_button(
                rx.heading("About me"),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.hstack(
                    about_me_text(),
                    about_me_image(),
                ),
            ),
        )

def index() -> rx.Component:
    return rx.vstack(
    rx.heading("Pablo Bort", font_size="2em"),
    rx.heading("Data Scientist", font_size="1.5em"),
    rx.accordion(
        about_me(),
        allow_toggle=True,
        width="80%",
    ),
)


app = rx.App()
app.add_page(index)
app.compile()
