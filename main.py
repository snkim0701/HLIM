from src.collectors.price_collector import PriceCollector

collector = PriceCollector(
    ticker="MU",
    start="2015-01-01"
)

collector.download()

collector.save()