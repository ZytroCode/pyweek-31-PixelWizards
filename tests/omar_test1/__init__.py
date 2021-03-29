from app import App

app = App(
    title = "Cops"
)

@app.update
def update():
    print("HELLO WROLD!")

app.run()