import argparse

from backup.postgres import PostgresBackup

def run_cli():
    parser=argparse.ArgumentParser(
        description="Databases utility"
    )

    subparser=parser.add_subparsers(dest="command")
    backup=subparser.add_parser("backup")
    backup.add_argument("--host",required=True)
    backup.add_argument("--port",default=5432)
    backup.add_argument("--user",required=True)
    backup.add_argument("--db",required=True)


    backup=subparser.add_parser("restore")
    backup.add_argument("--host",required=True)
    backup.add_argument("--port",default=5432)
    backup.add_argument("--user",required=True)
    backup.add_argument("--db",required=True)
    backup.add_argument("--file",required=True)

    arg=parser.parse_args()

    postgre=PostgresBackup()

    if arg.command=="backup":
        postgre.backup(arg.host,arg.port,arg.user,arg.db)

    elif arg.command=="restore":
        postgre.restore(arg.host,arg.port,arg.user,arg.db,arg.file)

    else:
        parser.print_help()









































# import argparse
# from backup.postgres import PostgresBackup

# def run_cli():
#     parser=argparse.ArgumentParser(
#         description="PostgreSql Database backup utility"
#     )
#     subparsers=parser.add_subparsers(dest="command")

#     backup=subparsers.add_parser("backup")
#     backup.add_argument("--host",required=True)
#     backup.add_argument("--port",default=5432)
#     backup.add_argument("--user",required=True)
#     backup.add_argument("--db",required=True)

#     restore=subparsers.add_parser("restore")
#     restore.add_argument("--host",required=True)
#     restore.add_argument("--port",default=5432)
#     restore.add_argument("--user",required=True)
#     restore.add_argument("--db",required=True)
#     restore.add_argument("--file", required=True)


#     args=parser.parse_args()
#     postgres=PostgresBackup()

#     if args.command=="backup":
#         postgres.backup(args.host,args.port,args.user,args.db)

#     elif args.command=="restore":
#         postgres.restore(
#             args.host,args.port,args.user,args.db,args.file
#         )

#     else:
#         parser.print_help()