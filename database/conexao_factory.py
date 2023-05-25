import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(host='silly.db.elephantsql.com', database='ifaxfwsg', user='ifaxfwsg', password='OreRWMOGSKLnjGq9CE5W-XM7cU8ztdLh')
