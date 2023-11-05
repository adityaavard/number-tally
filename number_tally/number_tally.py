"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

class State(rx.State):

    bar = 0

    def addone(self):
        self.bar = self.bar + 1

def index():   
    return rx.center(
rx.hstack(
    rx.circular_progress(
        rx.circular_progress_label(
            "", color="red",),
            value = 50
    ),
)
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
