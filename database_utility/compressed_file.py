import gzip

backup_file = "backups/postgres_backup_20251223_202853.sql.gz"

with gzip.open(backup_file, "rt") as f:  # 'rt' = read text
    for i, line in enumerate(f):
        print(line, end='')
        if i > 100:  # print first 50 lines
            break

