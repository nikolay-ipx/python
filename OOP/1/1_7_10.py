class AppStore:
    list_store = []
    def add_application(self, app):
        self.app = app
        self.list_store.append(self.app)

    def remove_application(self, app):
        self.app = app
        self.list_store.remove(self.app)

    def block_application(self, app):
        self.app = app
        self.app.blocked = True

    def total_apps(self):
        return len(self.list_store)


class Application:
    def __init__(self, name, blocked = False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.add_application(app_youtube)
# store.remove_application(app_youtube)
print(store.list_store)
print(store.total_apps())