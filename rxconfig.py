import reflex as rx

class ReflextestConfig(rx.Config):
    pass

config = ReflextestConfig(
    app_name="reflex_test",
    api_url="http://0.0.0.0:8000",
    port=3000,
)