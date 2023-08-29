import solara

import multipage.level1.page1 as uno
import multipage.page0 as p0


@solara.component
def Page():
    p0_color = "green"
    if p0.clicks.value >= 5:
        p0_color = "red"

    p1_color = "green"
    if uno.clicks.value >= 5:
        p1_color = "red"

    def increment_0():
        p0.clicks.value += 1

    def increment_1():
        uno.clicks.value += 1

    solara.Button(label=f"Level 0 Clicked: {p0.clicks}", on_click=increment_0, color=p0_color)
    solara.Button(label=f"Level 1 Clicked: {uno.clicks}", on_click=increment_1, color=p1_color)
