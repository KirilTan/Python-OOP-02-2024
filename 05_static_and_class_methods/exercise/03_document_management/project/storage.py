from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.documents: List[Document] = []
        self.topics: List[Topic] = []

    def add_category(self, category: Category) -> None:
        self.categories.append(category) if category not in self.categories else None

    def add_topic(self, topic: Topic) -> None:
        self.topics.append(topic) if topic not in self.topics else None

    def add_document(self, document: Document) -> None:
        self.documents.append(document) if document not in self.documents else None

    def edit_category(self, category_id: int, new_name: str) -> None or str:
        try:
            category = next(filter(lambda c: c.id == category_id, self.categories))
        except StopIteration:
            return f"Topic {category_id} is not found."

        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None or str:
        try:
            topic = next(filter(lambda x: x.id == topic_id, self.topics))
        except StopIteration:
            return f"Topic {topic_id} is not found."

        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None or str:
        try:
            document = next(filter(lambda d: d.id == document_id, self.documents))
        except StopIteration:
            return f"Document {document_id} is not found."

        document.edit(new_file_name)

    def delete_category(self, category_id: int) -> None or str:
        try:
            category = next(filter(lambda x: x.id == category_id, self.categories))
        except StopIteration:
            return f"Category {category_id} is not found."

        self.categories.remove(category) if category in self.categories else None

    def delete_topic(self, topic_id: int) -> None or str:
        try:
            topic = next(filter(lambda x: x.id == topic_id, self.topics))
        except StopIteration:
            return f"Topic {topic_id} is not found."

        self.topics.remove(topic) if topic in self.topics else None

    def delete_document(self, document_id: int) -> None or str:
        try:
            document = next(filter(lambda x: x.id == document_id, self.documents))
        except StopIteration:
            return f"Document {document_id} is not found."

        self.documents.remove(document) if document in self.documents else None

    def get_document(self, document_id: int) -> Document or str:
        try:
            document = next(filter(lambda x: x.id == document_id, self.documents))
        except StopIteration:
            return f"Document {document_id} is not found."

        return document

    def __repr__(self):
        text = '\n'.join(str(d) for d in self.documents)
        return text
