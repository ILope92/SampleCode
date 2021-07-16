import pandas as pd
from backend.database.models.documents import Documents
from backend.database.crud import CRUD_DOC
from datetime import datetime


class AddCSV:
    @classmethod
    async def add_data(cls, path):
        result = pd.read_csv(path)
        await cls.create_list_models(cls, csv=result)

    async def create_list_models(self, csv):
        documents = [
            Documents(
                **{
                    "rubrics": str(csv["rubrics"][num]),
                    "text": csv["text"][num],
                    "created_date": datetime.fromisoformat(csv["created_date"][num]),
                }
            )
            for num, _ in enumerate(csv["created_date"])
        ]
        await CRUD_DOC.add_many(models_db=documents)
