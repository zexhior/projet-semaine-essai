import sys
from pathlib import Path
from src.model.live_service_sheets import RecapRZ, DetailsApproRz, DetailsCP
from src.model.suivi import (
    TransactionRZ,
    TransactionGrossisteVersRZ,
    TransactionPDV,
    TransactionLivreur,
    TransactionGrossisteLivreur,
    SoldeAgents
)
from src.model.connexion import Connexion

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from config.connexion import session
from extract.extract import ExtractEngine

class Main():
    def __init__(self, engine):
        self.session = session
        
    def run(self):
        # sheets = [
        #     {'name': 'recap_rz', 'model': RecapRZ},
        #     {'name': 'details_appro_rz', 'model': DetailsApproRz},
        #     {'name': 'details_cp', 'model': DetailsCP}
        # ]
        sheets = {
            'Transaction RZ': TransactionRZ,
            'Transaction Grossiste vers RZ': TransactionGrossisteVersRZ,
            'Transaction PDV': TransactionPDV,
            'Transaction Livreur': TransactionLivreur,
            'Transaction Grossiste vers Livr': TransactionGrossisteLivreur,
            'Solde des Agents': SoldeAgents
        }
        extract_engine = ExtractEngine("./src/data", sheets)
        extract_engine.extract(self.session)
        # print("Running the main application...")
        
    def stop(self):
        print("Stopping the main application...")
    
    def read(self):
        print("Reading data from the database...")
        live_services = self.session.query(LiveService).all()
        for service in live_services:
            print(service)
            
import socket

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False
        
if __name__ == "__main__":
    engine = None  # Replace with your actual engine initialization
    app = Main(engine)
    app.run()
    
    from datetime import datetime
    import time

    while True:
        if is_connected():
            connexion = Connexion(source='application', status='connected',
            description='Internet connecté', checked_at=datetime.now())
            session.add(connexion)
            session.commit()
        else:
            print("Internet perdu")

        time.sleep(10)