from textual.app import App, ComposeResult
from textual.widgets import DataTable, Header, Footer

class TableExample(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="data-table")
        yield Footer()

    def on_mount(self) -> None:
        data_table = self.query_one(DataTable)
        # Define columns with optional width and a key for each column.
        data_table.add_column("ID", key="id", width=5)
        data_table.add_column("Name", key="name", width=20)
        data_table.add_column("Age", key="age", width=5)
        
        # Add some rows of data.
        data_table.add_row("1", "Alice", "30")
        data_table.add_row("2", "Bob", "25")
        data_table.add_row("3", "Charlie", "35")

if __name__ == "__main__":
    TableExample().run()
