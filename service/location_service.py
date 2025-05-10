import pandas as pd

class LocationService:
    def __init__(self, csv_path: str):
        self.locations_df = pd.read_csv(csv_path, encoding='latin1', sep=',')

    def get_departments(self):
        departments = self.locations_df[["Código Departamento", "Nombre Departamento"]].drop_duplicates()
        return [
            {"code": int(row["Código Departamento"]), "description": row["Nombre Departamento"]}
            for _, row in departments.iterrows()
        ]

    def get_municipalities_by_department_code(self, department_code: int):
        filtered = self.locations_df[self.locations_df["Código Departamento"] == department_code]
        return [
            {"code": int(row["Código Municipio"]), "description": row["Nombre Municipio"]}
            for _, row in filtered.iterrows()
        ]

    def get_municipality_by_code(self, municipality_code: int):
        match = self.locations_df[self.locations_df["Código Municipio"] == municipality_code]
        if not match.empty:
            row = match.iloc[0]
            return {"code": int(row["Código Municipio"]), "description": row["Nombre Municipio"]}
        return None

    def get_capital_municipalities(self):
        capitals = self.locations_df[self.locations_df["Código Municipio"] % 100 == 1]
        return [
            {"code": int(row["Código Municipio"]), "description": row["Nombre Municipio"]}
            for _, row in capitals.iterrows()
        ]
