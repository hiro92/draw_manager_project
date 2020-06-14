import os
import datetime
import csv
from django.conf import settings
from django.core.management import BaseCommand

from draw_manager_app.models import Draw


class Command(BaseCommand):
    help = "Backup Draw data"

    def handle(self,*args,**kwargs):
        #実行時のYYYYMMDDを取得
        date = datetime.date.today().strftime("%Y%m%d")

        #保存ファイルの相対パス
        file_path = settings.BACKUP_PATH + 'draw_' + date + '.csv'

        #保存ディレクトリが存在しなければ作成
        os.makedirs(settings.BACKUP_PATH,exist_ok=True)

        #バックアップファイルの作成
        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            #ヘッダーへの書き込み
            header = [field.name for field in Draw._meta.fields]
            writer.writerow(header)

            #Drawテーブルの全データを取得
            draws = Draw.objects.all()

            #データ部分の書き込み
            for draw in draws:
                writer.writerow([str(draw.user),
                draw.draw_number,
                draw.customer,
                draw.material,
                draw.material_size,
                draw.outsourcing,
                draw.outsourcing_content,
                str(draw.photo1),
                str(draw.photo2),
                str(draw.photo3),
                str(draw.created_at),
                str(draw.update_at)])

            #保存ディレクトリのファイルリストを取得
            files = os.listdir(settings.BACKUP_PATH)
            #ファイルが設定数以上あったら一番古いファイルを削除
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])