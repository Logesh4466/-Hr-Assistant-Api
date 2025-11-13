from pydantic import BaseModel
from typing import Dict, List, Optional

class FormsResponse(BaseModel):
    templates: List[str]

class QuestionItem(BaseModel):
    placeholder: str
    question: str

class QuestionsResponse(BaseModel):
    questions: List[QuestionItem]
    checkbox_options: Optional[List[str]] = []
    schedule_fields: Optional[List[str]] = []

class BuildQuestionsRequest(BaseModel):
    # Optional: allow client to pass placeholders to skip AI step
    placeholders: Optional[List[str]] = None
    user_query: Optional[str] = None  # if sending a free text to find best template (not required for API2)

class FillRequest(BaseModel):
    answers: Dict[str, str]  # mapping placeholder -> value
    selected_checkboxes: Optional[List[str]] = []
    schedule_values: Optional[Dict[str, str]] = {}

class FillResponse(BaseModel):
    output_path: str
