import pandas as pd
from io import StringIO, BytesIO, TextIOWrapper
from zipfile import ZipFile
import urllib.request
import rarfile
from scipy.io.arff import loadarff


def load_abalone():
    abalone = {'name': 'Abalone',
               'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'}
    abalone_uci_url = abalone['uci_url']
    names = ["Sex", "Length", "Diameter", "Height", "Weight.whole", "Weight.shucked",
             "Weight.viscera", "Weight.shell", "Rings"]
    df = pd.read_csv(abalone_uci_url, header=None, names=names)
    return df


def load_arrhythmia():
    arrhythmia = {'name': 'Arrhythmia',
                  'uci_url': 'http://archive.ics.uci.edu/ml//machine-learning-databases/arrhythmia/arrhythmia.data'}
    arrhythmia_uci_url = arrhythmia['uci_url']
    names = ["Age", "Sex", "Height", "Weight", "QRS_Dur", "P-R_Int", "Q-T_Int", "T_Int", "P_Int",
             "QRS", "T", "P", "QRST", "J", "Heart_Rate", "Q_Wave", "R_Wave", "S_Wave", "R'_Wave",
             "S'_Wave", "Int_Def", "Rag_R_Nom", "Diph_R_Nom", "Rag_P_Nom", "Diph_P_Nom", "Rag_T_Nom",
             "Diph_T_Nom", "DII00", "DII01", "DII02", "DII03", "DII04", "DII05", "DII06", "DII07",
             "DII08", "DII09", "DII10", "DII11", "DIII00", "DIII01", "DIII02", "DIII03", "DIII04",
             "DIII05", "DIII06", "DIII07", "DIII08", "DIII09", "DIII10", "DIII11", "AVR00", "AVR01",
             "AVR02", "AVR03", "AVR04", "AVR05", "AVR06", "AVR07", "AVR08", "AVR09", "AVR10", "AVR11",
             "AVL00", "AVL01", "AVL02", "AVL03", "AVL04", "AVL05", "AVL06", "AVL07", "AVL08", "AVL09",
             "AVL10", "AVL11", "AVF00", "AVF01", "AVF02", "AVF03", "AVF04", "AVF05", "AVF06", "AVF07",
             "AVF08", "AVF09", "AVF10", "AVF11", "V100", "V101", "V102", "V103", "V104", "V105",
             "V106", "V107", "V108", "V109", "V110", "V111", "V200", "V201", "V202", "V203", "V204",
             "V205", "V206", "V207", "V208", "V209", "V210", "V211", "V300", "V301", "V302", "V303",
             "V304", "V305", "V306", "V307", "V308", "V309", "V310", "V311", "V400", "V401", "V402",
             "V403", "V404", "V405", "V406", "V407", "V408", "V409", "V410", "V411", "V500", "V501",
             "V502", "V503", "V504", "V505", "V506", "V507", "V508", "V509", "V510", "V511", "V600",
             "V601", "V602", "V603", "V604", "V605", "V606", "V607", "V608", "V609", "V610", "V611",
             "JJ_Wave", "Amp_Q_Wave", "Amp_R_Wave", "Amp_S_Wave", "R_Prime_Wave", "S_Prime_Wave",
             "P_Wave", "T_Wave", "QRSA", "QRSTA", "DII170", "DII171", "DII172", "DII173", "DII174",
             "DII175", "DII176", "DII177", "DII178", "DII179", "DIII180", "DIII181", "DIII182",
             "DIII183", "DIII184", "DIII185", "DIII186", "DIII187", "DIII188", "DIII189", "AVR190",
             "AVR191", "AVR192", "AVR193", "AVR194", "AVR195", "AVR196", "AVR197", "AVR198", "AVR199",
             "AVL200", "AVL201", "AVL202", "AVL203", "AVL204", "AVL205", "AVL206", "AVL207", "AVL208",
             "AVL209", "AVF210", "AVF211", "AVF212", "AVF213", "AVF214", "AVF215", "AVF216", "AVF217",
             "AVF218", "AVF219", "V1220", "V1221", "V1222", "V1223", "V1224", "V1225", "V1226", "V1227",
             "V1228", "V1229", "V2230", "V2231", "V2232", "V2233", "V2234", "V2235", "V2236", "V2237",
             "V2238", "V2239", "V3240", "V3241", "V3242", "V3243", "V3244", "V3245", "V3246", "V3247",
             "V3248", "V3249", "V4250", "V4251", "V4252", "V4253", "V4254", "V4255", "V4256", "V4257",
             "V4258", "V4259", "V5260", "V5261", "V5262", "V5263", "V5264", "V5265", "V5266", "V5267",
             "V5268", "V5269", "V6270", "V6271", "V6272", "V6273", "V6274", "V6275", "V6276", "V6277",
             "V6278", "V6279", "diagnosis"]

    df = pd.read_csv(arrhythmia_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_audiology():
    audiology = {'name': 'Audiology',
                 'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/' +
                            'audiology.standardized.data'}
    audiology_uci_url = audiology['uci_url']
    names = ['age_gt_60', 'air', 'airBoneGap', 'ar_c', 'ar_u', 'bone', 'boneAbnormal', 'bser', 'history_buzzing',
         'history_dizziness', 'history_fluctuating', 'history_fullness', 'history_heredity', 'history_nausea',
         'history_noise', 'history_recruitment', 'history_ringing', 'history_roaring', 'history_vomiting',
         'late_wave_poor', 'm_at_2k', 'm_cond_lt_1k', 'm_gt_1k', 'm_m_gt_2k', 'm_m_sn', 'm_m_sn_gt_1k',
         'm_m_sn_gt_2k', 'm_m_sn_gt_500', 'm_p_sn_gt_2k', 'm_s_gt_500', 'm_s_sn', 'm_s_sn_gt_1k', 'm_s_sn_gt_2k',
         'm_s_sn_gt_3k', 'm_s_sn_gt_4k', 'm_sn_2_3k', 'm_sn_gt_1k', 'm_sn_gt_2k', 'm_sn_gt_3k', 'm_sn_gt_4k',
         'm_sn_gt_500', 'm_sn_gt_6k', 'm_sn_lt_1k', 'm_sn_lt_2k', 'm_sn_lt_3k', 'middle_wave_poor', 'mod_gt_4k',
         'mod_mixed', 'mod_s_mixed', 'mod_s_sn_gt_500', 'mod_sn', 'mod_sn_gt_1k', 'mod_sn_gt_2k', 'mod_sn_gt_3k',
         'mod_sn_gt_4k', 'mod_sn_gt_500', 'notch_4k', 'notch_at_4k', 'o_ar_c', 'o_ar_u', 's_sn_gt_1k', 's_sn_gt_2k',
         's_sn_gt_4k', 'speech', 'static_normal', 'tymp', 'viith_nerve_signs', 'wave_V_delayed',
         'waveform_ItoV_prolonged', 'indentifier', 'Class']
    df = pd.read_csv(audiology_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_autism_screening():
    autism_screening = {'name': 'Autism_Screening',
                        'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00426/' +
                                   'Autism-Adult-Data Plus Description File.zip'}
    autism_screening_uci_url = autism_screening['uci_url']
    resp = urllib.request.urlopen(
        autism_screening_uci_url[:-43] + urllib.request.quote(autism_screening_uci_url[-43:]))
    zipfile = ZipFile(BytesIO(resp.read()))
    in_mem_fo = TextIOWrapper(zipfile.open('Autism-Adult-Data.arff'), encoding='utf-8')
    data = loadarff(in_mem_fo)
    df = pd.DataFrame(data[0])
    for c in df.columns:
        if df[c].dtype == 'object':
            df[c] = df[c].str.decode('UTF-8')
    df = df.replace({'?': None})
    return df


def load_blood_transfusion():
    blood_transfusion = {'name': 'Blood Transfusion Service',
                         'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/' +
                                    'transfusion.data'}
    blood_transfusion_uci_url = blood_transfusion['uci_url']
    df = pd.read_csv(blood_transfusion_uci_url)
    return df


def load_breast_cancer():
    breast_cancer = {'name': 'Breast Cancer ',
                     'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data'}
    breast_cancer_uci_url = breast_cancer['uci_url']
    names = ["Class", "age", "menopause", "tumor-size", "inv-nodes", "node-caps",
             "deg-malig", "breast", "breast-quad", "irradiat"]
    df = pd.read_csv(breast_cancer_uci_url, names=names, na_values=["?"])
    return df


def load_breast_cancer_wis_diag():
    breast_cancer_wis_diag = {'name': 'Breast Cancer Wisconsin (Diagnostic) ',
                              'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/' +
                                         'wdbc.data'}
    breast_cancer_wis_diag_uci_url = breast_cancer_wis_diag['uci_url']
    names = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
             'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
             'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
             'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
             'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
             'fractal_dimension_se', 'radius_worst', 'texture_worst',
             'perimeter_worst', 'area_worst', 'smoothness_worst',
             'compactness_worst', 'concavity_worst', 'concave points_worst',
             'symmetry_worst', 'fractal_dimension_worst']
    df = pd.read_csv(breast_cancer_wis_diag_uci_url, header=None, names=names)
    return df


def load_cardiotocography():
    cardiotocography = {'name': 'Cardiotocography',
                        'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00193/CTG.xls'}
    cardiotocography_uci_url = cardiotocography['uci_url']
    df = pd.read_excel(cardiotocography_uci_url, sheet_name=1, skiprows=1)
    # keep the columns which are in Attribute Information in uci link
    # plus, skiping rows that are not in the data
    df = df.loc[:2125, list(df.columns[10:31]) + ['CLASS', 'NSP']]
    # Normal=1; Suspect=2; Pathologic=3
    df['NSP'] = df['NSP'].replace({1: 'Normal', 2: 'Suspect', 3: 'Pathologic'})
    df = df.rename(columns={'AC.1': 'AC', 'FM.1': 'FM', 'UC.1': 'UC',
                            'DL.1': 'DL', 'DS.1': 'DS', 'DP.1': 'DP'})
    return df


def load_cervical_cancer():
    cervical_cancer = {'name': 'Cervical_cancer',
                       'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00383/' +
                                  'risk_factors_cervical_cancer.csv'}
    cervical_cancer_uci_url = cervical_cancer['uci_url']
    df = pd.read_csv(cervical_cancer_uci_url, na_values=['?'])
    return df


def load_chess():
    chess = {'name': 'Chess (King-Rook vs. King-Pawn)',
             'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/chess/king-rook-vs-king-pawn/kr-vs-kp.data'}
    chess_uci_url = chess['uci_url']
    names = ['bkblk','bknwy','bkon8','bkona','bkspr','bkxbq','bkxcr','bkxwp','blxwp',
             'bxqsq','cntxt','dsopp','dwipd', 'hdchk','katri','mulch','qxmsq','r2ar8',
             'reskd','reskr','rimmx','rkxwp','rxmsq','simpl','skach','skewr', 'skrxp',
             'spcop','stlmt','thrsk','wkcti','wkna8','wknck','wkovl','wkpos','wtoeg',
             'class']
    df = pd.read_csv(chess_uci_url, header=None, names=names)
    return df


def load_chronic_kidney_disease():
    chronic_kidney_disease = {'name': 'Chronic_Kidney_Disease',
                              'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00336/' +
                                         'Chronic_Kidney_Disease.rar'}
    chronic_kidney_disease_uci_url = chronic_kidney_disease['uci_url']
    resp = urllib.request.urlopen(chronic_kidney_disease_uci_url)
    r = rarfile.RarFile(BytesIO(resp.read()))
    in_mem_fo = TextIOWrapper(r.open('Chronic_Kidney_Disease/chronic_kidney_disease_full.arff'), encoding='utf_8')
    data = []
    for line in in_mem_fo:
        line = line.replace('\n', '')
        data.append(line.split(','))

    names = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba',
             'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc',
             'rbcc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane',
             'class', 'no_name']

    df = pd.DataFrame(data[145:], columns=names)
    df = df.replace({'?': None})
    df = df.drop(['no_name'], axis=1)
    return df


