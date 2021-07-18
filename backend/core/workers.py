import os
import time
import asyncio
from backend.core.integrations.csv_parse import AddCSV
from backend.utils.send_mail import send_email
from backend.schemas.users import Registration


class ModifiedData:
    __files_data__ = {}
    __path_data__ = "data"
    __timeout__ = 30

    @classmethod
    async def search(cls):
        print("sfa")
        for root, dirs, files in os.walk(cls.__path_data__):
            for file in files:
                if file.endswith(".csv"):
                    modified = os.path.getmtime(os.path.join(root, file))
                    try:
                        if len(cls.__files_data__) == 0:
                            cls.__files_data__[file] = {
                                "modified": time.ctime(modified),
                                "path": os.path.join(root, file),
                            }
                            await cls.update(file)
                        elif cls.__files_data__[file]["modified"] != time.ctime(
                            modified
                        ):
                            await cls.update(file)

                        cls.__files_data__[file] = {
                            "modified": time.ctime(modified),
                            "path": os.path.join(root, file),
                        }
                    except KeyError:
                        cls.__files_data__[file] = {
                            "modified": time.ctime(modified),
                            "path": os.path.join(root, file),
                        }
        await asyncio.sleep(cls.__timeout__)

    @classmethod
    async def update(cls, file: str):
        await AddCSV.add_data(cls.__files_data__[file]["path"])


class EmailSends:
    __emails__ = []

    @classmethod
    async def wait_email(cls, data: Registration):
        while len(cls.__emails__) != 0:
            await send_email(cls.__emails__[-1], data)
            del cls.__emails__[-1]

    @classmethod
    async def add_email(cls, data: Registration):
        cls.__emails__.append(data.email)
        await cls.wait_email(data)
