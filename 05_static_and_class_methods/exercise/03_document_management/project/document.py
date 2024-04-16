from typing import List

from ex_1_and_2.project import Category
from ex_1_and_2.project import Topic


class Document:

    def __init__(self, _id: int, category_id: int, topic_id: int, file_name: str):
        self.id = _id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags: List[str] = []

    @classmethod
    def from_instances(cls, _id: int, category: Category, topic: Topic, file_name: str):
        return cls(_id=_id,
                   category_id=category.id,
                   topic_id=topic.id,
                   file_name=file_name)

    def add_tag(self, tag_content: str) -> None:
        self.tags.append(tag_content) if tag_content not in self.tags else None

    def remove_tag(self, tag_content: str) -> None:
        self.tags.remove(tag_content) if tag_content in self.tags else None

    def edit(self, new_file_name: str) -> None:
        self.file_name = new_file_name

    def __repr__(self):
        text = (f"Document {self.id}: {self.file_name}; "
                f"category {self.category_id}, topic {self.topic_id}, "
                f"tags: {', '.join(self.tags)}")
        return text
