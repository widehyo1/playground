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
