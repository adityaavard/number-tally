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

    def resetcounter(self):
        self.count = 0

#main page

def index():
    return rx.hstack(
        rx.vstack(
            rx.button("+1",
                      bg="green",
                      color="white",
                      on_click=State.incrementby1)
        )
    )

#reflex compiler
epp = rx.App(state=State)
epp.add_page(index, "/", title="numbertally")
epp.compile()