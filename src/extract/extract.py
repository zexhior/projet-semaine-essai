import pandas as pd
from src.model.file import File

class ExtractEngine:
    def __init__(self, file_path, sheets):
        self.file_path = file_path
        self.data = None
        self.sheets = sheets
        
    def load(self, session):
        self.data = pd.read_excel(self.file_path, sheet_name=None)
        file = File(name=self.file_path)
        session.add(file)
        session.commit()

    def clean(self):
        if self.data is not None:
            # Clean each sheet
            for sheet_name in self.data:
                if sheet_name == 'details_cp':
                    # Use first row as header and skip it
                    self.data[sheet_name].columns = self.data[sheet_name].iloc[0]
                    self.data[sheet_name] = self.data[sheet_name].iloc[1:].reset_index(drop=True)
                else:
                    # For other sheets, just drop first row if needed
                    self.data[sheet_name] = self.data[sheet_name].iloc[1:].reset_index(drop=True)
        
    def extract(self, session):
        if self.data is None or session is None:
            raise ValueError("Data not loaded or session not provided. Please call load() before extract() and provide a valid session.")
        for sheet_name, df in self.data.items():
            print(f"Extracting data from sheet: {sheet_name}")
            for index, row in df.iterrows():
                # Get file_id from the most recent file
                print(f"Processing row {index} in sheet {sheet_name}")
                latest_file = session.query(File).order_by(File.id.desc()).first()
                file_id = latest_file.id if latest_file else 1
                data=None
                
                if sheet_name == 'recap_rz':
                    sheet = next((data for data in self.sheets if data['name'] == 'recap_rz'), None)
                    if sheet:
                        data = sheet['model'](
                            week_start=row['WEEK_START'],
                            nom_tdp=row['NOM_TDP'],
                            nd_tdp=row['ND_TDP'],
                            nd_rz=row['ND_RZ'],
                            nom=row['NOM'],
                            prenom=row['PRENOM'],
                            region=row['REGION'],
                            ville=row['VILLE'],
                            nd_cp_appro=row['ND_CP_APPRO'],
                            appro_ume=row['APPRO_UME'],
                            appro_cash=row['APPRO_CASH'],
                            montant_ci=row['MONTANT_CI'],
                            file_id=file_id)
                        
                if sheet_name == 'details_appro_rz':
                    sheet = next((data for data in self.sheets if data['name'] == 'details_appro_rz'), None)
                    if sheet:
                        data = sheet['model'](
                            week_start=row['WEEK_START'],
                            nom_tdp=row['NOM_TDP'],
                            nd_rz=row['ND_RZ'],
                            nd_cp=row['ND_CP'],
                            nom=row['NOM'],
                            prenom=row['PRENOM'],
                            region=row['REGION'],
                            ville=row['VILLE'],
                            appro_ume_rz=row['APPRO_UME_RZ'],
                            appro_cash_rz=row['APPRO_CASH_RZ'],
                            file_id=file_id)
                        
                if sheet_name == 'details_cp':
                    sheet = next((data for data in self.sheets if data['name'] == 'details_cp'), None)
                    if sheet:
                        data = sheet['model'](
                            week_start=row['WEEK START'],
                            nom_tdp=row['NOM TDP'],
                            nd_cp=row['ND CP'],
                            nom_cp=row['NOM CP'],
                            prenom_cp=row['PRENOM CP'],
                            region=row['REGION'],
                            ville=row['VILLE'],
                            appro_ume_tdp=row['APPRO UME TDP'],
                            appro_cash_td=row['APPRO CASH TDP'],
                            appro_ume_rz=row['APPRO UME RZ'],
                            appro_cash_rz=row['APPRO CASH RZ'],
                            montant_ci=row['MONTANT CI'],
                            montant_co=row['MONTANT CO'],
                            montant_ci_shop=row['MONTANT CI SHOP'],
                            file_id=file_id)
                        
                session.add(data)
            session.commit()
        
    def read(self):
        if self.data is not None:
            print(self.data.head())