import pandas as pd 
import numpy as np 
import os
import itertools

def dados_teses():
    diretorio = "/media/hdvm02/bd/007/002/007/002"
    teses_anos = sorted(os.listdir(diretorio))
    lista_dfs = []

    for tese_ano in teses_anos:
        csv = os.path.join(diretorio,tese_ano)
        teses = pd.read_csv(csv, sep=";", encoding='latin-1', on_bad_lines='skip', low_memory=False)
        lista_dfs.append(teses)
        print(tese_ano)
        #print(teses.columns.tolist())
        #print(teses.shape)
        print(teses.dtypes)
        #print(teses.tail())
        #print(teses.describe())
        print("########")
        print("########")    
    #dataset_teses = pd.concat(lista_dfs, ignore_index=True)
    #dataset_teses.to_csv(f'{diretorio}/01_dados_1987_2012.csv', index=False)
    #print(dataset_teses)
    #return dataset_teses

def analisa_teses():
    diretorio = "/media/hdvm02/bd/007/002/007/002"
    #df_teses = dados_teses()
    teses = pd.read_csv(f'{diretorio}/01_dados_1987_2012.csv')
    busca = teses[teses["TituloTese"].str.contains("mercosul|mercosur", case=False, na=False)]
    #print(busca)
    agrupar_por_ano = busca["TituloTese"].groupby(busca["AnoBase"])
    busca_por_ano = agrupar_por_ano.count()
    #print(busca_por_ano)
    quant_termos = busca_por_ano.values.tolist()
    anos = busca_por_ano.index.tolist()
    fig_pandas = busca_por_ano.plot(kind="line", x=anos, y=quant_termos)
    print(fig_pandas)

def gera_dataframes():
    diretorio = "/media/hdvm02/bd/007/002/007/002"
    anos = sorted(os.listdir(diretorio))
    anos_1987_2012 = anos[1:27]
    anos_2013_2016 = anos[27:31]
    anos_2017_2021 = anos[31:]
    
    df_1987_2012 = []
    df_2013_2016 = []
    df_2017_2021 = []
    df_geral = []

    for ano_1987, ano_2013, ano_2017 in itertools.zip_longest(anos_1987_2012, anos_2013_2016, anos_2017_2021):
        csv_1987 = os.path.join(diretorio, ano_1987)
        teses = pd.read_csv(csv_1987, sep=";", encoding='latin-1', on_bad_lines='skip', low_memory=False)
        df_1987_2012.append(teses)
        if ano_2013 != None:
            csv_2013 = os.path.join(diretorio, ano_2013)
            teses = pd.read_csv(csv_2013, sep=";", encoding='latin-1', on_bad_lines='skip', low_memory=False)
            df_2013_2016.append(teses)
        if ano_2017 != None:
            csv_2017 = os.path.join(diretorio, ano_2017)
            teses = pd.read_csv(csv_2017, sep=";", encoding='latin-1', on_bad_lines='skip', low_memory=False)
            df_2017_2021.append(teses)
        
    df_1987_2012_final = pd.concat(df_1987_2012, ignore_index=True)
    df_2013_2016_final = pd.concat(df_2013_2016, ignore_index=True)
    df_2017_2021_final = pd.concat(df_2017_2021, ignore_index=True)
    # print(df_1987_2012_final)
    # print(df_2013_2016_final)
    
    df_1987_2012_final.to_csv(f'{diretorio}/01_dados_1987_2012.csv', index=False)
    df_2013_2016_final.to_csv(f'{diretorio}/01_dados_2013_2016.csv', index=False)
    df_2017_2021_final.to_csv(f'{diretorio}/01_dados_2017_2020.csv', index=False)


def main():
    pass
    

if __name__ == '__main__':
    main()