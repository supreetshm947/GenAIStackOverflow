from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP, TEXT, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from src.utils import convert_timestamp_to_datetime

# class StackOverflowPost(declarative_base()):
class StackOverflowPost:

    def __init__(self, post):
        # super(StackOverflowPost, self)
        self.question_id = post['question_id']
        self.title = post['title']
        self.answer_count = post.get('answer_count')
        self.creation_date = convert_timestamp_to_datetime(post.get('creation_date'))
        self.last_edit_date = convert_timestamp_to_datetime(post.get('last_edit_date')) if 'last_edit_date' in post and not post.get('last_edit_date') else None
        self.tags = post.get('tags')
        self.link = post['link']
        self.is_answered = post.get('is_answered')
        self.score = post.get('score')
        self.answer = post.get('answers')


    # __tablename__ = 'stackoverflow_posts'

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

    def __eq__(self, other):
        if isinstance(other, StackOverflowPost):
            return self.question_id == other.question_id
        return False

    def __hash__(self):
        return hash(self.question_id)
