import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from config.connexion import session
from extract.extract import ExtractEngine

class Main():
    def __init__(self, engine):
        self.session = session
        
    def read(self):
        self.session.execute("SELECT * FROM live_service")
        
    def run(self):
        extract_engine = ExtractEngine("./src/data/REPORT_WEEKLY_LIVE_SERVICES_S_1_2025 - Copy.xlsx")
        extract_engine.load(self.session)
        extract_engine.clean()
        extract_engine.extract(self.session)
        print("Running the main application...")
        
    def stop(self):
        print("Stopping the main application...")
        
if __name__ == "__main__":
    engine = None  # Replace with your actual engine initialization
    app = Main(engine)
    app.run()
    app.stop()