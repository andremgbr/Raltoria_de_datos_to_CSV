import pandas as pd
import tabula 

df1= tabula.read_pdf("my_pdf.pdf",pages='all',multiple_tables=False, stream=True, guess=False,columns=[50,420,460,510,570,640,690,750])
df1=df1[0]
df2= tabula.read_pdf("my_pdf.pdf",pages='all',multiple_tables=False, stream=True, guess=False,columns=[100,190,260,290,370,440,505,570,640,710,795])
df2=df2[0]

resultado = pd.DataFrame()

for i in range(len(df1)):
    if str(df1.iloc[i,0]).isnumeric():
        row = pd.Series([df1.iloc[i,0],df1.iloc[i,1],df1.iloc[i,2],df1.iloc[i,3],df1.iloc[i,4],df1.iloc[i,5],df1.iloc[i,6],df1.iloc[i,7],df1.iloc[i,8],
        				df2.iloc[i+2,1],df2.iloc[i+3,1],df2.iloc[i+4,1],str(df2.iloc[i+5,1]) + (str(df2.iloc[i+5,2]) if str(df2.iloc[i+5,2]) != "nan" else ""),df2.iloc[i+6,1],
        				df2.iloc[i+2,3],df2.iloc[i+3,3],df2.iloc[i+4,3],
        				df2.iloc[i+2,5],df2.iloc[i+3,5],        				
        				df2.iloc[i+2,7],df2.iloc[i+3,7],df2.iloc[i+4,7],df2.iloc[i+5,7],df2.iloc[i+6,7],df2.iloc[i+7,7],
        				df2.iloc[i+2,9],df2.iloc[i+3,9],df2.iloc[i+4,9],df2.iloc[i+5,9],df2.iloc[i+6,9],
        				df2.iloc[i+2,11],df2.iloc[i+3,11],df2.iloc[i+4,11],df2.iloc[i+5,11],
        				])
        row = pd.DataFrame([row])
        resultado = pd.concat([resultado,row],ignore_index=False)


resultado.rename(columns={
	0:'Código',
	1:'Descrição',
	2:'Cadastro',
	3:'Pis Compra',
	4:'Cofins Compra',
	5:'Pis Venda',
	6:'Cofins Venda',
	7:'Carga Trib Nacional',
	8:'Carga Trib Estadual',
	9:'ICMS: Tributação',
	10:'ICMS: Al. ICMS Int',
	11:'ICMS: Cálculo ICMS',
	12:'ICMS: Descreição Cálculo ICMS',
	13:'ICMS: Pauta Fiscal',
	14:'CSOSN: Origem Merc',
	15:'CSOSN: Trib/Isento',
	16:'CSOSN: Subst. Trib',
	17:'CST ICMS Não Trib/Isento: Pessoa Física',
	18:'CST ICMS Não Trib/Isento: Pessoa Jurídica',
	19:'IPI: CST IPI Entr',
	20:'IPI: CST IPI Saída',
	21:'IPI: Tipo Item',
	22:'IPI: Gên. Item',
	23:'IPI: Combustível',
	24:'IPI: Código ANP',
	25:'IPI: Cód. WFiscal',
	26:'IPI: Clas. IPI(NCM)',
	27:'IPI: Cód. Selo',
	28:'IPI: Classe Enq',
	29:'IPI: Cód. Reduz',
	30:'PIS/COFINS: CST PIS Entr',
	31:'PIS/COFINS: CST PIS Saída',
	32:'PIS/COFINS: CST Cofins Entr',
	33:'PIS/COFINS: CST Cofins Saída'
	}, inplace=True)

pd.options.display.max_columns =999
resultado.to_csv('resultado.csv',index=False)
print("Encerrado!....")


