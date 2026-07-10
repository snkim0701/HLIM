from pathlib import Path
import yfinance as yf

from .base_collector import BaseCollector


class PriceCollector(BaseCollector):

    def __init__(self, ticker, start, end=None):
        super().__init__(ticker, start, end)
        self.data = None

    
    def download(self):
        
        df = yf.download(
            self.ticker,
            start=self.start,
            end=self.end,
            progress=False,
            auto_adjust=False
        )
        # yfinance의 MultiIndex 컬럼 처리
        if df.columns.nlevels >1 : 
            df.columns = df.columns.get_level_values(0)

        self.data = df

        print(self.data.head())
        print(self.data.columns)

        return df

    def save(self):
        project_root = Path(__file__).resolve().parents[2]
        data_dir = project_root / "data" / "raw"
        data_dir.mkdir(parents=True, exist_ok=True)

        filename = data_dir / f"{self.ticker}_price.csv"
        self.data.to_csv(filename)

        print(f"Saved: {filename}")