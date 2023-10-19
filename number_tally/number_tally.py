#imports
import reflex as rx
#add state
class State(rx.State):
    count = 0

    def incrementby1(self):
        self.count += 1

    def decrementby1(self):
        self.count -= 1

    def multiplyby2(self):
        self.count *= 2

    def divideby2(self):
        self.count /= 2

    def incrementby5(self):
        self.count += 5
    
    def decrementby5(self):
        self.count -= 5

    def multiplyby5(self):
        self.count *= 5
    
    def divideby5(self):
        self.count /= 5
    
    def incrementby50(self):
        self.count += 50
    
    def decrementby50(self):
        self.count -= 50

    def multiplyby50(self):
        self.count *= 50
    
    def divideby50(self):
        self.count /= 50
    
    def incrementby500(self):
        self.count += 500
    
    def decrementby500(self):
        self.count -= 500

    def multiplyby500(self):
        self.count *= 500
    
    def divideby500(self):
        self.count /= 500

    def incrementby5000(self):
        self.count += 5000

    def decrementby5000(self):
        self.count -= 5000

    def multiplyby5000(self):
        self.count *= 5000

    def divideby5000(self):
        self.count /= 5000
    
    def incrementby50000(self):
        self.count += 50000

    def decrementby50000(self):
        self.count -= 50000

    def multiplyby50000(self):
        self.count *= 50000

    def divideby50000(self):
        self.count /= 50000
    
    def incrementby500000(self):
        self.count += 500000

    def decrementby500000(self):
        self.count -= 500000

    def multiplyby500000(self):
        self.count *= 500000

    def divideby500000(self):
        self.count /= 500000

    def incrementby5000000(self):
        self.count += 5000000

    def decrementby5000000(self):
        self.count -= 5000000

    def multiplyby5000000(self):
        self.count *= 5000000

    def divideby5000000(self):
        self.count /= 5000000

    def setzero(self):
        self.count = 0

    def funnyset(self):
        self.count = 69420
#main page
def index():
    return rx.vstack(
        rx.hstack(
            rx.heading(State.count, font_size="5em")
        ),
        rx.hstack(
            rx.button("+1", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby1),
            rx.button("-1", color_scheme="red", border_radius="2em",
                      on_click=State.decrementby1),
            rx.button("x2", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby2),
            rx.button("/2", color_scheme="red", border_radius="2em",
                      on_click=State.divideby2)
        ),
        rx.hstack(
            rx.button("+5", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby5),
            rx.button("-5", color_scheme="red", border_radius="2em",
                      on_click=State.decrementby5),
            rx.button("x5", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby5),
            rx.button("/5", color_scheme="red", border_radius="2em",
                      on_click=State.divideby5)
        ),
        rx.hstack(
            rx.button("+50", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby50),
            rx.button("-50", color_scheme="red", border_radius="2em",
                      on_click=State.decrementby50),
            rx.button("x50", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby50),
            rx.button("/50", color_scheme="red", border_radius="2em",
                      on_click=State.divideby50)
        ),
        rx.hstack(
            rx.button("+500", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby500),
            rx.button("/500", color_scheme="red", border_radius="2em",
                      on_click=State.divideby500)
        ),
        rx.hstack(
            rx.button("+5000", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby5000),
            rx.button("-5000", color_scheme="red", border_radius="2em",
                      on_click=State.decrementby5000),
            rx.button("x5000", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby5000),
            rx.button("/5000", color_scheme="red", border_radius="2em",
                      on_click=State.divideby5000)
        ),
        rx.hstack(
            rx.button("+50000", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby50000),
            rx.button("-50000", color_scheme="red", border_radius="2em",
                      on_click=State.decrementby50000),
            rx.button("x50000", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby50000),
            rx.button("/50000", color_scheme="red", border_radius="2em",
                      on_click=State.divideby50000)
        ),
        rx.hstack(
            rx.button("+500000", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby500000),
            rx.button("-500000", color_scheme="red", border_radius="2em",
                      on_click=State.decrementby500000),
            rx.button("x500000", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby500000),
            rx.button("/500000", color_scheme="red", border_radius="2em",
                      on_click=State.divideby500000)
        ),
        rx.hstack(
            rx.button("+5000000", color_scheme="green", border_radius="2em",
                      on_click=State.incrementby5000000),
            rx.button("-5000000", color_scheme="red", border_radius="2em", 
                      on_click=State.decrementby5000000),
            rx.button("x5000000", color_scheme="green", border_radius="2em",
                      on_click=State.multiplyby5000000),
            rx.button("/5000000", color_scheme="red", border_radius="2em",
                      on_click=State.divideby5000000)
        ),
        rx.hstack(
            rx.button("RESET", color_scheme="blue", border_radius="1em",
                      on_click=State.setzero),
            rx.button("69420", color_scheme="blue", border_radius="1em",
                      on_click=State.funnyset)
        )
    )
#reflex compiler
app = rx.App(state=State)
app.add_page(index, "/", title="calculate")
app.compile()