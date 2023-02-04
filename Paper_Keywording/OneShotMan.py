import pandas as pd
import os
from rake_nltk import Rake

def IMSD_2018():
    DF = pd.read_csv("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\IMSD_2018.CSV", encoding='cp949')
    for i in range(DF.shape[0]):
        DF['Title'].iloc[i] = DF['Title'].iloc[i].replace('\n', '')
    ExtractKeywords(DF)
    CategoryCompletion(DF)
    DF = DF.reset_index(drop=True)
    DF.index += 1
    return DF

def ECCOMAS_2019():
    f = open("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ECCOMAS\ECCOMAS_2019.txt", encoding='utf-8')
    lines = f.readlines()
    titles = []
    for num, line in enumerate(lines):
        if line != '\n':
            titles.append(line[:-1])
    f.close()
    DF = pd.DataFrame(titles, columns=['Title'])
    DF['Conference'] = 'ECCOMAS Thematic Conference on Multibody Dynamics'
    DF['Year'] = 2019
    DF['Keywords'] = ''
    DF['Category'] = ''
    DF['Note'] = ''
    DF = DF[['Conference', 'Year', 'Title', 'Keywords', 'Category', 'Note']]
    DF = DF.drop(index=DF.index[-1])
    DF = CategoryCompletion(DF)
    DF = ExtractKeywords(DF)
    DF = DF.reset_index(drop=True)
    DF.index += 1
    return DF

def ECCOMAS_2021():
    f = open("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ECCOMAS\ECCOMAS_2021.txt", encoding='utf-8')
    lines = f.readlines()
    for num, line in enumerate(lines):
        if '. .' in line or line == '\n':
            removal_index = lines.index(line)
            del lines[removal_index]
    for num, line in enumerate(lines):
        lines[num] = lines[num].replace('\n', '')
    DF = pd.DataFrame(lines, columns=['Title'])
    DF['Conference'] = 'ECCOMAS Thematic Conference on Multibody Dynamics'
    DF['Year'] = 2021
    DF['Keywords'] = ''
    DF['Category'] = ''
    DF['Note'] = ''
    DF = DF[['Conference', 'Year', 'Title', 'Keywords', 'Category', 'Note']]
    DF = DF.drop(index=DF.index[-1])
    DF = CategoryCompletion(DF)
    DF = ExtractKeywords(DF)
    DF = DF.reset_index(drop=True)
    DF.index += 1
    return DF

