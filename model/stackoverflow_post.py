from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP, TEXT, ARRAY
from sqlalchemy.ext.declarative import declarative_base

class StackOverflowPost(declarative_base()):
    __tablename__ = 'stackoverflow_posts'

    question_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    answer_count = Column(Integer)
    creation_date= Column(TIMESTAMP)
    last_edit_date = Column(TIMESTAMP)
    tags = Column(ARRAY(String))
    link = Column(String)
    is_answered = Column(Boolean)
    score = Column(Integer)
    answer = Column(TEXT)

    def __str__(self):
        return (
            f"Question ID: {self.question_id}\n"
            f"Title: {self.title}\n"
            f"Answer Count: {self.answer_count}\n"
            f"Score: {self.score}\n"
            f"Is Answered: {self.is_answered}\n"
            f"Tags: {', '.join(self.tags) if self.tags else 'None'}\n"
            f"Link: {self.link}\n"
            f"Creation Date: {self.creation_date}\n"
            f"Last Edit Date: {self.last_edit_date}\n"
            f"Answer: {self.answer}\n"
        )