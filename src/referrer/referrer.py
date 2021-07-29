class Referrer:
    __instance = None

    def __init__(self):
        self.__links = []
        self.set_of_links = set()

    def add_link(self, link: str, refers_to: str):
        self.set_of_links.add(link)
        self.set_of_links.add(refers_to)

        self.__links.append({
            "link": link,
            "refers_to": refers_to
        })

        self.__links = list(
            {item["refers_to"]: item for item in self.__links}.values())
        return self.__links

    def get_links(self):
        return self.__links

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance
