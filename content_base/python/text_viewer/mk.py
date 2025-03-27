from textual.app import App, ComposeResult
from textual.widgets import Markdown

class MarkdownTableApp(App):
    def compose(self) -> ComposeResult:
        md = """
# User Data Table

| ID | Name    | Age |
|----|---------|-----|
| 1  | ^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $^Alice  $| 30  |
| 2  | Bob     | 25  |
| 3  | Charlie | 35  |
"""
        yield Markdown(md)

if __name__ == "__main__":
    MarkdownTableApp().run()
