import mysql.connector

class DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(user="root",host="localhost",db="EconnomyBot")


    async def new_account(self,ctx,member):
        curseur = self.db.cursor()
        curseur.execute(f"SELECT * FROM users WHERE id = {member.id};")
        
        resultat = curseur.fetchone()
        try:
            for row in resultat:
                await ctx.send("Vous avez déjà un compte.")
                return
        except Exception:
            await ctx.send("Compte créé !")
        curseur.execute(f"INSERT INTO users (id,name,money) VALUES ('{member.id}','{member.name}',0);")
        curseur.close()
        self.db.commit()


    async def open_account(self,ctx,member):
        curseur = self.db.cursor()

        curseur.execute(f"SELECT money FROM users WHERE id = {member.id};")
        
        resultat = curseur.fetchone()
        try:
            for row in resultat:
                await ctx.send(f"Vous avez actuellement {row} € sur votre compte !")
        except Exception:
            await ctx.send("Vous n'avez pas de compte.")