def CategoryCompletion(DF, encoding=None):
    # DF=pd.read_csv(path,encoding=encoding)
    for i in range(DF.shape[0]):
        title = DF.iloc[i, :]['Title'].lower()
        
        AI_keywords = ['deep', 'learn', 'supervis', 'recogn', 'neural', 'network']
        Optimization_keywords = ['optim']
        Control_keywords = ['control']
        Modeling_keywords = ['simulation', 'model', 'contact', 'impact']
        NumericalAnalysis_keywords = ['analysis', 'real time', 'real-time', 'numerical']
        Formulation_keywords = ['formulation', 'constraint', 'reduced order']
        SystemID_keywords = ['identification', 'system identification']
        Robot_keywords = ['robot', 'motion', 'miniature', 'path']
        VehicleDyn_keywords = ['vehicle', 'ship', 'train']
        Algorithm_keywords = ['algorithm']
        Measurement_keywords = ['measur', 'lidar', 'estimation']
        UQ_keywords = ['probabili', 'uncertain', 'probabili']
        Electronics_keywords = ['electr', 'wireless', 'dc', 'impedance','power consum', 'power conver']
        SmartTechnologies_keywords = ['smart', 'wearable', 'digital']
        IOTVRAR_keywords = ['iot', 'internet', 'virtual reality', 'vr', 'augmented reality', 'internet of things']
        
        while 'category' not in locals():
            if 'category' not in locals():
                for keyword in AI_keywords:
                    if keyword in title:
                        category = 'AI'
            if 'category' not in locals():
                for keyword in SmartTechnologies_keywords:
                    if keyword in title:
                        category = 'Smart technologies'
            if 'category' not in locals():
                for keyword in IOTVRAR_keywords:
                    if keyword in title:
                        category = 'IoT & VR/AR'
            
            if 'category' not in locals():
                for keyword in Formulation_keywords:
                    if keyword in title:
                        category = 'Formulation'
            if 'category' not in locals():
                for keyword in SystemID_keywords:
                    if keyword in title:
                        category = 'System identification'
            if 'category' not in locals():
                for keyword in VehicleDyn_keywords:
                    if keyword in title:
                        category = 'Vehicle dynamics'
            if 'category' not in locals():
                for keyword in Robot_keywords:
                    if keyword in title:
                        category = 'Robotics'
            if 'category' not in locals():
                for keyword in Algorithm_keywords:
                    if keyword in title:
                        category = 'Algorithm'
            if 'category' not in locals():
                for keyword in Measurement_keywords:
                    if keyword in title:
                        category = 'Measurements'
            if 'category' not in locals():
                for keyword in UQ_keywords:
                    if keyword in title:
                        category = 'Uncertainty quantification'
            if 'category' not in locals():
                for keyword in Electronics_keywords:
                    if keyword in title:
                        category = 'Electronics'
            
            if 'category' not in locals():
                for keyword in Optimization_keywords:
                    if keyword in title:
                        category = 'Optimization'
            if 'category' not in locals():
                for keyword in Control_keywords:
                    if keyword in title:
                        category = 'Control'
            if 'category' not in locals():
                for keyword in Modeling_keywords:
                    if keyword in title:
                        category = 'Modeling'
            if 'category' not in locals():
                for keyword in NumericalAnalysis_keywords:
                    if keyword in title:
                        category = 'Numerical analysis'
            if 'category' not in locals():
                category = 'Dynamics'
        DF['Category'].iloc[i] = category
        del category
    DF.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)
    return DF

def ExtractKeywords(dataframe):
    NLP = Rake()
    for i in range(len(dataframe)):
        title = f"""{dataframe['Title'].iloc[i]}"""
        NLP.extract_keywords_from_text(title)
        keyword_extracted = NLP.get_ranked_phrases()[0]
        keyword_extracted = keyword_extracted.capitalize()
        dataframe['Keywords'].iloc[i] = keyword_extracted
    return dataframe

def ICRA(path, year, encoding):
    f = open(path, encoding=encoding)
    lines = f.readlines()
    lines.insert(0, '\n')
    edge_indices = []
    for num, line in enumerate(lines):
        if line == '\n':
            edge_indices.append(num)
    contents = []
    for i in range(len(edge_indices)):
        if i != len(edge_indices) - 1:
            content_single = lines[edge_indices[i] + 1:edge_indices[i + 1]]
            title = content_single[0].split('"')[1][:-1]
            contents.append(title)
    f.close()
    DF = pd.DataFrame(contents, columns=['Title'])
    DF['Conference'] = 'IEEE International Conference on Robotics and Automation'
    DF['Year'] = year
    DF['Keywords'] = ''
    DF['Category'] = ''
    DF['Note'] = ''
    DF = DF[['Conference', 'Year', 'Title', 'Keywords', 'Category', 'Note']]
    DF = CategoryCompletion(DF)
    DF = ExtractKeywords(DF)
    DF = DF.reset_index(drop=True)
    DF.index += 1
    return DF

def ICIT(path, year, encoding):
    f = open(path, encoding=encoding)
    lines = f.readlines()
    lines.insert(0, '\n')
    edge_indices = []
    for num, line in enumerate(lines):
        if line == '\n':
            edge_indices.append(num)
    contents = []
    for i in range(len(edge_indices)):
        if i != len(edge_indices) - 1:
            content_single = lines[edge_indices[i] + 1:edge_indices[i + 1]]
            title = content_single[0].split('"')[1][:-1]
            contents.append(title)
    f.close()
    DF = pd.DataFrame(contents, columns=['Title'])
    DF['Conference'] = 'IEEE International Conference on Industrial Technology (ICIT)'
    DF['Year'] = year
    DF['Keywords'] = ''
    DF['Category'] = ''
    DF['Note'] = ''
    DF = DF[['Conference', 'Year', 'Title', 'Keywords', 'Category', 'Note']]
    DF = CategoryCompletion(DF)
    DF = ExtractKeywords(DF)
    DF = DF.reset_index(drop=True)
    DF.index += 1
    return DF

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

