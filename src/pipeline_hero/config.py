from dataclasses import dataclass


@dataclass
class Config:
    input_path: str = "D:/DATA_EHRSHOT/EHRSHOT_ASSETS/EHRSHOT_ASSETS/data/ehrshot.csv"
    concept_dict: str = "D:/DATA_EHRSHOT/EHRSHOT_ASSETS/EHRSHOT_ASSETS/data_metadata/concept.csv"
    data_by_patient: str = "D:/DATA_EHRSHOT/extracted_data/data_by_patient.parquet"

class Vocabs:
    static_race:dict = ['Race/5',
                        'Race/3',
                        'Race/4',
                        'Race/1',
                        'Race/2',
                        ]
    static_gender:dict = ['Gender/M',
                        'Gender/F',
                        ]
    static_ethnicity:dict =   ['Ethnicity/Hispanic',
                                'Ethnicity/Not Hispanic'
                                ]
    birth_date = "SNOMED/3950001"
    
    prefix_codes = static_ethnicity + static_race + static_gender + [birth_date]

class Columns:
    columns_traj = ["patient_id", "code", "day_gap_bd", "visit_id", "start"]
    columns_static = ["birth_date", "race", "ethnicity", "gender"]

class Tokenizer_vocabs:
    data_vocab = "D:/DATA_EHRSHOT/extracted_data/data_vocab.parquet"