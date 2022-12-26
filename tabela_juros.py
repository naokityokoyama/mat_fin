#packet
import pandas as pd

class Price:
  def __init__(self, juros, principal, parcelas):
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
    return round (self.coeficiente() * self.principal,2)

  def dataframe(self):
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
    self.juros = juros
    self.principal = principal
    self.parcelas = parcelas
  
  def dataframe(self):
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

if __name__ == "__main__":
    print ('tabelas de SAC e Price')