ECCOMAS1 = ECCOMAS_2019()
ECCOMAS2 = ECCOMAS_2021()

IMSD1 = IMSD_2018()

ICIT1 = ICIT("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICIT\\2017 IEEE International Conference on Industrial Technology (ICIT).txt", 2017, 'utf-8')
ICIT2 = ICIT("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICIT\\2018 IEEE International Conference on Industrial Technology (ICIT).txt", 2018, 'utf-8')
ICIT3 = ICIT("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICIT\\2019 IEEE International Conference on Industrial Technology (ICIT).txt", 2019, 'utf-8')
ICIT4 = ICIT("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICIT\\2020 IEEE International Conference on Industrial Technology (ICIT).txt", 2020, 'utf-8')
ICIT5 = ICIT("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICIT\\2021 IEEE International Conference on Industrial Technology (ICIT).txt", 2021, 'utf-8')

ICRA1 = ICRA("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICRA\ICRA_2017.txt", 2017, 'utf-8')
ICRA2 = ICRA("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICRA\ICRA_2018.txt", 2018, 'utf-8')
ICRA3 = ICRA("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICRA\ICRA_2019.txt", 2019, 'utf-8')
ICRA4 = ICRA("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICRA\ICRA_2020.txt", 2020, 'utf-8')
ICRA5 = ICRA("C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\종합\ICRA\ICRA_2021.txt", 2021, 'utf-8')

# Save
SavePath = "C:\\Users\LHB-MSLab\Documents\GitHub\FUCKING_PAPER_ORGANIZING\최종본\\"

ECCOMAS1.to_excel(f"{SavePath}ECCOMAS_2019.xlsx", index=True, encoding='utf-8-sig')
ECCOMAS2.to_excel(f"{SavePath}ECCOMAS_2021.xlsx", index=True, encoding='utf-8-sig')

IMSD1.to_excel(f"{SavePath}IMSD_2018.xlsx", index=True, encoding='utf-8-sig')

ICIT1.to_excel(f"{SavePath}ICIT_2017.xlsx", index=True, encoding='utf-8-sig')
ICIT2.to_excel(f"{SavePath}ICIT_2018.xlsx", index=True, encoding='utf-8-sig')
ICIT3.to_excel(f"{SavePath}ICIT_2019.xlsx", index=True, encoding='utf-8-sig')
ICIT4.to_excel(f"{SavePath}ICIT_2020.xlsx", index=True, encoding='utf-8-sig')
ICIT5.to_excel(f"{SavePath}ICIT_2021.xlsx", index=True, encoding='utf-8-sig')

ICRA1.to_excel(f"{SavePath}ICRA_2017.xlsx", index=True, encoding='utf-8-sig')
ICRA2.to_excel(f"{SavePath}ICRA_2018.xlsx", index=True, encoding='utf-8-sig')
ICRA3.to_excel(f"{SavePath}ICRA_2019.xlsx", index=True, encoding='utf-8-sig')
ICRA4.to_excel(f"{SavePath}ICRA_2020.xlsx", index=True, encoding='utf-8-sig')
ICRA5.to_excel(f"{SavePath}ICRA_2021.xlsx", index=True, encoding='utf-8-sig')

Total = pd.concat([ECCOMAS1, ECCOMAS2, ICIT1, ICIT2, ICIT3, ICIT4, ICIT5, ICRA1, ICRA2, ICRA3, ICRA4, ICRA5, IMSD1], axis=0)
Total = Total.reset_index(drop=True)
Total.index += 1
Total.to_excel(f"{SavePath}종합.xlsx", index=True, encoding='utf-8-sig')