from crewai.flow.flow import Flow, listen, start, router, and_, or_
import random

from pydantic import BaseModel


class FlowState(BaseModel):
    user_id: int = 1
    is_admin: bool = False


class MyFlow(Flow[FlowState]):
    @start()
    def first(self):
        print(self.state)
        self.state.user_id = 2
        print("Starting the flow")

    @listen(first)
    def second(self):
        print(self.state)
        print("Second step")

    @listen(first)
    def third(self):
        print("Third step")

    @listen(and_(second, third))
    def final(self):
        self.state.is_admin = True
        print("Final step")

    @router(final)
    def route(self):
        print(self.state)
        a = random.randint(1, 100)
        if a % 2 == 0:
            return "even"
        else:
            return "odd"

    @listen("even")
    def handle_even(self):
        print("Even step")

    @listen("odd")
    def handle_odd(self):
        print("Odd step")


flow = MyFlow()

# flow.plot() -> to plot the flow

flow.kickoff()
