import reflex as rx

gradient = "linear(to-l, #7928CA, #FF0080)"
background_gradient = "bgGradient='radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);',"
shadow = "0 0 5px 5px #FF0080"

# Common styles for de app.
app_style = dict(
    bgGradient=background_gradient
)

# Common styles for text.
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.25em",
    display="inline-block",
    font_family= "Hack Nerd Font Mono",
    font_size="15px",
)

# Common styles for buttons.
button_style = dict(
    border_radius="1em",
    bgGradient=gradient,
    opacity="0.8",
    _hover={
        "background": "white",
        "box_shadow": shadow,
    },
)

# Common styles for headings.
heading_style = dict(
    #font_family= "Hack Nerd Font Mono",
    font_size="2.5em",
    font_weight="bold",
    margin_y="0.25em",
    margin_x="0.25em",
    text_align="center",
    bgGradient=gradient,
    bgClip="text",
)

subheading_style = dict(
    #font_family= "Hack Nerd Font Mono",
    font_size="1.5em",
    text_align="center",
    bgGradient=gradient,
    bgClip="text",
)



