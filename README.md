
# Dados Abertos CAPES. 

## Conjuntos de dados: catálogo de teses e dissertações


### Tabelas de atributos disponíveis

1987-2012|Tipo|2013-2016|Tipo|2017-2020|Tipo|
|--------|----|---------|----|---------|----|
|`AnoBase`|`int64`|`AN_BASE`|`int64`|`AN_BASE`|`int64`|
|`CodigoPrograma`|`object`|`CD_PROGRAMA`|`object`|`CD_PROGRAMA`|`object`|
|`Regiao`|`object`|`NM_PROGRAMA`|`object`|`NM_PROGRAMA`|`object`|
|`Uf`|`object`|`SG_ENTIDADE_ENSINO`|`object`|`SG_ENTIDADE_ENSINO`|`object`|
|`SiglaIes`|`object`|`NM_ENTIDADE_ENSINO`|`object`|`NM_ENTIDADE_ENSINO`|`object`|
|`NomeIes`|`object`|`ID_ADD_PRODUCAO_INTELECTUAL`|`int64`|`ID_ADD_PRODUCAO_INTELECTUAL`|`int64`|
|`NomePrograma`|`object`|`ID_PRODUCAO_INTELECTUAL`|`int64`|`ID_PRODUCAO_INTELECTUAL`|`int64`|
|`GrandeAreaCodigo`|`int64`|`NM_PRODUCAO`|`object`|`NM_PRODUCAO`|`object`|
|`GrandeAreaDescricao`|`object`|`ID_SUBTIPO_PRODUCAO`|`int64`|`ID_SUBTIPO_PRODUCAO`|`int64`|
|`AreaConhecimentoCodigo`|`int64`|`NM_SUBTIPO_PRODUCAO`|`object`|`NM_SUBTIPO_PRODUCAO`|`object`|
|`AreaConhecimento`|`object`|`ID_AREA_CONCENTRACAO`|`float64`|`ID_AREA_CONCENTRACAO`|`float64`|
|`AreaAvaliacao`|`object`|`NM_AREA_CONCENTRACAO`|`object`|`NM_AREA_CONCENTRACAO`|`object`|
|`DocumentoDiscente`|`object`|`ID_LINHA_PESQUISA`|`float64`|`ID_LINHA_PESQUISA`|`float64`|
|`Autor`|`object`|`NM_LINHA_PESQUISA`|`object`|`NM_LINHA_PESQUISA`|`object`|
|`TituloTese`|`object`|`ID_PROJETO`|`float64`|`ID_PROJETO`|`float64`|
|`Nivel`|`object`|`NM_PROJETO`|`object`|`NM_PROJETO`|`object`|
|`DataDefesa`|`object`|`DH_INICIO_AREA_CONC`|`object`|`DH_INICIO_AREA_CONC`|`object`|
|`PalavrasChave`|`object`|`DH_FIM_AREA_CONC`|`object`|`DH_FIM_AREA_CONC`|`object`|
|`Volume`|`int64`|`DH_INICIO_LINHA`|`object`|`DH_INICIO_LINHA`|`object`|
|`NumeroPaginas`|`int64`|`DH_FIM_LINHA`|`object`|`DH_FIM_LINHA`|`object`|
|`BibliotecaDepositaria`|`object`|`DT_TITULACAO`|`object`|`DT_TITULACAO`|`object`|
|`Idioma`|`object`|`DS_PALAVRA_CHAVE`|`object`|`DS_PALAVRA_CHAVE`|`object`|
|`ResumoTese`|`object`|`DS_ABSTRACT`|`object`|`DS_ABSTRACT`|`object`|
|`LinhaPesquisa`|`object`|`DS_KEYWORD`|`object`|`DS_KEYWORD`|`object`|
|`URLTextoCompleto`|`object`|`IN_TRABALHO_MESMA_AREA`|`float64`|`IN_TRABALHO_MESMA_AREA`|`int64`|
|`DocumentoOrientador_1`|`object`|`NM_TP_VINCULO`|`object`|`NM_TP_VINCULO`|`object`|
|`Orientador_1`|`object`|`IN_ORIENT_PARTICIPOU_BANCA`|`int64`|`IN_ORIENT_PARTICIPOU_BANCA`|`int64`|
|`DocumentoOrientador_2`|`object`|`DS_BIBLIOTECA_DEPOSITARIA`|`object`|`DS_BIBLIOTECA_DEPOSITARIA`|`object`|
|`Orientador_2`|`object`|`ID_TP_EXPECTATIVA_ATUACAO`|`int64`|`ID_TP_EXPECTATIVA_ATUACAO`|`int64`|
|`DocumentoOrientador_4`|`float64`|`NM_EXPECTATIVA_ATUACAO`|`object`|`NM_EXPECTATIVA_ATUACAO`|`object`|
|`Òrientador_4`|`float64`|`ID_PESSOA_DISCENTE`|`int64`|`ID_PESSOA_DISCENTE`|`int64`|
|`DocumentoCoOrientador_1`|`object`|`NM_DISCENTE`|`object`|`NM_DISCENTE`|`object`|
|`CoOrientador_1`|`object`|`DT_MATRICULA`|`object`|`DT_MATRICULA`|`object`|
|`DocumentoCoOrientador_2`|`object`|`ID_GRAU_ACADEMICO`|`int64`|`ID_GRAU_ACADEMICO`|`int64`|
|`CoOrientador_2`|`object`|`NM_GRAU_ACADEMICO`|`object`|`NM_GRAU_ACADEMICO`|`object`|
|`DocumentoCoOrientador_3`|`object`|`NM_ORIENTADOR`|`object`|`NM_ORIENTADOR`|`object`|
|`CoOrientador_3`|`object`|`DS_CATEGORIA_ORIENTADOR`|`object`|`DS_CATEGORIA_ORIENTADOR`|`object`|
|`DocumentoCoOrientador_4`|`object`|`NM_CATEGORIA_DOCENTE`|`object`|`NM_CATEGORIA_DOCENTE`|`object`|
|`CoOrientador_4`|`object`|`NM_REGIAO`|`object`|`NM_REGIAO`|`object`|
|-|-|`SG_UF_IES`|`object`|`SG_UF_IES`|`object`|
|-|-|`NM_UF_IES`|`object`|`NM_UF_IES`|`object`|
|-|-|`CD_GRANDE_AREA_CONHECIMENTO`|`int64`|`CD_GRANDE_AREA_CONHECIMENTO`|`int64`|
|-|-|`NM_GRANDE_AREA_CONHECIMENTO`|`object`|`NM_GRANDE_AREA_CONHECIMENTO`|`object`|
|-|-|`CD_AREA_CONHECIMENTO`|`float64`|`CD_AREA_CONHECIMENTO`|`float64`|
|-|-|`NM_AREA_CONHECIMENTO`|`object`|`NM_AREA_CONHECIMENTO`|`object`|
|-|-|`CD_SUBAREA_CONHECIMENTO`|`float64`|`CD_SUBAREA_CONHECIMENTO`|`float64`|
|-|-|`NM_SUBAREA_CONHECIMENTO`|`object`|`NM_SUBAREA_CONHECIMENTO`|`object`|
|-|-|`CD_ESPECIALIDADE`|`float64`|`CD_ESPECIALIDADE`|`float64`|
|-|-|`NM_ESPECIALIDADE`|`object`|`NM_ESPECIALIDADE`|`object`|
|-|-|`NM_AREA_AVALIACAO`|`object`|`NM_AREA_AVALIACAO`|`object`|
|-|-|`NR_VOLUME`|`object`|`NR_VOLUME`|`object`|
|-|-|`NR_PAGINAS`|`float64`|`NR_PAGINAS`|`float64`|
|-|-|`NM_IDIOMA`|`object`|`NM_IDIOMA`|`object`|
|-|-|`DS_RESUMO`|`object`|`DS_RESUMO`|`object`|
|-|-|`DS_URL_TEXTO_COMPLETO`|`object`|`DS_URL_TEXTO_COMPLETO`|`object`|
|-|-|`ID_PESSOA_ORIENTADOR`|`float64`|`ID_PESSOA_ORIENTADOR`|`float64`|
|-|-|-|-|`IN_TCC_COM_VINCULO_PRODUCAO`|`object`|
|-|-|-|-|`ID_ADD_PRODUCAO_VINCULO_CT`|`object`|


## Habilitar ambiente virtual

```
git pull origin main && conda activate env_capes && conda env update --prune

```