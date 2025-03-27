class MyScrollBarRender(ScrollBarRender): ...

app = MyApp()
ScrollBar.renderer = MyScrollBarRender
app.run()
