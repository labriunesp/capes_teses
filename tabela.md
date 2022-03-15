|Status|Nome|2013-2020|Tipo   |1987-2012|Tipo    |
|------|-------- |-------|-----|---------|-------|
|ok|Ano Base de Coleta dos Dados |`AN_BASE`|`int64`|`AnoBase`|`int64`|
|ok|Código de Identificação do Programa|`CD_PROGRAMA`|`object`|`CodigoPrograma`|`object`|
|ok|Nome da Produção |`NM_PRODUCAO`|`object`|`TituloTese`|`object`|
|ok|Nome da Região da IES |`NM_REGIAO`|`object`|`Regiao`|`object`|
|confirmar|Sigla da Entidade de Ensino|`SG_ENTIDADE_ENSINO`|`object`|`SiglaIes`|`object`|
||Nome do Programa|`NM_PROGRAMA`|`object`|-|-|
||-|-|-|`Uf`|`object`|
||Nome da Entidade de Ensino|`NM_ENTIDADE_ENSINO`|`object`|-|-|
||Identificador do Produto no Ano Base e no Programa na Base de Dados da CAPES |`ID_ADD_PRODUCAO_INTELECTUAL`|`int64`|-|-|
||-|-|-|`NomeIes`|`object`|
||Identificador do Produto na Base de Dados da CAPES|`ID_PRODUCAO_INTELECTUAL`|`int64`|`ID_PRODUCAO_INTELECTUAL`|`int64`|-|-|
||-|-|-|`NomePrograma`|`object`|
||-|-|-|`GrandeAreaCodigo`|`int64`|
||Identificador do Subtipo da Produção|`ID_SUBTIPO_PRODUCAO`|`int64`|-|-|
||-|-|-|`GrandeAreaDescricao`|`object`|
||Nome do Subtipo da Produção |`NM_SUBTIPO_PRODUCAO`|`object`|-|-|
||-|-|-|`AreaConhecimentoCodigo`|`int64`|
||Identificador da área de concentração |`ID_AREA_CONCENTRACAO`|`float64`|-|-|
||-|-|-|`AreaConhecimento`|`object`|
||Nome da área de concentração |`NM_AREA_CONCENTRACAO`|`object`|-|-|
||-|-|-|`AreaAvaliacao`|`object`|
||Identificador da Linha de Pesquisa|`ID_LINHA_PESQUISA`|`float64`|-|-|
||-|-|-|`DocumentoDiscente`|`object`|
||Nome da Linha de Pesquisa |`NM_LINHA_PESQUISA`|`object`|
||-|-|-|`Autor`|`object`|
||Identificador do Projeto |`ID_PROJETO`|`float64`|-|-|
||Nome do Projeto|`NM_PROJETO`|`object`|-|-|
||-|-|-|`Nivel`|`object`|
||Data e Hora do Início da Área de Concentração|`DH_INICIO_AREA_CONC`|`object`|-|-|
||-|-|-|`DataDefesa`|`object`|
||Data e Hora do Fim da Área de Concentração |`DH_FIM_AREA_CONC`|`object`|-|-|
||-|-|-|`PalavrasChave`|`object`|
||Data e Hora do Início da Linha de Pesquisa |`DH_INICIO_LINHA`|`object`|-|-|
||-|-|-|`Volume`|`int64`|
||Data e Hora do Fim da Linha de Pesquisa |`DH_FIM_LINHA`|`object`|-|-|
||-|-|-|`NumeroPaginas`|`int64`|
||Data da Titulação |`DT_TITULACAO`|`object`|-|-|
||-|-|-|`BibliotecaDepositaria`|`object`|
||Descrição da Palavra Chave |`DS_PALAVRA_CHAVE`|`object`|-|-|
||-|-|-|`Idioma`|`object`|
||Descrição do Abstract|`DS_ABSTRACT`|`object`|-|-|
||-|-|-|`ResumoTese`|`object`|
||Descrição do Keyword |`DS_KEYWORD`|`object`|-|-|
||-|-|-|`LinhaPesquisa`|`object`|
||Indicador de Expectativa de Atuação|`IN_TRABALHO_MESMA_AREA`|`float64`|-|-|
||-|-|-|`URLTextoCompleto`|`object`|
||Nome do Tipo de vinculo|`NM_TP_VINCULO`|`object`|
||-|-|-|`DocumentoOrientador_1`|`object`|
||Indicador se o Orientador Participou da Banca |`IN_ORIENT_PARTICIPOU_BANCA`|`int64`|-|-|
||-|-|-|`Orientador_1`|`object`|
||Descrição da Biblioteca Depositária |`DS_BIBLIOTECA_DEPOSITARIA`|`object`|-|-|
||-|-|-|`DocumentoOrientador_2`|`object`|
||Identificador do Tipo de Expectativa da Atuação|`ID_TP_EXPECTATIVA_ATUACAO`|`int64`|-|-|
||-|-|-|`Orientador_2`|`object`|
||Nome da Expectativa da Atuação |`NM_EXPECTATIVA_ATUACAO`|`object`|-|-|
||-|-|-|`DocumentoOrientador_4`|`float64`|
||Código de identificação da pessoa na base de dados da CAPES |`ID_PESSOA_DISCENTE`|`int64`|-|-|
||-|-|-|`Òrientador_4`|`float64`|
||Nome do Discente |`NM_DISCENTE`|`object`|-|-|
||-|-|-|`DocumentoCoOrientador_1`|`object`|
||Data da Matrícula do Discente |`DT_MATRICULA`|`object`|-|-|
||-|-|-|`CoOrientador_1`|`object`|
||Identificador do Grau Acadêmico ao qual o discente está vinculado|`ID_GRAU_ACADEMICO`|`int64`|-|-|
||-|-|-|`DocumentoCoOrientador_2`|`object`|
||Nome do Grau Acadêmico ao qual o discente está vinculado |`NM_GRAU_ACADEMICO`|`object`|-|-|
||-|-|-|`CoOrientador_2`|`object`|
||Nome do Orientador|`NM_ORIENTADOR`|`object`|-|-|
||-|-|-|`DocumentoCoOrientador_3`|`object`|
||Descrição da Categoria do Orientador|`DS_CATEGORIA_ORIENTADOR`|`object`|-|-|
||-|-|-|`CoOrientador_3`|`object`|
||Nome da Categoria do Docente |`NM_CATEGORIA_DOCENTE`|`object`|-|-|
||-|-|-|`DocumentoCoOrientador_4`|`object`|
||Nome da Região da IES |`NM_REGIAO`|`object`|-|-|
||-|-|-|`CoOrientador_4`|`object`|
||Sigla da Unidade da Federação da IES |`SG_UF_IES`|`object`|-|-|
||Nome da Unidade da Federação da IES|`NM_UF_IES`|`object`|-|-|
||Código da Grande Área de Conhecimento a que a Produção está vinculada |`CD_GRANDE_AREA_CONHECIMENTO`|`int64`|-|-|
||Nome da Grande Área de Conhecimento a que a Produção está vinculada |`NM_GRANDE_AREA_CONHECIMENTO`|`object`|-|-|
||Código da Área de Conhecimento a que o Programa de Pós-Graduação está vinculada|`CD_AREA_CONHECIMENTO`|`float64`|-|-|
||Nome da Área de Conhecimento a que o Programa de Pós-Graduação está vinculada|`NM_AREA_CONHECIMENTO`|`object`|-|-|
||Código da Subárea de Conhecimento a que o Programa de Pós-Graduação está vinculada |`CD_SUBAREA_CONHECIMENTO`|`float64`|-|-|
||Nome da Subárea de Conhecimento a que o Programa de Pós-Graduação está vinculada |`NM_SUBAREA_CONHECIMENTO`|`object`|-|-|
||Código da Especialidade |`CD_ESPECIALIDADE`|`float64`|-|-|
||Nome da Especialidade|`NM_ESPECIALIDADE`|`object`|-|-|
||Nome da Área de Avaliação |`NM_AREA_AVALIACAO`|`object`|-|-|
||Número do Volume da Produção|`NR_VOLUME`|`object`|-|-|
||Número de Páginas da Produção |`NR_PAGINAS`|`float64`|-|-|
||Nome do Idioma da Produção |`NM_IDIOMA`|`object`|-|-|
||Descrição do Resumo|`DS_RESUMO`|`object`|-|-|
||Descrição da URL do Texto Completo|`DS_URL_TEXTO_COMPLETO`|`object`|-|-|
||Código de identificação da pessoa orientador na base de dados da CAPES |`ID_PESSOA_ORIENTADOR`|`float64`|-|-|
||Indicada se o TCC tem vínculo com alguma Produção Intelectual |`IN_TCC_COM_VINCULO_PRODUCAO`|`object`|-|-|
||Representa os 'IDs' das produções intelectuais concatenadas, para caso o usuário deseje saber qual produção intelectual foi vinculada aquele TCC |`ID_ADD_PRODUCAO_VINCULO_CT`|`object`|-|-|