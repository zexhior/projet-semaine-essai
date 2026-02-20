import pandas as pd
from model.file import File
from model.live_service import LiveService

class ExtractEngine:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        
    def load(self, session):
        self.data = pd.read_excel(self.file_path)
        file = File(name=self.file_path)
        session.add(file)
        session.commit()

    def clean(self):
        if self.data is not None:
            # Drop the first two rows when they contain header-like column labels.
            self.data = self.data.iloc[2:].reset_index(drop=True)
        
    def extract(self, session):
        if self.data is None or session is None:
            raise ValueError("Data not loaded or session not provided. Please call load() before extract() and provide a valid session.")
        
        for index, row in self.data.iterrows():
            # Get file_id from the most recent file
            latest_file = session.query(File).order_by(File.id.desc()).first()
            file_id = latest_file.id if latest_file else 1
            
            live_service = LiveService(
                week_start=row['WEEK_START'],
                nom_tdp=row['NOM_TDP'],
                nd_cp=row['ND_TDP'],  # Map ND_TDP to nd_cp
                nom_cp=row['NOM'],
                prenom_cp=row['PRENOM'],
                region=row['REGION'],
                ville=row['VILLE'],
                appro_ume_tdp=int(row['APPRO_UME']) if pd.notna(row['APPRO_UME']) else 0,
                appro_cash_td=int(row['APPRO_CASH']) if pd.notna(row['APPRO_CASH']) else 0,
                appro_ume_rz=int(row['ND_RZ']) if pd.notna(row['ND_RZ']) else 0,
                appro_cash_rz=0,  # Not available in Excel
                montant_ci=int(row['MONTANT_CI']) if pd.notna(row['MONTANT_CI']) else 0,
                montant_co=0,  # Not available in Excel
                montant_ci_shop=0,  # Not available in Excel
                file_id=file_id
            )
            session.add(live_service)
        session.commit()