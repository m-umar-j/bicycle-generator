import pandas as pd
import itertools
import json

def generate_bicycles(file_path):
    excel_data = pd.ExcelFile(file_path)
    id_sheet = pd.read_excel(excel_data, sheet_name="ID")
    id_designators = id_sheet.columns.tolist()
    id_values = [id_sheet[designator].dropna().astype(str).tolist() for designator in id_designators]
    all_ids = list(itertools.product(*id_values))

    general_sheet = pd.read_excel(excel_data, sheet_name="GENERAL", header=None)
    general_fields = dict(zip(general_sheet.iloc[0], general_sheet.iloc[1]))

    specific_sheets = {}
    for sheet_name in excel_data.sheet_names:
        if sheet_name not in ["ID", "GENERAL"]:
            specific_sheet = pd.read_excel(excel_data, sheet_name=sheet_name)
            designator_name = specific_sheet.columns[0]
            specific_sheets[designator_name] = specific_sheet.set_index(designator_name).to_dict(orient="index")
    
    
    bicycles = []
    for id_combination in all_ids:
        bicycle_id = "".join(id_combination)
        bicycle_data = {"ID": bicycle_id}
        bicycle_data.update(general_fields)
        
        for designator, value in zip(id_designators, id_combination):
            if value in specific_sheets.get(designator, {}):
                bicycle_data.update(specific_sheets[designator][value])
        
        bicycles.append(bicycle_data)
    return json.dumps(bicycles, indent=4)


file_path = "Bicycle.xlsx" 
output_json = generate_bicycles(file_path)

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output_json, f, ensure_ascii=False, indent=4)