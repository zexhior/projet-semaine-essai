import sys
from pathlib import Path
from src.model.live_service_sheets import RecapRZ, DetailsApproRz, DetailsCP

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from config.connexion import session
from extract.extract import ExtractEngine

class Main():
    def __init__(self, engine):
        self.session = session
        
    def run(self):
        sheets = [
            {'name': 'recap_rz', 'model': RecapRZ},
            {'name': 'details_appro_rz', 'model': DetailsApproRz},
            {'name': 'details_cp', 'model': DetailsCP}
        ]
        extract_engine = ExtractEngine("./src/data/REPORT_WEEKLY_LIVE_SERVICES_S_1_2025 - Copy.xlsx", sheets)
        extract_engine.load(self.session)
        extract_engine.clean()
        extract_engine.extract(self.session)
        # print("Running the main application...")
        
    def stop(self):
        print("Stopping the main application...")
    
    def read(self):
        print("Reading data from the database...")
        live_services = self.session.query(LiveService).all()
        for service in live_services:
            print(service)
        
if __name__ == "__main__":
    engine = None  # Replace with your actual engine initialization
    app = Main(engine)
    app.run()
    # app.read()
    # app.stop()
    # app.read()