```py
from textual.app import App, ComposeResult
from textual.widgets import Static


class HorizontalLayoutExample(App):
    CSS_PATH = "css/horizontal_layout_overflow.tcss"

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")


if __name__ == "__main__":
    app = HorizontalLayoutExample()
    app.run()
```

```tcss
Screen {
    layout: horizontal;
    overflow-x: auto;
}

.box {
    height: 100%;
    border: solid green;
}
```


```py
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Static


class CombiningLayoutsExample(App):
    CSS_PATH = "css/combining_layouts.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for number in range(30):
                    yield Static(f"Vertical layout, child {number}")
            with Horizontal(id="top-right"):
                yield Static("Horizontally")
                yield Static("Positioned")
                yield Static("Children")
                yield Static("Here")
            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("panel")
                yield Static("is")
                yield Static("using")
                yield Static("grid layout!", id="bottom-right-final")


if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
```

```py
>>> from textual.containers import Container, Horizontal, VerticalScroll
>>> help(VerticalScroll.scroll_up)

Help on function scroll_up in module textual.widget:

scroll_up(self, *, animate: 'bool' = True, speed: 'float | None' = None, duration: 'float | None' = None, easing: 'EasingFunction | str | None' = None, force: 'bool' = False, on_complete: 'CallbackType | None' = None, level: 'AnimationLevel' = 'basic', immediate: 'bool' = False) -> 'None'
    Scroll one line up.

    Args:
        animate: Animate scroll.
        speed: Speed of scroll if `animate` is `True`; or `None` to use `duration`.
        duration: Duration of animation, if `animate` is `True` and speed is `None`.
        easing: An easing method for the scrolling animation.
        force: Force scrolling even when prohibited by overflow styling.
        on_complete: A callable to invoke when the animation is finished.
        level: Minimum level required for the animation to take place (inclusive).
        immediate: If `False` the scroll will be deferred until after a screen refresh,
            set to `True` to scroll immediately.
```


```py
from textual.app import App, ComposeResult
from textual.color import Color
from textual.widgets import Footer, Static


class Bar(Static):
    pass


class BindingApp(App):
    CSS_PATH = "css/binding01.tcss"
    BINDINGS = [
        ("r", "add_bar('red')", "Add Red"),
        ("g", "add_bar('green')", "Add Green"),
        ("b", "add_bar('blue')", "Add Blue"),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()

    def action_add_bar(self, color: str) -> None:
        bar = Bar(color)
        bar.styles.background = Color.parse(color).with_alpha(0.5)
        self.mount(bar)
        self.call_after_refresh(self.screen.scroll_end, animate=False)


if __name__ == "__main__":
    app = BindingApp()
    app.run()
```

---


from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Static

class CombiningLayoutsExample(App):
    CSS_PATH = "css/combining_layouts.tcss"
    BINDINGS = [
        ("j", "scroll_down", "Scroll Down"),
        ("k", "scroll_up", "Scroll Up"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for number in range(30):
                    yield Static(f"Vertical layout, child {number}")
            with Horizontal(id="top-right"):
                yield Static("Horizontally")
                yield Static("Positioned")
                yield Static("Children")
                yield Static("Here")
            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("panel")
                yield Static("is")
                yield Static("using")
                yield Static("grid layout!", id="bottom-right-final")

    def action_scroll_down(self) -> None:
        vertical_scroll = self.query_one("#left-pane", VerticalScroll)
        vertical_scroll.scroll_down(animate=True)

    def action_scroll_up(self) -> None:
        vertical_scroll = self.query_one("#left-pane", VerticalScroll)
        vertical_scroll.scroll_up(animate=True)

if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
