#packet
import pandas as pd

class Price:
  def __init__(self, juros, principal, parcelas):
    '''
    -> Calculo de prestacao connstante
       :juros -> insira o valor do juros \n   Ex: 2% input apenas o valor de 2\n
       :parcelas -> numero inteiro de parcelas\n
       :principal -> valor de entrada
    '''
    self.juros = juros
    self.principal = principal
    self.parcelas = parcelas

  def coeficiente(self):
    parcelas = self.parcelas
    juros = self.juros
    juros_convertido = juros/100 
    formula = 1-(1+juros_convertido)**-self.parcelas
    return juros_convertido / formula

  def valor_prestacao(self):
    '''Retorna o valor da prestação'''
    return round (self.coeficiente() * self.principal,2)

  def dataframe(self):
    ''' -> Retorna o dataframe da tabela PRICE'''
    n = self.parcelas 
    prestacao = self.valor_prestacao()
    juros = self.juros / 100
    data = {'Parcelas': range(n+1), 'Prestacao': self.valor_prestacao()}   
    df = pd.DataFrame(data)
    df['Juros'] = ''  
    df['Armotizacao'] = ''
    df['SD'] = ''
    df.loc[0 ,'SD'] = self.principal
    df.loc[0, 'Juros'] = '-'
    df.loc[0, 'Armotizacao'] = '-'
    for i in range(n):
      df.loc[i+1, 'Juros'] = df.loc[i, 'SD'] * juros
      df.loc[i+1, 'Armotizacao'] = round(prestacao - df.loc[i+1, 'Juros'],2)
      df.loc[i+1, 'SD'] = round(df.loc[i, 'SD'] - df.loc[i+1, 'Armotizacao'],2)
    return df

  def pago(self):
    pg = self.dataframe()['Prestacao'].values
    return round(pg[1:].sum(),2)

  def juros_pg(self):
    pg = self.dataframe()['Juros'].values
    return round(pg[1:].sum(),2)

class Sac:
  def __init__(self, juros, principal, parcelas):
    '''
    -> Calculo de armotização constante
       :juros -> insira o valor do juros \n   Ex: 2% input apenas o valor de 2\n
       :parcelas -> numero inteiro de parcelas\n
       :principal -> valor de entrada  
    '''
    self.juros = juros
    self.principal = principal
    self.parcelas = parcelas
  
  def dataframe(self):
    '''-> Retorna o dataframe da tabela SAC'''
    n = self.parcelas 
    vp = self.principal
    armotizacao = vp/n
    juros = self.juros / 100
    data = {'Parcelas': range(n+1)}   
    df = pd.DataFrame(data)
    df['Prestacao'] = ''
    df['Juros'] = ''
    df['Armotizacao'] = ''
    df['SD'] = ''
    df.loc[0 ,'SD'] = self.principal
    df.loc[0, 'Juros'] = '-'
    df.loc[0, 'Armotizacao'] = '-'
    df.loc[0, 'Prestacao'] = '-'
    df.loc[1: , 'Armotizacao'] = armotizacao
    for i in range(n):
       df.loc[i+1, 'Juros'] = df.loc[i, 'SD'] * juros
       df.loc[i+1, 'Prestacao'] = round(armotizacao + df.loc[i+1, 'Juros'],2)
       df.loc[i+1, 'SD'] = round(df.loc[i, 'SD'] - df.loc[i+1, 'Armotizacao'],2)
    return df

  def pago(self):
      pg = self.dataframe()['Prestacao'].values
      return round(pg[1:].sum(),2)

  def juros_pg(self):
      pg = self.dataframe()['Juros'].values
      return round(pg[1:].sum(),2)

class Hp12c:
  def __init__(self, juros=0, parcelas=0, pv=0, fv=0, pmt=0):
    '''
      -> Alguns calculos de matematica financeira
      :juros -> insira o valor do juros \n   Ex: 2% input apenas o valor de 2\n
       :parcelas -> numero inteiro de parcelas \n
       :pv -> valor presente (valor da entrada) \n
       :fv -> valor futuro (valor final) \n
       :pmt -> valor da prestação]
    '''
    self.juros=juros
    self.parcelas = parcelas
    self.pv = pv
    self.fv = fv
    self.pmt = pmt
  
  def coeficiente(self):
    parcelas = self.parcelas
    juros = self.juros
    juros_convertido = juros/100 
    formula = 1-(1+juros_convertido)**-self.parcelas
    return juros_convertido / formula

  def value_future(self):
    '''calcula o valor futuro'''
    pv = self.pv
    i = self.juros/100
    n = self.parcelas
    return round(pv * (1+i)**n,2)

  def present_value(self):
    '''calcula o valor presente'''
    fv = self.fv
    i = self.juros/100
    n = self.parcelas
    return round(fv / (1+i)**n,2)    

  def payment(self):
    '''calcula a prestação'''
    coeficiente = self.coeficiente()    
    pv = self.pv
    return round(coeficiente * pv, 2)

  def taxa_juros(self):
    '''calcula a taxa de juros efetiva'''
    n = self.parcelas
    fv = self.fv
    pv = self.pv
    i = (fv/pv)**(1/n) - 1
    return round (i*100,2)      

if __name__ == "__main__":
    print ('tabelas de SAC // Price // Hp12c')
