
# Dados Abertos CAPES

## Conjuntos de dados: catálogo de teses e dissertações


### Tabelas de atributos disponíveis

|1987-2012|Tipo   |Nome |2013-2016|Tipo   |2017-2020|Tipo   |
|-------- |-------|-----|---------|-------|---------|-------|
|`AnoBase`|`int64`|Ano Base de Coleta dos Dados |`AN_BASE`|`int64`|`AN_BASE`|`int64`|
|`CodigoPrograma`|`object`|Código de Identificação do Programa|`CD_PROGRAMA`|`object`|`CD_PROGRAMA`|`object`|
|`Regiao`|`object`|Nome do Programa|`NM_PROGRAMA`|`object`|`NM_PROGRAMA`|`object`|
|`Uf`|`object`|Sigla da Entidade de Ensino|`SG_ENTIDADE_ENSINO`|`object`|`SG_ENTIDADE_ENSINO`|`object`|
|`SiglaIes`|`object`|Nome da Entidade de Ensino|`NM_ENTIDADE_ENSINO`|`object`|`NM_ENTIDADE_ENSINO`|`object`|
|`NomeIes`|`object`|Identificador do Produto no Ano Base e no Programa na Base de Dados da CAPES |`ID_ADD_PRODUCAO_INTELECTUAL`|`int64`|`ID_ADD_PRODUCAO_INTELECTUAL`|`int64`|
|`NomePrograma`|`object`|Identificador do Produto na Base de Dados da CAPES|`ID_PRODUCAO_INTELECTUAL`|`int64`|`ID_PRODUCAO_INTELECTUAL`|`int64`|
|`GrandeAreaCodigo`|`int64`|Nome da Produção |`NM_PRODUCAO`|`object`|`NM_PRODUCAO`|`object`|
|`GrandeAreaDescricao`|`object`|Identificador do Subtipo da Produção|`ID_SUBTIPO_PRODUCAO`|`int64`|`ID_SUBTIPO_PRODUCAO`|`int64`|
|`AreaConhecimentoCodigo`|`int64`|Nome do Subtipo da Produção |`NM_SUBTIPO_PRODUCAO`|`object`|`NM_SUBTIPO_PRODUCAO`|`object`|
|`AreaConhecimento`|`object`|Identificador da área de concentração |`ID_AREA_CONCENTRACAO`|`float64`|`ID_AREA_CONCENTRACAO`|`float64`|
|`AreaAvaliacao`|`object`|Nome da área de concentração |`NM_AREA_CONCENTRACAO`|`object`|`NM_AREA_CONCENTRACAO`|`object`|
|`DocumentoDiscente`|`object`|Identificador da Linha de Pesquisa|`ID_LINHA_PESQUISA`|`float64`|`ID_LINHA_PESQUISA`|`float64`|
|`Autor`|`object`|Nome da Linha de Pesquisa |`NM_LINHA_PESQUISA`|`object`|`NM_LINHA_PESQUISA`|`object`|
|`TituloTese`|`object`|Identificador do Projeto |`ID_PROJETO`|`float64`|`ID_PROJETO`|`float64`|
|`Nivel`|`object`|Nome do Projeto|`NM_PROJETO`|`object`|`NM_PROJETO`|`object`|
|`DataDefesa`|`object`|Data e Hora do Início da Área de Concentração|`DH_INICIO_AREA_CONC`|`object`|`DH_INICIO_AREA_CONC`|`object`|
|`PalavrasChave`|`object`|Data e Hora do Fim da Área de Concentração |`DH_FIM_AREA_CONC`|`object`|`DH_FIM_AREA_CONC`|`object`|
|`Volume`|`int64`|Data e Hora do Início da Linha de Pesquisa |`DH_INICIO_LINHA`|`object`|`DH_INICIO_LINHA`|`object`|
|`NumeroPaginas`|`int64`|Data e Hora do Fim da Linha de Pesquisa |`DH_FIM_LINHA`|`object`|`DH_FIM_LINHA`|`object`|
|`BibliotecaDepositaria`|`object`|Data da Titulação |`DT_TITULACAO`|`object`|`DT_TITULACAO`|`object`|
|`Idioma`|`object`|Descrição da Palavra Chave |`DS_PALAVRA_CHAVE`|`object`|`DS_PALAVRA_CHAVE`|`object`|
|`ResumoTese`|`object`|Descrição do Abstract|`DS_ABSTRACT`|`object`|`DS_ABSTRACT`|`object`|
|`LinhaPesquisa`|`object`|Descrição do Keyword |`DS_KEYWORD`|`object`|`DS_KEYWORD`|`object`|
|`URLTextoCompleto`|`object`|Indicador de Expectativa de Atuação|`IN_TRABALHO_MESMA_AREA`|`float64`|`IN_TRABALHO_MESMA_AREA`|`int64`|
|`DocumentoOrientador_1`|`object`|Nome do Tipo de vinculo|`NM_TP_VINCULO`|`object`|`NM_TP_VINCULO`|`object`|
|`Orientador_1`|`object`|Indicador se o Orientador Participou da Banca |`IN_ORIENT_PARTICIPOU_BANCA`|`int64`|`IN_ORIENT_PARTICIPOU_BANCA`|`int64`|
|`DocumentoOrientador_2`|`object`|Descrição da Biblioteca Depositária |`DS_BIBLIOTECA_DEPOSITARIA`|`object`|`DS_BIBLIOTECA_DEPOSITARIA`|`object`|
|`Orientador_2`|`object`|Identificador do Tipo de Expectativa da Atuação|`ID_TP_EXPECTATIVA_ATUACAO`|`int64`|`ID_TP_EXPECTATIVA_ATUACAO`|`int64`|
|`DocumentoOrientador_4`|`float64`|Nome da Expectativa da Atuação |`NM_EXPECTATIVA_ATUACAO`|`object`|`NM_EXPECTATIVA_ATUACAO`|`object`|
|`Òrientador_4`|`float64`|Código de identificação da pessoa na base de dados da CAPES |`ID_PESSOA_DISCENTE`|`int64`|`ID_PESSOA_DISCENTE`|`int64`|
|`DocumentoCoOrientador_1`|`object`|Nome do Discente |`NM_DISCENTE`|`object`|`NM_DISCENTE`|`object`|
|`CoOrientador_1`|`object`|Data da Matrícula do Discente |`DT_MATRICULA`|`object`|`DT_MATRICULA`|`object`|
|`DocumentoCoOrientador_2`|`object`|Identificador do Grau Acadêmico ao qual o discente está vinculado|`ID_GRAU_ACADEMICO`|`int64`|`ID_GRAU_ACADEMICO`|`int64`|
|`CoOrientador_2`|`object`|Nome do Grau Acadêmico ao qual o discente está vinculado |`NM_GRAU_ACADEMICO`|`object`|`NM_GRAU_ACADEMICO`|`object`|
|`DocumentoCoOrientador_3`|`object`|Nome do Orientador|`NM_ORIENTADOR`|`object`|`NM_ORIENTADOR`|`object`|
|`CoOrientador_3`|`object`|Descrição da Categoria do Orientador|`DS_CATEGORIA_ORIENTADOR`|`object`|`DS_CATEGORIA_ORIENTADOR`|`object`|
|`DocumentoCoOrientador_4`|`object`|Nome da Categoria do Docente |`NM_CATEGORIA_DOCENTE`|`object`|`NM_CATEGORIA_DOCENTE`|`object`|
|`CoOrientador_4`|`object`|Nome da Região da IES |`NM_REGIAO`|`object`|`NM_REGIAO`|`object`|
|-|-|Sigla da Unidade da Federação da IES |`SG_UF_IES`|`object``SG_UF_IES`|`object`|
|-|-|Nome da Unidade da Federação da IES|`NM_UF_IES`|`object`|`NM_UF_IES`|`object`|
|-|-|Código da Grande Área de Conhecimento a que a Produção está vinculada |`CD_GRANDE_AREA_CONHECIMENTO`|`int64``CD_GRANDE_AREA_CONHECIMENTO`|`int64`|
|-|-|Nome da Grande Área de Conhecimento a que a Produção está vinculada |`NM_GRANDE_AREA_CONHECIMENTO`|`object``NM_GRANDE_AREA_CONHECIMENTO`|`object`|
|-|-|Código da Área de Conhecimento a que o Programa de Pós-Graduação está vinculada|`CD_AREA_CONHECIMENTO`|`float64`|`CD_AREA_CONHECIMENTO`|`float64`|
|-|-|Nome da Área de Conhecimento a que o Programa de Pós-Graduação está vinculada|`NM_AREA_CONHECIMENTO`|`object`|`NM_AREA_CONHECIMENTO`|`object`|
|-|-|Código da Subárea de Conhecimento a que o Programa de Pós-Graduação está vinculada |`CD_SUBAREA_CONHECIMENTO`|`float64`|`CD_SUBAREA_CONHECIMENTO`|`float64`|
|-|-|Nome da Subárea de Conhecimento a que o Programa de Pós-Graduação está vinculada |`NM_SUBAREA_CONHECIMENTO`|`object`|`NM_SUBAREA_CONHECIMENTO`|`object`|
|-|-|Código da Especialidade |`CD_ESPECIALIDADE`|`float64`|`CD_ESPECIALIDADE`|`float64`|
|-|-|Nome da Especialidade|`NM_ESPECIALIDADE`|`object`|`NM_ESPECIALIDADE`|`object`|
|-|-|Nome da Área de Avaliação |`NM_AREA_AVALIACAO`|`object`|`NM_AREA_AVALIACAO`|`object`|
|-|-|Número do Volume da Produção|`NR_VOLUME`|`object`|`NR_VOLUME`|`object`|
|-|-|Número de Páginas da Produção |`NR_PAGINAS`|`float64`|`NR_PAGINAS`|`float64`|
|-|-|Nome do Idioma da Produção |`NM_IDIOMA`|`object`|`NM_IDIOMA`|`object`|
|-|-|Descrição do Resumo|`DS_RESUMO`|`object`|`DS_RESUMO`|`object`|
|-|-|Descrição da URL do Texto Completo|`DS_URL_TEXTO_COMPLETO`|`object`|`DS_URL_TEXTO_COMPLETO`|`object`|
|-|-|Código de identificação da pessoa orientador na base de dados da CAPES |`ID_PESSOA_ORIENTADOR`|`float64`|`ID_PESSOA_ORIENTADOR`|`float64`|
|-|-|Indicada se o TCC tem vínculo com alguma Produção Intelectual |-|-|`IN_TCC_COM_VINCULO_PRODUCAO`|`object`|
|-|-|Representa os 'IDs' das produções intelectuais concatenadas, para caso o usuário deseje saber qual produção intelectual foi vinculada aquele TCC |-|-|`ID_ADD_PRODUCAO_VINCULO_CT`|`object`|


## Habilitar ambiente virtual

```
git pull origin main && conda activate env_capes_teses && conda env update --prune

```