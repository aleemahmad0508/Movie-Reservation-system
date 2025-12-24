import subprocess
import datetime
import gzip
import shutil
import os

from utiles.logger import logger
from utiles.compress import compress_file
from storage.local import save_locally

class PostgresBackup:

    def backup(self,host,port,user,dbname):
        logger.info("postgreSql backup started")

        timestamp= datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        sql_file = f"postgres_backup_{timestamp}.sql"

        cmd=[
            "pg_dump",
            "-h",host,
            "-p",str(port),
            "-U",user,
            dbname
        ]

        try:
            with open(sql_file,"w") as f:
                subprocess.run(cmd,stdout=f,check=True)

            compressed= compress_file(sql_file)
            final_path= save_locally(compressed)
            logger.info(f"Backup completed : {final_path}")
            print(f"Backup completed :{final_path}")

        except Exception as e:
            logger.error(f"Backup Failed :{e}")
            print("Backup failed")

    def restore(self,host,port,user,dbname,backup_file):
        logger.info("PostgresSql restore started")

        sql_file=backup_file.replace("gz","")

        try:
            with gzip.open(backup_file,"rb") as f_in:
                with open(sql_file,"wb") as f_out:
                    shutil.copyfileobj(f_in,f_out)

            cmd=[
            "psql",
            "-h",host,
            "-p",str(port),
            "-U",user,
            "-d",dbname
            ]

            with open(sql_file,"r") as f:
                subprocess.run(cmd,stdin=f,check=True)

            os.remove(sql_file)

            logger.info("restore completed succesfully")
            print("restore completed")
        except Exception as e:
            logger.error(f"Restore failed: {e}")
            print("restore failed")

