from icrawler.builtin import BingImageCrawler

# Definís qué querés buscar
busquedas = [
    "night sky no moon",
    "dark sky clouds night",
    "sunset sky no moon",
    "cloudy night sky",
    "black sky background"
]

for termino in busquedas:
    crawler = BingImageCrawler(storage={'root_dir': f'imagenesWWW/{termino.replace(" ", "_")}'})
    crawler.crawl(keyword=termino, max_num=200)