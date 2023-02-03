import requests,time
from datetime import datetime
boucle = 1
old_date = input('Date actuelle (YYYY-MM-DD : ')
now = datetime.now()
date = now.strftime(("%Y-%m-%d"))
discord_webhook_url = "[DISCORD WEBHOOK]"
apitoken = "[API TOKEN]"

while boucle == 1 :
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    if date != old_date :
        url = f"https://eodhistoricaldata.com/api/economic-events?api_token={apitoken}&from={date}&to={date}"
        old_date = now.strftime("%Y-%m-%d")
        reponse = requests.get(url)
        contenu = reponse.json()
        for r in contenu:
            atype = r['type']
            acountry = r['country']
            adate = r['date']
            aprevious = r['previous']
            aestimate = r['estimate']
            message = f'```Annonce économique du {adate} :\n Type : {atype}\n Pays : {acountry}\n Résultat précédent : {aprevious} \n Resultat estimé : {aestimate}%```'
            message = {"content" : message}
            requests.post(discord_webhook_url, data=message)
            time.sleep(1)
    time.sleep(3600)

