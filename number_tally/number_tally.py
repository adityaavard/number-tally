# hi, welcome to numbertally!

#imports

import reflex as rx

# addings state

class State(rx.State):

    # adding count

    count: int = 0

    def increase1(self):
        self.count + 1
    
    def decrease1(self):
        self.count - 1
    
    def increase2(self):
        self.count += 1
    
    def decrease2(self):
        self.count -= 1
    
    def resetcount(self):
        self.count = 0

def index():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.button("+1",
                          color="white",
                          bg="green",
                          border_radius="1g",
                          on_click=State.increase1)
        )
    )
)
app = rx.App(State=State)
app.add_page(index, "/", title="numtally")
app.compile