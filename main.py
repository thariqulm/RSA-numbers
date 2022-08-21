from factordb.factordb import FactorDB
from keep_alive import keep_alive
import rsa,requests,random,os
keep_alive()
while True:
  (pub_key, priv_key)= rsa.newkeys(62)
  f = FactorDB(pub_key.n)
  f.connect()
  print(f.get_status())
  print("%s = "%pub_key.n + "%s x %s "%(priv_key.p,priv_key.q))
  requests.get('http://www.factordb.com/report.php?report=%s = %s * %s'% (str(pub_key.n),str(priv_key.p),str(priv_key.q)))
  f = FactorDB(pub_key.n)
  f.connect()
  print(f.get_status())
  (pub_key, priv_key)= rsa.newkeys(random.randint(62,2500))
  f = FactorDB(pub_key.n)
  f.connect()
  print(f.get_status())
  print("%s = "%pub_key.n + "%s x %s "%(priv_key.p,priv_key.q))
  requests.get('http://www.factordb.com/report.php?report=%s = %s * %s'% (str(pub_key.n),str(priv_key.p),str(priv_key.q)))
  f = FactorDB(pub_key.n)
  f.connect()
  print(f.get_status())
  os.system('clear')