def load_climate_crashes():
    climate_crashes = {'name': 'Climate Model Simulation Crashes',
                       'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00252/pop_failures.dat'}
    climate_crashes_uci_url = climate_crashes['uci_url']
    df = pd.read_csv(climate_crashes_uci_url, sep='\s+', na_values=['?'])
    return df


def load_credit_approval():
    credit_approval = {'name': 'Credit Approval',
                       'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data'}
    credit_approval_uci_url = credit_approval['uci_url']
    names = ['A'+str(i) for i in range(1, 17)]
    df = pd.read_csv(credit_approval_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_cylinder_bands():
    cylinder_bands = {'name': 'Cylinder Bands',
                      'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/cylinder-bands/bands.data'}
    cylinder_bands_uci_url = cylinder_bands['uci_url']
    names = ['timestamp', 'cylinder number', 'customer', 'job number', 'grain screened',
             'ink color', 'proof on ctd ink', 'blade mfg', 'cylinder division', 'paper',
             'ink', 'direct steam', 'solvent type', 'type on cylinder', 'press type',
             'press', 'unit number', 'cylinder size', 'paper mill location', 'plating tank',
             'proof cut', 'viscosity', 'caliper', 'ink temperature', 'humifity', 'roughness',
             'blade pressure', 'varnish pct', 'press speed', 'ink pct', 'solvent pct',
             'ESA Voltage', 'ESA Amperage', 'wax', 'hardener', 'roller durometer',
             'current density', 'anode space ratio', 'chrome content', 'band type']
    df = pd.read_csv(cylinder_bands_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_dermatology():
    dermatology = {'name': 'Dermatology',
                   'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/dermatology/dermatology.data'}
    dermatology_uci_url = dermatology['uci_url']
    names = ['erythema', 'scaling', 'definite_borders', 'itching', 'koebner_phenomenon', 'polygonal_papules',
             'follicular_papules', 'oral_mucosal_involvement', 'knee_and_elbow_involvement', 'scalp_involvement',
             'family_history', 'melanin_incontinence', 'eosinophils_in_the_infiltrate', 'pnl_infiltrate',
             'fibrosis_of_the_papillary_dermis', 'exocytosis', 'acanthosis', 'hyperkeratosis', 'parakeratosis',
             'clubbing_of_the_rete_ridges', 'elongation_of_the_rete_ridges', 'thinning_of_the_suprapapillary_epidermis',
             'spongiform_pustule', 'munro_microabcess', 'focal_hypergranulosis', 'disappearance_of_the_granular_layer',
             'vacuolisation_and_damage_of_basal_layer', 'spongiosis', 'saw-tooth_appearance_of_retes',
             'follicular_horn_plug', 'perifollicular_parakeratosis', 'inflammatory_monoluclear_inflitrate',
             'band-like_infiltrate', 'age', 'class']
    df = pd.read_csv(dermatology_uci_url, header=None, names=names, na_values=['?'])
    df['class'] = df['class'].replace({1: 'psoriasis', 2: 'seboreic dermatitis',
                                       3: 'lichen planus', 4: 'pityriasis rosea',
                                       5: 'cronic dermatitis', 6: 'pityriasis rubra pilaris'})
    return df


def load_diabetic():
    diabetic = {'name': 'Diabetic Retinopathy Debrecen',
                'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00329/messidor_features.arff'}
    diabetic_uci_url = diabetic['uci_url']
    resp = urllib.request.urlopen(diabetic_uci_url)
    data, meta = loadarff(StringIO(resp.read().decode('utf-8')))
    names = ["quality", "pre_screening", "MA_2", "MA_3", "MA_4", "MA_5", "MA_6", "MA_7",
             "exudates_8", "exudates_9", "exudates_10", "exudates_11", "exudates_12",
             "exudates_13", "exudates_14", "exudates_15", "distance", "diameter",
             "AM_FM", "Class"]
    df = pd.DataFrame(data)
    df.columns = names
    for c in df.columns:
        if df[c].dtype == 'object':
            df[c] = df[c].str.decode('UTF-8')
    return df


def load_dishonest_users():
    dishonest_users = {'name': 'Dishonest Internet users',
                       'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00453/DataSet.zip'}
    dishonest_users_uci_url = dishonest_users['uci_url']
    resp = urllib.request.urlopen(dishonest_users_uci_url)
    zipfile = ZipFile(BytesIO(resp.read()))
    df = pd.read_csv(zipfile.open('Dishonest Internet users dataset.txt'),
                     sep='\s+', na_values=['?'])
    return df


def load_early_stage_diabetes_risk():
    early_stage_diabetes_risk = {'name': 'Early_stage_diabetes_risk',
                                 'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00529/' +
                                            'diabetes_data_upload.csv'}
    early_stage_diabetes_risk_uci_url = early_stage_diabetes_risk['uci_url']
    df = pd.read_csv(early_stage_diabetes_risk_uci_url, na_values=['?'])
    return df


def load_echocardiogram():
    echocardiogram = {'name': 'Echocardiogram',
                      'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/echocardiogram/' +
                                 'echocardiogram.data'}
    echocardiogram_uci_url = echocardiogram['uci_url']
    names = ['survival', 'still-alive', 'age-at-heart-attack', 'pericardial-effusion', 'fractional-shortening',
             'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'mult', 'name', 'group', 'alive-at-1']
    df = pd.read_csv(echocardiogram_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_exasens():
    exasens = {'name': 'Exasens',
               'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00523/Exasens.csv'}
    exasens_uci_url = exasens['uci_url']
    df = pd.read_csv(exasens_uci_url, na_values=['?'])
    return df


def load_fertility():
    fertility = {'name': 'Fertility',
                 'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00244/fertility_Diagnosis.txt'}
    fertility_uci_url = fertility['uci_url']
    names = ['Season', 'Age', 'Childish diseases', 'Accident or serious trauma', 'Surgical intervention',
             'High fevers', 'alcohol', 'Smoking', 'sitting', 'Diagnosis']
    df = pd.read_csv(fertility_uci_url, header=None, names=names)
    return df


def load_haberman():
    haberman = {'name': "Haberman's Survival",
                'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/haberman/haberman.data'}
    haberman_uci_url = haberman['uci_url']
    names = ['age', 'operation_year', 'positive nodes', 'survival']
    df = pd.read_csv(haberman_uci_url, header=None, names=names)
    return df


def load_hayes_roth():
    hayes_roth = {'name': 'Hayes-Roth',
                  'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data'}
    hayes_roth_uci_url = hayes_roth['uci_url']
    names = ['name', 'hobby', 'age', 'educational level',
             'marital status', 'class']
    df = pd.read_csv(hayes_roth_uci_url, names=names, na_values=['?'])
    return df


def load_hcc_survival():
    hcc_survival = {'name': 'Hepatocellular Carcinoma',
                    'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00423/hcc-survival.zip'}
    hcc_survival_uci_url = hcc_survival['uci_url']
    names = ['Gender', 'Symptoms', 'Alcohol', 'Hepatitis B Surface Antigen', 'Hepatitis B e Antigen',
             'Hepatitis B Core Antibody', 'Hepatitis C Virus Antibody', 'Cirrhosis', 'Endemic Countries',
             'Smoking', 'Diabetes', 'Obesity', 'Hemochromatosis', 'Arterial Hypertension',
             'Chronic Renal Insufficiency', 'Human Immunodeficiency Virus', 'Nonalcoholic Steatohepatitis',
             'Esophageal Varices', 'Splenomegaly', 'Portal Hypertension', 'Portal Vein Thrombosis',
             'Liver Metastasis', 'Radiological Hallmark', 'Age at diagnosis', 'Grams of Alcohol per day',
             'Packs of cigarets per year', 'Performance Status', 'Encefalopathy degree', 'Ascites degree',
             'International Normalised Ratio', 'Alpha-Fetoprotein (ng/mL)', 'Haemoglobin (g/dL)',
             'Mean Corpuscular Volume (fl)', 'Leukocytes(G/L)', 'Platelets (G/L)', 'Albumin (mg/dL)',
             'Total Bilirubin(mg/dL)', 'Alanine transaminase (U/L)', 'Aspartate transaminase (U/L)',
             'Gamma glutamyl transferase (U/L)', 'Alkaline phosphatase (U/L)', 'Total Proteins (g/dL)',
             'Creatinine (mg/dL)', 'Number of Nodules', 'Major dimension of nodule (cm)', 'Direct Bilirubin (mg/dL)',
             'Iron (mcg/dL)', 'Oxygen Saturation (%)', 'Ferritin (ng/mL)', 'Class']
    resp = urllib.request.urlopen(
            hcc_survival_uci_url[:-16] + urllib.request.quote(hcc_survival_uci_url[-16:]))
    zipfile = ZipFile(BytesIO(resp.read()))
    data = TextIOWrapper(zipfile.open('hcc-survival/hcc-data.txt'), encoding='utf-8')
    df = pd.read_csv(data, header=None, names=names, na_values=['?'])
    return df


def load_hcv():
    hcv = {'name': 'HCV',
           'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00571/hcvdat0.csv'}
    hcv_uci_url = hcv['uci_url']
    df = pd.read_csv(hcv_uci_url, na_values=['?'])
    return df


def load_heart_disease():
    heart_disease = {'name': 'Heart Disease',
                     'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/' +
                     'processed.cleveland.data'}
    heart_disease_uci_url = heart_disease['uci_url']
    names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
             'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    df = pd.read_csv(heart_disease_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_hepatitis():
    hepatitis = {'name': 'Hepatitis',
                 'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/hepatitis/hepatitis.data'}
    hepatitis_uci_url = hepatitis['uci_url']
    names = ['Class', 'AGE', 'SEX', 'STEROID', 'ANTIVIRALS', 'FATIGUE', 'MALAISE',
             'ANOREXIA', 'LIVER BIG', 'LIVER FIRM', 'SPLEEN PALPABLE', 'SPIDERS',
             'ASCITES', 'VARICES', 'BILIRUBIN', 'ALK PHOSPHATE', 'SGOT', 'ALBUMIN',
             'PROTIME', 'HISTOLOGY']
    df = pd.read_csv(hepatitis_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_indian_liver():
    indian_Liver = {'name': 'Indian_Liver',
                    'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00225/' +
                               'Indian Liver Patient Dataset (ILPD).csv'}
    indian_liver_uci_url = indian_Liver['uci_url']
    resp = urllib.request.urlopen(
                indian_liver_uci_url[:-39] + urllib.request.quote(indian_liver_uci_url[-39:]))
    names = ['Age', 'Gender', 'TB', 'DB', 'Alkphos', 'Sgpt', 'Sgot',
             'TP', 'ALB', 'A/G', 'Selector']
    df = pd.read_csv(resp, header=None, names=names)
    return df


def load_liver_disorders():
    liver_disorders = {'name': 'Liver Disorders',
                       'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/bupa.data'}
    liver_disorders_uci_url = liver_disorders['uci_url']
    names = ['mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt',
             'drinks', 'selector']
    df = pd.read_csv(liver_disorders_uci_url, names=names, na_values=['?'])
    return df


def load_lymphography():
    lymphography = {'name': 'Lymphography',
                    'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/lymphography/lymphography.data'}
    lymphography_uci_url = lymphography['uci_url']
    names =['class', 'lymphatics', 'block of affere', 'bl. of lymph. c', 'bl. of lymph. s', 'by pass',
            'extravasates', 'regeneration', 'early uptake', 'lym.nodes dimin', 'lym.nodes enlar',
            'changes in lym', 'defect in node', 'changes in node', 'changes in stru', 'special forms',
            'dislocation', 'exclusion', 'no. of nodes']
    df = pd.read_csv(lymphography_uci_url, header=None, names=names)
    return df


def load_obesity_levels():
    obesity_levels = {'name': 'Estimation of obesity levels based on eating habits and physical condition',
                      'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00544/' +
                                 'ObesityDataSet_raw_and_data_sinthetic (2).zip'}
    obesity_levels_uci_url = obesity_levels['uci_url']
    resp = urllib.request.urlopen(
        obesity_levels_uci_url[:-45] + urllib.request.quote(obesity_levels_uci_url[-45:]))
    zipfile = ZipFile(BytesIO(resp.read()))
    data = TextIOWrapper(zipfile.open('ObesityDataSet_raw_and_data_sinthetic.csv'), encoding='utf-8')
    df = pd.read_csv(data)
    return df


def load_parkinson():
    parkinson = {'name': 'Parkinsons',
                 'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.data'}
    parkinson_uci_url = parkinson['uci_url']
    df = pd.read_csv(parkinson_uci_url)
    return df


def load_primary_tumor():
    primary_tumor = {'name': 'Primary Tumor',
                     'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/'+
                     'primary-tumor/primary-tumor.data'}
    primary_tumor_uci_url = primary_tumor['uci_url']
    names = ['class', 'age', 'sex', 'histologic-type', 'degree-of-diffe', 'bone',
             'bone-marrow', 'lung', 'pleura', 'peritoneum', 'liver', 'brain', 'skin',
             'neck', 'supraclavicular', 'axillar', 'mediastinum', 'abdominal']
    df = pd.read_csv(primary_tumor_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_qsar_bioconcentration():
    qsar_bioconcentration = {'name': 'QSAR Bioconcentration classes',
                             'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00510/' +
                             'Grisoni_et_al_2016_EnvInt88.csv'}
    qsar_bioconcentration_uci_url = qsar_bioconcentration['uci_url']
    df = pd.read_csv(qsar_bioconcentration_uci_url, na_values=['?'])
    return df


def load_thoracic_surgery():
    thoracic_surgery = {'name': 'Thoracic_Surgery',
                        'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00277/ThoraricSurgery.arff'}
    thoracic_surgery_uci_url = thoracic_surgery['uci_url']
    resp = urllib.request.urlopen(thoracic_surgery_uci_url)
    data, meta = loadarff(StringIO(resp.read().decode('utf-8')))
    df = pd.DataFrame(data)
    for c in df.columns:
        if df[c].dtype == 'object':
            df[c] = df[c].str.decode('UTF-8')
    return df


def load_thyroid_disease():
    thyroid_disease = {'name': 'Thyroid Disease',
                       'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/sick-euthyroid.data'}
    thyroid_disease_uci_url = thyroid_disease['uci_url']
    names = ['sick-euthyroid', 'age', 'sex', 'on_thyroxine', 'query_on_thyroxine',
             'on_antithyroid_medication', 'thyroid_surgery', 'query_hypothyroid',
             'query_hyperthyroid', 'pregnant', 'sick', 'tumor', 'lithium', 'goitre',
             'TSH_measured', 'TSH', 'T3_measured', 'T3', 'TT4_measured',
             'TT4', 'T4U_measured', 'T4U',  'FTI_measured', 'FTI',
             'TBG_measured', 'TBG']
    df = pd.read_csv(thyroid_disease_uci_url, header=None, names=names, na_values=['?'])
    return df


def load_wilt():
    wilt = {'name': 'Wilt',
            'uci_url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00285/wilt.zip'}
    wilt_uci_url = wilt['uci_url']
    resp = urllib.request.urlopen(wilt_uci_url)
    zipfile = ZipFile(BytesIO(resp.read()))
    train = pd.read_csv(zipfile.open('training.csv'), na_values=['?'])
    test = pd.read_csv(zipfile.open('testing.csv'), na_values=['?'])
    df = pd.concat([train, test])
    return df
