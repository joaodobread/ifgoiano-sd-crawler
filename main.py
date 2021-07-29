import time
from dotenv import load_dotenv, find_dotenv
from src.crawler.factory import crawler_factory
from src.referrer.referrer import Referrer
from src.csv_writter.csv_writter import CSVWritter


load_dotenv(find_dotenv())


def main():

    crawler = crawler_factory(
        'https://gizmodo.uol.com.br/', 'https://gizmodo.uol.com.br/')

    crawler.setDaemon(True)
    crawler.start()
    crawler.join()

    reffer = Referrer.get_instance()
    links = reffer.get_links()
    set_of_links = reffer.set_of_links

    csvwritter = CSVWritter(
        './output/graph_node.csv', './output/graph_edges.csv', links, set_of_links)
    csvwritter.run()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print((time.time() - start_time))
