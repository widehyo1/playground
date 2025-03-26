from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Static

class CombiningLayoutsExample(App):
    CSS_PATH = "css/combining_layouts.tcss"
    BINDINGS = [
        ("j", "scroll_down", "Scroll Down"),
        ("k", "scroll_up", "Scroll Up"),
        ("h", "scroll_left", "Scroll Left"),
        ("l", "scroll_right", "Scroll Right"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            # Vertical scrolling pane
            with VerticalScroll(id="left-pane"):
                for number in range(30):
                    yield Static(f"Vertical layout, child {number}")
            # Horizontal scrolling pane (using ScrollView)
            with HorizontalScroll(id="top-right"):
                yield Static("Horizontally")
                yield Static("Positioned")
                yield Static("Children")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
                yield Static("Here")
            # Bottom right panel remains unchanged
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

    def action_scroll_left(self) -> None:
        horizontal_scroll = self.query_one("#top-right", HorizontalScroll)
        horizontal_scroll.scroll_left(animate=True)

    def action_scroll_right(self) -> None:
        horizontal_scroll = self.query_one("#top-right", HorizontalScroll)
        horizontal_scroll.scroll_right(animate=True)

if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
