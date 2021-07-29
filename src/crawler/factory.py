from .crawler import Crawler


def crawler_factory(actual_link: str, actual_domain: str, deep_level=1):
    crawler = Crawler(deep_factor=deep_level,
                      actual_domain=actual_domain, actual_link=actual_link)

    return crawler
