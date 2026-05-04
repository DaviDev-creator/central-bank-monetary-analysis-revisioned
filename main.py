import sys
from scraper import CentralBankScraper

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <instrument> <date>")
        return

    instrument = sys.argv[1]
    date = sys.argv[2]
    
    scraper = CentralBankScraper()
    print(f"Processing {instrument} for {date}...")
    result = scraper.execute(instrument, date)
    print("\n--- Processed News ---\n")
    print(result)

if __name__ == "__main__":
    main()
