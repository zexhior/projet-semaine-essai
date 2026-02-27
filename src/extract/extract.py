import pandas as pd
import glob
import numpy as np
from sqlalchemy import Date
from src.model.file import File

class ExtractEngine:
    def __init__(self, folder_path, sheets):
        self.folder_path = folder_path
        self.data = None
        self.sheets = sheets

    def clean(self):
        if self.data is not None:
            # Clean each sheet
            for sheet_name in self.data:
                if sheet_name == 'Transaction RZ' or sheet_name == 'Transaction Grossiste vers RZ':
                    self.data[sheet_name].columns = self.data[sheet_name].iloc[2]
                    self.data[sheet_name] = self.data[sheet_name].iloc[3:].reset_index(drop=True)
                else:
                    self.data[sheet_name].columns = self.data[sheet_name].iloc[0]
                    self.data[sheet_name] = self.data[sheet_name].iloc[1:].reset_index(drop=True)
                    
    def clean_empty_data(self, data):
        if pd.isna(data):
            return None
        if isinstance(data, pd.Timestamp):
            return data.date()
        if isinstance(data, np.generic):
            return data.item()
        if isinstance(data, str):
            data = data.strip()
            return data if data else None
        return data

    def has_missing_required_fields(self, model, payload):
        ignored_columns = {"id", "created_at", "updated_at"}
        missing_fields = []

        for column in model.__table__.columns:
            if column.name in ignored_columns:
                continue
            if column.nullable:
                continue
            if column.default is not None or column.server_default is not None:
                continue
            if payload.get(column.name) is None:
                missing_fields.append(column.name)

        return missing_fields

    def normalize_payload_for_model(self, model, payload):
        normalized_payload = {}

        for column in model.__table__.columns:
            column_name = column.name
            if column_name not in payload:
                continue

            value = payload[column_name]

            if pd.isna(value):
                value = None

            if isinstance(value, str):
                value = value.strip()
                value = value if value else None

            if value is not None and isinstance(column.type, Date):
                if isinstance(value, pd.Timestamp):
                    value = value.date()
                else:
                    parsed_date = pd.to_datetime(value, errors='coerce')
                    value = None if pd.isna(parsed_date) else parsed_date.date()

            normalized_payload[column_name] = value

        return normalized_payload
            
    def extract(self, session):
        folder_path = self.folder_path
        files = glob.glob(folder_path+'/*.xlsx')
        for file_path in files:
            self.data = pd.read_excel(file_path, sheet_name=None)
            file = File(name=file_path)
            session.add(file)
            session.commit()
            file_id = file.id
            self.clean()
            print('Extract from file:', file_path)
            if self.data is None or session is None:
                raise ValueError("Data not loaded or session not provided. Please call load() before extract() and provide a valid session.")
            for sheet_name, sheet_model in self.sheets.items():
                if sheet_name not in self.data:
                    continue

                print(f"Processing sheet: {sheet_name} from file: {file_path}")
                for _, row in self.data[sheet_name].iterrows():
                    payload = None

                    if sheet_name == 'Solde des Agents':
                        payload = {
                            'date': self.clean_empty_data(row['Date']),
                            'type_agent': self.clean_empty_data(row['Type Agent']),
                            'rattachement': self.clean_empty_data(row['Rattachement']),
                            'agent_msisdn': self.clean_empty_data(row['Agent Msisdn']),
                            'agent_nom': self.clean_empty_data(row['Agent Nom']),
                            'balance': self.clean_empty_data(row['Balance']),
                            'file_id': file_id,
                        }

                    if sheet_name == 'Transaction Grossiste vers Livr':
                        payload = {
                            'date': self.clean_empty_data(row['Date']),
                            'msisdn_grossiste': self.clean_empty_data(row['Msisdn Grossiste']),
                            'msisdn_livreur': self.clean_empty_data(row['Msisdn Livreur']),
                            'nombre_transferts_reçus': self.clean_empty_data(row['Nombre De Tranferts Reçus Par Le Livreur']),
                            'montant_transferts_reçus': self.clean_empty_data(row['Montant Des Tranferts Reçus Par Le Livreur']),
                            'file_id': file_id,
                        }

                    if sheet_name == 'Transaction Livreur':
                        payload = {
                            'date': self.clean_empty_data(row['Date']),
                            'msisdn_livreur': self.clean_empty_data(row['Msisdn Livreur']),
                            'msisdn_pdv': self.clean_empty_data(row['Msisdn Pdv']),
                            'nombre_transferts_reçus': self.clean_empty_data(row['Nombre De Tranferts Reçus Par Le Pdv']),
                            'montant_transferts_reçus': self.clean_empty_data(row['Montant Des Tranferts Reçus Par Le Pdv']),
                            'file_id': file_id,
                        }

                    if sheet_name == 'Transaction PDV':
                        payload = {
                            'date': self.clean_empty_data(row['Date']),
                            'msisdn_pdv': self.clean_empty_data(row['Msisdn Pdv']),
                            'date_activation': self.clean_empty_data(row['Date Activation']),
                            'last_date': self.clean_empty_data(row['Last Date']),
                            'msisdn_rattachement': self.clean_empty_data(row['Liv Msisdn Rattachement']),
                            'nombre_transactions': self.clean_empty_data(row['Nombre De Transactions']),
                            'montant_transactions': self.clean_empty_data(row['Montant Transactions']),
                            'file_id': file_id,
                        }

                    if sheet_name == 'Transaction Grossiste vers RZ':
                        payload = {
                            'date': self.clean_empty_data(row['Date']),
                            'msisdn_grossiste': self.clean_empty_data(row['Msisdn Grossiste']),
                            'msisdn_rz': self.clean_empty_data(row['Msisdn Rz']),
                            'nombre_transferts_reçus': self.clean_empty_data(row['Nombre De Tranferts Reçus Par Le Rz']),
                            'montant_transferts_reçus': self.clean_empty_data(row['Montant Des Tranferts Reçus Par Le Rz']),
                            'file_id': file_id,
                        }

                    if sheet_name == 'Transaction RZ':
                        payload = {
                            'date': self.clean_empty_data(row['Date']),
                            'msisdn_rz': self.clean_empty_data(row['Msisdn Rz']),
                            'msisdn_livreur': self.clean_empty_data(row['Msisdn Livreur']),
                            'tld_msisdn_rattachement': self.clean_empty_data(row['Tld Msisdn Rattachement']),
                            'nombre_transferts_reçus': self.clean_empty_data(row['Nombre De Tranferts Reçus Par Le Livreur']),
                            'montant_transferts_reçus': self.clean_empty_data(row['Montant Des Tranferts Reçus Par Le Livreur']),
                            'file_id': file_id,
                        }

                    if payload is None:
                        continue

                    payload = self.normalize_payload_for_model(sheet_model, payload)
                    missing_fields = self.has_missing_required_fields(sheet_model, payload)
                    if missing_fields:
                        print(f"Skipping row due to missing required fields: {missing_fields} {sheet_name} in file {file_path}")
                        # continue

                    data = sheet_model(**payload)
                    session.add(data)
                session.commit()
        
        
    def read(self):
        if self.data is not None:
            print(self.data.head())